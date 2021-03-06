# cmsc461-db-project

### How To
`python3 setup.py` to build and load database

`python3 soap_app.py` to run application

Note:

`setup.py` requires correctly formatted csv files in the dummy_data folder
with the following names:
- customer_agency.csv
- gsa_office.csv
- rental_agreements.csv
- agency_rental_agreements.csv

Existing data in the repository should work fine, but dummy data generators are
included if more data is needed. See below for more details.

### About
Small project creating a database driven application based on mock requirements.
Emphasis is on creating an ERM model and DDL SQL script.
Application code is provided to query database from a terminal.
This is a console based application built with python and sqlite.

### ER Diagrams and Relational Diagrams
The Entity Relationship Diagrams and Relational Diagrams were created using draw.io
The .drawio files contained in this repository can be used to upload and modify the diagrams.
The pdf files were generated by exporting the draw.io diagrams as pdf.

### Dummy Data
The gsa_office and customer_agency tables are independent. They do not reference
any foreign keys. However, both the rental_agreements and agency_rental_agreements
tables have foreign key references. In order to generate dummy data for these tables
with correct references, a script is used which pulls valid foreign references
from the gsa_office and customer_agency csv files. To use the scripts, move to the
following directory: `dummy_data/dummy_data_generators`
and execute the following commands:

`python3 generate_rental_agreements_csv.py <no_records> <filename>`

`python3 generate_agency_rental_agreements_csv.py <no_records> <filename>`

To use the new files, name them appropriately (as rental_agreements.csv
or agency_rental_agreements.csv) and move to the dummy_data folder.
