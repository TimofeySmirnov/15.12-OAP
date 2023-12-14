def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('А') + shift) % 33 + ord('А'))
            else:
                result += chr((ord(char) - ord('а') + shift) % 33 + ord('а'))
        else:
            result += char
    return result

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)


plaintext = input("Введите текст: ")
shift_value = int(input("Введите значение сдвига: "))

encrypted_text = encrypt_caesar(plaintext, shift_value)

print("Зашифрованный текст:", encrypted_text)

