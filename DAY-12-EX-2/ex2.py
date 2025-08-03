# WAP to print greeting for people at different time of the day.

# import time module to get current time
import time as tm

# get current hour (0 to 23)
current_hour = tm.localtime().tm_hour

if 4 <= current_hour < 12:
    print("Good Morning")
elif 12 <= current_hour < 16:
    print("Good Afternoon")
elif 16 <= current_hour < 18:
    print("Good Evening")
else:
    print("Good Night")

