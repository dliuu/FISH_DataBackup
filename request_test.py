import requests
import json
from datetime import datetime
import psycopg2

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

def single_GET_request(url:str, **kwargs):
    '''GET call for a single Bubble record. URL needs to contain obj/data_type/unique_id

    example usage:
    1. print(single_GET_request('https://fish-platform.bubbleapps.io/version-test/api/1.1/obj/Loan/1711461138915x125141837305315250'))

    '''
    r = requests.get(url)
    print(r.status_code)
    response = r.json()

    return response

def GET_all_objects(url:str, **kwargs):
    '''
    Three optional parameters for constraints:
    key_list: list of str
    type_list: list of str
    value_list: list of str

    example usage: GET_all_objects('https://fish-platform.bubbleapps.io/version-test/api/1.1/obj/Loan')
    '''
    if kwargs:
        key_list = kwargs.get(key_list)
        type_list = kwargs.get(type_list)
        value_list = kwargs.get(value_list)

        constraints = merge_constraints(key_list, type_list, value_list)

        if len(constraints) == 0:
            r = requests.get(url)
            return r.json()

        else:
            url = f"{url}?constraints={constraints}"
            r = requests.get(url)
            return r.json()
    
    else:
        r = requests.get(url)
        return r.json()


#__Main__
raw_obj = GET_all_objects('https://fish-platform.bubbleapps.io/version-test/api/1.1/obj/Loan') #modify to fit live version url
json_obj = json.dumps(raw_obj, indent=4)
day = get_datetime()

#with open(f"{day}-loan-snapshot.json", "w") as outfile:
    #outfile.write(json_obj)

#Write to Postgres
hostname = 'ls-85eee0d2cc3d8908046ecb29cdfe4e2ddb241ebc.cktchk5fub2f.us-east-1.rds.amazonaws.com'
username = 'dbmasteruser'
password = 'oj^2Uv|IXfE~SSS$`C6Zo:[&[1sln]_1'
database = 'bubble-backup'

try:
    connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cursor = connection.cursor()

    # SQL query to insert JSON data into a table
    sql_query = "INSERT INTO loan (jsonstring) VALUES (%s)"
    cursor.execute(sql_query, (json_obj,))

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