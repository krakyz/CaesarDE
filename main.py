import encryption
import decryption
import tools
import tkinter as tk
from tkinter import ttk


# Функция для обновления событий
def update_cipher(event=None):
    cipher_text = decoder_input.get("1.0", tk.END).strip()
    # if cipher_text:
    #     decrypted_text, shift = decryption.decrypt_message(cipher_text)
    #     calculated_shift_label.config(text=f"Сдвиг: {shift}")
    #     decoder_output.config(state=tk.NORMAL)
    #     decoder_output.delete("1.0", tk.END)
    #     decoder_output.insert(tk.END, decrypted_text)
    #     decoder_output.config(state=tk.DISABLED)
    # else:
    #     calculated_shift_label.config(text="")
    try:
        if cipher_text:
            decrypted_text, shift = decryption.decrypt_message(cipher_text)
            calculated_shift_label.config(text=f"Сдвиг: {shift}")
            decoder_output.config(state=tk.NORMAL)
            decoder_output.delete("1.0", tk.END)
            decoder_output.insert(tk.END, decrypted_text)
            decoder_output.config(state=tk.DISABLED)
        else:
            calculated_shift_label.config(text="")
    except ValueError as e:
        decryption_error_label.config(text=str(e))

    try:
        set_shift = cipher_shift.get()
        text_original = encoder_input.get(1.0, tk.END).strip()
        encrypted_message = encryption.encrypt_message(text_original, set_shift)
        encoder_output.config(state=tk.NORMAL)
        encoder_output.delete(1.0, tk.END)
        encoder_output.insert(tk.END, encrypted_message)
        encoder_output.config(state=tk.DISABLED)
        encryption_error_label.config(text="")
    except ValueError as e:
        encryption_error_label.config(text=str(e))


def move_text():
    text = encoder_output.get("1.0", tk.END)  # Получаем текст из первого текстового поля
    decoder_input.delete("1.0", tk.END)  # Очищаем второе текстовое поле
    decoder_input.insert(tk.END, text)  # Вставляем текст во второе текстовое поле


# Создание главного окна
root = tk.Tk()
root.title('Caesar Cipher Encryption & Decryption')

# Создание фрейма-хэдера и его содержимого
header_frame = ttk.Frame(root, borderwidth=1, relief=tk.SOLID, padding=[16])
header_frame.pack(anchor=tk.NW, fill=tk.X, padx=16, pady=8)

name_label = tk.Label(header_frame, text="Шифратор и дешифратор шифра Цезаря", font='bold')
name_label.pack(anchor=tk.NW)

DE_logo = tk.PhotoImage(file="./logo.png")
logo_label = ttk.Label(header_frame, image=DE_logo, padding=[0, 16, 0, 0])
logo_label.pack(anchor=tk.NW)

link = tk.Label(header_frame, text="Что такое шифр Цезаря?", fg="blue", cursor="hand2")
link.pack(anchor=tk.NE)
link.bind("<Button-1>", lambda e: tools.callback(
    "https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F"))

link = tk.Label(header_frame, text="Взлом методом частотного анализа", fg="blue", cursor="hand2")
link.pack(anchor=tk.NE)
link.bind("<Button-1>", lambda e: tools.callback(
    "https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F#%D0%92%D0%B7%D0%BB%D0%BE%D0%BC_%D1%88%D0%B8%D1%84%D1%80%D0%B0"))

# Создание меню вкладок и вкладок кодирования и расшифровки
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill=tk.BOTH)

encoder_frame = ttk.Frame(notebook, padding=[16, 8])
encoder_frame.pack(fill=tk.BOTH, expand=True)
decoder_frame = ttk.Frame(notebook, padding=[16, 8])
decoder_frame.pack(fill=tk.BOTH, expand=True)

notebook.add(encoder_frame, text="Зашифрование")
notebook.add(decoder_frame, text="Расшифрование")

# Наполнение вкладки зашифрования
encoder_input_label = ttk.Label(encoder_frame, text='Исходное сообщение', padding=[0, 0, 0, 4])
encoder_input_label.pack(anchor=tk.NW)
encoder_input = tk.Text(encoder_frame, width=100, height=12, wrap=tk.WORD)
encoder_input.bind("<KeyRelease>", update_cipher)

encoder_input.pack(anchor=tk.NW)

# Создание кнопок для копирования, вставки и очищения текстового поля, создание сетки
button_grid = ttk.Frame(encoder_frame, padding=[0, 8, 0, 0])
copy_button = ttk.Button(button_grid, text="Копировать", padding=[8, 4], command=lambda: tools.copy_text(encoder_input))
copy_button.grid(row=1, column=0, padx=8)
paste_button = ttk.Button(button_grid, text="Вставить", padding=[8, 4], command=lambda: tools.paste_text(encoder_input))
paste_button.bind("<Motion>", update_cipher)
paste_button.grid(row=1, column=1)
clear_button = ttk.Button(button_grid, text="Очистить", padding=[8, 4],
                          command=lambda: tools.clear_textfield(encoder_input))
clear_button.bind("<ButtonRelease-1>", update_cipher)
clear_button.grid(row=1, column=2, padx=8)
button_grid.pack(anchor=tk.NE)

# Создание слайдера для регулировки смещения шифра

encoder_scale = ttk.Frame(encoder_frame, padding=[0, 8])
encoder_scale.pack(fill=tk.X)

label = ttk.Label(encoder_scale, text='Смещение шифра', padding=[0, 8])
label.pack(anchor=tk.NW)

cipher_shift = tk.IntVar()
scale = tk.Scale(encoder_scale, orient=tk.HORIZONTAL, length=600, from_=-0, to=32, variable=cipher_shift)
scale.pack(fill=tk.X)
scale.bind("<Motion>", update_cipher)
scale.bind("<ButtonRelease-1>", update_cipher)

# Поле для отображения ошибок
encryption_error_label = ttk.Label(encoder_scale, text="", foreground="red")
encryption_error_label.pack(pady=8)

encoder_output_label = ttk.Label(encoder_frame, text='Зашифрованное сообщение', padding=[0, 0, 0, 4])
encoder_output = tk.Text(encoder_frame, width=100, height=12, wrap=tk.WORD, state=tk.DISABLED)

encoder_output_label.pack(anchor=tk.NW)
encoder_output.pack(anchor=tk.NW)

button_grid = ttk.Frame(encoder_frame, padding=[0, 8, 0, 0])

copy_button = ttk.Button(button_grid, text="Копировать", padding=[8, 4],
                         command=lambda: tools.copy_text(encoder_output))
copy_button.grid(row=1, column=0, padx=8)
# paste_button = ttk.Button(button_grid, text='Перенести в "Расшифрование"', padding=[8, 4], command=move_text)
# paste_button.grid(row=1, column=1)

button_grid.pack(anchor=tk.NE)

# Наполнение вкладки расшифрования
decoder_input_label = ttk.Label(decoder_frame, text='Зашифрованное сообщение', padding=[0, 0, 0, 4])
decoder_input_label.pack(anchor=tk.NW)

decoder_input = tk.Text(decoder_frame, width=100, height=12, wrap=tk.WORD)
decoder_input.bind("<KeyRelease>", update_cipher)
decoder_input.pack(anchor=tk.NW)

button_grid = ttk.Frame(decoder_frame, padding=[0, 8, 0, 0])
copy_button = ttk.Button(button_grid, text="Копировать", padding=[8, 4], command=lambda: tools.copy_text(decoder_input))
copy_button.grid(row=1, column=0, padx=8)
paste_button = ttk.Button(button_grid, text="Вставить", padding=[8, 4], command=lambda: tools.paste_text(decoder_input))
paste_button.bind("<Motion>", update_cipher)
paste_button.grid(row=1, column=1)
clear_button = ttk.Button(button_grid, text="Очистить", padding=[8, 4],
                          command=lambda: tools.clear_textfield(decoder_input))
clear_button.bind("<ButtonRelease-1>", update_cipher)
clear_button.grid(row=1, column=2, padx=8)
button_grid.pack(anchor=tk.NE)

calculated_shift_label = ttk.Label(decoder_frame, text="", foreground="blue")
calculated_shift_label.pack(anchor=tk.NW, pady=8)

decryption_error_label = ttk.Label(decoder_frame, text="", foreground="red")
decryption_error_label.pack(pady=8)

decoder_output_label = ttk.Label(decoder_frame, text='Расшифрованное сообщение', padding=[0, 0, 0, 4])
decoder_output_label.pack(anchor=tk.NW)
decoder_output = tk.Text(decoder_frame, width=100, height=12, wrap=tk.WORD, state=tk.DISABLED)
decoder_output.pack(anchor=tk.NW)

button_grid = ttk.Frame(decoder_frame, padding=[0, 8, 0, 0])
copy_button = ttk.Button(button_grid, text="Копировать", padding=[8, 4],
                         command=lambda: tools.copy_text(decoder_output))
copy_button.grid(row=1, column=0, padx=8)
button_grid.pack(anchor=tk.NE)

root.mainloop()
