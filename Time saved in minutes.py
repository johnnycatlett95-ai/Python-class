#calculating the amount of time saved When traveling at
#average speed above the speed limit as compared to
#traveling with a average speed exactly at the speed limit.

#getting the inputs.
Avg_speed = float(input("enter average speed (mph)"))
Speed_limit = float(input("enter speed limit (mph)"))
Distance = float(input("enter distance traveled in (miles)"))

#calculating time saved.
time_spent_speeding = Distance / Avg_speed
time_spent_at_limit = Distance / Speed_limit
Time_saved = (time_spent_speeding - time_spent_at_limit) * 60

#output
print(f"time saved is: {Time_saved:.2f} minutes")
