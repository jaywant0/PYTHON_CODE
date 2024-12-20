# good morning sir program using time module in python
import time

timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

print("Hour")
hour =int(time.strftime('%H'))
print(hour)

if( hour >= 0 and hour < 12):
    print("good morning sir")
elif(hour >=12 and hour < 17):
   print("good afternoon sir!")
elif(hour >=17 and hour<0):
    print("good night sir")



