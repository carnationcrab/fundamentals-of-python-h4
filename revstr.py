# SAM MARTORANA

# ################################# [H4_1] ################################# #
# The code below uses the accumulator pattern to reverse a string s:
#
# reversed = ''
# for char in s:
#     reversed = char + reversed
#
# (This is like debug_4.py in [L3-2].) Use this code to define a function def
# reverse(st) which returns the reversed version of st as its result. Then
# define a main() function which reads the string s from the user, and prints
# out the value returned by reverse(s). Finally, call your main() function as
# the last line in your program.
# ########################################################################## #

def reverse(s):

    reversed_str = ''

    for char in s:
        reversed_str = char + reversed_str

    return reversed_str


def main():

    usrStr = input('String please: ')

    print(reverse(usrStr))


main()