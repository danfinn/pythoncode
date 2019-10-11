#!/usr/bin/python
#
# An interesting interview question that I didn't quite nail during
# the interview but wanted to take a stab at when I got home
#

pyramid_character = raw_input("Enter some text: ")
pyramid_size = int(raw_input("And the size of your side word pyramid: "))


def create_pyramid(character, size):
    """ Prints a sideword pyramid """
    for i in range(1, size + 1):
        print character * i
    for i in range(size -1 , 1, -1):
         print character * i


create_pyramid(pyramid_character, pyramid_size)
