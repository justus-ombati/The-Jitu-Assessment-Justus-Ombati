def filterEvenNumbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numArray = []

while True:
    userInput = input("Enter an integer (or press 'C' to finish): ")
    
    if userInput.upper() == 'C':
        break 
    
    try:
        numArray.append(int(userInput))
    except ValueError:
        print("Please enter a valid integer.")

numOutput = filterEvenNumbers(numArray)

print("Even numbers in your array are:", numOutput)