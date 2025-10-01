# LV 2nd For Loops
import time
nums = [6, 51, 61, 94, 351,946, 5489,4,654,684]

for num in nums:
    div = num/2
    if div > 100:
        print(f"{div} is half of {num}. And it is still a large nuber!")
    else:
        print(num)


for x in range(1,10):
    print(x)
time.sleep(3)

print("Count by 2s")
for x in range(2,11,2):
    print(x)
time.sleep(3)

print("Count down")
for x in range(10,0,-1):
    print(x)
    time.sleep(1)