import pyfiglet
import random
import sys

def main():
    try:
        if len(sys.argv) == 1:

            x = random.choice(pyfiglet.FigletFont.getFonts())

            result =pyfiglet.figlet_format(input("input: "), font=x)
            print("Output: " + result)

        elif len(sys.argv) == 3:
            if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                result = pyfiglet.figlet_format(input("input: "), font=sys.argv[2])
                print("Output: " + result)

            else:
                sys.exit("either -f or --font or the second is not the name of a font, please try again")
        else:
            sys.exit()

    except pyfiglet.FontNotFound:
        sys.exit("Invalid input")


main()