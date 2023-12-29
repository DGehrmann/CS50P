def main():
    months = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
              ]

    while True:
        try:
            date = input("Date: ")
            date = date.strip()
            date_split1 = date.split(sep="/")
            if len(date_split1) == 3:
                month = int(date_split1[0])
                year = date_split1[2]
                day = int(date_split1[1])
                #print(f"{date_split1[2]}-{int(date_split1[0]):02}-{int(date_split1[1]):02}")
                #break
            elif len(date_split1) == 1:
                date_split2 = date.split(sep=" ")
                month = months.index(date_split2[0]) + 1 #.index() raises ValueError if the item is not in the list!
                year = date_split2[2]
                if not "," in date_split2[1]:
                    raise ValueError
                else:
                    day = int(date_split2[1].strip(","))
            else:
                raise ValueError

            if day not in range(1, 32):
                raise ValueError
            elif month not in range(1, 13):
                raise ValueError

            print(f"{year}-{month:02}-{day:02}")
            break

        except ValueError:
            pass
        except IndexError:
            pass
        except EOFError:
            print("\n")
            break


if __name__ == "__main__":
    main()