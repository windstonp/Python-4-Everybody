
file = './text.txt'

openFile = open(file)

dictionary = dict()
largest = 0

for line in openFile :
    words = line.split()
    for word in words :
        dictionary[word] = dictionary.get(word,0) + 1

for key,value in dictionary.items() :
    print(key,value)
    if value > largest :
        largest = value
        word = key
print("Done! Repetions:", largest, "Word:", word)