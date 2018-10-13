import csv 

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile,
        delimiter =';',
        quotechar = '"',
        quoting = csv.QUOTE_NONNUMERIC,
        fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


with open('names.csv', newline='') as csvfile:
    reader=csv.reader(csvfile,
        delimiter =';',
        quotechar = '"',
        quoting = csv.QUOTE_NONNUMERIC)
    for row in reader:
        #print(row['first_name'], row['last_name'])
        print(row)
        