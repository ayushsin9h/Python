nterms=int(input("Enter the number of terms"))
n1,n2=0,1
c=0
if nterms<=0:
    print("Please enter a positive integer")
elif nterms==1:
    print("Fibonnacci series upto n terms :")
    print(n1)
else:
    print("Fibonnacci series")
    while c < nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        c+=1
     
