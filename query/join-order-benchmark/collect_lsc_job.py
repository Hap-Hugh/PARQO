from collections import Counter

# Read the content of the lsc.txt file
with open('LSC-Train.txt', 'r') as file:
    lines = file.readlines()

# Count the frequency of each row
row_counts = Counter(lines)

# Write distinct rows to a new file
with open('job_distinct_rows.txt', 'w') as distinct_file:
    distinct_rows = list(row_counts.keys())
    distinct_file.writelines(distinct_rows)

# Write frequencies to another file
with open('job_row_frequencies.txt', 'w') as frequencies_file:
    for row, count in row_counts.items():
        frequencies_file.write(f"{count}\n")

print("Files created: distinct_rows.txt and row_frequencies.txt")