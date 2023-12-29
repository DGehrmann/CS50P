def main():
    exp = input("Expression: ")

    x, y, z = exp.split(" ")
    #x = int(exp[0])
    #y = exp[1]
    #z = int(exp[2])

    result = float(eval(x + y + z))

    print(result)

if __name__ == "__main__":
    main()
