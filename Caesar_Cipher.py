def encrypt(text, shift, letter_bank):
    letter_bank = abcdefghijklnopqrstuvwxyz
    encrypted_text = int(input("Enter the text you wish to encrypt: "))
    for i in text.upper():
        if i in letter_bank:
            index = (letter_bank.index(i) + shift) % len(letter_bank)
            encrypted_text += letter_bank[index]
        else:
            encrypted_text += i
    return encrypted_text

print(encrypt(text, shift, letter_bank))    