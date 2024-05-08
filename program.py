def prime(a):
    if a==1:
        print("the number is not prime")
    elif a>1:
        for i in range(2,a):
            if a%i:
                print("the number is prime")
                break
            else:
                print("the number is not prime")
                break

a=int(input("enter the nmber:"))
print(prime(a))