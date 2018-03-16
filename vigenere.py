#vigenere cipher

def encrypt(message, key):
    encryption = ""
    
    for l in range(len(message)):
     
        value = ord(message[l])+ord(key[l])
               
        if value < 32:
            new = 31 - value
            new_value = 126 - new
        
        elif value > 126:
            new = value - 126
            new_value = 31 + new

        else:
            new_value = value
        
        new_letter = chr(new_value)
        encryption += new_letter
        
    return(encryption)


def decrypt(message, key):
    decryption = ""
    
    for l in range(len(message)):
        value = ord(message[l])-ord(key[l])
        
        while value < 32:
            value+=95
        
        new_letter = chr(value)
        decryption += new_letter
         
    return(decryption)

                   
def key(message, word):
    
    key = ""
    
    full_times = len(message)//len(word)
    
    for i in range(full_times):
        key += word

    end = len(message)% len(word)
    key += word[0:end]

    return key


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



with open(get_file_name(16499), 'r') as f:
    message = f.read()
print(decrypt(message, key(message, "enigma")))
