num=int(input("Enter a number:"))
s=0
temp=num
while temp>0:
   di=temp%10
   s=s+di**3
   temp=temp//10
if(num==s):
   print("is an armstrong number",num)
else:
   print("is not an armstrong number",num)
