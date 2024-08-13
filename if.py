a=int(input("enter the number:"));
if a%2==0:
    print("Even");
else:
    print("odd");
# age to vote
a=int(input("enter you age:"));
if a>=18:
    print("You can vote.");
else:
    print("Youn can't vote.");

# max number
a=int(input("Enter 1st number: "));
b=int(input("Enter 2nd number: "));
if a>b:
    print("A is greater than B");
else:
    print("B is greater than A");

# max bertween three numbers
a=int(input("Enter 1st number: "));
b=int(input("Enter 2nd number: "));
c=int(input("Enter 3rd number: "));
if a>b and a>c:
    print("A is greatest number");
elif b>a and b>c:
    print("B is greatest number");
else:
    print("C is greatest number");


# positive negative or zero
a=int(input("Enter 1st number: "));
if a>0:
    print("The number is positive");
elif a<0:
    print("The number is negative");
else:
    print("Zero");

# total marks in 5 subjects
a=int(input("Enter 1st number: "));
b=int(input("Enter 2nd number: "));
c=int(input("Enter 3rd number: "));
d=int(input("Enter 4th number: "));
e=int(input("Enter 5th number: "));
total=a+b+c+d+e;
percent=(total/500)*100;
print("Total marks",total,"Percentage",percent);
if percent>=80:
    print("You have got Grade A");
elif percent>=60:
    print("You have got Grade B");
elif percent>=40:
    print("You have got Grade C");
else:
    print("You have got Grade D");
    


