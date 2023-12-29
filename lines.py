import sys


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a python file")

    counter = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#"):
                    continue
                elif line == "":
                    continue
                else:
                    counter += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(counter)


if __name__ == "__main__":
    main()
