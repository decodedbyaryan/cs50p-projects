amount = 50
while amount > 0:
    print(f"Amount Due: {amount}")
    insert = int(input("insert coin: "))
    if insert in [5, 10, 25]:
        amount = amount - insert

print(f"Changed Owed: {amount * -1}")
    