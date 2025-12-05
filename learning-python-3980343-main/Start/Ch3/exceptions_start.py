# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
# x = 10 / 0

# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
# try:
#     x = 10 / 0
# except:
#     print("An error occurred")

# You can also catch specific exceptions
try:
    answer = input("Enter a number to divide 10: ")
    num = int(answer) # could cause a ValueError
    x = 10 / num     # could cause a ZeroDivisionError
    print("10 divided by", num, "is", int(x))
except ZeroDivisionError as e:
    print("You can't divide by zero!", e)
except ValueError as e:
    print("You need to enter a valid number!", e)
finally:
    print("This always runs")
