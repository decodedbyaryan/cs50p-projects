camelcase = input("camelCase: ")
result = ""

for character in camelcase:
    if character.isupper():
        result = result + "_" + character.lower()
    else:
        result = result + character

print("snake_case: " + result)