# Package imports
import customtkinter as ctk
from tkinter import *
from PIL import Image
from setup3_2_points_screen import *

def setup3_1_points_screen(get_study_break_split):
    '''
    Window
    '''
    root = ctk.CTkToplevel()
    root.title("Earn Points")
    root.geometry("1000x600")
    root.protocol("WM_DELETE_WINDOW", exit)

    backdrop_image = Image.open("Assets/setup3_1_points_backdrop.png")
    backdrop_image = ctk.CTkImage(backdrop_image, backdrop_image, backdrop_image.size)
    backdrop_label = ctk.CTkLabel(root, image=backdrop_image, text="")

    start_button_image = Image.open("Assets/setup3_1_start_button.png")
    start_button_image = ctk.CTkImage(start_button_image, start_button_image, (150, 60))
    start_button = ctk.CTkButton(root, command=lambda: (root.withdraw(), setup3_2_points_screen(get_study_break_split)), text="", fg_color="#e5d2e9", corner_radius=20, image=start_button_image)

    backdrop_label.place(relx=0, rely=0, anchor=NW)
    start_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    root.mainloop()
