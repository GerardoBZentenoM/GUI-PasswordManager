import tkinter
from turtle import title
import random

import pyperclip


# ---------------------------- PASSWORD GENERATOR ---------------------------#
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters)
                        for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols)
                        for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers)
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    entry_website.get()
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(username) == 0 or len(password):
        tkinter.messagebox.askokcancel(
            title="Error", message=f"Please fill all the entries")
    else:
        is_ok = tkinter.messagebox.askokcancel(
            title=website, message=f"Username: {username} Password: {password}")
        if is_ok:
            file_object = open('secrets.txt', 'a+')
            file_object.write(
                f"{website} | {username} | {password} \n")
            file_object.close()
            entry_website.delete(0, tkinter.END)
            entry_password.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(135, 100, image=logo_img)

canvas.grid(column=1, row=0)

label_website = tkinter.Label(text="Website: ")
label_website.grid(column=0, row=1)

label_username = tkinter.Label(text="Email/Username: ")
label_username.grid(column=0, row=2)

label_password = tkinter.Label(text="Password: ")
label_password.grid(column=0, row=3)

entry_website = tkinter.Entry(width=44)
entry_website.grid(column=1, row=1, columnspan=2)

entry_username = tkinter.Entry(width=44)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "brallanzenteno@gmail.com")

entry_password = tkinter.Entry(width=25)
entry_password.grid(column=1, row=3)

button_generate_password = tkinter.Button(
    text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3)

button_add_password = tkinter.Button(text="Add", width=41, command=save)
button_add_password.grid(column=1, row=4, columnspan=2)


window.mainloop()
