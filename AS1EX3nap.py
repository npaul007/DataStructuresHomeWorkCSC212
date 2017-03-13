text = input("Enter some text:")
word = input("Enter a word:")

if word in text:
    i = 0
    index = 0
    
    print("Indices:")
    
    while index != -1:
        if index != text.find(word,i) and text.find(word,i) != -1:
            print(text.find(word,i))

        index = text.find(word,i)    
        i = i + 1
else:
    print("Not Found")
    
