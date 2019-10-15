#!/usr/bin/env python3

# Created by: Paul M
# Created on: Oct 2019
# This program uses a compound boolean statement


def main():
    # this function uses a compound boolean statement

    # input
    handsome = input("Are you handsome: ")
    rich = input("Are you rich: ")
    print("")

    # process & output
    if handsome == "no" and rich == "no":
        print("You failed the granny test.")

    elif handsome == "yes" or rich == "yes":
        print("You passed the granny test.")

    else:
        print("You entered an invalid response.")


if __name__ == "__main__":
    main()
