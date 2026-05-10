# Package imports
import customtkinter as ctk
from tkinter import *
from PIL import Image

def setup2_strategy_screen():
     # Window
    root = ctk.CTkToplevel()
    root.title("Your Strategy")
    root.geometry("1000x600")
    root.configure(fg_color="#ead2d2")

    title_image = Image.open("Assets/setup2_strategy_title.png")
    title_image = ctk.CTkImage(title_image, title_image, (700, 210))
    title_label = ctk.CTkLabel(root, image=title_image, text="")
    heart_image = Image.open("Assets/setup2_strategy_heartdrop.png")
    heart_image = ctk.CTkImage(heart_image, heart_image, (330, 300))
    heart_label = ctk.CTkLabel(root, image=heart_image, text="")
    next_button = ctk.CTkButton(root, command=lambda: (root.withdraw(), setup2_strategy_screen()), text="Next")

    pom_button_image = Image.open("Assets/setup2_strategy_pombutton.png")
    pom_button_image = ctk.CTkImage(pom_button_image, pom_button_image, (340, 280))
    pom_button = ctk.CTkButton(root, text="", fg_color="#e5d2e9", corner_radius=20, image=pom_button_image)

    block_button_image = Image.open("Assets/setup2_strategy_blockbutton.png")
    block_button_image = ctk.CTkImage(block_button_image, block_button_image, (150, 100))
    block_button = ctk.CTkButton(root, text="", fg_color="#e5d2e9", corner_radius=20, image=block_button_image)

    com_button_image = Image.open("Assets/setup2_strategy_combutton.png")
    com_button_image = ctk.CTkImage(com_button_image, com_button_image, (150, 100))
    com_button = ctk.CTkButton(root, text="", fg_color="#e5d2e9", corner_radius=20, image=com_button_image)

    title_label.place(relx=0.4, rely=0.2, anchor=CENTER)
    heart_label.place(relx=0.85, rely=0.75, anchor=CENTER)
    pom_button.place(relx=0.25, rely=0.6, anchor=CENTER)
    block_button.place(relx=0.55, rely=0.52, anchor=CENTER)
    com_button.place(relx=0.55, rely=0.72, anchor=CENTER)
    next_button.place(relx=0.35, rely=0.9, anchor=CENTER)

    root.mainloop()
