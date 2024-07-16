import requests
import json
from sqlalchemy import create_engine, Column, Integer, JSON, Float, String, Boolean, Numeric, Time, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from schema import Reporting

def combine_and_clean_json_strings(json_list):
    combined_string = ''.join(json_list)
    return combined_string.replace('\n', '').replace(',"loan":}', ',"loan":null}')

def parse_datetime(date_string):
    if not date_string:
        return None
    try:
        return datetime.strptime(date_string, "%b %d, %Y %I:%M %p")
    except ValueError:
        return None

def parse_float(float_string):
    if not float_string or float_string == '':
        return None
    try:
        return float(float_string)
    except ValueError:
        return None

# API
url = "https://ifish.tech/version-test/api/1.1/wf/Reporting_Disbursements"

print("Requesting data from API...")
try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    print("API request successful.")
    try:
        data = response.json()
        print("Data successfully parsed as JSON.")
    except requests.exceptions.JSONDecodeError as json_err:
        print(f"JSON decode error: {json_err}")
        print("Response text:", response.text)
        data = None
except requests.exceptions.RequestException as req_err:
    print(f"Request error: {req_err}")
    data = None

if data is not None and 'response' in data:
    # Process the data
    print("Data:", data['response'])
else:
    print("No data to process")
    data = {'response': {}}

username = 'dbmasteruser'
password = 'P#7N12nj!qRwlZTDt>XeQ_ODbd2,}QvS'
hostname = 'ls-85eee0d2cc3d8908046ecb29cdfe4e2ddb241ebc.cktchk5fub2f.us-east-1.rds.amazonaws.com'
database = 'bubble-backup'

print("Setting up database connection...")
Base = declarative_base()
engine = create_engine(f'postgresql://{username}:{password}@{hostname}/{database}')

Base.metadata.drop_all(engine, [Reporting.__table__], checkfirst=True)  # Drop table if exists
Base.metadata.create_all(engine)  # Create table

Session = sessionmaker(bind=engine)
session = Session()
print("Database connection established.")

# Check if 'Disbursement' key is in the response
if 'Disbursement' in data.get('response', {}):
    print("Processing disbursement data...")
    for disbursement_json_list in data['response']['Disbursement']:
        # Combine the list elements into a single JSON string and clean it
        disbursement_json = combine_and_clean_json_strings(disbursement_json_list)
        print("Combined and Cleaned JSON:", disbursement_json)
        
        try:
            disbursement_data = json.loads(disbursement_json)
            print("JSON successfully parsed:", disbursement_data)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            continue
        
        new_record = Reporting(
            id=parse_float(disbursement_data.get('loan')),
            disbursement=disbursement_data.get('disbursement'),
            disbursement_type=disbursement_data.get('disbursement_type'),
            disbursement_interest_start=parse_datetime(disbursement_data.get('disbursement_interest_start')),
            disbursement_interest_end=parse_datetime(disbursement_data.get('disbursement_interest_end')),
            disbursement_due_on=parse_datetime(disbursement_data.get('disbursement_due_on')),
            disbursement_paid_on=parse_datetime(disbursement_data.get('disbursement_paid_on')),
            disbursement_amount_due=parse_float(disbursement_data.get('disbursement_amount_due')),
            disbursement_amount_collected=parse_float(disbursement_data.get('disbursement_amount_collected')),
            disbursement_amount_paid=parse_float(disbursement_data.get('disbursement_amount_paid')),
            loan=disbursement_data.get('loan'),
            loan_maturity_date=parse_datetime(disbursement_data.get('loan_maturity_date')),
            loan_servicer=disbursement_data.get('loan_servicer'),
            loan_foreclosure_start=parse_datetime(disbursement_data.get('loan_foreclosure_start')),
            loan_foreclosure_on=parse_datetime(disbursement_data.get('loan_foreclosure_on')),
            loan_foreclosure_schedule_on=parse_datetime(disbursement_data.get('loan_foreclosure_schedule_on')),
            loan_foreclosure_sent_on=parse_datetime(disbursement_data.get('loan_foreclosure_sent_on')),
            loan_owner=disbursement_data.get('loan_owner'),
            loan_servicing_status=disbursement_data.get('loan_servicing_status'),
            loan_primary_borrower=disbursement_data.get('loan_primary_borrower'),
            loan_closing_date=parse_datetime(disbursement_data.get('loan_closing_date')),
            loan_rate=parse_float(disbursement_data.get('loan_rate')),
            bankruptcyfiled=disbursement_data.get('bankruptcyfiled'),
            property_address=disbursement_data.get('property_address'),
            investor=disbursement_data.get('investor'),
            wcp_loan_amount=parse_float(disbursement_data.get('wcp_loan_amount')),
            wcp_funding_date=parse_datetime(disbursement_data.get('wcp_funding_date')),
            funding_amount=parse_float(disbursement_data.get('funding_amount')),
            funding_interest_rate=parse_float(disbursement_data.get('funding_interest_rate')),
            days_of_interest=parse_float(disbursement_data.get('days_of_interest')),
            next_payment=disbursement_data.get('next_payment'),
            next_payment_due_on=parse_datetime(disbursement_data.get('next_payment_due_on')),
            payment=disbursement_data.get('payment'),
            payment_due_on=parse_datetime(disbursement_data.get('payment_due_on')),
            payment_unpaid_balance=parse_float(disbursement_data.get('payment_unpaid_balance')),
            payment_type=disbursement_data.get('payment_type'),
            last_payment_paid_on=parse_datetime(disbursement_data.get('last_payment_paid_on')),
            payment_interest_amount_due=parse_float(disbursement_data.get('payment_interest_amount_due')),
            payment_late_fee_due=parse_float(disbursement_data.get('payment_late_fee_due')),
            payment_late_fee_paid=parse_float(disbursement_data.get('payment_late_fee_paid')),
            payment_interest_paid=parse_float(disbursement_data.get('payment_interest_paid')),
            payment_prepaid_interest=parse_float(disbursement_data.get('payment_prepaid_interest')),
            payment_amount_due_total=parse_float(disbursement_data.get('payment_amount_due_total')),
            payment_total_interest_paid=parse_float(disbursement_data.get('payment_total_interest_paid')),
            payment_total_amount_paid=parse_float(disbursement_data.get('payment_total_amount_paid')),
            payment_balance_interest=parse_float(disbursement_data.get('payment_balance_interest')),
            payment_balance_late_fee=parse_float(disbursement_data.get('payment_balance_late_fee')),
            payment_paid_on=parse_datetime(disbursement_data.get('payment_paid_on')),
            payment_balance_total=parse_float(disbursement_data.get('payment_balance_total')),
            payment_status_reason=disbursement_data.get('payment_status_reason'),
            payment_servicing_status=disbursement_data.get('payment_servicing_status'),
            payoff_received_on=parse_datetime(disbursement_data.get('payoff_received_on')),
            created_on=parse_datetime(disbursement_data.get('created_on_date'))
        )
        session.add(new_record)
        print(f"Record added: {new_record}")

session.commit()
print('Finished posting data')