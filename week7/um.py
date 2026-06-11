import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um = len(re.findall(r"\bum\b", s.lower()))
    return um

    

if __name__ == "__main__":
    main()