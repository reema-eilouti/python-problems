#CA01 Problem2

# Write a program which converts all units of time into seconds.
# Sample input: "3 days, 14 hours, 27 minutes, 33 seconds.
# Sample output: 311253 seconds

time = input("Please enter: Days, Hours, Minutes, Seconds: ")

print(list(time))

days, hours, minutes, seconds = time

days_in_seconds = days * 24 * 60 * 60
hours_in_seconds = hours * 60 * 60
minutes_in_seconds = minutes * 60

result = days_in_seconds + hours_in_seconds + minutes_in_seconds + seconds

print(f"\n{result} seconds.")