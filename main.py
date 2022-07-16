import email
import tkinter
import json
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
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        tkinter.messagebox.askokcancel(
            title="Error", message=f"Please fill all the entries")
    else:

        is_ok = tkinter.messagebox.askokcancel(
            title=website, message=f"Username: {username} Password: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                entry_website.delete(0,  tkinter.END)
                entry_password.delete(0, tkinter.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            tkinter.messagebox.showinfo(title=website, message=f"username: {username}\nPassword: {password}")
        else:
            tkinter.messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

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

search_button = tkinter.Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()
