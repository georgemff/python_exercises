NUM_1 = 1000
NUM_2 = 2000
NUM_3 = 100

inp = int(input("Enter Number: "))

print(abs(NUM_1 - inp) <= NUM_3 or abs(NUM_2 - inp) <= NUM_3)