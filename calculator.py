#Calculator
print("----Calculator----");
print('''Select which operator youn want to use
1. Addition(+)
2. Subtraction(-)
3. Multiplication(*)
4. Division(/)
5. Exponent(**)
''');
d=int(input("Enter your choice:"));
a=int(input("Enter a number:"));
b=int(input("Enter another number:"));
if(d==1):
    print("Addition of (a) and (b) is=",a+b);
elif(d==2):
    print("Subtraction of (a) and (b) is=",a-b);
elif(d==3):
    print("Multiplication of (a) and (b) is=",a*b);
elif(d==4):
    print("Division of (a) and (b) is=",a/b);
elif(d==5):
    print("Exponent of (a) and (b) is=",a**b);
else:
    print("Invalid Choice");