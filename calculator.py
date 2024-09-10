import math


operands=[]
print("enter the values")
n=int(input("enter the no of values "))
for i in range(n):
    a=int(input(f"enter the {i+1} value"))
    operands.append(a)
print("enter the operator")
op=str(input("choose between +,-,*,/"))
if op=="+":
    result=0
    for i in range(n):
        result+=operands[i]
elif op=="-":
    result=0
    for i in range(n):
        result-=operands[i]
elif op=="*":
    result=1
    for i in range(n):
        result*=operands[i]
else:
    result=1
    for i in range(n):
        result/=operands[i]
print("result=",result)