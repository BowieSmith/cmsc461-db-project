import sqlite3, csv

# Connect to database
db = sqlite3.connect('soap.db')

# Do the following if connected to database
if db is not None:
    cur = db.cursor()

    # List path and files used to upload data
    path = 'dummy_data/'
    filenames = ['gsa_office', 'customer_agency', 'rental_agreements', 'agency_rental_agreements']
    for filename in filenames:
        # Open the CSV file and read it
        csv_file = open(path+filename+'.csv', 'r')
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Skip first line
        next(csv_reader)
        
        # Insert data from CSV into appropriate table
        for item in csv_reader:
            # Basic SQL statement to insert data into the tables
            sql_import_data = 'INSERT INTO ' + filename + ' VALUES '

            # Execute the appropriate SQL statement based on the file name, which
            # matches the corresponding table name
            if(filename == 'gsa_office'):
                cur.execute(sql_import_data + '(?,?,?)', item)
            elif(filename == 'customer_agency'):
                cur.execute(sql_import_data + '(?,?,?,?,?,?,?)', item)
            elif(filename == 'rental_agreements'):
                cur.execute(sql_import_data + '(?,?,?,?,?,?)', item)
            else:
                cur.execute(sql_import_data + '(?,?)', item)

    # Close file and cursor
    csv_file.close()
    cur.close()

    # Commit changes to database so it properly updates
    db.commit()
    db.close()

else:
    print("Error connecting to database. Cannot import dummy data.")