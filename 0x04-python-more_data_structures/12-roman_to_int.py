def roman_to_int(roman_string: str):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    
    for i in range(len(roman_string)):
        if i > 0 and data[roman_string[i]] > data[roman_string[i - 1]]:
            total += data[roman_string[i]] - 2 * data[roman_string[i - 1]]
        else:
            total += data[roman_string[i]]
            
    return total
