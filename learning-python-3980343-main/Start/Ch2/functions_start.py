# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
def hello_func1():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)
  
hello_func1()

# function that takes parameters
def hello_func2(greeting):
  print("hello world!")
  name = input("What is your name? ")
  print(greeting, name)
  
hello_func2("How are you doing")
hello_func2("Hey what's up")

# function that returns a value
def cube(x):
  return x*x*x

result = cube(3)
print(result)

# function with default value for an parameter
def hello_func3(greeting, name = None):
  if name == None:
    name = input("What is your name? ")
  print(greeting, name)
  
hello_func3("How are you doing")
hello_func3("Hey What's up", "Li")
# 显性调用(参数=值)
hello_func3(name = "Bitch", greeting = "Hey")

# function with variable number of parameters
def multi_add(start, *args):
  result = start
  for x in args:
    result = result + x
  return result

print(multi_add(0, 1, 2, 3, 4, 5))