# PRODIGY_CS_02
# Caesar Cipher Program

This project is a Python implementation of the Caesar Cipher, a simple encryption technique. The program allows users to encrypt and decrypt messages by shifting the letters of the input text by a specified amount. It provides a menu-driven interface to choose between encryption, decryption, and exiting the program.

## Features

- **Encryption:** Encrypts a message using a user-defined shift value.
- **Decryption:** Decrypts a message using the same shift value.
- **User Input:** Prompts the user to input the message and the shift value (between 0 and 25).
- **Menu-Driven:** Easy-to-use menu interface to select operations.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Running the Program

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/raby02/PRODIGY_CS_01.git
    ```
2. Navigate to the project directory.
    ```bash
    cd caesar-cipher
    ```
3. Run the Python program.
    ```bash
    python caesar_cipher.py
    ```

## Code Overview

The core functions of the program are:

- **`shift_character(char, shift_amount, encrypt=True)`**:
  - Shifts a single character by the specified amount. Handles both encryption and decryption.
  - Keeps the character's case (uppercase or lowercase) intact.
  - Returns the shifted character.

- **`encrypt(message, shift)`**:
  - Encrypts an entire message using the Caesar Cipher technique by shifting each character in the message by the specified shift value.

- **`decrypt(message, shift)`**:
  - Decrypts a message that was encrypted using the Caesar Cipher by shifting each character back by the shift value.

- **`print_result(operation, original, result, shift)`**:
  - Prints the operation (encryption/decryption), the original message, the processed (encrypted/decrypted) message, and the shift value in a formatted way.

- **Main Loop**:
  - Provides a menu for the user to choose between encryption, decryption, or quitting the program.
  - Takes user input for the message and shift value.
  - Calls the appropriate function based on the user's choice.

## Example Usage

```plaintext
Welcome to the Caesar Cipher Program!
-------------------------------------

MENU:
1. Encrypt a message
2. Decrypt a message
3. Quit

Enter your choice (1/2/3): 1
Enter the message: Hello World
Enter the shift value (0-25): 3

========================================
Operation: Encryption
Shift value: 3
----------------------------------------
Original message: Hello World
Processed message: Khoor Zruog
========================================
