#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None
smallest = None
while True :
    sval = input('Enter a Number: ')
    if sval == 'done' : break
    try :
        ival = int(sval)
    except:
        print('Invalid input')
        continue
    else :
        if smallest == None :
            largest = ival
            smallest = ival
        elif ival < smallest :
            smallest = ival
        elif ival > largest :
            largest = ival
print('Maximum is',largest)
print('Minimum is', smallest)
