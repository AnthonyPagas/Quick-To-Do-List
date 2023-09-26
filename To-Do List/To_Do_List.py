from tkinter.tix import ComboBox
import customtkinter as ctk
import tkinter
from tkinter import ttk
from tkinter import messagebox

def add():
    activity = activity_entry.get()
    time = time_entry.get()
    am_pm = combobox.get()
    location = loc_entry.get()
    if (activity != None) and (time != None) and (location != None):
        if (len(time) == 4) and (time[0].isnumeric()) and (time[1] == ":") and (time[-2:].isnumeric()) and (int(time[0]) >= 1 and int(time[0]) <= 12) and (int(time[-2:]) >= 0 and int(time[-2:]) <= 59):
            added_label = ctk.CTkLabel(scroll_frame, text = activity + " - " + time + " " + am_pm + " - " + location)
            added_label.pack()
            activity_entry.delete(0, ctk.END)
            time_entry.delete(0, ctk.END)
            loc_entry.delete(0, ctk.END)
        elif (len(time) == 5) and (time[0:2].isnumeric()) and (time[2] == ":") and (time[-2:].isnumeric()) and (int(time[0:2]) >= 10 and int(time[0:2]) <= 12) and (int(time[-2:]) >= 0 and int(time[-2:]) <= 59):
            added_label = ctk.CTkLabel(scroll_frame, text = activity + " - " + time + " " + am_pm + " - " + location)
            added_label.pack()
            activity_entry.delete(0, ctk.END)
            time_entry.delete(0, ctk.END)
            loc_entry.delete(0, ctk.END)
        else:
            tkinter.messagebox.showwarning(title = "Time Error", message = "Invalid time input (correct input ex. 4:30)")
    else:
        tkinter.messagebox.showwarning(title = "Input Error", message = "Make sure all boxes are filled with the correct information")

#Main window
root = ctk.CTk()
ctk.set_appearance_mode("Dark")
root.geometry("800x500")
root.title("To-Do List")
#Individual widgets
title_label = ctk.CTkLabel(root, text = "To-Do List", font = ctk.CTkFont(size = 50, weight = "bold"))
title_label.pack(padx = 10, pady = (40,20))
#Activity entry label
activity_entry = ctk.CTkEntry(root, width = 425, placeholder_text="Activity")
activity_entry.pack(padx=10, pady=0)
#Spacer label
spacer_label = ctk.CTkLabel(root, text = "", font = ctk.CTkFont(size = 1, weight = "bold"))
spacer_label.pack(padx = 1, pady = 1)
#Scrollable frame widget
scroll_frame = ctk.CTkScrollableFrame(root, width = 400, height = 100)
scroll_frame.pack()
#Time Entry
time_entry = ctk.CTkEntry(scroll_frame, placeholder_text= "Enter Time (ex. 7:32)")
time_entry.pack(fill = "x")
#Combobox
combobox = ctk.CTkOptionMenu(scroll_frame, values=["AM", "PM"])
combobox.pack(fill = "x")
#Location
loc_entry = ctk.CTkEntry(scroll_frame, placeholder_text= "Enter Location (ex. Park)")
loc_entry.pack(fill = "x")
#Add button
button = ctk.CTkButton(root, text = "Add", width = 400, command= add)
button.pack(pady = 20)
#Running interface until exited
root.mainloop()

