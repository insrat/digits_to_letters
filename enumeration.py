import sys

KEYBOARD_DEFINE = {
    0: (''),
    1: (''),
    2: ('a', 'b', 'c'),
    3: ('d', 'e', 'f'),
    4: ('g', 'h', 'i'),
    5: ('j', 'k', 'l'),
    6: ('m', 'n', 'o'),
    7: ('p', 'q', 'r', 's'),
    8: ('t', 'u', 'v'),
    9: ('w', 'x', 'y', 'z'),
}

def divided_digits(digits_list):
    """
    Separate numbers into digits
    """
    n_digits_list = []
    for val in digits_list:
        tmp = []
        while val:
            tmp.append(val % 10)
            val //= 10
        n_digits_list.extend(tmp[::-1])
    return n_digits_list

def digits_to_letters(digits_list, letters_list, pos, data):
    """
    Converting the digits into letters
    """
    # Verification end position
    if len(digits_list) == pos:
        letters_list.append(data)
        return
    # Recursive processing
    for val in KEYBOARD_DEFINE[digits_list[pos]]:
        digits_to_letters(digits_list, letters_list, pos+1, data+val)
    return

if __name__ == '__main__':
    # Verify input data
    try:
        input_data = input('Input (Separated by commas): ')
        digits_list = [int(val) for val in input_data.split(',')]
        digits_list = divided_digits(digits_list)
    except Exception as err:
        print ('Input data error:', err)
        sys.exit(1)
    # Calculation results
    letters_list = []
    digits_to_letters(digits_list, letters_list, 0, '')
    print ('Ouput:', letters_list)