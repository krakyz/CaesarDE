import re
import webbrowser
from tkinter import *


def callback(url):
    webbrowser.open_new(url)


def copy_text(containing_widget):
    """ Копировать содержимое виджета текстового поля в буфер обмена. """
    containing_widget.clipboard_clear()  # Очистить буфер обмена
    containing_widget.clipboard_append(
        containing_widget.get("1.0", END))  # Скопировать текст из Text виджета в буфер обмена


def paste_text(containing_widget):
    """ Вставить текст из буфера обмена в виджет текстового поля. """
    try:
        text = containing_widget.selection_get(selection='CLIPBOARD')  # Получить текст из буфера обмена
        containing_widget.insert(INSERT, text)  # Вставить текст в виджет Text
    except TclError:
        pass  # Обработка ошибки, если буфер обмена пуст или содержимое невозможно получить


def clear_textfield(containing_widget):
    """ Очистить содержимое виджета текстового поля. """
    containing_widget.delete("1.0", END)


def detect_language(text):
    if re.search(r'[А-Я]', text):
        language = 'ru'
    elif re.search(r'[A-Z]', text):
        language = 'en'
    else:
        raise ValueError("Введите текст на русском или английском.")

    return language


def fix_text(text, mode: str):
    """ mode - decryption или encryption"""
    text = text.upper().replace('Ё', 'Е')

    if re.search(r'[\d]', #^a-zA-Zа-яА-ЯёЁ\s.,!?;:\-–—\'"«»“”
                 text):  # или просто \d, чтобы уведомлять, что в тексте есть цифры
        raise ValueError(
            "В тексте не должно быть цифр или других небуквенных символов. Напишите их текстом или очистите текст от этих символов.")

    if re.search(r'[А-Я]', text) and re.search(r'[A-Z]', text):
        raise ValueError("Текст содержит символы из русского и английского алфавитов. Используйте один алфавит.")

    if mode == 'encryption':
        text = re.sub(r'[^A-ZА-Я]', '', text)
        # text = ' '.join([text[i:i + 5] for i in range(0, len(text), 5)])
    return text


def get_frequency(cipher):
    cipher_frequencies = {}
    total_count = len(cipher)
    for char in cipher:
        if char in cipher_frequencies:
            cipher_frequencies[char] += 1
        else:
            cipher_frequencies[char] = 1
    for char in cipher_frequencies:
        cipher_frequencies[char] = (cipher_frequencies[char] / total_count)
    return cipher_frequencies


def least_squares(real_frequency, expected_frequency):
    return sum(
        (real_frequency.get(char, 0) - expected_frequency.get(char, 0)) ** 2 for char in expected_frequency)


def decryption(cipher, alphabet, frequency_table):
    # cipher = fix_text(cipher, 'decryption')
    best_shift = None
    min_error = float('inf')
    for shift in range(len(alphabet)):
        decrypted_text = ''.join(
            alphabet[(alphabet.index(char) - shift) % len(alphabet)] if char in alphabet else char
            for char in cipher
        )
        decrypted_frequency = get_frequency(decrypted_text)
        error = least_squares(decrypted_frequency, frequency_table)
        if error < min_error:
            min_error = error
            best_shift = shift
    decrypted_text = ''.join(
        alphabet[(alphabet.index(char) - best_shift) % len(alphabet)] if char in alphabet else char
        for char in cipher
    )
    return decrypted_text, best_shift
