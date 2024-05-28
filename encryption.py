import tools
import re


# def caesar_encryption(text, cipher_shift):
#     """
#     Кодирование текста с заданным сдвигом.
#     Автоматическое обнаружение кириллицы и латиницы.
#     Замена буквы Ё на Е.
#     Очистка текста от знаков препинания, небуквенных символов, пробелов.
#     Разбивка обработанного текста группами по пять символов.
#     Защита от неправильных действий пользователя.
#     """
#
#     if re.search(r'[^a-zA-Zа-яА-ЯёЁ\s.,!?;:\-–—\'"«»“”]',
#                  text):  # или просто \d, чтобы уведомлять, что в тексте есть буквы
#         raise ValueError(
#             "В тексте не должно быть цифр или других небуквенных символов. Напишите их текстом или очистите текст от этих символов.")
#
#     text = text.upper()
#     text = text.replace('Ё', 'Е')
#
#     ru_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     en_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#     if re.search(r'[А-Я]', text) and re.search(r'[A-Z]', text):
#         raise ValueError("Текст содержит символы из русского и английского алфавитов. Используйте один алфавит.")
#
#     if re.search(r'[А-Я]', text):
#         alphabet = ru_alphabet
#     elif re.search(r'[A-Z]', text):
#         alphabet = en_alphabet
#     else:
#         raise ValueError("Введите текст на русском или английском.")
#
#     cleaned_text = re.sub(r'[^A-ZА-Я]', '', text)
#
#     shifted_text = []
#
#     for char in cleaned_text:
#         if char in alphabet:
#             # поиск индекса символа в алфавите для навигации по алфавиту
#             index = (alphabet.index(char) + cipher_shift) % len(alphabet)
#             # добавление смещенного символа к зашифрованному тексту
#             shifted_text.append(alphabet[index])
#
#     ungrouped_encrypted_text = ''.join(shifted_text)
#     encrypted_text = ' '.join([ungrouped_encrypted_text[i:i + 5] for i in range(0, len(ungrouped_encrypted_text), 5)])
#
#     return encrypted_text


def encrypt_message(message, cipher_shift):

    message = tools.fix_text(message, 'encryption')
    language = tools.detect_language(message)

    if language == 'ru':
        alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    cipher = []
    for char in message:
        if char in alphabet:
            index = (alphabet.index(char) + cipher_shift) % len(alphabet)
            cipher.append(alphabet[index])

    cipher = ''.join(cipher)
    cipher = ' '.join([cipher[i:i + 5] for i in range(0, len(cipher), 5)])

    return cipher


print(encrypt_message('ВОТ оТКРЫТ БАЛАГАНЧИК ДЛЯ ВЕСЕЛЫХ И СЛАВНЫХ ДЕТЕЙ СМО', 14))
