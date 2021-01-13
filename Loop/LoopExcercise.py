total = 0
number = 0

while True :
    value = input("Enter a number: ")
    if value == "done" :
        break
    try : 
        value = float(value)
    except :
        print("Invalid input")
        continue
    
    number = number + 1
    total = total + value

print(total,number,total/number)