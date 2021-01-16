fh = open("romeo.txt")
text = list()
for line in fh:
    line = line.split()
    for word in line :
        if word not in text :
            text.append(word)

text.sort()
print(text)