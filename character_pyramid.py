#!/usr/bin/python
#
# An interesting interview question that I didn't quite nail during
# the interview but wanted to take a stab at when I got home
#

pyramid_character = raw_input("Enter some text: ")
pyramid_size = int(raw_input("And the size of your side word pyramid: "))

def create_pyramid(character, size):
    """ Prints a sideword pyramid """
    loop_counter = 1
    increment = 1
    while loop_counter > 0:
        if increment:
            print character * loop_counter
            loop_counter += 1
            if (loop_counter == size):
                # You've reached the top, start heading down the other side
                print character * loop_counter
                increment = 0
        else:
            loop_counter -= 1
            print character * loop_counter


create_pyramid(pyramid_character, pyramid_size)
