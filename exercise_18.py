multiplier = 3

numbers = [0,0,0]
sum = 0
for i, x in enumerate(numbers):
    numbers[i] = int(input('Enter Number: '))
    sum = sum + numbers[i]

if sum / multiplier == numbers[0]:
    print(sum*multiplier)
else:
    print(sum)
