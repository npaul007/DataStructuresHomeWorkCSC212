print("Please enter 3 words.")

words = []

for i in range(0,3):
    words.append(input("Enter Word %i:" % (i+1)))

uniqueWords = []
unique = False
occurence = 0

for p in range(0,len(words)):
    for k in range(0,len(words)):
        if words[p] == words[k]:
            occurence = occurence + 1
            
        if occurence < 2:
            unique = True
            
        else:
            unique = False

    if unique:
        uniqueWords.append(words[p])

    occurence = 0


if len(uniqueWords) > 0:
    print("Unique Words:")
    for i in range(0,len(uniqueWords)):
        print(uniqueWords[i])
else:
    print("No Unique Words")