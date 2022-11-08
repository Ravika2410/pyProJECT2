a=int(input("Enter upper range limit."))
b=int(input("Enter lower range limit."))
c=int(input("Enter the number to be divided by: "))
for i in range(a,b+1):
    if(i%c==0):
        print(i)
