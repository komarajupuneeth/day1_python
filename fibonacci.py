n=int(input("enter how many terms: ")) 
a,b=1,1
for _ in range(n):
    print(a) 
    a,b=b,a+b 