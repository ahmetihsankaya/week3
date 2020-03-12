leave_day=int(input("Which day are you leaving?\n"))
number_days=int(input("How many days will you stay there?\n"))
return_day=(leave_day+number_days)%7
print("The return day is %s" % return_day)
if return_day == 0:
    print("Sunday")
elif return_day == 1:
    print("Monday")
elif return_day == 2:
    print("Tuesday")
elif return_day == 3:
    print("Wednesday")
elif return_day == 4:
    print("Thursday")
elif return_day == 5:
    print("Friday")
elif return_day == 6:
    print("Saturday")
