# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

try:
    multipliers = [1, 10, 100]
    n = int(input("Enter number: "))
    sum = 0
    for i in range(3):
        d = 0
        for j in range(i+1):
            d += n * multipliers[j]
        sum += d
    print(sum)
except:
    print("Something went wrong!")