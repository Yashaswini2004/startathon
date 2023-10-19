def roman_to_integer(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10,'L':50, 'C': 100, 'D': 500, 'M': 1000}
    previous_value = 0
    result = 0
    for char in roman_numeral[::-1]:
        current_value = roman_dict[char]
        if current_value >= previous_value:
            result += current_value
        else:
            result -= current_value
        previous_value = current_value
    return result

print(roman_to_integer('XXIV'))       # Output: 24
print(roman_to_integer('MMMCMLXXXVI')) # Output: 3986
