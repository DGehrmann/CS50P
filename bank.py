def main():
    greeting = input("Greeting: ")

    greeting = greeting.strip()
    greeting = greeting.lower()

    if greeting[0:5] == "hello":
        print("$0")

    elif greeting[0] == "h":
        print("$20")

    else:
        print("$100")

if __name__ == "__main__":
    main()