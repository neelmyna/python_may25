# program to check if a number is positive or negative or zero

# print('Enter the input number', end=': ')
input_number = int(input('Enter the input number: '))

if input_number > 0:
    print(input_number, 'is positive')
elif input_number < 0:
    print(f'{input_number} is negative number')
else:
    print('The input number is Zero')