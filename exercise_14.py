# 14. Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import datetime

d1 = (2014, 7, 2)
d2 = (2014, 7, 11)

date_1 = datetime.strptime("/".join(map(str,d1)), "%Y/%m/%d")
date_2 = datetime.strptime("/".join(map(str,d2)), "%Y/%m/%d")
d = date_2 - date_1
print("{} days".format(d.days))