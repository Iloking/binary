def binary_to_decimal(binary_str):
    decimal = 0
    power = len(binary_str) - 1  

   
    for digit in binary_str:
        decimal += int(digit) * (2 ** power)
        power -= 1  
    
    return decimal

binary_input = input("Enter a binary number: ")

if all(char in '01' for char in binary_input):
    
    result = binary_to_decimal(binary_input)
    print(f"The decimal equivalent of binary {binary_input} is: {result}")
else:
    print("Invalid input! Please enter a binary number (only 0s and 1s).")
