def countVowels(input_string):
    # Define the set of vowels
    vowels = "aeiouAEIOU"
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for char in input_string:
        # If the character is a vowel, increment the counter
        if char in vowels:
            count += 1
    
    return count

sentence = input("Type sentence and hit enter: ")

numvowels = countVowels(sentence)
print("Your sentence has ",numvowels, "vowels.")