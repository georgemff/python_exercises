from datetime import datetime
# 3. Write a Python program to display the current date and time.
print(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) #24 format
print(datetime.now().strftime("%Y-%m-%d %I-%M-%S %p")) #12 format
