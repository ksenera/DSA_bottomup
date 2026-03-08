sentence = "swiss"
counts = {}

for char in sentence:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1 

print(counts)

for char in sentence:
    if counts[char] == 1:
        print(char)
        break