# stack class
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def reverse(self):
        self.items.reverse()

    def wordIsPalindrome(self,word):
        status = False
        stackOne = Stack()
        stackTwo = Stack()
        
        for char in word:
            stackOne.push(char)
            stackTwo.push(char)

        # format stackTwo backwards
        stackTwo.reverse()

        # if sequence is not perfectly the same break loop return false
        for i in range(0,len(word)-1):
            if stackOne.items[i] == stackTwo.items[i]:
                status = True
            else:
                status = False
                break
                 
        return status

#main method
def main():
    #stack instance
    stack = Stack()

    # user inputs word
    word = input("Please enter a word: ")

    # method returns true if word is a palindrome
    if stack.wordIsPalindrome(word) == True:
        print("This word is a palindrome.")
    else:
        print("This word is not a palindrome")

if __name__ == "__main__":
    main()
    