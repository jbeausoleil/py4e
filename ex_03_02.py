sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
try:
    hours = float(sh)
    rate = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
print(hours, rate)
if hours <= 40:
    pay = hours * rate
elif hours > 40:
    pay = 40 * rate + (hours - 40) * rate * 1.5
print('Pay:', pay)
