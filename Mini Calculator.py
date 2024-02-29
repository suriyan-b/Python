a=int(input("Enter the number:"  ))#gets the first number from the user
b=int(input("Enter the number;"  ))#gets the second number from the user
c=input("Enter the valid operator:+,*,/,-")#gets the operator from the user

if c=="+":
    print(a+b) 
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="-":
    print(a-b)     
else:
    print("Invalid operator")          
