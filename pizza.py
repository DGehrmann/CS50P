import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a csv file")

    headers = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            print(tabulate(reader,headers="keys",tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File not found")




if __name__ == "__main__":
    main()
