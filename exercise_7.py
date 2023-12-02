# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

try:
    filename = input("Enter filename: ")
    splitted = filename.split('.')

    if len(splitted) == 1:
        print("file \'{}\' does not contains extension".format(filename))
    else:
        #take last element of index.
        #if filename contains multiple dot, last one should be extension
        extension = splitted[-1]
        print(extension)
except:
    print("Something went wrong!")