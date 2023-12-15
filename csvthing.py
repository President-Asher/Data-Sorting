import csv

peopleover64 = 0

seniors = []

with open('Sample_Data_Age.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) 
    
    for row in csv_reader:
        age = int(row[1])  
        if age > 64:
            peopleover64 += 1

print(f"Over the age of 64: {peopleover64}")

with open('Sample_Data_Age.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        age = int(row[1])  # Convert age from string to integer
        if age >= 65:
            seniors.append(row)

# Write the seniors' data to a new CSV file
with open('seniors.csv', mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)

    # Write the header
    csv_writer.writerow(['Name', 'Age'])

    # Write the data
    for row in seniors:
        csv_writer.writerow(row)