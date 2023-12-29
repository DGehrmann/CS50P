def main():
    item_dict = {}
    while True:
        try:
            item = input()
            if item in item_dict:
                item_dict[item] += 1
            else:
                item_dict[item] = 1
        except KeyError:
            pass
        except EOFError:
            print("\n")
            break

    item_dict_sorted = sorted(item_dict)
    for i in item_dict_sorted:
        print(f"{item_dict[i]} {i.upper()}")


if __name__ == "__main__":
    main()