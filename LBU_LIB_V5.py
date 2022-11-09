#Importing Necessary Lib
import customtkinter 
import tkinter as tk

#Importing Functions From Other Py File 
from FileHandling import *

# from LBULIB import *

#Universal File-Path Location For Necessary Data
FILE_PATH = "/home/exzyle/gitcloneproject/LBU_LIB/lib.txt"
FILE_PATH_N = "/home/exzyle/gitcloneproject/LBU_LIB/lendrec.txt"  

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

#Gettting Entry Value In The Form Of String
book_name=tk.StringVar()
user_name=tk.StringVar()

#Getting The String Into Variable
b_name = book_name.get()
u_name = user_name.get()

#Defining Class For Various Section
class Library():
    
    def __init__(self,book_name,user_name):
        
        booklst_data=(open(FILE_PATH,"r")).read() 
        self._bookList=list(booklst_data.split('\n'))                    
        (open(FILE_PATH,"r")).close()
        
        self.book = book_name
        self._name = user_name

class Additional_Function(Library):                                       
    
    def __init__(self, book_name, user_name):
        self._lendrecord = {}
        super().__init__(book_name, user_name)
        
    def _lendBooks(self):                                                  
        
        if book_name.get() not in self._bookList:
            print(f"{book_name.get()} is not in the Library!")
        
        else:
            indx = int((self._bookList).index(book_name.get()))                   
            self._lendrecord[user_name.get()] = self._bookList.pop(indx)                        
            
            book_add(str(self._lendrecord),FILE_PATH_N)
            replace(((list(self._lendrecord.values()))[0]),FILE_PATH)
            print("Successfully lend!")

    def _returnBooks(self):
        
        booklst_data=(open(FILE_PATH_N,"r")).read()                         
        self._lendrecord=booklst_data
        (open(FILE_PATH_N,"r")).close() 
        
        book_add(book_name.get(),FILE_PATH)                                       
        replace(self._lendrecord,FILE_PATH_N)                               
        
        print("Book Returned!!!")

class Display(Library):
    
    def __init__(self, book_name,user_name):
        super().__init__(book_name,user_name)
        
    def _addBooks(self):
        book_add(book_name.get(),FILE_PATH)
        print("Book successfully added")

#Function Show Book
def Show_Book():
    
    Label_For_Library_Books = customtkinter.CTkLabel(master=app,width=120,text="Library Records",height=25,fg_color=("white", "black"),corner_radius=8)
    Label_For_Library_Books.grid(row=0, column=1, padx=130, pady=20)
    
    Dis_Data_Book = customtkinter.CTkTextbox(master=app,height=100,width=200)
    Dis_Data_Book.grid(row=1, column=1, padx=0, pady=0)
    
    FILE_DATA_Book = open(FILE_PATH,'r')
    Content_Book = FILE_DATA_Book.read()
    Dis_Data_Book.insert("0.0",Content_Book)
    
    #Lend Book Data
    Label_For_Lends_Books = customtkinter.CTkLabel(master=app,width=120,text="Lending Record",height=25,fg_color=("white", "black"),corner_radius=8)
    Label_For_Lends_Books.grid(row=2, column=1, padx=130, pady=20)
    
    Dis_Data_Lend = customtkinter.CTkTextbox(master=app,height=100,width=200)
    Dis_Data_Lend.grid(row=3, column=1, padx=0, pady=0)
    
    FILE_DATA_L = open(FILE_PATH_N,'r')
    content_Lend = FILE_DATA_L.read()
    Dis_Data_Lend.insert("0.0",content_Lend)
    
    Back_Button = customtkinter.CTkButton(master=app, text="Back", command=lambda:[CLEAR(),GUI_USER_HOME()])
    Back_Button.grid(row=4, column=1, padx=130, pady=20) 
        
#User-Choice Function 
def Use_Case(use_case):

    if __name__=='__main__':
        book_name = b_name
        user_name = u_name
        
        li = Library(book_name,user_name)                                       
        af = Additional_Function(object,user_name)                              
        dd = Display(book_name,user_name)
    
    if use_case == "Add Books":
        dd._addBooks()
    elif use_case == "Lend Books":
        af._lendBooks()
    elif use_case == "Return Books":
        af._returnBooks()
        
#FUNCTION DEFININNG FOR GUI USER-INPUT
def GUI_USER_INPUT(user_case):
    
    #Main GUI --> Asking User Input
    Book_Name_Title=customtkinter.CTkLabel(master=app,width=120,text="Enter Book Name",height=25,fg_color=("white", "black"),corner_radius=8)
    Book_Name_Title.grid(row=0, column=1, padx=130, pady=30)
    
    Book_Name_Entry = customtkinter.CTkEntry(master=app,textvariable=book_name)
    Book_Name_Entry.grid(row=1, column=1, padx=0, pady=0)
    
    Name_Title=customtkinter.CTkLabel(master=app,width=120,text="Enter User Name",height=25,fg_color=("white", "black"),corner_radius=8)
    Name_Title.grid(row=2, column=1, padx=130, pady=30)
    
    Name_Entry = customtkinter.CTkEntry(master=app,textvariable=user_name)
    Name_Entry.grid(row=3, column=1, padx=0, pady=0)
    
    Submit_Button = customtkinter.CTkButton(master=app, text="SUBMIT", command=lambda:[Use_Case(user_case)])
    Submit_Button.grid(row=4, column=1, padx=130, pady=30)
    
    Back_Button = customtkinter.CTkButton(master=app, text="Back", command=lambda:[CLEAR(),GUI_USER_HOME()])
    Back_Button.grid(row=5, column=1, padx=0, pady=0)    
    #Main GUI ENDING

def GUI_USER_HOME():
    
    #Main GUI Section --> HOME
    Home_Title=customtkinter.CTkLabel(master=app,width=120,text="CHOOSE A FUNCTION",height=30,fg_color=("white", "black"),corner_radius=8)
    Home_Title.grid(row=0, column=1, padx=130, pady=30)

    Show_Book_Button = customtkinter.CTkButton(master=app, text="Show Books",command=lambda:[CLEAR(),Show_Book()])
    Show_Book_Button.grid(row=3, column=1, padx=0, pady=0)

    Add_Books_Button = customtkinter.CTkButton(master=app, text="Add Books",command=lambda:[CLEAR(),GUI_USER_INPUT("Add Books")])
    Add_Books_Button.grid(row=4, column=1, padx=130, pady=30)

    Lend_Books_Button = customtkinter.CTkButton(master=app, text="Lend Books",command=lambda:[CLEAR(),GUI_USER_INPUT("Lend Books")])
    Lend_Books_Button.grid(row=5, column=1, padx=0, pady=0)

    Return_Books_Button = customtkinter.CTkButton(master=app, text="Return Books",command=lambda:[CLEAR(),GUI_USER_INPUT("Return Books")])
    Return_Books_Button.grid(row=6, column=1, padx=130, pady=30)

    Exit_Button = customtkinter.CTkButton(master=app, text="Exit",command=exit)
    Exit_Button.grid(row=7, column=1, padx=0, pady=0)
    #HOME GUI SECTION CLOSE

GUI_USER_HOME()

#Looping The GUI
app.mainloop()
