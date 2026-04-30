# Package mports
import customtkinter as ctk
from tkinter import *
from PIL import Image

def welcome_screen():
    # Window
    root = ctk.CTk()
    root.title("Studos")
    root.geometry("1000x600")
    root.configure(fg_color="#e5d2e9")

    welcome_image = Image.open("Assets/welcome.png")
    welcome_image = ctk.CTkImage(welcome_image, welcome_image, (456, 185))
    welcome_label = ctk.CTkLabel(root, text="", image=welcome_image)
    caption_label = ctk.CTkLabel(root, text="Learning. Redefined.", text_color="black", font=ctk.CTkFont(weight='bold', size=30))
    welcome_button_image = Image.open("Assets/welcome_button.png")
    welcome_button_image = ctk.CTkImage(welcome_button_image, welcome_button_image, (115, 100))
    welcome_button = ctk.CTkButton(root, text="", fg_color="#e5d2e9", corner_radius=20, image=welcome_button_image)

    welcome_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    caption_label.place(relx=0.5, rely=0.6, anchor=CENTER)
    welcome_button.place(relx=0.5, rely=0.75, anchor=CENTER)

    root.mainloop()
