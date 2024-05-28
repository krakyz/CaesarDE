import tools

ENGLISH_FREQUENCIES = {
    'E': 12.7, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.49, 'V': 0.98, 'K': 0.77, 'X': 0.15, 'J': 0.15,
    'Q': 0.1, 'Z': 0.05
}

RUSSIAN_FREQUENCIES = {
    'А': 8.01, 'Б': 1.59, 'В': 4.54, 'Г': 1.70, 'Д': 2.98, 'Е': 8.49,
    'Ж': 0.94, 'З': 1.65, 'И': 7.35, 'Й': 1.21, 'К': 3.49, 'Л': 4.40,
    'М': 3.21, 'Н': 6.70, 'О': 10.97, 'П': 2.81, 'Р': 4.73, 'С': 5.47,
    'Т': 6.26, 'У': 2.62, 'Ф': 0.26, 'Х': 0.97, 'Ц': 0.48, 'Ч': 1.44,
    'Ш': 0.73, 'Щ': 0.36, 'Ъ': 0.04, 'Ы': 1.90, 'Ь': 1.74, 'Э': 0.32,
    'Ю': 0.64, 'Я': 2.01
}


def hack_message(cipher):
    cipher = tools.fix_text(cipher, 'hacking')
    language = tools.detect_language(cipher)

    if language == 'ru':
        alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        frequency_table = RUSSIAN_FREQUENCIES
    else:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        frequency_table = ENGLISH_FREQUENCIES
    decrypted_message, shift = tools.decryption(cipher, alphabet, frequency_table)
    return decrypted_message, shift


# print(decrypt_message('РЬАЬА ШЮЙАП ОЩОСО ЫЕЦШТ ЩНРУЯ УЩЙГЦ ЯЩОРЫ ЙГТУА УЧЯЪЬ'))
