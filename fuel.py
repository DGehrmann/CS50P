def main():
    percentage = get_fraction()
    print(percentage)


def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            zaehler = int(fraction.split(sep="/")[0])
            nenner = int(fraction.split(sep="/")[1])
            percent = round((zaehler / nenner) * 100)
            if nenner < zaehler:
                raise ValueError
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        else:
            break

    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        percent = str(percent) + "%"
        return percent


if __name__ == "__main__":
    main()