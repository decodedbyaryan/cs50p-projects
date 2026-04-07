def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    for character in s:
        if not character.isalnum():
            return False
    found_number = False
    for character in s:
        if character.isdigit():
            found_number = True
        if found_number and character.isalpha():
            return False
    for character in s:
        if character.isdigit():
            if character == "0":
                return False
            break    
    return True




main()