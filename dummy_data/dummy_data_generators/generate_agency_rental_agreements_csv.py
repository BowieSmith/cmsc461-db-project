import sys
import random

# check for correct number of args. Give usage if incorrect.
if len(sys.argv) != 3:
    print("Usage: python3 generate_agency_rental_agreements_csv.py <no_records> <filename>")
    sys.exit()

# extract agency_ids from customer_agency.csv file
agency_ids = []
with open('../customer_agency.csv') as cust_agency_file:
    for line in cust_agency_file:
        agency_ids.append(line.split(',')[0])
agency_ids.remove('agency_id')

# extract rental agreement ids from rental_agreements.csv file
ra_ids = []
with open('../rental_agreements.csv') as ra_file:
    for line in ra_file:
        ra_ids.append(line.split(',')[0])
ra_ids.remove('ra_id')

# generate random combinations of agency_ids and ra_ids
agency_id_ra_id_combos = set()
for i in range(int(sys.argv[1])):
    agency_id_ra_id_combos.add((agency_ids[random.randint(0, len(agency_ids) - 1)],
                ra_ids[random.randint(0, len(ra_ids) - 1)]))

# write random records to file named given by user
with open(sys.argv[2], 'w') as agency_ra_csv_file:
    agency_ra_csv_file.write('agency_id,ra_id\n')
    for agency_id,ra_id in list(agency_id_ra_id_combos):
        agency_ra_csv_file.write(f'{agency_id},{ra_id}\n')

