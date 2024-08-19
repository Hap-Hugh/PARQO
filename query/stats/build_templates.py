import re
from collections import defaultdict

# Read the input queries from the file
with open('queries.txt', 'r') as file:
    queries = file.readlines()

# Define a dictionary to store queries grouped by involved tables
grouped_queries = defaultdict(list)

# Regular expression pattern to match all table names
table_pattern = r'\b(?:FROM|JOIN)\s+((?:\w+\s+as\s+\w+|\w+)(?:\s*,\s*(?:\w+\s+as\s+\w+|\w+))*)'

# Iterate over each query
for query in queries:
    # Extract all table names from the query
    tables = set(re.findall(table_pattern, query, flags=re.IGNORECASE)[0].replace(' as ', ' ').split(', '))
    # Convert the set of table names to a sorted tuple
    tables = tuple(sorted(tables))
    # Append the query to the corresponding group based on the involved tables
    grouped_queries[tables].append(query.strip())

# Sequentially label each set of tables (template)
table_labels = {}
label_count = 1
for tables in grouped_queries.keys():
    if tables not in table_labels:
        table_labels[tables] = f"{label_count}"
        label_count += 1

# Create SQL files for each query template
for tables, queries in grouped_queries.items():
    label = table_labels[tables]
    letter_count = 97  # ASCII code for 'a'
    for query in queries:
        # Add newline characters as requested
        query = query.replace('FROM', '\nFROM')
        query = query.replace(',', ',\n')
        query = query.replace('WHERE', '\nWHERE')
        query = query.replace('AND', '\nAND')
        # Write the query to a SQL file
        filename = f"stats_{label}{chr(letter_count)}.sql"
        with open(filename, 'w') as file:
            file.write(query)
        letter_count += 1

print("SQL files created.")
