#!/usr/bin/env python

def int2words(number: int) -> str:
    from inflect import engine as convert

    return ' '.join(convert().number_to_words(number, wantlist=True, andword=' '))

def dollars2words(number: float) -> tuple[str, str | None]:
    from math import modf as splitter

    frac, intpart = splitter(number) # extract integer and fraction as seperate variables.

    intdollars: int = int(intpart)
    intcents: int = int(round(frac, 2) * 100) # convert fraction to integer

    strdollars: str = int2words(intdollars)
    strcents: str | None = int2words(intcents) if intcents and int(intcents) else None

    return strdollars, strcents


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Converts a decimal number into words')
    parser.add_argument('-n',type=float,required=False,help="a decimal number to convert to words",default=None)
    args, unknown = parser.parse_known_args()

    try:
        if args.n is None:
            number: float = float(input("Enter a number: "))
        else:
            number = args.n

        dollars, cents = dollars2words(round(number,2))

        if number.is_integer():
            print(f"${number:,.2f} is {dollars.capitalize()} dollars")
        else:
            print(f"${number:,.2f} is {dollars.capitalize()} dollars and {cents} cents")

    except ValueError as e:
        print("Error: Please enter a valid float (decimal number)....")

    except Exception as e:
        print(f"An unknown error occured.... {e}")