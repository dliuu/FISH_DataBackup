import re
import psycopg2
import requests
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import itertools

tables = []
email_body = ''
with open('output.txt', 'r') as f:
    line = re.sub('Duplicate entry[^\n]+\n', '', f.read(), re.MULTILINE)

if not line:
    email_body = '<div>bubble database backup failed to run. Please check</div>'
elif 'Data inserted successfully' not in line:
    email_body = '<div>bubble database backup ran with error. Please check</div>'
else:
    tables = [re.sub('Finished: ', '', t.strip('\n')) for t in re.findall('(Finished:.+\n)', line)]

'''
#length of table_data should always be an even number
for i in range(2, len(table_data)+1, 2):
    tables_raw.append(table_data[start_idx:i])
    start_idx = i

for t in tables_raw:
    table_name = re.sub('Finished:', '', t[1]).replace('\n', '').strip()
    tables[table_name] = set()
    table_body = re.split('(?<=})\n', re.sub('"', '', t[0]))[:-2]
    rows = [re.sub('Resulting dictionary: ', '', r.replace('\n', '')) for r in table_body]
    keys = [re.findall("'[^']+': ", r) for r in rows]
    for key in keys:
        for k in key:
            tables[table_name].add(k)
    tables[table_name] = [re.sub(r"[':\s]", '', c) for c in list(tables[table_name])]
'''
table_mapping = {
    'Company': ['(fish)company', 'company'],
    'Disbursement':[ '(fish)disbursement_new', 'disbursement'],
    'Loan_Application': ['loan_application', 'loan_application'],
    'Loan': ['loan', 'loan_backup'],
    'Payment': ['(fish)payments', 'payment'],
    'Funding': ['(fish)funding', 'funding']
}

def send_email(msg):
    recipient = 'tdewiler@wcp.team'
    subject = 'Daily bubble-backup report'
    sender = 'xzhao@wcp.team'
    sender_password = 'Joe#4865@wcp'
    
    email = MIMEMultipart('alternative')
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.attach(MIMEText(msg, 'html'))
    
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(sender, sender_password)
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()
    
def retrieve_pg_schema(table):
    connection = psycopg2.connect(
        database='bubble-backup', 
        user='dbmasteruser', 
        password='P#7N12nj!qRwlZTDt>XeQ_ODbd2,}QvS', 
        host='ls-85eee0d2cc3d8908046ecb29cdfe4e2ddb241ebc.cktchk5fub2f.us-east-1.rds.amazonaws.com', 
        port='5432')
    
    query = f"select column_name from information_schema.columns where table_schema = 'public' and table_name = '{table_mapping[table][1]}'"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    
    return [r[0] for r in rows]

def retrieve_bubble_schema():
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    URL = 'https://ifish.tech/api/1.1/meta'
    res = requests.get(URL, headers)
    return json.loads(res.text)['types']
    #return [r for r in feedback[table_mapping[table_name][0]]['fields']]

def convert_colname(col):
    return re.sub('_+', '_', re.sub('\s+', '_', re.sub(r'[%/\-\(\){}&]', ' ', col.lower().strip()))).strip('_')

feedback = retrieve_bubble_schema()

for t in tables:
    bubble_cols = [(c['display'], convert_colname(c['display']), c['type']) for c in [r for r in feedback[table_mapping[t][0]]['fields']]]
    pg_cols = [c for c in retrieve_pg_schema(t)]
    
    added_columns = [col[0] for col in bubble_cols if not col[1] in pg_cols]
    removed_columns = [col for col in pg_cols if not col in [v[1] for v in bubble_cols]]
    
    if len(added_columns) == 0 and len(removed_columns) == 0:
        email_body = email_body + '<div>No schema changed detected in table ' + table_mapping[t][1] + '</div>'
    else:
        cols = list(itertools.zip_longest(added_columns, removed_columns, fillvalue=''))
        email_body = email_body + ''.join([
            '<table style="width: 600px"><thead><tr><th style="text-align: left; width: 300px">bubble table: ',
            table_mapping[t][0], '</th><th style="text-align: left; width: 300px">pg table: ',
            table_mapping[t][1], '</th></tr></thead><tbody>',
            ''.join(['<tr><td>'+col[0]+'</td><td>'+col[1]+'</td></tr>' for col in cols]),
            '</tbody></table>'
        ])       

send_email(email_body)
