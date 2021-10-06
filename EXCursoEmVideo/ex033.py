num1 = int(input('Enter a number'))
num2 = int(input('Enter a second number'))
num3 = int(input('enter a third numeber'))
lowest = num1
high = num1
if num2 < num1 and num2 < num3:
    lowest = num2
if num3 < num2 and num3 < num1:
    lowest = num3
print('the lowest number is {}'.format(lowest))
if num2 > num3 and num2 > num1:
    high = num2
if num3 > num2 and num3 > num1:
    high = num3
print('the highest number is {}'.format(high))
