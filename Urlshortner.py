import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x250")
root.title("URL Shortener")
root.configure(bg="#F5F5F5")

url = StringVar()
url_address = StringVar()

def urlshortener():
    url_add = url.get()
    s = pyshorteners.Shortener()
    url_short = s.tinyurl.short(url_add)
    url_address.set(url_short)

def copy():
    url_short = url_address.get()
    pyperclip.copy(url_short)

title = Label(root, text="URL Shortener", font=("Roboto", 20), bg="#F5F5F5",fg="#333333")
title.pack(pady=10)

url_entry = Entry(root, textvariable=url, font=("calibar", 12), bd=2, relief=SOLID)
url_entry.pack(pady=10, padx=20, fill=X)

shorten_button = Button(root, text="Shorten URL", command=urlshortener, font=("Roboto", 12), bg="#D4A5A5", fg="#333333")
shorten_button.pack(pady=5)

url_result = Entry(root, textvariable=url_address, font=("Arial", 12), bd=2, relief=SOLID)
url_result.pack(pady=10, padx=20, fill=X)

copy_button = Button(root, text="Copy Short URL", command=copy, font=("Arial", 12), bg="#D4A5A5", fg="#333333")
copy_button.pack(pady=5)

root.mainloop()
