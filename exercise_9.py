# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)

# The "%" operator is used to format a set of variables enclosed in a "tuple"
print('The examination will start from : %i / %i / %i' % exam_st_date)