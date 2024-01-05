input_string = input('Enter the desired string or value: ')

uppercase_count = lowercase_count = digit_count = space_count = special_char_count = 0

for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        special_char_count += 1

print(f'The number of uppercase letters is {uppercase_count}')
print(f'The number of lowercase letters is {lowercase_count}')
print(f'The number of digits is {digit_count}')
print(f'The number of spaces is {space_count}')
print(f'The number of special characters is {special_char_count}')