def convert(text):

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    s = input("Text: ")
    o = convert(s)

    print(o)

main()