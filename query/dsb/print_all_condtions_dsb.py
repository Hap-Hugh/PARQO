import os
import glob

query_id = '_099'

# Define the directory containing .sql files
directory = '/winhomes/hx68/robust-vcm/query/dsb/query_condition' + query_id

# Define the output file name
output_file = '/winhomes/hx68/robust-vcm/query/dsb/DSB-local-sel-cond' + query_id + '.txt'

# Function to read and concatenate rows from .sql files
def read_sql_files(directory):
    all_rows = []
    # Traverse the directory
    for file_path in glob.glob(os.path.join(directory, '*.sql')):
        with open(file_path, 'r') as file:
            # Read rows from the file and concatenate them
            rows = file.readlines()
            all_rows.extend(rows)
    return all_rows

# Read rows from .sql files
all_rows = read_sql_files(directory)

all_rows = [row for row in all_rows if row.strip() and row.strip() != ';']

# Sort the rows
all_rows.sort()

# Write sorted rows to the output file
with open(output_file, 'w') as file:
    file.writelines(all_rows)

print(f"Sorted rows have been written to {output_file}")


# Count the frequency of each row
row_frequency = {}
for row in all_rows:
    if row in row_frequency:
        row_frequency[row] += 1
    else:
        row_frequency[row] = 1

# Write unique rows to the first file and corresponding frequencies to the second file
unique_rows_file = '/winhomes/hx68/robust-vcm/query/dsb/unique_condition'+query_id+'.txt'
frequency_file = '/winhomes/hx68/robust-vcm/query/dsb/frequency'+query_id+'.txt'

# Write unique rows to the first file
with open(unique_rows_file, 'w') as file:
    for row in sorted(row_frequency.keys()):
        file.write(row)

# Write corresponding frequencies to the second file
with open(frequency_file, 'w') as file:
    for row, freq in sorted(row_frequency.items()):
        file.write(f"{freq}\n")

print(f"Unique rows have been written to {unique_rows_file}")
print(f"Frequency of each row has been written to {frequency_file}")