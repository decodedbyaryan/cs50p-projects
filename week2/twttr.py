text = input("your input ")
a = ["a", "e", "i", "o", "u"]

result = ""
for character in text:   
    if character.lower() not in a:
        result = result + character

print(result)