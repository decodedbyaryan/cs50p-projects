from datetime import date
from num2words import num2words
import re
import sys

def main():
    dob = input("What is you dob? YYYY-MM-DD ")
    match = re.fullmatch(r"(\d{4})\-(\d{2})\-(\d{2})", dob)
    if not match:
        sys.exit("Invalid Input or Format")
    
    yyyy = int(match.group(1))
    mm = int(match.group(2))
    dd = int(match.group(3))

    try:
        birthday = date(yyyy, mm, dd)
    except ValueError:
        sys.exit("Invalid DOB")

    today_date = date.today()

    minutes = calculate(birthday, today_date)
    word_out = num2words(minutes).replace(" and "," ").replace(",","")
    print(word_out + "minutess")

def calculate(birthday, today_date):
    cal = (today_date - birthday).days * 1440
    return cal


if __name__ == "__main__":
    main()