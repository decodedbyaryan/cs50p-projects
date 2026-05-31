def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    parts = fraction.split("/", 1)

    x = int(parts[0])
    y = int(parts[1])
    
    if y == 0:
        raise ZeroDivisionError

    elif x > y: 
        raise ValueError
            
    else:
        return round(x / y * 100)


def gauge(percentage):

    if percentage <= 1:
        return("E")

    elif percentage >= 99:
        return("F")

    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()