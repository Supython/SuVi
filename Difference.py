#To Find difference of the given numbers
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
    difference=a-b
    print("difference of {0} and {1} is {2}".format(a,b,difference))
else:
    difference=b-a
    print("difference of {0} and {1} is {2}".format(a,b,difference))
