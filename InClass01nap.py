sentence = input("Enter a sentence: ")
dictionary = dict()

print("\nNumber of times each character appears in sentence:\n")

for character in sentence:
    occurences = sentence.count(character)
    dictionary[character] = occurences
    
print(dictionary)
