CREATE TABLE payment (
    unique_id VARCHAR PRIMARY KEY,
    raw_json JSON NULL,
    a_amount_due NUMERIC NULL,
    a_amount_paid NUMERIC NULL,
    a_default_fee NUMERIC NULL,
    a_default_per_diem NUMERIC NULL,
    a_ending_principal NUMERIC NULL,
    a_fee_override_reason VARCHAR NULL,
    a_payment_credit NUMERIC NULL,
    a_per_diem NUMERIC NULL,
    charged_on TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NULL,
    cleared_on TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NULL,
    date_due TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NULL,
    days_of_interest NUMERIC NULL,
    dynamics_r_loan VARCHAR NULL,
    dynamics_u_payee VARCHAR NULL,
    failed_on TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NULL,
    fish_id NUMERIC NULL,
    interest_rate NUMERIC NULL,
    interest_start_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NULL,
    late_fee NUMERIC NULL,
    r_loan VARCHAR NULL,
    loan_application VARCHAR NULL,
    p_customer_id VARCHAR NULL,
    p_days_past_due NUMERIC NULL,
    p_failure_code VARCHAR NULL,
    p_failure_message VARCHAR NULL,
    p_payment_method VARCHAR NULL,
    p_scheduled_on TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NULL,
    p_source_id VARCHAR NULL,
    p_stripe_status VARCHAR NULL,
    paid_default_fee NUMERIC NULL,
    paid_late_fee NUMERIC NULL,
    paid_principle NUMERIC NULL,
    payee VARCHAR NULL,
    payment_amount NUMERIC NULL,
    payment_id1 VARCHAR NULL,
    payment_id VARCHAR NULL,
    payment_subtype VARCHAR NULL,
    payment_type VARCHAR NULL,
    payment_url VARCHAR NULL,
    prepaid_balance_postpayment NUMERIC NULL,
    prepaid_interest NUMERIC NULL,
    price_id VARCHAR NULL,
    principal_amount NUMERIC NULL,
    related_payment VARCHAR NULL,
    source_record_id VARCHAR NULL,
    status VARCHAR NULL,
    t_other_statuses_list VARCHAR NULL,
    created_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NULL,
    modified_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NULL,
    created_by VARCHAR NULL
);