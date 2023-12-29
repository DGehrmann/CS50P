def main():
    menu = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }

    price_list = []
    while True:
        try:
            item = input("Item: ").title()
            price = menu[item]
            price_list.append(price)
            p_sum = sum(price_list)
            p_sum = "{:.2f}".format(p_sum)
            print(f"Total: ${p_sum}")
        except KeyError:
            pass
        except EOFError:
            print("\n")
            break



if __name__ == "__main__":
    main()