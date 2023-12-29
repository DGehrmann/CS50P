def main():
    s = input("Input: ")

    print("Output: ", end="")
    for c in s:
        if c not in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
            print(c, end="")
    print("\n")


if __name__ == "__main__":
    main()