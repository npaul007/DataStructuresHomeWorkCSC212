# function that returns reversed string using recursion
def reverseString(string):
    if len(string) < 1:
        return string
    else:
        foo = reverseString(string[1:]) + string[0]
        return foo

# function that prints string in reverse starting from rightmost character
def rec_string(string):
    if len(string) < 1:
        return string
    else:
        foo = rec_string(string[1:]) + string[0]
        print(string[0:])
        return foo

def main():
    # reverse function
    print(reverseString("hello world"))
    print('\n')

    # rec_string function 
    rec_string('abcde')
    print('\n')
    rec_string('abc')
        
if __name__ == "__main__":
    main()


