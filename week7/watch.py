import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    result = re.search(r"/embed/(\w+)", s)

    if result:
        return(f"https://youtu.be/{result.group(1)}")
    
    else:
        return None





if __name__ == "__main__":
    main()