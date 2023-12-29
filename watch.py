import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r'^<iframe src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+)"></iframe>$',s,re.IGNORECASE):
        s = s.split('"')[1]
        short = re.sub(r"https?://(?:www\.)?youtube\.com/embed/","https://youtu.be/",s)
        return short
    else:
        return None



if __name__ == "__main__":
    main()