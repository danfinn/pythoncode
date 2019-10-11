#!/usr/bin/python
#
# An interesting interview question that I didn't quite nail during
# the interview but wanted to take a stab at when I got home
#

pyramid_character = raw_input("Enter some text: ")
pyramid_size = int(raw_input("And the size of your side word pyramid: "))


<<<<<<< HEAD
def create_pyramid(character,size):
  """ Prints a sideword pyramid """
  loop_counter = 1
  increment = 1
  while loop_counter > 0:
   if increment:
      print character * loop_counter
      loop_counter += 1
      if (loop_counter == size):
        # Flip the increment counter and print the top of the pyramid
        print character * loop_counter
        increment = 0
   else:
     loop_counter -= 1
     print character * loop_counter

create_pyramid(pyramid_character,pyramid_size)
=======
def print_pyramid(pyramid_character, pyramid_size):
    """ Prints a sideword pyramid """
    loop_counter = 1
    increment = 1
    while loop_counter > 0:
        if increment:
            print pyramid_character * loop_counter
            loop_counter += 1
            if (loop_counter == pyramid_size):
                # Flip the increment counter and print the top of the pyramid
                print pyramid_character * loop_counter
                increment = 0
        else:
            loop_counter -= 1
            print pyramid_character * loop_counter


print_pyramid(pyramid_character, pyramid_size)
>>>>>>> 8dacbdb3844b4d4091dfc58553a1031fda99b491
