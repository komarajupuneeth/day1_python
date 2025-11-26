s=input("enter a string: ") 
s=s.lower() 
count=0 
for char in s : 
    if char in "aeiou":
        count+=1 
print("vowels:",count)