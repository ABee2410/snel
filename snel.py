import random

def generate_random_text(num_chars):
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text


def mean(counts):
    pass

    return 0

def chi_square(counts):
    expected = mean(counts)
    
    X = 0

    for n in counts:
        pass

    return X



#bunch_of_text = "asdfhjkjaewhfkljsadhflkjhasedfi9835u2xifu-q3ymtocfjd;sk^%$#^YJH&I*^%$*%TNIOUYTYU^RYI^RGLKHNJJKYTB"


#print(counts)


with open(file, 'r') as f:
    text = f.read()
    
counts = [0] * 127
    
for c in text:
    n = ord(c)
    counts[n] += 1

counts = counts[32:]

mean(counts)

print(chi_square(counts))


