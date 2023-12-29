def main():
    s = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

    s = s.lower()
    s = s.strip()

    if s in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()