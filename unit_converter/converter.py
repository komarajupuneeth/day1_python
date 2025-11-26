def km_to_miles(km):
    return km * 0.621371 
def celsius_to_fahrenheit(c):
    return c* 9/5 +32
def rupee_to_dollars(rs):
    return rs / 83 
def hours_to_minutes(h):
    return h*60  

while True:
    print("unit converter") 
    print("1. km to miles")
    print("2. celsius t ofaherenhiet")
    print("3. rupees to dollars")
    print("4.hours to minutes") 

    choice=int(input("enter your choice(1 to 4): ")) 

    if choice==1:
        km=float(input("enter km:")) 
        print("miles: ",km_to_miles(km)) 
    elif choice==2:
        c=float(input("enter c:")) 
        print("fahreheit: ",celsius_to_fahrenheit(c)) 
    elif choice==3:
        rs=float(input("enter rupees:")) 
        print("dollars: ",rupee_to_dollars(rs)) 
    elif choice==4:
        h=float(input("enter hours:")) 
        print("minutes: ",hours_to_minutes(h)) 
    else:
        print("invalid choice,try agian") 
