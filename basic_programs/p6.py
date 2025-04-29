input_alpha = input('Enter an alphabet to check if it is small case: ')

if input_alpha >= 'a' and input_alpha <= 'z':
    print(f'{input_alpha} is a small alphabet')
else:
    print(f'{input_alpha} is not a small alphabet')

'''
values of upper case letters is from 65 to 90
65 A
66 B
90 Z

values of small case letters is from 97 to 122
97 a
98 b
99 c
122 z
'''