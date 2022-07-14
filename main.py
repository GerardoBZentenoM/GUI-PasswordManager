import tkinter

# ---------------------------- PASSWORD GENERATOR ---------------------------#

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    file_object = open('secrets.txt', 'a+')
    file_object.write(
        f"{entry_website.get()} | {entry_username.get()} | {entry_password.get()} \n")
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

button_generate_password = tkinter.Button(text="Generate Password")
button_generate_password.grid(column=2, row=3)

button_add_password = tkinter.Button(text="Add", width=41, command=save)
button_add_password.grid(column=1, row=4, columnspan=2)


window.mainloop()
