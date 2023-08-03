# overheads.py
import os
from pathlib import Path
import csv

original_working_dir = os.getcwd()

# Set the current working directory to the folder containing the CSV file
csv_folder = os.path.join(os.getcwd(), "csv_reports")
os.chdir(csv_folder)

# Now you can open and read the CSV file
csv_file = "overheads.csv"

with open(csv_file, mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    overhead_data = []

    for row in reader:
        overhead_data.append([row[0].upper(), float(row[1])])

