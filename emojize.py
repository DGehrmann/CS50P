import emoji

def main():
    coded = input("Input: ")
    emojized = emoji.emojize(coded, language="alias")
    print(f"Output: {emojized}")

if __name__ == "__main__":
    main()