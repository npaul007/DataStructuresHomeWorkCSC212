file = open('example.txt','r')
newFile = open('fourLetter.txt','w')

for word in file.read().split():
    if len(word) == 4:
        newFile.write('****' + ' ')
    else:
        newFile.write(word + ' ')

newFile.close()
file.close()


