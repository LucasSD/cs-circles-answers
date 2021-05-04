start_time = input()#enter a starting time in 24hr format
duration = int(input())#enter a duration in minutes

start_hours = int(start_time[0:2]) #change hours to an integer
start_mins = int(start_time[3:5]) #change minutes to an integer

adjusted_mins = start_mins + duration #add the duration to the minutes
adjusted_hours = start_hours + adjusted_mins // 60 # convert 60 minute chunks into whole hours

final_hours = str(adjusted_hours % 24) #adjust so that time always in correct 24hr format up to 23:59
final_mins = str(adjusted_mins % 60) #remove any extra 60 minute chunks which have already been converted to hours

if int(final_hours) < 10: # if it's a single digit
   final_hours = '0' + final_hours #add the preceding zero for 24hr clock

if int(final_mins) < 10:
   final_mins = '0' + final_mins # add a preceding zero for minutes less than 10

print(final_hours + ':' + final_mins)