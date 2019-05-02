import sys
import random

# check for correct number of args. Give usage if incorrect.
if len(sys.argv) != 3:
    print("Usage: python3 generate_rental_agreements_csv.py <no_records> <filename>")
    sys.exit()

# extract gsa offices from gsa_office.csv file
gsa_offices = []
with open('../gsa_office.csv') as gsa_file:
    for line in gsa_file:
        gsa_offices.append(line.split(',')[0])
gsa_offices.remove('office_name')

# generate random rental_agreement_ids. Equal to total number passed in by user.
ra_ids = set()
for i in range(int(sys.argv[1])):
    ra_ids.add('R' + str(random.randint(0,999999)).zfill(6))

# write random records to file named given by user
with open(sys.argv[2], 'w') as ra_csv_file:
    ra_csv_file.write('ra_id,office_name,rent_amount,end_month,end_day,end_year\n')
    for ra_id in list(ra_ids):
        office_name = gsa_offices[random.randint(0, len(gsa_offices) - 1)]
        rent_amount = 1000 * random.randint(1,1000)
        end_month = random.randint(1,12)
        end_day = random.randint(1,31)
        end_year = random.randint(2019,2050)
        ra_csv_file.write(f'{ra_id},{office_name},{rent_amount},{end_month},{end_day},{end_year}\n')

