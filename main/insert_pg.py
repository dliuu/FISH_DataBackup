import json
import psutil

from sqlalchemy import create_engine, Column, Integer, JSON, Float, String, Boolean, Numeric, Time, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
import datetime

from bubble_api import BubbleAPI
from schema import Loan, Company, Funding, Disbursement, Contact, Payment

process = psutil.Process()
Base = declarative_base()


class InsertPostgres:
    def __init__(self, obj:object, hostname: str, username: str, password: str, database: str):
        self.engine = create_engine(f'postgresql://{username}:{password}@{hostname}/{database}')
        self.obj = obj
        Base.metadata.create_all(self.engine)

    def create_loan_dict(self, data):
        '''
        inputs: data(str), an input json

        creates a dictionary from an input json (data)
         {
        "_id": "123",
        "created_by": "Alice",
        "created_date": "2023-01-01T00:00:00",
        "modified_date": "2023-01-02T00:00:00",
        "product_type": "Type A",
        "property_fish": "Property A}
        
        where empty columns are ommitted
        '''
        dict = {}
        mapper = inspect(self.obj)
        for column in mapper.attrs:
            column_name = column.key
            if column_name in data:
                dict[column_name] = data[column_name]
        return dict

    def insert_json_data(self, json_list: str):
        try:
            results = json.loads(json_list)["response"]["results"]

            print("Extracted data from json_list:")

            # Create a session
            Session = sessionmaker(bind=self.engine)
            session = Session()

            # Insert JSON data into the 'loan' table
            for data in results:
                json_string = json.dumps(data)
                print(json_string) #remove when needed

                validated_dict = self.create_loan_dict(data) #call self.create_loan_dict
                validated_dict['unique_id'] = data['_id'] + str(3523) #sync with joe

                entry = self.obj(**validated_dict)

                session.add(entry)

            # Commit the changes
            session.commit()
            print("Data inserted successfully")

        except Exception as error:
            print("Error while connecting to PostgreSQL:", error)

        finally:
            session.close()
            print("PostgreSQL connection is closed")

#__Main__
hostname = 'ls-85eee0d2cc3d8908046ecb29cdfe4e2ddb241ebc.cktchk5fub2f.us-east-1.rds.amazonaws.com'
username = 'dbmasteruser'
password = 'oj^2Uv|IXfE~SSS$`C6Zo:[&[1sln]_1'
database = 'bubble-backup'

test_url = 'https://ifish.tech/version-7yyc/api/1.1/obj'
apikey = 'ac090d3276b654b46f8dc62f52a50452'
bubble_api = BubbleAPI(test_url, apikey)
json_list = bubble_api.GET_all_objects('Loan')

processed_json = json.dumps(json_list)

postgres_insert = InsertPostgres(Loan,hostname, username, password, database)
postgres_insert.insert_json_data(processed_json)

print(process.memory_info().rss)