total = 0
smallest = None
biggest = None

while True :
    value = input("Enter a number: ")
    if value == "done" :
		break
    try : 
        value = float(value)
        
        if biggest is None :
			biggest = value
        elif biggest < value :
            biggest = value

        if smallest is None :
            smallest = value
        elif smallest > value :
            smallest = value
    except :
        print("Invalid input")
        continue
        
    
print("Maximum is",int(biggest))
print("Minimum is",int(smallest))