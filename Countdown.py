import time

# Countdown starting number
start = 10

print("Countdown starting...")
for i in range(start, 0, -1):
    print(i)
    time.sleep(3)  # Pause for 3 seconds
print("Countdown complete!")
