import inflect

def main():

    p = inflect.engine()
    names = []

    

    while True:
        try:
            user_input = input("Name: ")
            names.append(user_input)
            
            


        except EOFError:
            break

    print("Adieu, Adieu, to " + p.join(names))


main()