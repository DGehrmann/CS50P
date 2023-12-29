import sys
from pyfiglet import Figlet

figlet = Figlet()

def main():
    if len(sys.argv) not in [1,3]:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3 and (sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts()):
        sys.exit("Invalid usage")

    else:
        s = input("Input: ")

        if len(sys.argv) == 3:
            # setting font:
            figlet.setFont(font=sys.argv[2])
            #print(figlet.renderText(s))
        s = figlet.renderText(s)
        print(f"Output:\n{s}")



if __name__ == "__main__":
    main()