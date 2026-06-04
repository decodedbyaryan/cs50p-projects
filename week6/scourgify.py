import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Invalid number of arguments")

try:
    with open(f"{sys.argv[1]}", "r" ) as infile:
        with open(f"{sys.argv[2]}", "w", newline="") as outfile:

            befores =csv.DictReader(infile)

            write = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            write.writeheader()

            for row in befores:
                last, first = row["name"].split(", ")
                house = row["house"]
                write.writerow({"first": first, "last": last, "house": house})

    



        
    
except FileNotFoundError:
    sys.exit("Unable to read the file")