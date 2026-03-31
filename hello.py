def main():
    name = input("What's yor name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()