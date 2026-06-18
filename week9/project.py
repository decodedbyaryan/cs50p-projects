import argparse
import csv

def main():
    """runs the desired function"""
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    args = parser.parse_args()

    if args.command == "add":
        name = input("Name: ")
        amt = float(input("Amount: ", ))
        add_expenses(name, amt)
    elif args.command == "view":
        for row in get_expenses():
            print(f"{row[0]} - {row[1]}")

    elif args.command == "total":
        print(f"Total: ${get_total():.2f}")

    else:
        print("Please enter a valid input")


def add_expenses(name: str, amt: float) -> None:
    """Adds a new expense to the list"""
    with open("expenses.csv", "a", newline= "") as file:
        writer = csv.writer(file)
        writer.writerow([name, amt])
    
    
def get_expenses() -> list:
    """Shows the list of expenses"""
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        expenses = []
        for row in reader:
            expenses.append(row)
        return expenses


def get_total() -> float:
    """Gives the total of all the expenses"""
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        total = 0
        for row in reader:
            total += float(row[1])
        return total

if __name__ == "__main__":
    main()