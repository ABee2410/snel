#vigenere cipher

def encrypt(message, key):
    encryption = ""
    loc = 0
    for i in range(len(message)):
        
        ######total = ord(message[loc]) + ord(key[loc])
        ######basic = total / 2
               
        if basic < 32:
            new = 31 - basic
            new_value = 126 - new
        
        elif basic > 126:
            new = basic - 126
            new_value = 31 + new

        else:
            new_value = basic
        
        new_letter = chr(new_value)


        encryption += new_letter
        loc +=1
        
    return(encryption)


                   
def key(message):

    key = ""

    for i in range(len(message)):
        if len(key)==0:
            key+="e"
        elif key[-1]=="e":
            key+="n"
        elif key[-1]=="n":
            key+="i"
        elif key[-1]=="i":
            key+="g"
        elif key[-1]=="g":
            key+="m"
        elif key[-1]=="m":
            key+="a"
        elif key[-1]=="a":
            key+="e"

    return key

with open("text_files/file_007474.txt", 'r') as f:
    message = f.read()
print(encrypt(message, key(message)))
