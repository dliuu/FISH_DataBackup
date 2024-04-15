import requests
import json
from datetime import datetime
import psycopg2
from requests.auth import HTTPBasicAuth

#Utility Functions:

def merge_constraints(key_list, type_list, value_list):
    '''
    Takes three lists of strings and returns a list of dictionaries in the form:
    [ { "key": "unitname", "constraint_type": "equals", "value": "Unit A" } ,{ "key": "unitnumber", "constraint_type": "greater than", "value": "3" }]

    '''
    if len(key_list) != len(type_list) or len(key_list) != len(value_list):
        raise ValueError("Input lists must have the same length")

    merged_dicts = []
    for i in range(len(key_list)):
        merged_dicts.append({
            "key": key_list[i],
            "constraint_type": type_list[i],
            "value": value_list[i]
        })
    return merged_dicts

def get_datetime():
    ''' Returns the current day in datetime for file naming
    '''
    return datetime.today().strftime('%Y-%m-%d')

#API Calls

def GET_single_object(raw_url:str, obj:str, **kwargs):
    '''GET call for a single Bubble record. URL needs to contain obj/data_type/unique_id

    example usage:
    raw_json = GET_single_object('https://fish-platform.bubbleapps.io/version-test/api/1.1/obj', 'Loan/1711461138915x125141837305315250')


    '''
    url = f"{raw_url}/{obj}"

    r = requests.get(url)
    print(r.status_code)
    response = r.json()

    return response

def GET_all_objects(input_url:str, obj:str, **kwargs):
    '''
    Three optional parameters for constraints:
    key_list: list of str
    type_list: list of str
    value_list: list of str

    example usage: GET_all_objects('https://fish-platform.bubbleapps.io/version-test/api/1.1/obj', 'Loan')
    '''
    #Modify to fit bubble url
    url = f"{input_url}/{obj}"
    apikey = 'ac090d3276b654b46f8dc62f52a50452'

    headers = {
    'Content-type': 'application/json', 
    'Authorization': f'ApiKey {apikey}',}  

    if kwargs:
        key_list = kwargs.get(key_list)
        type_list = kwargs.get(type_list)
        value_list = kwargs.get(value_list)

        constraints = merge_constraints(key_list, type_list, value_list)

        if len(constraints) == 0:
            r = requests.get(url, headers=headers)
            return r.json()

        else:
            url = f"{url}?constraints={constraints}"
            r = requests.get(url, headers=headers)
            return r.json()
    
    else:
        r = requests.get(url)
        return r.json()
    
def write_to_file(url:str, obj:str, api_type:str, filename:str):
    ''' Takes  a URL and writes the JSON object returned by that URL to a file on disk. 
    Returns api_type if it is invalid.
    
    Args:
        url: str
        api_type: str (either 'single' or 'all')
        filename: str (date and .json are pre-appended)

    Example Usage: write_to_file(url=url, obj='Loan', api_type='all', filename='test-loans-snapshot')

    '''
    if api_type == 'single':
        raw_obj = GET_single_object(url, obj)
    elif api_type == 'all':
        raw_obj = GET_all_objects(url, obj)
    else:
        print('Error: Write_to_File: Please input a valid api_type')
        return api_type
    
    json_obj = json.dumps(raw_obj, indent=4)
    day = get_datetime()

    with open(f"{day}-{filename}.json", "w") as outfile:
        outfile.write(json_obj)


#Write to Postgres
def write_postgres(hostname:str, username:str, password:str, database:str, json_list:str):
    try:
        connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        cursor = connection.cursor()

        # SQL query to insert JSON data into a table
        for data in json_list:
            print('Posting JSON object...')
            print(data)
            json_string = json.dumps(data)
            sql_query = "INSERT INTO loan (jsonstring) VALUES (%s)"
            cursor.execute(sql_query, (json_string,))

        # Commit the changes
        connection.commit()
        print("Data inserted successfully")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


#__Main__

#Test Space
raw_json = GET_all_objects('https://fish-platform.bubbleapps.io/version-test/api/1.1/obj', '(FISH) Funding')
processed_json = json.dumps(raw_json)
print(processed_json)

#Write to File
url = 'https://fish-platform.bubbleapps.io/version-test/api/1.1/obj'

#Loan
write_to_file(url=url, obj='Loan', api_type='all', filename='test-loans-snapshot')

#Loan Application
write_to_file(url=url, obj='Loan Application', api_type='all', filename='test-loan-applications-snapshot')

#(FISH) Contact
write_to_file(url=url, obj='(FISH) Contact', api_type='all', filename='test-contacts-snapshot')

#(FISH) Company
write_to_file(url=url, obj='(FISH) Company', api_type='all', filename='test-companies-snapshot')

#(FISH) Property
write_to_file(url=url, obj='(FISH) Property', api_type='all', filename='test-properties-snapshot')

#(FISH) Payment
write_to_file(url=url, obj='(FISH) Payments', api_type='all', filename='test-payments-snapshot')

#(FISH) Funding
write_to_file(url=url, obj='(FISH) Funding', api_type='all', filename='test-funding-snapshot')

#(FISH) Disbursement_new
write_to_file(url=url, obj='(FISH) Disbursement_new', api_type='all', filename='test-disbursements-snapshot')

#(FISH)_Draw
write_to_file(url=url, obj='(FISH)_Draw', api_type='all', filename='test-draws-snapshot')

#Loan Extension
write_to_file(url=url, obj='Loan Extension', api_type='all', filename='test-draws-snapshot')

#Loan Payoff
write_to_file(url=url, obj='Loan Payoff', api_type='all', filename='test-payoffs-snapshot')

#User
write_to_file(url=url, obj='User', api_type='all', filename='test-payoffs-snapshot')

#Write to Postgres
hostname = 'ls-85eee0d2cc3d8908046ecb29cdfe4e2ddb241ebc.cktchk5fub2f.us-east-1.rds.amazonaws.com'
username = 'dbmasteruser'
password = 'oj^2Uv|IXfE~SSS$`C6Zo:[&[1sln]_1'
database = 'bubble-backup'

#write_postgres(hostname, username, password, database, json_obj)