#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """The any_lowercase1(s) function will terminate after the first character is examined because of the return statement.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """This function is only examining whether or not the string 'c' is a lowercase letter (which it is),
        so it will always return 'True'.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """The flag will change with each letter in s, so if s ends with an upper-case letter but also contains lowercase letters, 
    it will return False.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Similar to the previous function, this examines each character of the string. 
        If s ends with 2 upper-case letters but also contains lower-case letters, flag == False,
        but the answer should be True.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """This function will stop at the first uppercase character it comes across and return False. 
        If the first character is uppercase and the rest are lowercase, the result will be False.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print("Hello World!")


if __name__ == '__main__':
    main()
