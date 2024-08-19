import re
from collections import defaultdict

# Read input file and extract predicates
with open('query.txt', 'r') as file:
    lines = file.readlines()


# Define a defaultdict to store predicates grouped by table name
predicates_by_table = defaultdict(list)
join_predicates = []

# Regular expression pattern to match predicates
predicate_pattern = r'\b(\w+)\.(\w+)\s*([=<>!]+)\s*([^;]+)'

# Regular expression pattern to match join predicates
join_predicate_pattern = r'(\b\w+\b)\.(\w+)\s*=\s*(\b\w+\b)\.(\w+)'

# Iterate over each line in the input file
for line in lines:
    # Split the line by "AND" to divide conditions
    conditions = line.split('AND')
    # Iterate over each condition
    temp_predicates = {}

    for condition in conditions:
        # Find all matches of the join predicate pattern in the condition
        join_matches = re.findall(join_predicate_pattern, condition)
        # If join predicates found, add them to the join_predicates list
        if len(join_matches) > 0:
            for match in join_matches:
                # Extract table names from the match and form a join predicate
                join_predicates.append((match[0], match[1], match[2], match[3]))
        else:
            # Find all matches of the predicate pattern in the condition
            matches = re.findall(predicate_pattern, condition)
            # Iterate over each match (predicate)
            for match in matches:
                # Extract table name from the match
                table_name = match[0]
                # Append the predicate with the table name
                if table_name not in temp_predicates.keys():
                    temp_predicates[table_name] = f"{match[0]}.{match[1]} {match[2]} {match[3]}"
                else:
                    temp_predicates[table_name] = temp_predicates[table_name] + f"AND {match[0]}.{match[1]} {match[2]} {match[3]}"
        # print("dict: ", temp_predicates)
            
    for table_name, predicates in temp_predicates.items():
        predicates_by_table[table_name].append(predicates)

# Open lsc.txt file for writing
with open('lsc.txt', 'w') as file:
    # Write the content to the file
    for table_name, predicates in predicates_by_table.items():
        # Write table name
        # file.write(f"Table: {table_name}\n")
        # Write predicates
        for predicate in predicates:
            file.write(f"{predicate}\n")
        # Add an empty line between tables
        # file.write('\n')



from collections import Counter

# Read the content of the lsc.txt file
with open('lsc.txt', 'r') as file:
    lines = file.readlines()

# Count the frequency of each row
row_counts = Counter(lines)

# Write distinct rows to a new file
with open('distinct_rows.txt', 'w') as distinct_file:
    distinct_rows = list(row_counts.keys())
    distinct_file.writelines(distinct_rows)

# Write frequencies to another file
with open('row_frequencies.txt', 'w') as frequencies_file:
    for row, count in row_counts.items():
        frequencies_file.write(f"{count}\n")

print("Files created: distinct_rows.txt and row_frequencies.txt")
