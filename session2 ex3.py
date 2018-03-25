##a=(1,2,3,4,5,6,7,8,9,0)
##print("Minimum Number",min(a))
##print("Maximum Number",max(a))

i=0
while(i<11):
    num=int(input("enter the number"))
    if (i==0):
        m1=num
        m2=num
    if (num<m2):
        m2=num
    if (num>m1):
        m1=num
    i=i+1
print("Maximum Number : ",m1)
print("Minimum Number : ",m2)
