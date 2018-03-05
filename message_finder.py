#functions
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

#loop through the files and do this


for i in range(18000):
    file_name = get_file_name(i)
    
    

    with open(file_name, 'r') as f:
        text = f.read()
    
    counts = [0] * 127
    
    for c in text:
        n = ord(c)
        counts[n] += 1

    counts = counts[32:]

    mean(counts)

    if (chi_square(counts))>155:
        print(file_name)
        print(chi_square(counts))

print("done")
