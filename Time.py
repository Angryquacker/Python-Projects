from datetime import *
from math import *

now = datetime.now()
type = raw_input("What type of time do you wish to view? Current, Day, Month, or Year? ")
def time():
  if type.lower() == 'day':
    if now.day == 1:
      print "The day is the " + str(now.day) + "st"
    elif now.day == 2:
      print "The day is the " + str(now.day) + "nd"
    elif now.day == 3:
      print "The day is the " + str(now.day) + "rd"
    else:
      print "The day is the " + str(now.day) + "th"
  elif type.lower() == 'month':
    if now.month == 1:
      print "We are in the month of January"
    elif now.month == 2:
      print "We are in the month of February"
    elif now.month == 3:
      print "We are in the month of March"
    elif now.month == 4:
      print "We are in the month of April"
    elif now.month == 5:
      print "We are in the month of May"
    elif now.month == 6:
      print "We are in the month of June"
    elif now.month == 7:
      print "We are in the month of July"
    elif now.month == 8:
      print "We are in the month of August"
    elif now.month == 9:
      print "We are in the month of September"
    elif now.month == 10:
      print "We are in the month of October"
    elif now.month == 11:
      print "We are now in the month of November"
    elif now.month == 12:
      print "We are now in the month of December"
  elif type.lower() == 'year':
    print "The year is " + str(now.year)
  elif type.lower() == 'current':
    print "The current time is " + str(now)
  else:
    print "That is not a valid type!"
    
time()
