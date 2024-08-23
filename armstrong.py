i=int(input("Enter the number:"));
org=i;
sum=0;
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10;
if(sum==org):
    print(org,"Is an armstrong number");
else:
    print(org,"Is not an armstrong number");