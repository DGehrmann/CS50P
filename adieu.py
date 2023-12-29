def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else :
        print("Adieu, adieu, to ", end="")
        for name in names[:-1]:
            print(f"{name}", end=", ")
        print(f"and {names[-1]}")


if __name__ == "__main__":
    main()