def expanded_form(num):
    result = ''
    digits = str(num) # convert number to string
    for i, digit in enumerate(digits):
        if int(digit) > 0:
            if result == '':
                result += str(digit).ljust(len(str(digits))-i,'0')
            else:
                result += ' + ' + str(digit).ljust(len(str(digits))-i,'0')
    return result
