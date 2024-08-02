import json
import psutil

from sqlalchemy import create_engine, Column, Integer, JSON, Float, String, Boolean, Numeric, Time, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
import datetime

process = psutil.Process()

Base = declarative_base()

class Loan(Base):
    __tablename__ = 'loan_backup'
    __table_args__ = {'extend_existing': True}
    unique_id = Column(String, primary_key=True)
    raw_json = Column(JSON)

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
    __tablename__ = 'company'
    __table_args__ = {'extend_existing': True}
    unique_id = Column(String, primary_key=True)
    raw_json = Column(JSON)

    account_number = Column(Numeric)
    address_full_text = Column(String)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    amendments_resolution = Column(String)
    article_of_incorporation = Column(String)
    articles_of_organization_article_of_corporation = Column(String)
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
    __tablename__ = 'funding'
    __table_args__ = {'extend_existing': True}
    unique_id = Column(String, primary_key=True)
    raw_json = Column(JSON)

    arbitrage = Column(String)
    archived  = Column(DateTime(timezone=True), default=func.now())
    default_fee_split = Column(Numeric)
    funded_amount = Column(Numeric)
    funded_base = Column(Numeric)
    funded_end_date = Column(DateTime(timezone=True), default=func.now())
    funded_start_date = Column(DateTime(timezone=True), default=func.now())
    interest_percent_of_total = Column(Numeric)
    interest_rate_split = Column(Numeric)
    investor_company = Column(String)
    investor_type = Column(String)
    late_payment_fee_split = Column(Numeric)
    loan = Column(String)
    no_of_days = Column(Numeric)
    percentage_of_loan = Column(Numeric)
    purchase_date = Column(DateTime(timezone=True), default=func.now())
    source_record_id =  Column(String)
    temporary = Column(DateTime(timezone=True), default=func.now())
    #dynamics_investor_company = Column(String)
    z_dynamics_loan = Column(String)
    created_by = Column(String)
    created_date = Column(DateTime(timezone=True), default=func.now())
    modified_date = Column(DateTime(timezone=True), default=func.now())

class Disbursement(Base):
    __tablename__ = 'disbursement'
    __table_args__ = {'extend_existing': True}
    unique_id = Column(String, primary_key=True)
    raw_json = Column(JSON)

    amount_collected = Column(Numeric)
    #disb_amount = Column(Numeric)
    amount_owed = Column(Numeric)
    disbursement_type = Column(String)
    end_date = Column(DateTime(timezone=True), default=func.now())
    fish_id = Column(Numeric)
    funding = Column(String)
    loan = Column(String)
    loan_payment_parent = Column(String)
    payment = Column(String)
    source_record_id = Column(String)
    start_date = Column(DateTime(timezone=True), default=func.now())
    status = Column(String)
    temp_amt = Column(Numeric)

    created_by = Column(String)
    created_date = Column(DateTime(timezone=True), default=func.now())
    modified_date = Column(DateTime(timezone=True), default=func.now())

class Contact(Base):
    __tablename__ = 'contact'
    __table_args__ = {'extend_existing': True}
    unique_id = Column(String, primary_key=True)
    raw_json = Column(JSON)

    three_years_experiences = Column(String)
    account_owner = Column(String)
    account_type = Column(String)
    active_client = Column(Boolean)
    active_deals = Column(Numeric)
    additional_email_address = Column(String)
    additional_phone_number = Column(String)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    asian_races = Column(String)
    available_funds = Column(String)
    avatar = Column(String)
    bdr_owner = Column(String)
    borrower_delinquent_on_any_loans = Column(Boolean)
    borrower_experiences = Column(String)
    borrower_provided_credit_score = Column(String)
    borrower_reward_tier = Column(String)
    city = Column(String)
    contact_disposition = Column(String)
    contact_dispositions = Column(String)
    contact_method_preference = Column(String)
    contact_temp = Column(String)
    contact_type = Column(String)
    county = Column(String)
    credit_report_date = Column(DateTime(timezone=True), default=func.now())
    date_of_birth = Column(DateTime(timezone=True), default=func.now())
    demographic_info_provided_through = Column(String)
    dynamics_id = Column(String)
    effective_date = Column(DateTime(timezone=True), default=func.now())
    email_address = Column(String)
    enrolled_principle_tribe = Column(String)
    ethnicity = Column(String)
    ethnicity_via_observation = Column(String)
    fax_number = Column(String)
    fico_score = Column(Numeric)
    first_name = Column(String)
    fish_id = Column(String)
    foreign_national = Column(String)
    full_name = Column(String)
    gender_via_observation = Column(String)
    guarantor_address_line_1 = Column(String)
    guarantor_address_line_2 = Column(String)
    guarantor_address_line_3 = Column(String)
    guarantor_contact_information = Column(String)
    guarantor_county = Column(String)
    guarantor_email = Column(String)
    guarantor_first_name =  Column(String)
    guarantor_full_address = Column(String)
    guarantor_last_name = Column(String)
    guarantor_phone = Column(String)
    guarantor_state = Column(String)
    guarantor_zip = Column(String)
    hispanic_or_latino = Column(Boolean)
    hubspot_id = Column(String)
    import_contact_dispositions = Column(String)
    islander_race = Column(String)
    job_title = Column(String)
    last_name = Column(String)
    loan = Column(String)
    loan_apps = Column(String)
    loan_officer = Column(String)
    loan_team = Column(String)
    mailing_address = Column(String)
    middle_fico = Column(String)
    middle_name = Column(String)
    mobile_phone_number = Column(String)
    mortgage_lates_past_12_months = Column(Boolean)
    number_of_borrower_experiences = Column(Numeric)
    oafc = Column(String)
    other_asian_race = Column(String)
    other_islander_race = Column(String)
    owner1 = Column(String)
    permissions_editable_users = Column(String)
    phone_number = Column(Numeric)
    phone_number_1 = Column(String)
    preferred_language = Column(String)
    properties_fish = Column(String)
    race = Column(String)
    race_via_observation = Column(String)
    related_companies = Column(String)
    rental_projects = Column(String)
    reward_points = Column(Numeric)
    reward_tier = Column(String)
    sex = Column(String)
    ssn = Column(String)
    state1 = Column(String)
    statement_dates = Column(String)
    status = Column(String)
    total_experience = Column(String)
    track_record_projects = Column(String)
    validated_mailing_address = Column(Boolean)
    validated_physical_address = Column(Boolean)
    zip_code = Column(String)

    #created_by = Column(String)
    #created_date = Column(DateTime(timezone=True), default=func.now())
    #modified_date = Column(DateTime(timezone=True), default=func.now())

class Payment(Base):
    __tablename__ = 'payment'
    __table_args__ = {'extend_existing': True}
    unique_id = Column(String, primary_key=True)
    raw_json = Column(JSON)

    a_amount_due = Column(Numeric)
    a_amount_paid = Column(Numeric)
    a_default_fee = Column(Numeric)
    a_default_per_diem= Column(Numeric)
    a_ending_principal= Column(Numeric)
    a_fee_override_reason = Column(String)
    a_payment_credit = Column(Numeric)
    a_per_diem = Column(Numeric)
    charged_on = Column(DateTime(timezone=True), default=func.now())
    cleared_on = Column(DateTime(timezone=True), default=func.now())
    date_due = Column(DateTime(timezone=True), default=func.now())
    days_of_interest = Column(Numeric)
    dynamics_r_loan = Column(String)
    dynamics_u_payee = Column(String)
    failed_on = Column(DateTime(timezone=True), default=func.now())
    fish_id = Column(Numeric)
    interest_rate = Column(Numeric)
    interest_start_date = Column(DateTime(timezone=True), default=func.now())
    late_fee= Column(Numeric)
    r_loan = Column(String)
    loan_application = Column(String)
    p_customer_id = Column(String)
    p_days_past_due = Column(Numeric)
    p_failure_code = Column(String) 
    p_failure_message = Column(String)
    p_payment_method = Column(String)
    p_scheduled_on = Column(DateTime(timezone=True), default=func.now())
    p_source_id = Column(String)
    p_stripe_status = Column(String)
    paid_default_fee = Column(Numeric)
    paid_late_fee = Column(Numeric)
    paid_principle = Column(Numeric)
    payee  = Column(String)
    payment_amount = Column(Numeric)
    payment_id1 = Column(String)
    payment_id = Column(String)
    payment_subtype = Column(String)
    payment_type = Column(String)
    payment_url = Column(String)
    prepaid_balance_postpayment = Column(Numeric)
    prepaid_interest = Column(Numeric)
    price_id = Column(String)
    principal_amount = Column(Numeric)
    related_payment = Column(String)
    source_record_id = Column(String)
    status= Column(String)
    t_other_statuses_list = Column(String)
    
    created_date = Column(DateTime(timezone=True), default=func.now())
    modified_date = Column(DateTime(timezone=True), default=func.now())
    created_by = Column(String)


class Loan_Application(Base):
    __tablename__ = 'loan_application'
    __table_args__ = {'extend_existing': True} 
    unique_id = Column(String, primary_key=True)
    raw_json = Column(JSON)

    second_appraisal_value = Column(Numeric)
    third_party_arv_units = Column(Numeric)
    third_party_as_is_units = Column(Numeric)
    actual_purchase_price_new = Column(Numeric)
    actual_rent_amount = Column(Numeric)
    acquisition_cost = Column(Numeric)
    additional_funds_to_close = Column(Numeric)
    aiv_ltv = Column(Numeric)
    annual_qualifying_rent = Column(Numeric)
    arv = Column(String)
    arv_ltv = Column(Numeric)
    arv_mapped = Column(Numeric)
    as_is_ltv = Column(Numeric)
    assignment_fee = Column(Numeric)
    assignment_fee_percent_credited = Column(Numeric)
    assignment_fee_credit = Column(Numeric)
    available_tasks_count = Column(Numeric)
    balloon_feature = Column(Boolean)
    borrower = Column(String)
    borrower_application = Column(String)
    borrower_arv_units = Column(Numeric)
    borrower_as_is_units = Column(Numeric)
    borrower_brings_to_closing = Column(Numeric)
    borrower_down_payment = Column(Numeric)
    borrower_est_arv = Column(Numeric)
    borrower_est_as_is_mapped = Column(Numeric)
    borrower_est_as_is = Column(String)
    borrower_est_repair_cost = Column(Numeric)
    borrower_provided_arv_bath = Column(Numeric)
    borrower_provided_arv_bed = Column(Numeric)
    borrower_provided_arv_sqft = Column(Numeric)
    borrower_provided_as_is_bath = Column(Numeric)
    borrower_provided_as_is_bed = Column(Numeric)
    borrower_provided_as_is_sqft = Column(Numeric)
    buy_up_down_amount = Column(Numeric)
    buy_up_down = Column(Boolean)
    buy_up_down_bps = Column(Numeric)
    capital_expenditures = Column(Numeric)
    cash_for_deal = Column(Numeric)
    cash_out_refinance_amount = Column(Numeric)
    cashout_hud_mapped = Column(Numeric)
    cashout_hud = Column(String)
    cashout_refinance = Column(Boolean)
    cda_value = Column(Numeric)
    closing_date = Column(DateTime(timezone=True), default=func.now())
    closing_fee = Column(Numeric)
    combined_arv_ltv = Column(Numeric)
    commitment_fee_new = Column(Numeric)
    company_fish = Column(String)
    company_contact_merges = Column(String)
    conditions = Column(String)
    contact = Column(String)
    contacts_loanapp_loan = Column(String)
    contract_price = Column(Numeric)
    cost_spend_to_date = Column(Numeric)
    credit_and_vacancy_loss = Column(Numeric)
    cross_collateral_property_equity = Column(String)
    down_payment_source = Column(String)
    downpayment_percent = Column(Numeric)
    dscr = Column(Numeric)
    effective_ltc = Column(Numeric)
    effective_purchase_price = Column(Numeric)
    effective_total_cost = Column(Numeric)
    estimated_monthly_interest_only_payment = Column(Numeric)
    estimated_revenue = Column(Numeric)
    existing_debt_balance = Column(Numeric)
    feature = Column(String)
    first_adjustment_date = Column(DateTime(timezone=True), default=func.now())
    fish_id = Column(Numeric)
    fixed_rate_period = Column(Numeric)
    geo_tier = Column(String)
    gross_margin = Column(Numeric)
    has_subordinate_financing_new = Column(Boolean)
    hoa_costs = Column(Numeric)
    index_name = Column(String)
    initial_ltc = Column(Numeric)
    initial_rate_change_cap = Column(Numeric)
    insurance_deposit = Column(Numeric)
    insurance_premium = Column(Numeric)
    interest_calculation = Column(String)
    interest_only_feature = Column(Boolean)
    interest_only_term_months = Column(Numeric)
    interest_rate_mapped = Column(Numeric)
    interest_rate = Column(String)
    interest_rate_second_trust = Column(Numeric)
    interest_reserve_new = Column(Numeric)
    interest_type = Column(String)
    intro_rate = Column(Numeric)
    intro_terms_mapped = Column(Numeric)
    intro_terms = Column(String)
    introductory_period = Column(String)
    introductory_rate_mapped = Column(Numeric)
    introductory_rate = Column(String)
    lease_amount = Column(Numeric)
    lease_in_place = Column(Boolean)
    lease_term = Column(Numeric)
    lender_arv_units = Column(Numeric)
    lender_as_is_units = Column(Numeric)
    lifetime_rate_cap = Column(Numeric)
    lifetime_rate_floor = Column(Numeric)
    loan_active = Column(String)
    loan_amount_first_trust = Column(Numeric)
    loan_amount_second_trust = Column(Numeric)
    loan_application_type = Column(String)
    loan = Column(String)
    lo_est_repair_cost = Column(String)
    loan_officer_arv = Column(Numeric)
    loan_officer_as_is_value = Column(Numeric)
    loan_officer_bathrooms_arv = Column(Numeric)
    loan_officer_bathrooms_as_is = Column(Numeric)
    loan_officer_bedrooms_arv = Column(Numeric)
    loan_officer_bedrooms_as_is = Column(Numeric)
    loan_officer_estimated_repair_cost = Column(Numeric)
    loan_officer_sqft_arv = Column(Numeric)
    loan_officer_sqft_as_is = Column(Numeric)
    loan_points = Column(Numeric)
    loan_rate = Column(Numeric)
    loan_strategy = Column(String)
    loan_team = Column(String)
    loan_term_months = Column(Numeric)
    loan_terms = Column(String)
    loan_type = Column(String)
    lock_back_days = Column(Numeric)
    loss_of_rent = Column(Numeric)
    market_rent_amount = Column(Numeric)
    meets_investor_guidelines = Column(Boolean)
    monthly_insurance_amount = Column(Numeric)
    monthly_market_rent = Column(Numeric)
    monthly_p_i = Column(Numeric)
    monthly_property_taxes_amount = Column(Numeric)
    monthly_rent_amount = Column(Numeric)
    months_of_interest_reserves = Column(Numeric)
    months_prepaid_interest = Column(Numeric)
    net_operating_income = Column(Numeric)
    number_of_occupied_units = Column(Numeric)
    occupancy_status = Column(String)
    origination_fee = Column(Numeric)
    other_closing_costs = Column(Numeric)
    other_costs = Column(Numeric)
    past_wcp_borrower = Column(String)
    pdas_approval_comments = Column(String)
    permissions_viewable_users_list_user = Column(String)
    point_of_contact = Column(String)
    points_second_trust = Column(Numeric)
    prepaid_interest = Column(Numeric)
    prepayment_penalty = Column(Boolean)
    prepayment_penalty_term = Column(Numeric)
    prepayment_penalty_old = Column(String)
    prepayment_penalty_type = Column(String)
    previous_purchase_date = Column(DateTime(timezone=True), default=func.now())
    primary_borrower_search = Column(String)
    primary_borrower = Column(String)
    probable_investors = Column(String)
    process = Column(String)
    product_type_not_in_use = Column(String)
    product_type = Column(String)
    program = Column(String)
    program_type = Column(String)
    project_type = Column(String)
    property_fish = Column(String)
    property_currently_listed = Column(Boolean)
    property_last_sale_amount = Column(Numeric)
    property_list_price = Column(Numeric)
    property_management_fee = Column(Numeric)
    property_taxes_deposit = Column(Numeric)
    property_taxes = Column(Numeric)
    property_type = Column(String)
    qualifying_value = Column(Numeric)
    rate_lock = Column(Boolean)
    rate_lock_date = Column(DateTime(timezone=True), default=func.now())
    rate_rounding_method = Column(String)
    referral_fee = Column(Numeric)
    refinance_of_existing_debt = Column(String)
    related_companies = Column(String)
    released_ltv = Column(Numeric)
    repair_and_maintenance_expenses = Column(Numeric)
    requested_closing_date = Column(DateTime(timezone=True), default=func.now())
    requested_construction_fund_amount = Column(String)
    requested_loan_amount = Column(Numeric)
    reset_frequency = Column(Numeric)
    retail_construction_amount = Column(Numeric)
    second_trust_loan_app = Column(String)
    secondary_borrower = Column(String)
    servicing_set_up_fee = Column(Numeric)
    source_record_id = Column(String)
    status = Column(String)
    submission_date = Column(DateTime(timezone=True), default=func.now())
    subsequent_change_cap = Column(Numeric)
    subsequent_change_floor = Column(Numeric)
    summary = Column(String)
    term_sheet_signed = Column(DateTime(timezone=True), default=func.now())
    term_sheet_signed_question = Column(Boolean)
    total_loan_calculated = Column(Numeric)
    total_ltc = Column(Numeric)
    total_operating_expenses = Column(Numeric)
    total_project_cost_calculated = Column(Numeric)
    total_purchase_price = Column(Numeric)
    turnover_costs = Column(Numeric)
    valuation_comments = Column(String)
    valuation_fee = Column(Numeric)
    wcp_purchase_price = Column(Numeric)
    new_borrower_est_as_is = Column(Numeric)
    new_requested_construction_fund_amount = Column(Numeric)

    created_date = Column(DateTime(timezone=True), default=func.now())
    modified_date = Column(DateTime(timezone=True), default=func.now())
    created_by = Column(String)

class Reporting(Base):
    __tablename__ = 'reporting'

    id = Column(Integer, primary_key=True)
    disbursement = Column(String(20), nullable=True)
    disbursement_type = Column(String(30), nullable=True)
    disbursement_interest_start = Column(DateTime(timezone=True), default=func.now())
    disbursement_interest_end = Column(DateTime(timezone=True), default=func.now())
    disbursement_due_on = Column(DateTime(timezone=True), default=func.now())
    disbursement_paid_on = Column(DateTime(timezone=True), default=func.now())
    disbursement_amount_due = Column(Numeric(12, 2), nullable=True)
    disbursement_amount_collected = Column(Numeric(12, 2), nullable=True)
    disbursement_amount_paid = Column(Numeric(12, 2), nullable=True)
    loan = Column(String(20), nullable=True)
    loan_maturity_date = Column(DateTime(timezone=True), default=func.now())
    loan_servicer = Column(String(30), nullable=True)
    loan_foreclosure_start = Column(DateTime(timezone=True), default=func.now())
    loan_foreclosure_on = Column(DateTime(timezone=True), default=func.now())
    loan_foreclosure_schedule_on = Column(DateTime(timezone=True), default=func.now())
    loan_foreclosure_sent_on = Column(DateTime(timezone=True), default=func.now())
    loan_owner = Column(String(30), nullable=True)
    loan_servicing_status = Column(String(30), nullable=True)
    loan_primary_borrower = Column(String(30), nullable=True)
    loan_closing_date = Column(DateTime(timezone=True), default=func.now())
    loan_rate = Column(Numeric(5, 2), nullable=True)
    bankruptcyfiled = Column(Boolean, nullable=True)
    property_address = Column(String(150), nullable=True)
    investor = Column(String(50), nullable=True)
    wcp_loan_amount = Column(Numeric(12, 2), nullable=True)
    wcp_funding_date = Column(DateTime(timezone=True), default=func.now())
    funding_amount = Column(Numeric(12, 2), nullable=True)
    funding_interest_rate = Column(Numeric(5, 2), nullable=True)
    days_of_interest = Column(Numeric, nullable=True)
    next_payment = Column(String(20), nullable=True)
    next_payment_due_on = Column(DateTime(timezone=True), default=func.now())
    payment = Column(String(20), nullable=True)
    payment_due_on = Column(DateTime(timezone=True), default=func.now())
    payment_unpaid_balance = Column(Numeric(12, 2), nullable=True)
    payment_type = Column(String(20), nullable=True)
    last_payment_paid_on = Column(DateTime(timezone=True), default=func.now())
    payment_interest_amount_due = Column(Numeric(12, 2), nullable=True)
    payment_late_fee_due = Column(Numeric(12, 2), nullable=True)
    payment_late_fee_paid = Column(Numeric(12, 2), nullable=True)
    payment_interest_paid = Column(Numeric(12, 2), nullable=True)
    payment_prepaid_interest = Column(Numeric(12, 2), nullable=True)
    payment_amount_due_total = Column(Numeric(12, 2), nullable=True)
    payment_total_interest_paid = Column(Numeric(12, 2), nullable=True)
    payment_total_amount_paid = Column(Numeric(12, 2), nullable=True)
    payment_balance_interest = Column(Numeric(12, 2), nullable=True)
    payment_balance_late_fee = Column(Numeric(12, 2), nullable=True)
    payment_paid_on = Column(DateTime(timezone=True), default=func.now())
    payment_balance_total = Column(Numeric(12, 2), nullable=True)
    payment_status_reason = Column(String(30), nullable=True)
    payment_servicing_status = Column(String(30), nullable=True)
    payoff_received_on = Column(DateTime(timezone=True), default=func.now())
    created_on = Column(DateTime(timezone=True), default=func.now())
