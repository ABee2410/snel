alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
key =      "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "


def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]
    return result


with open("text_files/file_007271.txt", 'r') as f:
    file = f.read()
print(decrypt(file))


