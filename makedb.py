import sqlite3

conn = sqlite3.connect('soap.db')
if conn is not None:
	c = conn.cursor()

	sql_cr_gsa_office = """
                CREATE TABLE IF NOT EXISTS gsa_office (
		office_name text PRIMARY KEY,
		office_city text,
		sqft_managed real);"""

	sql_cr_customer_agency = """
                CREATE TABLE IF NOT EXISTS customer_agency ( 
		agency_id text PRIMARY KEY,
		street_name text,
		street_number text,
		agency_city text,
		agency_state text,
		zip_code text,
		phone_number text);"""

	sql_cr_rental_agreements = """
                CREATE TABLE IF NOT EXISTS rental_agreements (
		ra_id text PRIMARY KEY,
		office_name text,
		rent_amount real, 
		end_month integer,
		end_day integer,
		end_year integer,
                FOREIGN KEY (office_name) REFERENCES gsa_office(office_name));"""

	sql_cr_agency_rental_agreements = """
                CREATE TABLE IF NOT EXISTS agency_rental_agreements (
		agency_id text,
		ra_id text,
		FOREIGN KEY (agency_id) REFERENCES customer_agency(agency_id),
		FOREIGN KEY (ra_id) REFERENCES rental_agreements(ra_id));"""

	c.execute(sql_cr_gsa_office)
	c.execute(sql_cr_customer_agency)
	c.execute(sql_cr_rental_agreements)
	c.execute(sql_cr_agency_rental_agreements)
	conn.close()

else: 
	print("Error creating database.")
