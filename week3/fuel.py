def main():
    
    x, y = get_fraction()

    percentage = round(x / y * 100)

    if percentage <= 1:
        print("E")

    elif percentage >= 99:
        print("F")

    else:
        print(f"{percentage}%")


def get_fraction():
    while True:
        try:
            parts = input("Fraction: ").split("/" , 1)

            x = int(parts[0])
            y = int(parts[1])
            
            if x > y or y == 0:
                continue

            else:
                return(x, y)
                


        except ValueError:
            pass
   
main()