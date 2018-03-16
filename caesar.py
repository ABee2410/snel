def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount

    if unicode_value < 32:
        new = 31 - unicode_value
        new_value = 126 - new
        
    elif unicode_value > 126:
        new = unicode_value - 126
        new_value = 31 + new

    else:
        new_value = ord(letter) + shift_amount
        
    
    new_letter = chr(new_value)

    return new_letter


def decrypt(message, shift_amount):
    decryption = ""
    for letter in message:
        decryption += shift(letter, shift_amount)
        
    return decryption
def get_file_name(i):
    if i<10:
        zeros = "00000"
    elif i<100:
        zeros = "0000"
    elif i<1000:
        zeros = "000"
    elif i<10000:
        zeros = "00"
    else:
        zeros = "0"

    file_name = "text_files/file_" + zeros + str(i) + ".txt"

    return file_name



with open(get_file_name(1597), 'r') as f:
    message = f.read()
print(decrypt(message, -34))
