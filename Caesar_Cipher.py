def shift_character(char, shift_amount, encrypt=True):
    if char.isalpha():
        is_upper = char.isupper()
        num = ord(char.lower()) - ord('a')
        if encrypt:
            num = (num + shift_amount) % 26
        else:
            num = (num - shift_amount) % 26
        shifted_char = chr(num + ord('a'))
        return shifted_char.upper() if is_upper else shifted_char
    else:
        return char

def encrypt(message, shift):
    return ''.join(shift_character(char, shift, encrypt=True) for char in message)

def decrypt(message, shift):
    return ''.join(shift_character(char, shift, encrypt=False) for char in message)

def print_result(operation, original, result, shift):
    print("\n" + "=" * 40)
    print(f"Operation: {operation}")
    print(f"Shift value: {shift}")
    print("-" * 40)
    print(f"Original message: {original}")
    print(f"Processed message: {result}")
    print("=" * 40 + "\n")

print("Welcome to the Caesar Cipher Program!")
print("-------------------------------------")

while True:
    print("\nMENU:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '3':
        break
    elif choice not in ['1', '2']:
        print("Invalid choice. Please try again.")
        continue
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (0-25): "))
    
    if choice == '1':
        result = encrypt(message, shift)
        print_result("Encryption", message, result, shift)
    else:
        result = decrypt(message, shift)
        print_result("Decryption", message, result, shift)

print("\nThank you for using the Caesar Cipher program!")
