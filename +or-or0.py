#To Check whether the given number is positive or negative
S=int(input("Enter a number: "))
if S>0:
    print("Given number {0} is positive number".format(S))
elif S<0:
    print("Given number {0} is negative number".format(S))
else:
    print("Given number {0} s Zero".format(S))