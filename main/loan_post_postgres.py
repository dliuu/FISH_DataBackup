import json
from sqlalchemy import create_engine, Column, Integer, JSON, Float, String, Boolean, Numeric, Time, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
import datetime

from bubble_api import BubbleAPI

Base = declarative_base()

class Loan(Base):
    __tablename__ = 'loan_backup'
    unique_id = Column(String, primary_key=True)
    #jsonstring = Column(JSON)


    accrued_interest = Column(Numeric)
    acquisition_cost = Column(Numeric)
    additional_funds_to_close = Column(Numeric)
    aiv_ltv = Column(Numeric)
    amount = Column(Numeric)
    amount_to_add = Column(Numeric)
    amount_to_add_2 = Column(Numeric)
    amount_to_add_3 = Column(Numeric)
    amount_to_add_4 = Column(Numeric)
    amount_to_add_memo = Column(String)
    amount_to_add2_memo = Column(String)
    amount_to_add3_memo = Column(String)
    amount_to_add4_memo = Column(String)
    appraisal_effective_date = Column(DateTime(timezone=True), default=func.now())
    arm_index = Column(Numeric)
    arm_margin = Column(Numeric)
    arv_ltv = Column(Numeric)
    as_is_aiv = Column(String)
    aside_investor_legal_entity_name = Column(String)
    assignment_fee = Column(Numeric)
    assignment_fee_credited = Column(Numeric)
    assignment_fee_credit = Column(Numeric)
    balloon_flag_y_n = Column(Boolean)
    base_interest_rate = Column(Numeric)
    bathrooms_after_renovations = Column(Numeric)
    bedrooms_after_renovations = Column(Numeric)
    borrower = Column(String)
    contact_user = Column(String)
    borrower_arv = Column(Numeric)
    borrower_as_is = Column(Numeric)
    borrower_brings_to_closing = Column(Numeric)
    borrower_down_payment = Column(Numeric)
    borrower_est_repair_cost = Column(Numeric)
    borrower_provided_arv_bath = Column(Numeric)
    borrower_provided_arv_bed = Column(Numeric)
    borrower_provided_arv_sqft = Column(Numeric)
    borrower_provided_as_is_bath = Column(Numeric)
    borrower_provided_as_is_bed = Column(Numeric)
    borrower_provided_as_is_sqft = Column(Numeric)
    bpo_special_instructions = Column(String)
    business_affidavit = Column(Boolean)
    cash_out_amount = Column(Numeric)
    cash_out_mapped = Column(Boolean)
    clean_proceeds = Column(Numeric)
    closing_conditions = Column(String)
    closing_date = Column(DateTime(timezone=True), default=func.now())
    closing_fee = Column(Numeric)
    closing_instruction_letter = Column(Boolean)
    cltv = Column(Numeric)
    combined_arv_ltv = Column(Numeric)
    commercial_mixed_use_sqft_unit = Column(String)
    commercial_mixed_use_unit = Column(String)
    commercial_mixed_use_unit_mapped = Column(Numeric)
    commitment_authorization_number = Column(String)
    commitment_fee = Column(Numeric)
    company = Column(String)#FK
    company_fish = Column(String)
    company_contact_merges = Column(String)
    conduit_origination_fee = Column(Numeric)
    construction_balance = Column(Numeric)
    construction_budget1 = Column(Numeric)
    construction_draw_fund_balance = Column(Numeric)
    construction_fund_amount = Column(Numeric)
    contact = Column(String)
    contacts = Column(String)
    correspondent_price = Column(Numeric)
    cost_basis = Column(Numeric)
    retail_construction_amount = Column(Numeric)
    cross_collateral_property_equity = Column(String)
    cross_collateral_property_equity_mapped = Column(Numeric)
    current_loan_amount = Column(Numeric)
    current_term = Column(Numeric)
    cutoff_date = Column(DateTime(timezone=True), default=func.now())
    date_of_first_payment = Column(DateTime(timezone=True), default=func.now())
    days_accrued = Column(Numeric)
    days_to_maturity = Column(Numeric)
    days_in_year = Column(Numeric)
    deed = Column(Boolean)
    default_reason = Column(String)
    disbursement_date = Column(DateTime(timezone=True), default=func.now())
    down_payment_source = Column(String)
    downpayment = Column(Numeric)
    downpayment_source = Column(String)
    effective_ltc = Column(Numeric)
    effective_purchase_price = Column(Numeric)
    total_cost = Column(Numeric)
    escrow_deposit = Column(Numeric)
    estimated_monthly_interest_only_payment = Column(Numeric)
    estimated_revenue = Column(Numeric)
    existing_debt_balance = Column(Numeric)
    expected_payoff_date = Column(DateTime(timezone=True), default=func.now())
    external_funding_date = Column(DateTime(timezone=True), default=func.now())
    feature = Column(String)
    fish_id = Column(Numeric)
    funded_date = Column(DateTime(timezone=True), default=func.now())
    funding_entity_state = Column(String)
    guaranty = Column(Boolean)
    hoa_costs = Column(Numeric)
    hud_interest = Column(Numeric)
    initial_draw = Column(Numeric)
    initial_ltc = Column(Numeric)
    initial_rate_fixed_period = Column(Numeric)
    insurance_premium = Column(Numeric)
    interest_only_y_n = Column(Boolean)
    interest_rate = Column(Numeric)
    interest_rate_second_trust = Column(Numeric)
    interest_reserve = Column(Numeric)
    interest_type = Column(String)
    intro_rate = Column(Numeric)
    intro_terms = Column(String)
    last_sale_amount = Column(Numeric)
    lease_amount = Column(Numeric)
    lease_in_place = Column(Boolean)
    lease_term = Column(Numeric)
    lien_amount = Column(Numeric)
    lien_information = Column(String)
    lien_payoff_amount = Column(Numeric)
    llc_cert = Column(Boolean)
    lo_arv = Column(Numeric)
    lo_as_is = Column(Numeric)
    lo_bath_arv = Column(Numeric)
    lo_bath_as_is = Column(Numeric)
    lo_beds_arv = Column(Numeric)
    lo_beds_as_is = Column(Numeric)
    lo_est_repair_cost = Column(Numeric)
    lo_sqft_arv = Column(Numeric)
    lo_sqft_as_is = Column(Numeric)
    loan_amount = Column(Numeric)
    loan_amount_second_trust = Column(Numeric)
    loan_application_new = Column(String) #fk
    loan_extensions = Column(String)#fk 
    loan_maturity_link = Column(String) #fk
    loan_points = Column(Numeric)
    loan_rate = Column(Numeric)
    loan_rate_mapped = Column(Numeric)
    loan_team = Column(String)
    loan_term = Column(Numeric)
    loan_type = Column(String)
    ltaiv = Column(Numeric)
    ltc = Column(Numeric)
    ltv = Column(Numeric)
    maturity_date = Column(DateTime(timezone=True), default=func.now())
    months_of_interest_reserves = Column(Numeric)
    months_of_prepaid_interest = Column(Numeric)
    months_remaining_io_term = Column(Numeric)
    net_wire = Column(Numeric)
    net_wire_interest = Column(Numeric)
    next_due_date = Column(DateTime(timezone=True), default=func.now())
    note_rate = Column(Numeric)
    number = Column(String)
    occupancy_status = Column(String)
    original_deed_of_trust = Column(Boolean)
    original_p_i_amount = Column(Numeric)
    origination_date = Column(DateTime(timezone=True), default=func.now())
    origination_points = Column(Numeric)
    other_closing_costs = Column(Numeric)
    owner = Column(String)
    paid_to_date = Column(DateTime(timezone=True), default=func.now())
    payoff_amount = Column(Numeric)
    payoff_approved_by_user = Column(String)
    per_diem = Column(Numeric)
    permissions_viewable_users_list_user = Column(String)
    point_of_contact = Column(String)
    points_second_trust = Column(Numeric)
    prepaid_interest_amount = Column(Numeric)
    prepaid_interest_balance = Column(Numeric)
    property_last_sold_date = Column(DateTime(timezone=True), default=func.now())
    primary_borrower = Column(String)
    primary_contact = Column(String)
    principal_balance = Column(Numeric)
    proceeds = Column(Numeric)
    process = Column(String)
    product_type = Column(String)
    loan_product = Column(String)
    property = Column(String)
    property_fish = Column(String)
    property_currently_listed = Column(String)
    property_currently_listed_mapped = Column(Boolean)
    property_list_price = Column(Numeric)
    property_management_fee = Column(Numeric)
    property_purchase_price = Column(Numeric)
    property_taxes = Column(Numeric)
    property_type = Column(String)
    property_valuation_comps_link = Column(String)
    rate_cap_first = Column(Numeric)
    rate_cap_life = Column(Numeric)
    rate_cap_periodic = Column(Numeric)
    rate_lookback_period = Column(Numeric)
    rate_max_life = Column(Numeric)
    rate_min_life = Column(Numeric)
    rate_reset_date_first = Column(DateTime(timezone=True), default=func.now())
    rate_reset_date_next = Column(DateTime(timezone=True), default=func.now())
    rate_reset_frequency = Column(Numeric)
    rate_rounding_method = Column(Numeric)
    rate_rounding_method_mapped = Column(String)
    referral_fee = Column(Numeric)
    refinance_of_existing_debt = Column(Boolean)
    refinancing_amount = Column(Numeric)
    related_companies = Column(String)
    released_ltv = Column(Numeric)
    reminder_day_checked = Column(DateTime(timezone=True), default=func.now())
    remittance_account_name = Column(String)
    remittance_account_number = Column(String)
    remittance_bank_name = Column(String)
    remittance_city = Column(String)
    remittance_postal_zip_code = Column(String)
    remittance_routing_number = Column(String)
    remittance_state = Column(String)
    remittance_street_address = Column(String)
    report_type = Column(String)
    retail_construction_amount1 = Column(Numeric)
    services = Column(String)
    servicing_fee = Column(Numeric)
    servicing_transfer_date = Column(DateTime(timezone=True), default=func.now())
    settlement_date = Column(DateTime(timezone=True), default=func.now())
    settlement_statement_hud = Column(Boolean)
    source_id = Column(String)
    submission_date = Column(DateTime(timezone=True), default=func.now())
    subordinate_financing = Column(Boolean)
    summary = Column(String)
    summary_loan_app = Column(String)
    term_sheet_signed = Column(Boolean)
    testing = Column(Boolean)#?
    total_default_interest = Column(Numeric)
    total_experience = Column(String)
    total_interest_paid = Column(Numeric)
    total_loan_calculated = Column(Numeric)
    total_ltc = Column(Numeric)
    total_normal_interest = Column(Numeric)
    total_project_cost = Column(Numeric)
    total_purchase_price = Column(Numeric)
    total_unpaid_late_fees = Column(Numeric)
    valuation_comments = Column(String)
    valuation_fee = Column(Numeric)
    wcp_past_borrower = Column(Boolean)
    wire_approval_ready = Column(Boolean)
    wire_confirmation = Column(String)
    wire_sent_on = Column(DateTime(timezone=True), default=func.now())
    
    created_by = Column(String)
    created_date = Column(DateTime(timezone=True), default=func.now())
    modified_date = Column(DateTime(timezone=True), default=func.now())

class Company(Base):
    __tablename__ = 'loan_backup'
    unique_id = Column(String, primary_key=True)

    account_number = Column(Numeric)
    address_full_text = Column(String)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    amendments_resolution = Column(String)
    article_of_incorporation = Column(String)
    articles_of_organization_article_of_incorporation = Column(String)
    authorized_signor_resolution = Column(String)
    bank_address = Column(String)
    bank_forcreditto = Column(String)
    bank_name = Column(String)
    bank_specialinstructions = Column(String)
    borrower_entity = Column(String)
    by_laws_corporation = Column(String)
    certificate_of_good_standing_fact_status_existence = Column(String)
    city = Column(String)
    company_id = Column(String)
    company_photo = Column(String)
    company_type = Column(String)
    country = Column(String)
    ein = Column(String)
    email_address = Column(String)
    entity_type = Column(String)
    fish_id = Column(Numeric)
    foreign_entity_registration = Column(String)
    formation_date = Column(DateTime(timezone=True), default=func.now())
    loan = Column(String)
    name = Column(String)
    operating_agreement = Column(String)
    primary_contact_custom_fish_contact = Column(String)
    primary_phone = Column(String)
    property_fish_custom_property1 = Column(String)
    property = Column(String)
    related_members_shares = Column(String)
    routing_number = Column(Numeric)
    shareholder_list_stock_certificate = Column(String)
    sole_member_llc = Column(Boolean)
    state_of_incorporation = Column(String)
    state = Column(String)
    w9_form = Column(String)
    zip = Column(String)

    created_by = Column(String)
    created_date = Column(DateTime(timezone=True), default=func.now())
    modified_date = Column(DateTime(timezone=True), default=func.now())

class Funding(Base):
    __tablename__ = 'loan_backup'
    unique_id = Column(String, primary_key=True)

    arbitrage = Column(String)
    archived  = Column(DateTime(timezone=True), default=func.now())
    default_fee_split = Column(Numeric)
    funded_amount = Column(Numeric)
    funded_base = Column(Numeric)
    end_date = Column(DateTime(timezone=True), default=func.now())
    start_date = Column(DateTime(timezone=True), default=func.now())
    interest_percent_of_total = Column(Numeric)
    interest_rate = Column(Numeric)
    investor_company = Column(String)
    investor_type = Column(String)
    late_payment_fee_split = Column(Numeric)
    loan = Column(String)
    no_of_days = Column(Numeric)
    percentage_of_loan = Column(Numeric)
    purchase_date = Column(Numeric)
    source_record_id =  Column (String)
    temporary = Column(DateTime(timezone=True), default=func.now())
    dynamics_investor_company = Column(String)
    z_dynamics_loan = Column(String)
    created_by = Column(String)
    created_date = Column(DateTime(timezone=True), default=func.now())
    modified_date = Column(DateTime(timezone=True), default=func.now())



class InsertPostgres:
    def __init__(self, hostname: str, username: str, password: str, database: str):
        self.engine = create_engine(f'postgresql://{username}:{password}@{hostname}/{database}')
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
        mapper = inspect(Loan)
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

                loan_dict = self.create_loan_dict(data) #call self.create_loan_dict
                loan_dict['unique_id'] = data['_id'] + str(123) #sync with joe

                loan_entry = Loan(**loan_dict)

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

test_url = 'https://ifish.tech/version-7yyc/api/1.1/obj'
apikey = 'ac090d3276b654b46f8dc62f52a50452'
bubble_api = BubbleAPI(test_url, apikey)
json_list = bubble_api.GET_all_objects('Loan')

processed_json = json.dumps(json_list)

postgres_api = InsertPostgres(hostname, username, password, database)
postgres_api.insert_json_data(processed_json)


'''
    third_party_arv = Column(Integer)
    third_party_arv_beds = Column(Integer)
    third_party_asis = Column(Integer)
    third_party_arv_baths = Column(Integer)
    third_party_asis_beds = Column(Integer)
    third_party_asis_baths = Column(Integer)
    third_party_est_repair_cost = Column(Integer)
    third_party_sqft_arv = Column(Integer)
    third_party_sqft_asis = Column(Integer)

'''