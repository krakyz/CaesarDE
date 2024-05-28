import tools


def encode_message(message, cipher_shift):
    message = tools.fix_text(message, 'encryption')

    cipher = []

    for char in message:
        language = tools.detect_language(char)

        if language == 'ru':
            alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        if language == 'en':
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        cipher_shift = cipher_shift % len(alphabet)

        if char in alphabet:
            index = (alphabet.index(char) + cipher_shift) % len(alphabet)
            cipher.append(alphabet[index])

    cipher = ''.join(cipher)
    cipher = ' '.join([cipher[i:i + 5] for i in range(0, len(cipher), 5)])

    return cipher


# print(encrypt_message('ABCDE. АБВГДЕЁ', 1))
