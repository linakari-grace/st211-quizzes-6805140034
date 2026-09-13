import re

roman_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def roman_to_number(roman_string):
    total = 0
    for i in range(len(roman_string)):
        current_value = roman_map[roman_string[i]]
        if i + 1 < len(roman_string) and current_value < roman_map[roman_string[i + 1]]:
            total -= current_value
        else:
            total += current_value
    return total

def validate_roman_rules(roman_string):
    if re.search(r'V{2,}|L{2,}|D{2,}', roman_string):
        return False, "Error: Symbols V, L, and D cannot be repeated."
    
    if re.search(r'I{4,}|X{4,}|C{4,}|M{4,}', roman_string):
        return False, "Error: Symbols I, X, C, and M cannot be repeated more than 3 times."
        
    for i in range(len(roman_string) - 1):
        curr = roman_string[i]
        nxt = roman_string[i+1]
        curr_val = roman_map[curr]
        nxt_val = roman_map[nxt]
        
        if curr_val < nxt_val:
            if curr in 'VLD':
                return False, f"Error: '{curr}' cannot be placed in front of a larger symbol to subtract."
            if curr == 'I' and nxt not in 'VX':
                return False, "Error: 'I' can only be subtracted from 'V' or 'X'."
            if curr == 'X' and nxt not in 'LC':
                return False, "Error: 'X' can only be subtracted from 'L' or 'C'."
            if curr == 'C' and nxt not in 'DM':
                return False, "Error: 'C' can only be subtracted from 'D' or 'M'."
                
    return True, ""

# Test multiple Roman numerals
roman_numbers = ["III", "VIII", "VV", "IIII", "IX"]

for roman_number in roman_numbers:
    print(f"Evaluating Roman numeral: {roman_number}")

    is_valid, error_message = validate_roman_rules(roman_number)

    if not is_valid:
        print(error_message)
    else:
        result = roman_to_number(roman_number)
        print("The integer value is:", result)

    print()  # Blank line between results