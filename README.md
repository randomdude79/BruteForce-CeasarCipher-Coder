# Encryption and Decryption Python system with BruteForce

This Python program provides functionality for text encryption, decryption, and brute force decryption. Upon execution, it prompts the user to choose an operation: encrypt, decrypt, or brute force decrypt. 

For encryption (`encrypt` or `e`), the user is asked to input text and a key. Each character in the input text is shifted by the key value, and the encrypted text is saved to a file called `encrypt.txt` along with the encryption key.

For decryption (`decrypt` or `d`), the user is asked to input the text to decrypt and the decryption key. Each character in the input text is shifted back by the key value, and the decrypted text is printed to the console.

For brute force decryption (`bruteForceDecrypt` or `bDF`), the user is asked to input the text to decrypt. The program then attempts all possible key values (1 to 126) to decrypt the text and saves all decryption results to a file called `bruteForceDecrypt.txt`.

The program uses a global `resultsList` to store encryption/decryption results temporarily and provides a recursive `main` function to allow the user to perform multiple operations without restarting the program.

### All credits go to Me, ChatGPT (for simplifying the code), and my Python code teacher.
