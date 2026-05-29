def main():

    word = input("your input ")

    result = shorten(word)
    print(result)

def shorten(word):
    
    a = ["a", "e", "i", "o", "u"]

    result = ""
    for character in word:   
        if character.lower() not in a:
            result = result + character

    return(result)


if __name__ == "__main__":
    main()