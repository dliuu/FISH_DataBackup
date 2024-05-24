create table disbursement (
	unique_id varchar(36) not null primary key,
	amount_collected numeric null,
	disb_amount numeric null,
	amount_owed numeric null,
	disbursement_type varchar(2000) null,
	end_date timestamptz null,
	funding varchar(2000) null,
	loan varchar(2000) null,
	loan_payment_parent varchar(2000) null,
	payment varchar(2000) null,
	source_record_id varchar(2000) null,
	start_date timestamptz null,
	status varchar(2000) null,
	temp_amt numeric null,
	created_by varchar(36) null,
	created_date date null,
	modified_date date null
)