#To Check whether the given number is positive or negative
S=int(input("Enter a number: "))
if S%2==0:
    print("Given number {0} is Even number".format(S))
elif S%2!=0:
    print("Given number {0} is Odd number".format(S))
else:
    print("Kindly Enter a number")