import random


def main():
    #number of problems:
    i = 0

    #keep track of score aka correctly solved problems:
    score = 0

    #counter for reprompting user the same problem:
    j = 0

    #counter if result-input not an int:
    k = 0

    #level festlegen:
    level = get_level()

    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            try:
                if k < 3:
                    result = int(input(f"{x} + {y} = "))
                    if result == (x+y):
                        i += 1
                        score += 1
                        j = 0
                        break
                    elif j < 2:
                        raise ValueError
                    else:
                        print("EEE")
                        print(f"{x} + {y} = {x+y}")
                        i += 1
                        j = 0
                        break
                else:
                    #print("EEE")
                    print(f"{x} + {y} = {x+y}")
                    i += 1
                    k = 0
                    break
            except ValueError:
                print("EEE")
                j += 1
                k += 1
                pass

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()