a = int(input("Enter the number : "))
if a!=5 and a!=11 and a!=7 and a!=17:
    if a%3!=0 and a%2!=0 and a%5!=0 and a%7!=0 and a%11!=0 and a%17!=0:
        print("{} is a Prime Number".format(a))
    else:
        print("{} is not a Prime Number".format(a))
else:
    print("{} is a Prime Number".format(a))
