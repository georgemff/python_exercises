# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user 
# and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

try:
    data = input("Enter sequence of comma-separated numbers: ")
    
    list_of_numbers = data.split(',')
    tuple_of_numbers = tuple(list_of_numbers)

    print(list_of_numbers)
    print(tuple_of_numbers)
except:
    print("Something went wrong!")