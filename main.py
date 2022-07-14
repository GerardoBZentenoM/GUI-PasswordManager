import tkinter

# ---------------------------- PASSWORD GENERATOR ---------------------------#

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(column=1, row=0)

label_website = tkinter.Label(text="Website: ")
label_website.grid(column=0, row=1)

label_username = tkinter.Label(text="Email/Username: ")
label_username.grid(column=0, row=2)

label_password = tkinter.Label(text="Password: ")
label_password.grid(column=0, row=3)

entry_website = tkinter.Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)

entry_username = tkinter.Entry(width=35)
entry_username.grid(column=1, row=2, columnspan=2)

entry_password = tkinter.Entry(width=21)
entry_password.grid(column=1, row=3)

button_generate_password = tkinter.Button(text="Generate Password")
button_generate_password.grid(column=2, row=3)

button_add_password = tkinter.Button(text="Add", width=36)
button_add_password.grid(column=1, row=4)


window.mainloop()
