def main():
    time = (input("What's the time right now? "))
    result = convert(time)
    if 7 <= result <= 8:
        print("Breakfast Time")
    elif 12 <= result <= 13:
        print("Lunch Time")
    elif 18 <= result <= 19:
        print("Dinner Time")
    else:
        print("")

def convert(time):
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours + minutes / 60



if __name__ == "__main__":
    main()