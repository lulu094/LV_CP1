# LV 2nd Mapping Notes

numbers = [651,94,76,789]
"""divide = []

for num in numbers:
    divide.append(num/2)"""


"""def divide(number):
    return number/2"""
divided = list( map(lambda num: num/2, numbers))

for i, num in enumerate(numbers):
    print(f"{num} divide by 2 is {divided[i]}")
