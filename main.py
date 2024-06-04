from main.insert_pg import InsertPostgres
from main.bubble_api import BubbleAPI
from main.schema import Loan, Company, Funding, Disbursement, Contact, Payment

import json

#PG Credentials
hostname = 'ls-85eee0d2cc3d8908046ecb29cdfe4e2ddb241ebc.cktchk5fub2f.us-east-1.rds.amazonaws.com'
username = 'dbmasteruser'
password = 'P#7N12nj!qRwlZTDt>XeQ_ODbd2,}QvS'
database = 'bubble-backup'

#Bubble Side Credentials
url = 'https://ifish.tech/version-7yyc/api/1.1/obj'
apikey = 'ac090d3276b654b46f8dc62f52a50452'

bubble_api = BubbleAPI(url, apikey)
json_list = bubble_api.GET_all_objects('(FISH) Contact')
processed_json = json.dumps(json_list)

postgres_insert = InsertPostgres(Contact, hostname, username, password, database)
postgres_insert.insert_json_data(processed_json)

