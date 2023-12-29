from validator_collection import checkers


def main():
    email = input("What's your email adress? ")
    print(validate(email))


def validate(s):
    if checkers.is_email(s) == True:
        return "Valid"
    else:
        return "Invalid"



if __name__ == "__main__":
    main()