# Package imports
import customtkinter as ctk
from tkinter import *
from PIL import Image
from dashboard import *

def setup3_2_points_screen(get_study_break_split):
    # Window
    root = ctk.CTkToplevel()
    root.title("Earn Points")
    root.geometry("1000x600")
    root.protocol("WM_DELETE_WINDOW", exit)

    backdrop_image = Image.open("Assets/setup3_2_points_backdrop.png")
    backdrop_image = ctk.CTkImage(backdrop_image, backdrop_image, backdrop_image.size)
    backdrop_label = ctk.CTkLabel(root, image=backdrop_image, text="")

    coins_button_image = Image.open("Assets/setup3_2_coins_button.png")
    coins_button_image = ctk.CTkImage(coins_button_image, coins_button_image, (522, 132))
    coins_button = ctk.CTkButton(root, command=lambda: (root.withdraw(), dashboard(get_study_break_split, "COINS")), text="", fg_color="#e5d2e9", corner_radius=20, image=coins_button_image)

    xp_button_image = Image.open("Assets/setup3_2_xp_button.png")
    xp_button_image = ctk.CTkImage(xp_button_image, xp_button_image, (522, 132))
    xp_button = ctk.CTkButton(root, command=lambda: (root.withdraw(), dashboard(get_study_break_split, "XP")), text="", fg_color="#e5d2e9", corner_radius=20, image=xp_button_image)

    backdrop_label.place(relx=0, rely=0, anchor=NW)
    coins_button.place(relx=0.5, rely=0.42, anchor=CENTER)
    xp_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    root.mainloop()
