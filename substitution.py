alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
key =      "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "


def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]
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


with open(get_file_name(10005), 'r') as f:
    file = f.read()

print(decrypt(file))


