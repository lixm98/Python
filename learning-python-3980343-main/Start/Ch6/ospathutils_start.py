#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import time
from datetime import datetime

# Print the name of the OS
print(os.name)

# Check for item existence and type
print("Item exists:", path.exists("textfile.txt"))
print("Item is a file:", path.isfile("textfile.txt"))
print("Item is a directory:", path.isdir("textfile.txt"))

# Work with file paths
print("Item's path:", path.realpath("textfile.txt"))
print("Item's path and name:", path.split(path.realpath("textfile.txt")))

# Get the modification time
t = time.ctime(path.getmtime("textfile.txt"))
print("Item's modification time:", t)
print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

# Calculate how long ago the item was modified
t_now = datetime.now()
mod_time = datetime.fromtimestamp(path.getmtime("textfile.txt"))
delta = t_now - mod_time
print("Item was modified", delta, "seconds ago")
print("Item was modified", delta.total_seconds(), "seconds ago")