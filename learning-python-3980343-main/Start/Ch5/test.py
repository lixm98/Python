import calendar
def count_days(year, month, whichday):
    # Your code goes here.
    this_year_month = calendar.monthcalendar(year, month)
    result = whichday
    for i in this_year_month:
        if i[whichday] != 0:
           result += 1
    return result
x = count_days(2026,12,0)
print(x)                                           