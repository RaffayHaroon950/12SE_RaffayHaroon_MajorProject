# Package imports
import customtkinter as ctk
from tkinter import *
from PIL import Image
from setup2_strategy_screen import *

year_9_subjects = [
    "English", "Mathematics", "Science", 
    "Health and Physical Education (HPE/PDHPE)",
    "History", "Geography", "Civics and Citizenship",
    "Economics and Business", "Commerce",
    "Visual Arts", "Music", "Drama (Theatre)", 
    "Dance", "Media Arts", "Photography",
    "Design and Technologies", "Digital Technologies", 
    "Computing Technology", "Food Technology", 
    "Agricultural Technology", "Industrial Technology",
    "Japanese", "French", "Italian", "Korean",
    "Outdoor Education", "Sport, Lifestyle and Recreation",
    "Work Studies", "International Relations",
    "Philosophy", "STEM", "Graphic Design"
]

selected_subjects = []


def setup1_studyplan_screen():
    # Window
    root = ctk.CTkToplevel()
    root.title("Your Study Plan")
    root.geometry("1000x600")
    root.configure(fg_color="#ead2d2")
    root.protocol("WM_DELETE_WINDOW", exit)

    title_image = Image.open("Assets/setup1_studyplan_title.png")
    title_image = ctk.CTkImage(title_image, title_image, title_image.size)
    title_label = ctk.CTkLabel(root, image=title_image, text="")
    heart_image = Image.open("Assets/setup1_studyplan_heartdrop.png")
    heart_image = ctk.CTkImage(heart_image, heart_image, (315, 300))
    heart_label = ctk.CTkLabel(root, image=heart_image, text="")
    subjects_frame = ctk.CTkScrollableFrame(root, 500, 250, fg_color="#cb6ce6")
    next_button = ctk.CTkButton(root, command=lambda: (root.withdraw(), setup2_strategy_screen()), text="Next")

    title_label.place(relx=0.4, rely=0.2, anchor=CENTER)
    heart_label.place(relx=0.85, rely=0.75, anchor=CENTER)
    subjects_frame.place(relx=0.35, rely=0.6, anchor=CENTER)
    next_button.place(relx=0.35, rely=0.9, anchor=CENTER)

    # Inputting subject checkboxes into the scrollable frame
    row = 0

    for subject in year_9_subjects:
        subject_checkbox = ctk.CTkCheckBox(subjects_frame, text=subject, text_color="black", fg_color="black", border_color="black")
        subject_checkbox.grid(row=row, column=0, sticky="W")
        row += 1

    root.mainloop()
