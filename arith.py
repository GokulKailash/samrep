a=int(input("enter the first number : "));
b=int(input("enter the second number : "));
op=int(input("select 1)add 2)sub 3)mul 4)div 5)mod 6)sqr :"));
if(op==1):
    print(a+b);
elif(op==2):
    print(a-b);
elif(op==3):
    print(a*b);
elif(op==4):
    print(a/b);
elif(op==5):
    print(a%b);
elif(op==6):
    print(a**b);
else:
    print("choose any operation")
