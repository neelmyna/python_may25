# Right angled Triangle of N lines

number_of_lines = int(input('Enter number of lines to print X shape: '))


for i in range(1, number_of_lines+1):
    for j in range(1, number_of_lines+1):
        if i == j or j == number_of_lines - i + 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print() # to take the cursor to next line

'''
     *
    ***
   *****
  *******
 *********
***********

for i in range(1, number_of_lines+1):
    print('@ ' * n)

'''