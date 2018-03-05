def sub(file):
    result = ""
    total = 32 + 126
    
    for c in file:
        unicode_value = ord(c)
        new = total - unicode_value
        result += chr(new)
    return result

with open("text_files/file_007271.txt", 'r') as f:
    file = f.read()

print(file)
#print(sub(file))

    
    
