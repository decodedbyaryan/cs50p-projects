import random

def main():
    while True:
        try:
            n = int(input("Level: "))

            if n <= 0:
                continue

            else:
                break

        except ValueError:
            continue
        
    random_num = random.randint(1, n)
        
    while True:
        try:
            guess = int(input("Guess: "))

            if guess <= 0:
                continue
            
            elif guess < random_num:
                print("Too small!")

            elif guess > random_num:
                print("Too large")

            else:
                print("Just right!")
                break

        except ValueError:
            continue

main()
