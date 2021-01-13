def computePayment(hour, rate) :
    if hour > 40 :
        reg = hour * rate
        otp = (hour - 40.0) * (rate * 0.5)
        pay = reg * otp
    else : 
        pay = hour * rate
    return pay

hour = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hour = float(hour)
    rate = float(rate)
except:
    print('Error, some of the values is not a number.')
    quit()

computePayment(hour, rate)


print('pay:',pay)