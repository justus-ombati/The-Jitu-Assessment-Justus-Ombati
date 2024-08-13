def reverseString(input_string):
    # Reverse the string using slicing
    return input_string[::-1]

# Get input from the user
string = input("Type a string and hit enter: ")

revStr = reverseString(string)

print("Reversed word:", revStr)