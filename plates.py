def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 1 < len(s) <= 6:
        return False
    elif not (s[0].isalpha() and s[1].isalpha()):
        return False
    elif not s[0:].isalnum():
        return False
    elif not check_num(s):
        return False
    elif not check_first_num_not_0(s):
        return False
    return True


def check_num(t):
    #check if string contains any numbers, if not condition is omittable
    if t.isalpha():
        return True

    num_list = []
    for c in range(0,len(t)):
        #plate must start with letters, thus num is False to begin with.
        #If any number is found, num becomes True.
        #If num turns False again afterwards, that means that another
        #letter was found which is invalid.
        num = t[c].isnumeric()
        num_list.append(num)

    for c in range(0, len(num_list)):
        if num_list[c] == True:
            if c == len(num_list)-1:
                return True
            elif num_list[c+1] == False:
                return False

    return True


def check_first_num_not_0(u):
    num_exist = False
    for c in u:
        if c.isnumeric() and num_exist == False:
                if c == "0":
                    return False
                else:
                    num_exist = True

    return True


main()