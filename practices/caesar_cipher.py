# LV - 2nd Caesar Cipher
# This program encodes or decodes a message using the Caesar Cipher.
# It includes two main functions: encode() and decode().
# The program asks the user for input, applies the cipher, and prints the result.

# PSEUDOCODE
# 1. Ask user if they want to encode or decode a message
# 2. Get the message text from the user
# 3. Get the shift amount (integer)
# 4. If encode, call encode(message, shift)
# 5. If decode, call decode(message, shift)
# 6. Print the result in a clear format


# FUNCTION: encode()
def encode(message, shift):
    '''Encodes a message by shifting letters forward in the alphabet'''
    result = ""  # Empty string to store result

    for char in message:
        if char.isalpha():  # Check if character is a letter
            base = ord('A') if char.isupper() else ord('a')
            # Convert to number, shift forward, wrap around, then convert back
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result


# FUNCTION: decode()
def decode(message, shift):
    '''Decodes a message by shifting letters backward in the alphabet'''
    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Convert to number, shift backward, wrap around, then convert back
            shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result


# MAIN PROGRAM FLOW
# 1. Ask user for operation type
print("Choose operation (1 for encode, 2 for decode):")
operation = input("Enter 1 or 2: ")

# 2. Ask for the message
message = input("Enter the message: ")

# 3. Ask for shift value (ensure it’s an integer)
while True:
    try:
        shift = int(input("Enter the shift value: "))
        break
    except ValueError:
        print("Please enter a valid integer for the shift value.")

# 4. Perform the chosen operation and store result
encoded = ""
decoded = ""
output_message = ""

if operation == "1":
    output_message = encode(message, shift)
    result_type = "Encoded"
elif operation == "2":
    output_message = decode(message, shift)
    result_type = "Decoded"
else:
    result_type = "Invalid"
    output_message = "Invalid choice. Please restart and choose 1 or 2."

# 5. Print final result (moved to end)
print("\n---------------------------")
if result_type == "Invalid":
    print(output_message)
else:
    print(f"{result_type} message: {output_message}")
print("---------------------------")


