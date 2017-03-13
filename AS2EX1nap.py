# returns dictionary of string
def getDictionary(string):
	dictionary = dict()

	for char in string:
	    dictionary[char] = string.count(char)

	return dictionary

''' compares dictionaries, returns true if both contain
    same number of characters, false if otherwise
'''
def checkDictionaries(d1,d2):
	possible = []

	for char1 in d1:
		for char2 in d2:
			if len(d1) != len(d2):
				del possible[:]
				possible.append(False)

			elif char1 == char2:
				if d1[char1] == d2[char2]:
					possible.append(True)
				else:
					del possible[:]
					possible.append(False)

	return possible[0]

magazine = input("Enter the magazine: ")
ransomNote = input("Enter the required ransome note: ")

print(checkDictionaries(getDictionary(magazine),getDictionary(ransomNote)))