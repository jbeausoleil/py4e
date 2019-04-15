count = 0
sum = 0
numbers = [1,2,3,4,5,6,7,8,9]
print('Beginning Sum: ', sum)
for number in numbers:
    count = count + 1
    sum = number + sum
    print('Count:', count, 'Number:', number, 'Sum:', sum)
print('Ending Sum: ', sum)
print('The Average Is:', sum / count)
