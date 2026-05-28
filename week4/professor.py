import random


def main():

    level = get_level()
    score = 0 


    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        
        for q in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == x + y:
                    score += 1
                    break

                else:
                    print("EEE")
                    continue
            except ValueError:
                print("EEE")
            
        else:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")            



def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level < 1 or level > 3:
                continue

            else:
                return level 

        except ValueError:
            continue

def generate_integer(level):

    if level == 1:
        n = random.randint(0, 9)

    elif level == 2:
        n = random.randint(10, 99)
        

    else:
        n = random.randint(100, 999) 
    return(n)


if __name__ == "__main__":
    main()