import customtkinter 
import tkinter as tk

# from FileHandling import *

#THEMING THE GUI
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

#CREATING GUI WINDOW
app = customtkinter.CTk()
app.geometry("400x400")
app.title("Leeds Beckkett Library")

#ESSENTIALS FUNCTIONS TO CLEAR OUT THE WINDOW
def CLEAR():
    list = app.grid_slaves()
    for l in list:l.destroy()

book_name=tk.StringVar()
user_name=tk.StringVar()

#FUNCTION DEFININNG FOR GUI USER-INPUT
def GUI_USER_INPUT():
    #Main GUI --> Asking User Input
    Book_Name_Title=customtkinter.CTkLabel(master=app,width=120,text="Enter Book Name",height=25,fg_color=("white", "black"),corner_radius=8)
    Book_Name_Title.pack(padx=20, pady=10)
    
    Book_Name_Entry = customtkinter.CTkEntry(master=app,textvariable=book_name)
    Book_Name_Entry.pack(padx=20, pady=10)
    
    Name_Title=customtkinter.CTkLabel(master=app,width=120,text="Enter User Name",height=25,fg_color=("white", "black"),corner_radius=8)
    Name_Title.pack(padx=20, pady=10)
    
    Name_Entry = customtkinter.CTkEntry(master=app,textvariable=user_name)
    Name_Entry.pack(padx=20, pady=10)
    
    Submit_Button = customtkinter.CTkButton(master=app, text="SUBMIT", command=print(book_name.get(),user_name.get()))
    Submit_Button.pack(padx=20, pady=10)
    #Main GUI ENDING

#FUNCTION DEFININNG FOR GUI USER-FRONT-VIEW
def GUI_USER_HOME():
    #Main GUI Section --> HOME
    Home_Title=customtkinter.CTkLabel(master=app,width=120,text="CHOOSE A FUNCTION",height=30,fg_color=("white", "black"),corner_radius=8)
    Home_Title.pack(padx=20, pady=40)

    Show_Book_Button = customtkinter.CTkButton(master=app, text="Show Books")
    Show_Book_Button.pack(padx=20, pady=10,anchor=tk.CENTER)

    Add_Books_Button = customtkinter.CTkButton(master=app, text="Add Books",command=lambda:[CLEAR(),GUI_USER_INPUT()])
    Add_Books_Button.pack(padx=20, pady=10)

    Lend_Books_Button = customtkinter.CTkButton(master=app, text="Lend Books",command=lambda:[CLEAR(),GUI_USER_INPUT()])
    Lend_Books_Button.pack(padx=20, pady=10)

    Return_Books_Button = customtkinter.CTkButton(master=app, text="Return Books",command=lambda:[CLEAR(),GUI_USER_INPUT()])
    Return_Books_Button.pack(padx=20, pady=10)

    Exit_Button = customtkinter.CTkButton(master=app, text="Exit",command=exit)
    Exit_Button.pack(padx=20, pady=10)
    #HOME GUI SECTION CLOSE

# GUI_USER_HOME()
GUI_USER_INPUT

app.mainloop()



    def _showBooks(self):
        new=customtkinter.CTk()
        new.geometry("400x600")
        new.title("New Window")
        
        
        
        label1 = customtkinter.CTkLabel(master=new,width=120,text="Library Record",height=25,fg_color=("white", "black"),corner_radius=8)
        label1.pack(padx=20, pady=10)
        textbox1 = customtkinter.CTkTextbox(new,height=200,width=200)
        textbox1.pack(pady=20)
        text_file=open(r'C:\Users\User\Desktop\Library GUI\LBU_LIB-main\lib.txt','r')
        content = text_file.read()
        textbox1.insert("0.0",content)
        
        
        
        label1 = customtkinter.CTkLabel(master=new,width=120,text="Lending Record",height=25,fg_color=("white", "black"),corner_radius=8)
        label1.pack(padx=20, pady=10)
        textbox2 = customtkinter.CTkTextbox(new)
        textbox2.pack(pady=20)
        text_file2=open(r'C:\Users\User\Desktop\Library GUI\LBU_LIB-main\lendrec.txt','r')
        content2 = text_file2.read()
        textbox2.insert("0.0",content2)
        
        
        new.mainloop()