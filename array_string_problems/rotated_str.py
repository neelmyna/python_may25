import sys

input_str = input('Enter the input string: ')
rotated_str = input('Enter the rotated string: ')

if len(input_str) != len(rotated_str):
    sys.exit('The input given are incorrect')
    
temp_str = rotated_str * 2
if temp_str.find(input_str) != -1:
    print(f'{rotated_str} is rotated string of {input_str}')
else:
    print(f'{rotated_str} is not a rotated string of {input_str}')

'''
strcpy(t_str, r_str)
strcat(t_str, r_str)
ptr = strstr(t_str, i_str)
if(ptr == NULL)
    printf("%s is not rotatted string of %s", r_str, i_str);
else
    printf("%s is a rotatted string of %s", r_str, i_str);
'''