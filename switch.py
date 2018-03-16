def switch(file):
    result = ""
    total = 32 + 126
    
    for c in file:
        unicode_value = ord(c)
        new = total - unicode_value
        result += chr(new)
    return result

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



with open(get_file_name(7271), 'r') as f:
    file = f.read()

print(switch(file))

    
    
