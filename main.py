resultsList = []

def main():
    global resultsList
    result = ''
    initialInput = input('Would you like to encrypt, decrypt, or brute force decrypt?\n')

    if initialInput == 'encrypt':
        text = input('Enter text to encrypt:\n')
        key = int(input('Enter key:\n'))
        result = ''
        for char in text:
            symbol_code = ord(char)
            result += chr(symbol_code + key)
        resultsList.append(result)
        with open('encrypt.txt', 'w') as results:
            for result in resultsList:
                results.write(result + '\n')
        print("Encryption completed. Check 'encrypt.txt' for results.")
        print()
        main()

    elif initialInput == 'decrypt':
        text = input('Enter text to decrypt\n')
        key = int(input('Enter key:\n'))
        result = ''
        for char in text:
            symbol_code = ord(char)
            result += chr(symbol_code - key)
        print(result)
        print()
        main()

    elif initialInput == 'bruteForceDecrypt' or initialInput == 'bDF':
        text = input('Enter text to decrypt\n')
        for shift in range(1, 127):
            result = ''
            for char in text:
                symbol_code = ord(char)
                result += chr((symbol_code - shift) % 127)
            resultsList.append(result)
        with open('bruteForceDecryption.txt', 'w') as results:
            for result in resultsList:
                results.write(result + '\n')
        print("Brute force decryption completed. Check 'bruteForceDecryption.txt' for results.")
        print()
        main()

    else:
        print("Invalid input. Please try again.\n")
        main()

main()
