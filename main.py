
# Import the customtkinter module
import customtkinter as ctk
from tkinter import StringVar

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x1000")
app.title("Component Organizer")
def search(event):
    # This function will be called when the Enter key is pressed
    print("Search:", search_var.get())

 

#search bar    
search_var = StringVar() 
search_bar = ctk.CTkEntry(app, textvariable=search_var, width=50, font=("Arial", 12),text_color="white",corner_radius=10, border_width=1, border_color="grey",)
search_bar.pack(fill="x", padx=10, pady=10)
search_bar.bind('<Return>', search)  # Bind the Enter key to the search function

app.mainloop()