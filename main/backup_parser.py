import re
import psycopg2
import requests
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

tables = []
email_body = ''
with open('output.txt', 'r') as f:
	line = re.sub('Duplicate entry[^\n]+\n', '', f.read(), re.MULTILINE)

if not line:
    email_body = '<div>bubble database backup failed to run. Please check</div>'
elif 'Data inserted successfully' not in line:
    email_body = '<div>bubble database backup ran with error. Please check</div>'
else:
    tables = [re.sub('Finished: ', '', t.strip('\n')) for t in re.findall('(Finished:[^\n]+\n)', line)]

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
    'Company': '(fish)company',
    'Disbursement': '(fish)disbursement_new'
}

def send_email(msg):
    recipient = 'tdetwiler@wcp.team'
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
    
    query = f"select column_name from information_schema.columns where table_schema = 'public' and table_name = '{table.lower()}'"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    
    return [r[0] for r in rows]

def retrieve_bubble_schema(table_name):
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    URL = 'https://ifish.tech/api/1.1/meta'
    res = requests.get(URL, headers)
    feedback = json.loads(res.text)['types']
    return [r for r in feedback[table_name]['fields']]

def convert_colname(col):
    return re.sub('_+', '_', re.sub('\s+', '_', re.sub(r'[%/\-\(\){}&]', ' ', col.lower().strip()))).strip('_')

for t in tables:
    bubble_cols = [(c['display'], convert_colname(c['display']), c['type']) for c in retrieve_bubble_schema(table_mapping[t])]
    
    if t.lower() == 'loan': t='loan_backup'
    pg_cols = [c for c in retrieve_pg_schema(t)]
    
    added_columns = [col[0] for col in bubble_cols if not col[1] in pg_cols]
    removed_columns = [col for col in pg_cols if not col in [v[1] for v in bubble_cols]]
    
    if len(added_columns) == 0 and len(removed_columns) == 0:
        email_body = email_body + '<div>No schema changed detected in table ' + table_mapping[t] + '</div>'
    else:
        email_body = email_body + ''.join([
            '<div style="width: 500px"><span>Table: ' + table_mapping[t] + '</span><span style="margin-left: 10px">' + t + '</span></div>',
            '<div style="width: 200px"><span style="width: 100%; color: gray;">columns in bubble but not in pg</span></div>',
            '<table style="width: 500px; margin-left: 20px; margin-bottom: 10px;"><tbody>' + ''.join(['<tr><td>'+convert_colname(c)+'</td></tr>' for c in added_columns])+'</tbody></table>'
            '<div style="width: 200px"><span style="width: 100%; color: gray;">columns in pg but not in bubble</span></div>',
            '<table style="width: 500px; margin-left: 20px; margin-bottom: 10px;"><tbody>' + ''.join(['<tr><td>'+c+'</td></tr>' for c in removed_columns])+'</tbody></table>'
        ])
    

send_email(email_body)  
