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

with open("text_files/file_001597.txt", 'r') as f:
    message = f.read()
print(decrypt(message, -34))
