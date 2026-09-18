import time

minutes = int(input("How many minutes do you want to study? "))

seconds = minutes * 60

print(f"Your study session will be {minutes} minutes.")
print("Study session started!")

time.sleep(seconds)

print("Time's up!")
