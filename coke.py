def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        c = int(input("Insert Coin: "))
        if c not in [5, 10, 25]:
            continue
        else:
            amount_due = amount_due - c

    amount_due = abs(amount_due)
    print(f"Change Owed: {amount_due}")

if __name__ == "__main__":
    main()