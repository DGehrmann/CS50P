import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise ValueError
            else:
                break

        except ValueError:
            pass

    rand = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                raise ValueError
            else:
                if guess < rand:
                    print("Too small!")
                    pass
                elif guess > rand:
                    print("Too large!")
                    pass
                else:
                    print("Just right!")
                    break
                #break

        except ValueError:
            pass




if __name__ == "__main__":
    main()