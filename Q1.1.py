import csv
import os
import sys




# Define the directory where the CSV files are located and output text file name
csv_directory = './CSVs'
# Define the destination txt file path
output_txt_file = './output_data.txt'

# Get a list of all CSV files in the directory
csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

# Create a set that will contain all the column names found in all CSV files
all_columns = set()

for file_name in csv_files:
    with open(os.path.join(csv_directory, file_name), mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        all_columns.update(csv_reader.fieldnames)


# Write the merged data to the txt file
# Using newline='' to prevent adding extra newline characters in Windows
with open(output_txt_file, 'w', newline='', encoding='utf-8') as txtfile:
    writer = csv.DictWriter(txtfile, fieldnames=all_columns, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
      # Process each CSV file
    for file_name in csv_files:
        with open(os.path.join(csv_directory, file_name), mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            # Read each row in the CSV file
            for row in csv_reader:
                # Only write shared columns to the .txt file
                shared_data = {col: row.get(col, '') for col in all_columns}
                writer.writerow(shared_data)

print(f'Data has been successfully merged into {output_txt_file}')
