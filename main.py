from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_pas():
    try:
        with open("myfile.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        print("No data file found")
        sites = [x for x in data]
        website = website_input.get()
        for x in data:
            if x == website:
                email=data[x]["email"]
                password=data[x]["password"]
                messagebox.showinfo(title="Credentials", message=f"Your credentials are:\nemail: {email}\npassword: {password}")
            if website not in sites:
                messagebox.showinfo(title="Credentials", message="No data to show for this site")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_pas():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    psd_input.delete(0, END)
    rand_letters = [choice(letters) for _ in range(randint(8, 10))]
    rand_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    rand_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = rand_letters + rand_symbols + rand_numbers
    shuffle(password_list)

    password = "".join(password_list)
    psd_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    psd = psd_input.get()
    new_data={
        website:{
            "email": email,
            "password": psd
        }
    }
    if website == "" or email == "" or psd == "":
        messagebox.showerror(title="error", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title="Is ok ?", message=f"Here are your credentials\nwebsite: {website}\ne-mail: "
                                                                f"{email}\npassword :{psd}\nDo you want to save them?")
        if is_ok:
            try:
                with open("myfile.json", 'r') as file:
                    data=json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("myfile.json", 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("myfile.json", 'w') as file2:
                    json.dump(data, file2, indent=4)
                website_input.delete(0, 'end')
                email_input.delete(0, 'end')
                email_input.insert(0, "florin@gmail.com")
                psd_input.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

psd_label = Label(text="Password:")
psd_label.grid(row=3, column=0)

website_input = Entry(width=34)
website_input.grid(row=1, column=1, sticky='w')
website_input.focus()

email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2, sticky='w')
email_input.insert(0, "florin@gmail.com")
psd_input = Entry(width=34)
psd_input.grid(row=3, column=1, sticky='w')

buton_generate = Button(text="Generate Password", command=random_pas)
buton_generate.grid(row=3, column=2)

buton_add = Button(text="Add", width=44, command=save)
buton_add.grid(row=4, column=1, columnspan=2)

buton_search = Button(text="Search", width=14, command=find_pas)
buton_search.grid(row=1, column=2, sticky="w")
window.mainloop()