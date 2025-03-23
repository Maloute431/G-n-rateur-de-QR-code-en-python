import os
import qrcode
from tkinter import *

def on_focus_in(event, entry, hint_text):
    if entry.get() == hint_text:
        entry.delete(0, END)
        entry.config(fg='black')

def on_focus_out(event, entry, hint_text):
    
    if entry.get() == '':
        entry.insert(0, hint_text)
        entry.config(fg='gray')

def on_focus_in2(event, entry, hint_text2):
    if entry.get() == hint_text2:
        entry.delete(0, END)
        entry.config(fg='black')

def on_focus_out2(event, entry, hint_text2):
    if entry.get() == '':
        entry.insert(0, hint_text2)
        entry.config(fg='gray')

hint_text = "Contenu du QR Code"
hint_text1 = "Nom du fichier"

window = Tk()
window.geometry("420x420")
window.config(bg='#ecdaf5')
window.title("Générateur de QR Code V1.43")

title = Label(window, text="Générateur de QR Code  ", fg='black', bg='#ecdaf5', font=("Poppins", 20, 'bold'))
title.pack()

thing_to_say = Entry(window, font=('Poppins', 15))
thing_to_say.pack(pady=10)
thing_to_say.insert(0, hint_text)
thing_to_say.bind("<FocusIn>", lambda event: on_focus_in(event, thing_to_say, hint_text))
thing_to_say.bind("<FocusOut>", lambda event: on_focus_out(event, thing_to_say, hint_text))

file_name = Entry(window, font=('Poppins', 15))
file_name.pack(pady=10)
file_name.insert(0, hint_text1)
file_name.bind("<FocusIn>", lambda event: on_focus_in(event, file_name, hint_text1))
file_name.bind("<FocusOut>", lambda event: on_focus_out(event, file_name, hint_text1))



def save():
    data = thing_to_say.get()
    file = file_name.get()

    if not data or not file:
        message_label.config(text="Erreur : Veuillez remplir tous les champs", fg="red")
        return
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    save_dir = os.path.join(desktop_path, "QR Codes")
    os.makedirs(save_dir, exist_ok=True)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    file_path = os.path.join(save_dir, f"{file}.png")
    img.save(file_path)

    message_label.config(text=f"QR code enregistré dans {desktop_path}", fg="black", font=('Poppins'))

action = Button(window, text='Générer le QR Code', command=save, font=('Poppins', 12))
action.pack(pady=20)

message_label = Label(window, text="", fg="green", bg='#ecdaf5', font=("Poppins", 12))
message_label.pack(pady=10)

window.mainloop()
