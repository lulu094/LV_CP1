# LV 2nd Squared Numbers
# hacer que los numeros se multipliquen por si mismo 
# numbers to be square rooted
numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]

# 
def squared(numbers):
    return(numbers ** 2)

squared = list(map(lambda num: num/2, numbers))


