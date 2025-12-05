#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.today()
print("Today's date is: " + str(now))

# print today's date one year from now
print("One year from now it will be: " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("In two weeks and 3 days it will be: " + str(now + timedelta(weeks=2, days=3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was ", s)

### How many days until April Fools' Day?
today = date.today()  # get today's date
afd = date(today.year, 4, 1)  # get April Fools' Day for this year
# if April Fools' Day has passed this year, use the next year
if afd < today:
    print("April Fools' Day already went by %d days ago" % ((today - afd).days))
    afd = date(today.year+1, 4, 1)
  
time_to_afd = afd - today
print(f"There are {time_to_afd.days} days until April Fools' Day.")
    