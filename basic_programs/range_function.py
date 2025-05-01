user_number = int(input('Enter a number of your choice till 100: '))

for number in range(user_number):
    print(number, end = '  ')

print('\n')
for number in range(5, user_number):
    print(number, end = '  ')

print('\n')
for number in range(5, user_number, 2):
    print(number, end = '  ')

print('\n')
for number in range(user_number, 3, -2):
    print(number, end = '  ')

print('\n')
for number in range(user_number, 1, -1):
    print(number, end = '  ')

