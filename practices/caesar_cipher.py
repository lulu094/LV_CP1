# LV - 2nd Caesar Cipher
# CS1400 A - Caesar Cipher Encoder and Decoder

# Access to numbers using ord() and chr()
# ord() = get ASCII number for a character
# chr() = get character from a number
# Combined with a for loop to process each character
for ch in "abc":
    print(f"{ch}= {ord(ch)}")
print(f"100 = {chr(100)}")
print()

# 1. Define encode() function: shift each letter forward by given amount.
# 2. Define decode() function: shift each letter backward by given amount.
# 3. Use for loop + ord()/chr() to convert and shift letters.
# 4. Ask user for inputs and print encoded/decoded message.

def encode(message,shift):
    '''Encodes a message by shifting letters forward in the alphabet'''
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord ('a')
        #Convert to number, shift, wrap, then convert it back
        shifted = (ord(char) - base + shift) %26 + base
        result += chr(shifted)
        else:
            result += char
    return result 


def decode(message,shift):
    '''Decodes a message by shifting letters backwards'''
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord ('a')
        #Convert to number, shift, wrap, then convert it back
        shifted = (ord(char) - base - shift) %26 + base
        result += chr(shifted)
        else:
            result += char
    return result 


# Main Program- Print statements
print("Choose operaration(1 for encode, 2 for decode):")
operation = input("Enter 1 or 2:")

message = input("Enter the message:")

