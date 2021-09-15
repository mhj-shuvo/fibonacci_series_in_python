# Script Begins

nth = int(input('Enter the nth element number: '))

n1 = 0
n2 = 1

if nth <= 0:
    print('Negative or zero value:', nth, 'is not acceptable.')

elif nth == 1:
    print('1st element of Fibonacci series is 0 which is defined element.')

elif nth == 2:
    print('Fibonacci series starts from 0 and 1, which are defined 1st & 2nd elements respectively.')

else:
    print(nth, 'elements of Fibonacci series:')
    sqnc = [n1, n2]
    for a in range (2, nth):
        sqnc.append(n1 + n2)
        n1 = n2
        n2 = sqnc[a]
    print(sqnc)

# Script Ends