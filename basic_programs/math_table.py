input_number = int(input('Enter a number to print its Math table: '))

for i in range(1, 21):
    #print(f'{input_number} * {i} =', input_number * i)
    print('%d * %02d = %03d'%(input_number, i, input_number*i))
'''
15 * 1 = 15
15 * 2 = 30


15 * 10 = 150
'''