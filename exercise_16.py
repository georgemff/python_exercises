num_1 = 17
num_2 = int(input("Enter Number: "))

diff = num_2 - num_1

if diff < 0:
    print(abs(diff))
else:
    print(2*diff)