# To check if the given character is alphanumeric

input_char = input('Enter a character: ')
if (input_char >= 'a' and input_char <= 'z') or (input_char >= 'A' and input_char <= 'Z') or (input_char >= '0' and input_char <= '9'):
    print(f'{input_char} is an alphanumeric character')
else:
    print(f'{input_char} is not an alphanumeric character')

'''
input_char = input_char.lower()
if (input_char >= 'a' and input_char <= 'z') or (input_char >= '0' and input_char <= '9'):
    print(f'{input_char} is an alphanumeric character')
else:
    print(f'{input_char} is not an alphanumeric character')
'''