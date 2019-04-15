num = 0
tot = 0
while True :
    sval = input('Enter a Number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input. Enter Numeric Value')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval
#print('ALL DONE')
print('Total:',tot,'Number Count:',num,'Average:',tot/num)
