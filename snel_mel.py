import random

def generate_random_text(num_chars):
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text


def mean(counts):
    total=0
    for n in counts:
        total+=n
        
    a = total/len(counts)
    return a
    

def chi_square(counts):
    expected = mean(counts)
    
    X = 0

    for n in counts:
        X+=(n-expected)**2

    return X/expected


'''
content = generate_random_text(15000)

# code here to write content to a file
with open('new_file.txt', 'w') as f:
    f.write(content)
    
with open('new_file.txt', 'r') as f:
    random = f.read()

#print(random)

'''

counts = [0] * 127


'''
for c in random:
    n = ord(c)
    counts[n] += 1

print(counts)

counts = counts[32:]

mean(counts)
print(mean(counts))


print(chi_square(counts))
'''
with open('all_caps.txt', 'r') as f:
    caps = f.read()

for c in caps:
    n = ord(c)
    counts[n] += 1

print(counts[35])
