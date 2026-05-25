def main():


    counts = {}

    while True:
        try:
            items = input("Grocery Items: ").upper()

            counts[items] = counts.get(items, 0) + 1

        except EOFError:
            break


    for items in sorted(counts):
        print(counts[items], items)


main()