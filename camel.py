def main():
    camel = input("camelCase: ")
    snake = camel_to_snake(camel)

    print(snake)


def camel_to_snake(s_cam):
    s_snake = " "
    for l in s_cam:
        if l.isupper():
            l = "_" + l.lower()
        s_snake = s_snake + l

    s_snake = s_snake.strip()

    return s_snake


if __name__ == "__main__":
    main()