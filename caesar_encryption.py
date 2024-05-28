import re


def caesar_cipher(text, shift):
    # Убираем цифры из текста
    if re.search(r'\d', text):
        raise ValueError("В тексте не должно быть цифр.")

    # Заменяем Ё на Е
    text = text.replace('Ё', 'Е').replace('ё', 'е')

    # Определяем используемый алфавит
    ru_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    en_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    text = text.upper()

    if re.search(r'[А-Я]', text) and re.search(r'[A-Z]', text):
        raise ValueError("Текст содержит символы из обоих алфавитов. Используйте один алфавит.")

    if re.search(r'[А-Я]', text):
        alphabet = ru_alphabet
    elif re.search(r'[A-Z]', text):
        alphabet = en_alphabet
    else:
        raise ValueError("Текст не содержит букв.")

    # Обрабатываем текст, игнорируя пробелы и знаки препинания
    clean_text = re.sub(r'[^A-ZА-Я]', '', text)

    shifted_text = []

    for char in clean_text:
        if char in alphabet:
            idx = (alphabet.index(char) + shift) % len(alphabet)
            shifted_text.append(alphabet[idx])

    # Формируем зашифрованный текст с разделением по пять символов
    cipher_text = ''.join(shifted_text)
    grouped_cipher_text = ' '.join([cipher_text[i:i + 5] for i in range(0, len(cipher_text), 5)])

    return grouped_cipher_text


# Пример использования
try:
    text = input("Введите текст для шифрования: ")
    shift = int(input("Введите смещение: "))
    encrypted_text = caesar_cipher(text, shift)
    print("Зашифрованный текст:", encrypted_text)
except ValueError as e:
    print("Ошибка:", e)
