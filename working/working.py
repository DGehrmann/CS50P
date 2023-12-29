import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    conversion_dict_AM = {"12":"00", "1":"01", "2":"02", "3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09"}
    conversion_dict_PM = {"1":"13", "2":"14", "3":"15","4":"16","5":"17","6":"18","7":"19","8":"20","9":"21","10":"22","11":"23","12":"12"}

    if matches := re.search(r"^(1?\d):?([0-5]\d)? (A|P)M to (1?\d):?([0-5]\d)? (A|P)M$",s):
        if matches.group(3) == "A":
            if matches.group(1) in conversion_dict_AM:
                hours_from = conversion_dict_AM[matches.group(1)]
            else:
                hours_from = matches.group(1)

            hours_to = conversion_dict_PM[matches.group(4)]

        else: # ==> if matches.group(3) == "P"!
            hours_from = conversion_dict_PM[matches.group(1)]

            if matches.group(4) in conversion_dict_AM:
                hours_to = conversion_dict_AM[matches.group(4)]
            else:
                hours_to = matches.group(4)

        if matches.group(2) == None:
            minutes_from = "00"
        else:
            minutes_from = matches.group(2)

        if matches.group(5) == None:
            minutes_to = "00"
        else:
            minutes_to = matches.group(5)


        return hours_from + ":" + minutes_from + " to " + hours_to + ":" + minutes_to

    else:
        raise ValueError





if __name__ == "__main__":
    main()