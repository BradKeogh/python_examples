"""
function to print a time statement dpending on number of args
"""
import sys
import datetime
import numpy as np

dates = sys.argv[-3:]
#print(dates)

def convert_int(x):
    x = np.int(x)
    return(x)

def timething(dates):
    then = datetime.datetime(convert_int(dates[0]),convert_int(dates[1]),convert_int(dates[2]))
    now = datetime.datetime.now()
    days = now - then
    return(days)

def timething2(day_to_add):
    day_to_add = convert_int(day_to_add)
    days = datetime.datetime.now() + datetime.timedelta(days=day_to_add)
    return(days)

#print(dates)
if len(sys.argv) == 2:
    print('1 var given')
    print(timething2(sys.argv[-1]))
    
elif len(sys.argv) == 4:
    print('3 vars given')
    print(timething(dates))
else:
    print('There were neither 1 or 3 args given.')