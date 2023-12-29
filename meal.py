def main():
    time = input("What time is it? ")

    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")

    elif 12 <= time <= 13:
        print("lunch time")

    elif 18 <= time <= 19:
        print("dinner time")

    else:
        return

def convert(t):
    h, min = t.split(":")
    h = int(h) * 60
    total = h + int(min)

    total = float(total / 60)

    return total


if __name__ == "__main__":
    main()