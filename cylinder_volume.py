#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: November 2019
# This program calculates volume of a cylinder

import math


def cylinder(h, r,):
    # this function calculates volume of a cylinder

    volume = math.pi*pow(r, 2)*h
    return volume


def main():
    # This program uses volume of a cylinder

    # input
    print("Lets calculate the volume of a cylinder!")
    a_value = input("Enter radius: ")
    b_value = input("Enter height: ")
    print("")

    # process
    try:
        radius = int(a_value)
        height = int(b_value)

        # call function
        solution = cylinder(r=radius, h=height)

    # output
        print("The volume is {0} cm^3".format(solution))
    except Exception:
        print("Theses are not integers")


if __name__ == "__main__":
    main()
