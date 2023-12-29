from datetime import date, datetime
import inflect
import sys


def main():
    birth = input("Date of Birth: ")
    delta = get_timedelta(birth)
    words = int2str(delta)

    print(f"{words} minutes")


def get_timedelta(birth):
    try:
        birth = datetime.strptime(birth,"%Y-%m-%d").date()
    except ValueError:
        sys.exit(1)

    now = date.today()
    delta = now - birth

    return delta.days * 24 * 60


def int2str(delta_min):
    p = inflect.engine()
    words = p.number_to_words(delta_min, andword="").capitalize()

    return words



if __name__ == "__main__":
    main()