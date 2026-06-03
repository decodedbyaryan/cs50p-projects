import sys
from tabulate import tabulate
from csv import DictReader

if len(sys.argv) != 2:
    sys.exit("Invalid number of arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("not .csv file ") 


rows = []
try:
    with open(f"{sys.argv[1]}", "r") as file:
        reader = DictReader(file)
        for row in reader:
            rows.append(row)

        

except FileNotFoundError:
    sys.exit("file doesn't exist")

print(tabulate(rows, headers="keys" ,tablefmt="grid"))