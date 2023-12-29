import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].rsplit(".",1)[-1] not in ["jpg","jpeg","png","JPG","JPEG","PNG"]:
        sys.exit("Invalid input")
    elif sys.argv[2].rsplit(".",1)[-1] not in ["jpg","jpeg","png","JPG","JPEG","PNG"]:
        sys.exit("Invalid input")
    elif sys.argv[1].rsplit(".",1)[-1] != sys.argv[2].rsplit(".",1)[-1]:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        before = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("File not found")

    size = shirt.size
    before_resized = ImageOps.fit(before, size)
    before_resized.paste(shirt,shirt)
    before_resized.save(sys.argv[2])


if __name__ == "__main__":
    main()