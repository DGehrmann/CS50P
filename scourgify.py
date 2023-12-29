import sys
import csv


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a csv file")
    elif sys.argv[2][-4:] != ".csv":
        sys.exit("Not a csv file")

    firsts = []
    lasts = []
    houses = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                name = name.split(",")
                first = name[1].lstrip()
                firsts.append(first)

                last = name[0]
                lasts.append(last)

                house = row["house"]
                houses.append(house)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=['first','last','house'])
        writer.writeheader()

        for first, last, house in zip(firsts, lasts, houses):
            writer.writerow({"first":first, "last":last, "house":house})


if __name__ == "__main__":
    main()