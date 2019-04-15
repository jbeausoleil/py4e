hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hours <= 40:
    pay = hours * rate
elif hours > 40:
    pay = 40 * rate + (hours - 40) * rate * 1.5
print(pay)
