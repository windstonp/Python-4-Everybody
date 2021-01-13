hour = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hour = float(hour)
    rate = float(rate)
except:
    print('Error, some of the values is not a number.')
    quit()

if hour > 40 :
    pay = 40 * rate + (hour - 40.0) * (rate * 1.5)

else : 
    pay = hour * rate

print('pay:',pay)