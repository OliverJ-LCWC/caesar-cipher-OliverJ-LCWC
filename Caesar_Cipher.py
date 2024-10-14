def encrypt(text, shift):
    letter_bank = "abcdefghijklnopqrstuvwxyz"
    encrypted_text = ""
    for i in text.lower():
        if i in letter_bank:
            index = (letter_bank.index(i) + shift) % len(letter_bank)
            encrypted_text += letter_bank[index]
        else:
            encrypted_text += i
    return encrypted_text

def unencrypt(text, shift):
    letter_bank = "abcdefghijklnopqrstuvwxyz"
    encrypted_text = ""
    for i in text.lower():
        if i in letter_bank:
            index = (letter_bank.index(i) - shift) % len(letter_bank)
            encrypted_text += letter_bank[index]
        else:
            encrypted_text += i
    return encrypted_text