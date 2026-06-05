# Package imports
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image
from setup3_1_points_screen import *
from dataclasses import dataclass

global study_time, break_time
study_time = break_time = None

def setup2_strategy_screen():

    # Window
    root = ctk.CTkToplevel()
    root.title("Your Strategy")
    root.geometry("1000x600")
    root.configure(fg_color="#ead2d2")
    root.protocol("WM_DELETE_WINDOW", exit)

    title_image = Image.open("Assets/setup2_strategy_title.png")
    title_image = ctk.CTkImage(title_image, title_image, (700, 210))
    title_label = ctk.CTkLabel(root, image=title_image, text="")
    heart_image = Image.open("Assets/setup2_strategy_heartdrop.png")
    heart_image = ctk.CTkImage(heart_image, heart_image, (330, 300))
    heart_label = ctk.CTkLabel(root, image=heart_image, text="")
    next_button = ctk.CTkButton(root, command=lambda: (root.withdraw(), setup3_1_points_screen()), text="Next")

    '''
    Pomodoro technique option
    '''
        
    pom_button_image = Image.open("Assets/setup2_strategy_pombutton.png")
    pom_button_image = ctk.CTkImage(pom_button_image, pom_button_image, (300, 250))
    pom_button = ctk.CTkButton(root, text="", fg_color="#ead2d2", corner_radius=20, image=pom_button_image)

    '''
    Custom study and break time option
    '''

    com_button_image = Image.open("Assets/setup2_strategy_combutton.png")
    com_button_image = ctk.CTkImage(com_button_image, com_button_image, (300, 250))
    com_button = ctk.CTkButton(root, text="", fg_color="#ead2d2", corner_radius=20, image=com_button_image)

    '''
    Plugging in button commands
    '''

    def pom_button_command():
        '''
        Deselect the other button and select the one that's clicked on
        '''
        com_button.configure(fg_color="#ead2d2")
        pom_button.configure(fg_color="#1F6AA5")

    def com_button_command():
        global study_time, break_time
        '''
        Same deselection
        '''
        pom_button.configure(fg_color="#ead2d2")
        com_button.configure(fg_color="#1F6AA5")
        '''
        Use a pop-up to ask what study-break split they'd like.
        '''
        while study_time is None:
            try:
                study_time = int(ctk.CTkInputDialog(title="Quick question!", text="How many minutes would you like for one study session?").get_input())
            except:
                messagebox.showerror(title="Error!", message="Please enter a number!")

        while break_time is None:
            try:
                break_time = int(ctk.CTkInputDialog(title="Quick question!", text="What about for a break after a study session?").get_input())
                '''
                We won't allow more break time than study time.
                '''
                if break_time > study_time:
                    break_time = None
                    messagebox.showerror(title="Hold on!", text="Break time cannot be greater than study time!")
                    '''
                    Triggers the loop to run and ask the user again.
                    '''
            except:
                messagebox.showerror(title="Error!", message="Please enter a number!")
    
    pom_button.configure(command=pom_button_command)
    com_button.configure(command=com_button_command)

    '''
    Widget placing
    '''
    title_label.place(relx=0.4, rely=0.2, anchor=CENTER)
    heart_label.place(relx=0.85, rely=0.75, anchor=CENTER)
    pom_button.place(relx=0.2, rely=0.6, anchor=CENTER)
    com_button.place(relx=0.52, rely=0.6, anchor=CENTER)
    next_button.place(relx=0.35, rely=0.9, anchor=CENTER)

    root.mainloop()

'''
To get the time data that the user inputted, but from other files.
'''

@dataclass
class StudyBreakSplit:
    study_time: int
    break_time: int

def get_study_break_split():
    return StudyBreakSplit(study_time, break_time)
