input_number = int(input('Enter a number to find sum of its digits: '))
sum_of_digits = 0
temp_number = input_number
while temp_number != 0:
    remainder_digit = temp_number % 10
    temp_number = temp_number // 10
    sum_of_digits = sum_of_digits + remainder_digit

print(f'Sum of the digits of {input_number} is {sum_of_digits}')