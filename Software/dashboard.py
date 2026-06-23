# Package imports
import customtkinter as ctk
from tkinter import *
from PIL import Image
from time import sleep

def dashboard(get_study_break_split, point_system):
    '''
    Window
    '''
    root = ctk.CTkToplevel()
    root.title("Dashboard")
    root.geometry("1000x600")
    root.configure(fg_color="#ead2d2")
    root.protocol("WM_DELETE_WINDOW", exit)

    '''
    Dashboard title
    '''
    dashboard_title_image = Image.open("Assets/dashboard_title.png")
    dashboard_title_image = ctk.CTkImage(dashboard_title_image, dashboard_title_image, (500, 100))
    dashboard_title_image_label = ctk.CTkLabel(root, text="", image=dashboard_title_image)

    '''
    Editable to-do list
    '''
    global todo_cur
    todo_cur = 0

    '''
    Timer
    '''
    global timer_remaining_time, timer_paused, timer_study
    study_break_split = get_study_break_split()
    timer_remaining_time = study_break_split.study_time * 60
    mins, secs = divmod(timer_remaining_time, 60)
    timer_label = ctk.CTkLabel(root, 400, 370, text=f"{mins:02d}:{secs:02d}\n", text_color="black", fg_color="white", corner_radius=20)
    timer_label.cget("font").configure(size=70)
    timer_type_label = ctk.CTkLabel(timer_label, text="   Pomodoro: 25m study, 5m break" if study_break_split.study_time == 25 and study_break_split.break_time == 5 else f"   Custom: {study_break_split.study_time}m study, {study_break_split.break_time}m break", text_color="black", fg_color="lightgray", image=ctk.CTkImage(Image.open("Assets/tomato.png"), Image.open("Assets/tomato.png"), (20, 20)) if study_break_split.study_time == 25 and study_break_split.break_time == 5 else ctk.CTkImage(Image.open("Assets/clock.png"), Image.open("Assets/clock.png"), (20, 20)), compound="left", corner_radius=20)
    timer_paused = False
    timer_study = True

    '''
    Coin/XP count (for finishing tasks)
    '''
    point_label = ctk.CTkLabel(root, text="  0", text_color="black", fg_color="white", image=ctk.CTkImage(Image.open("Assets/coin.png"), Image.open("Assets/coin.png"), (30, 30)) if point_system == "COINS" else ctk.CTkImage(Image.open("Assets/xp.png"), Image.open("Assets/xp.png"), (30, 30)), compound="left", padx=8, pady=5, corner_radius=20)
    point_label.cget("font").configure(size=15)

    def timer_update():
        global timer_remaining_time, timer_paused, timer_study
        if not timer_paused:
            if timer_remaining_time > 0:
                timer_remaining_time -= 1
                mins, secs = divmod(timer_remaining_time, 60)
                timer_label.configure(text=f"{mins:02d}:{secs:02d}\n")
                root.after(1000, timer_update)
            else:
                '''
                If we're in study mode, switch to break mode once the
                timer has ended. Else, switch back to study mode.
                '''
                timer_study = False if timer_study else True
                timer_paused = True
                timer_play_button.configure(text="▶️ Start studying" if timer_study else "▶️ Start break", command=timer_play_button_unpaused_command)
                timer_remaining_time = study_break_split.study_time * 60 if timer_study else study_break_split.break_time * 60
                mins, secs = divmod(timer_remaining_time, 60)
                timer_label.configure(text=f"{mins:02d}:{secs:02d}\n")
                root.update_idletasks()
                sleep(1)

    timer_play_button = ctk.CTkButton(timer_label, text="▶️  Start studying", width=50, height=50, corner_radius=20)
    timer_play_button.cget("font").configure(size=15)

    def timer_play_button_pause_command():
        global timer_paused, timer_study
        timer_paused = True
        timer_play_button.configure(text="▶️ Continue studying" if timer_study else "▶️ Continue break", command=timer_play_button_unpaused_command)
        root.update_idletasks()
        sleep(1)

    def timer_play_button_unpaused_command():
        global timer_paused, timer_study
        timer_paused = False
        timer_play_button.configure(text="⏸️ Pause study" if timer_study else "⏸️ Pause break", command=timer_play_button_pause_command)
        root.after(1000, timer_update)

    timer_play_button.configure(command=timer_play_button_unpaused_command)

    def todo_add_button_command():
        global todo_cur

        temp_textbox = ctk.CTkEntry(todo_frame, height=20)

        ''' 
        When the user clicks on a created task, it 
        brings up two options - to check it as done,
        or delete it. 
        '''
        
        def todo_task_checkbox_checked_command(checked_checkbox):
            '''
            Search for the checkbox that was checked and get
            the grid row for it.
            '''
            for i in todo_frame.winfo_children():
                if isinstance(i, ctk.CTkCheckBox):
                    if i.get():
                        i.deselect()

            checked_checkbox.select()

            temp_row = checked_checkbox.grid_info()['row']
            todo_task_complete_button.grid(row=temp_row, column=1, sticky='W', padx=5, pady=5)
            todo_task_delete_button.grid(row=temp_row, column=2, sticky='W', padx=5, pady=5)

        def todo_task_checkbox_unchecked_command():
            todo_task_complete_button.grid_remove()
            todo_task_delete_button.grid_remove()

        def todo_task_checkbox_command(todo_task_checkbox):
            state = todo_task_checkbox.get()
            
            if state == 1:
                todo_task_checkbox_checked_command(todo_task_checkbox)
            else:
                todo_task_checkbox_unchecked_command()

        def temp_confirm_button_command():
            global todo_cur
            todo_task_checkbox = ctk.CTkCheckBox(todo_frame, command=lambda: todo_task_checkbox_command(todo_task_checkbox), text=temp_textbox.get(), text_color="black", fg_color="black", border_color="black")
            todo_task_checkbox.grid(row=todo_cur, column=0, sticky='W', pady=5)
            temp_textbox.destroy()
            temp_confirm_button.destroy()
            temp_cancel_button.destroy()
            todo_add_button.configure(state="normal")
            todo_cur += 1

        def temp_cancel_button_command():
            temp_textbox.destroy()
            temp_confirm_button.destroy()
            temp_cancel_button.destroy()
            todo_add_button.configure(state="normal")

        temp_confirm_button = ctk.CTkButton(todo_frame, command=temp_confirm_button_command, text="✅ Confirm", width=28)
        temp_cancel_button = ctk.CTkButton(todo_frame, command=temp_cancel_button_command, text="❌ Cancel", width=28)
        
        temp_textbox.grid(row=todo_cur, column=0, sticky='W')
        temp_confirm_button.grid(row=todo_cur, column=1, sticky='W', padx=5)
        temp_cancel_button.grid(row=todo_cur, column=2, sticky='W', padx=5)

        todo_cur += 1
        todo_add_button.configure(state="disabled")

    todo_frame = ctk.CTkScrollableFrame(root, 400, 330, fg_color="#cb6ce6", corner_radius=20)
    todo_add_button = ctk.CTkButton(root, command=todo_add_button_command, text="Add task", corner_radius=20)

    def todo_task_delete_button_command():
        '''
        Iterate through the grid items to find the checkbox whose 
        row matches the delete button's - the checkbox selected for
        deletion.
        '''
        for i in todo_frame.winfo_children():
            if isinstance(i, ctk.CTkCheckBox) and i.grid_info()['row'] == todo_task_delete_button.grid_info()['row']:
                i.destroy()
                break
        todo_task_complete_button.grid_remove()
        todo_task_delete_button.grid_remove()

    def todo_task_complete_button_command():
        '''
        Iterate the same way, except to find task marked for COMPLETION.
        '''
        for i in todo_frame.winfo_children():
            if isinstance(i, ctk.CTkCheckBox) and i.grid_info()['row'] == todo_task_complete_button.grid_info()['row']:
                '''
                Make the completed task green and put a line through the text for a second,
                then remove from the todo list.
                '''
                todo_task_complete_button.grid_remove()
                todo_task_delete_button.grid_remove()
                i.configure(text_color="green", fg_color="green", border_color="green")
                i.cget("font").configure(overstrike=1)
                root.update_idletasks()
                sleep(0.8)
                i.destroy()
                '''
                Also, increment the coin/XP count.
                '''
                point_label.configure(text=f"  {int(point_label.cget("text")) + 1}")
                break

    todo_task_complete_button = ctk.CTkButton(todo_frame, command=todo_task_complete_button_command, text="✅ Mark as done", width=28)
    todo_task_delete_button = ctk.CTkButton(todo_frame, command=todo_task_delete_button_command, text="🗑️ Delete", width=28)

    '''
    Widget placements
    '''
    dashboard_title_image_label.place(relx=0.03, rely=0.22, anchor=SW)
    todo_frame.place(relx=0.03, rely=0.88, anchor=SW)
    todo_add_button.place(relx=0.03, rely=0.91, anchor=NW)
    timer_label.place(relx=0.5, rely=0.88, anchor=SW)
    timer_type_label.grid(row=0, column=0, sticky='NW', padx=10, pady=10)
    timer_play_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    point_label.place(relx=0.8, rely=0.1, anchor=NW)

    root.mainloop()
