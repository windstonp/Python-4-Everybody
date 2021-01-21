
file = './text.txt'

openFile = open(file)

dictionary = dict()

for line in openFile :
    words = line.split()
    for word in words :
        dictionary[word] = dictionary.get(word,0) + 1

temp = list()
for k,v in dictionary.items() :
    newt = (v,k)
    temp.append(newt)

temp =sorted(temp, reverse=True)

for v,k in temp[:5] :
    print(k,v)