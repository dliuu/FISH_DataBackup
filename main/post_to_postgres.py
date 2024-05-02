import json
from sqlalchemy import create_engine, Column, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from main.bubble_api import BubbleAPI

Base = declarative_base()

class Loan(Base):
    __tablename__ = 'loan'
    id = Column(Integer, primary_key=True)
    jsonstring = Column(JSON)

class PostgresAPI:
    def __init__(self, hostname: str, username: str, password: str, database: str):
        self.engine = create_engine(f'postgresql://{username}:{password}@{hostname}/{database}')
        Base.metadata.create_all(self.engine)

    def insert_json_data(self, json_list: str):
        try:
            results = json.loads(json_list)["response"]["results"]

            print("Extracted data from json_list:")
            #for data in results:
                #print(json.dumps(data))

            # Create a session
            Session = sessionmaker(bind=self.engine)
            session = Session()

            # Insert JSON data into the 'loan' table
            for data in results:
                json_string = json.dumps(data)
                print(json_string)
                loan_entry = Loan(jsonstring=json_string)
                session.add(loan_entry)

            # Commit the changes
            session.commit()
            print("Data inserted successfully")

        except Exception as error:
            print("Error while connecting to PostgreSQL:", error)

        finally:
            session.close()
            print("PostgreSQL connection is closed")

# Example usage:
hostname = 'ls-85eee0d2cc3d8908046ecb29cdfe4e2ddb241ebc.cktchk5fub2f.us-east-1.rds.amazonaws.com'
username = 'dbmasteruser'
password = 'oj^2Uv|IXfE~SSS$`C6Zo:[&[1sln]_1'
database = 'bubble-backup'

test_url = 'https://fish-platform.bubbleapps.io/version-test/api/1.1/obj'
apikey = 'ac090d3276b654b46f8dc62f52a50452'
bubble_api = BubbleAPI(test_url, apikey)
json_list = bubble_api.GET_all_objects('Loan')

processed_json = json.dumps(json_list)

postgres_api = PostgresAPI(hostname, username, password, database)
postgres_api.insert_json_data(processed_json)
