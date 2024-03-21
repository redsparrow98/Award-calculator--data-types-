#==================== pseudo code ===================
# 1: ask the user to put in times it tok to
#        finish every section for the triathlon
#        ask them to put it in minutes for eas of
#        calculation

# 2: calculate the total minutes for all
#        sections and get total time for it took
#        to finish the race and show that final time

# 3 compare the total time of the contestant
#        to the qualifying requirements for the race
#        and determine if an award needs to be given
#        and what that award is

#======================== code ========================

#ask the user to enter minutes it took
#to complete every section for the marathon
print("please provide time it took to complete the sections in minutes")

#ask for input for sections and cast to int() and save to variable
swimming = int(input("Minutes to do swimming section: "))
cycling = int(input("Minutes to do cycling section: "))
running = int(input("Minutes to do running section: "))

#calculate the sum of the inputs
# to get the total time to finish the marathon
total_time = swimming + cycling + running
print(f"The contestant took {total_time} mins to finish the race")

#check the total time against qualifying time
# using the if/elif/else statements and determine the award that gets given out
if total_time <= 100:
    print("Give the Provincial colours award")
elif total_time <= 105:
    print("Give the Provincial half colours award")
elif total_time <= 110:
    print("Give the Provincial scroll award")
else:
    print("Over the 10mins for qualifying time, no award")
