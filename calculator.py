#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 24, 2021
# This program asks the user for an operation and two numbers.
# then it calculates the answer using another
# function.


# calculates the result of two numbers
def calculate(sign, first_num, second_num):

    if sign == '*':
        answer = first_num * second_num
    elif sign == '/':
        answer = first_num / second_num
    elif sign == '%':
        answer = first_num % second_num
    elif sign == '-':
        answer = first_num - second_num
    else:
        answer = first_num + second_num
    return answer


# check for invalid input and calls
# function to calculate the answer of two numbers.
def main():

    # display opening message
    print("This program performs calculations between two numbers.")

    # get operation from user
    sign_user = input("Enter the operation you want to perform "
                      "(*, /, %, -, +): ")

    # check if invalid operator is entered
    if sign_user == '*' or sign_user == '/' or sign_user == '%' \
       or sign_user == '-' or sign_user == '+':
        # get first number from user
        first_num_string = input("Enter the first number: ")

        try:
            # convert input from string to float
            first_num_float = float(first_num_string)

            # get second number from user
            second_num_string = input("Enter the second number: ")

            try:
                # convert input from string to float
                second_num_float = float(second_num_string)

                # assign variable to function call that gives return value
                answer_user = calculate(sign_user,
                                        first_num_float, second_num_float)

                # display results to user
                print("The answer of {} {} {} is {:.2f}"
                      .format(first_num_float, sign_user,
                              second_num_float, answer_user))

            # catch any invalid input
            except Exception:
                print("{} is not a valid input." .format(second_num_string))

        # catch any invalid input
        except Exception:
            print("{} is not a valid input." .format(first_num_string))

    else:
        print(" {} is not a valid sign." .format(sign_user))


if __name__ == "__main__":
    main()
