import customtkinter 
import tkinter as tk


from FileHandling import *      

FILE_PATH = r'C:\Users\User\Desktop\Library GUI\LBU_LIB-main\lib.txt'                   #universal filepath location for library data
FILE_PATH_N = r'C:\Users\User\Desktop\Library GUI\LBU_LIB-main\lendrec.txt'                  #universal filepath location for lending book records

class Library():
    
    def __init__(self,book_name,user_name):
        
        booklst_data=(open(FILE_PATH,"r")).read()                           #txt file data into list form
        self._bookList=list(booklst_data.split('\n'))                    
        (open(FILE_PATH,"r")).close()
        
        self.book = book_name
        self._name = user_name

class Additional_Function(Library):                                         #use case of inheritance 
    
    def __init__(self, book_name, user_name):
        self._lendrecord = {}
        super().__init__(book_name, user_name)
        
    def _lendBooks(self):                                                  
        
        if book_name not in self._bookList:
            print(f"{book_name} is not in the Library!")
        
        else:
            indx = int((self._bookList).index(book_name))                   #abstraction of data from list 
            self._lendrecord[user_name] = self._bookList.pop(indx)                        
            
            book_add(str(self._lendrecord),FILE_PATH_N)
            replace(((list(self._lendrecord.values()))[0]),FILE_PATH)
            
            print("Successfully lend!")

    def _returnBooks(self):
        
        booklst_data=(open(FILE_PATH_N,"r")).read()                         #txt file data into list form
        self._lendrecord=booklst_data
        (open(FILE_PATH_N,"r")).close() 
        
        book_add(book_name,FILE_PATH)                                       #use case of custom library
        replace(self._lendrecord,FILE_PATH_N)                               #use case of custom library
        
        print("Book Returned!!!")

class Display(Library):
    
    def __init__(self, book_name,user_name):
        super().__init__(book_name,user_name)
        
    def _addBooks(self):
        book_add(book_name.get(),FILE_PATH)
        book_add(user_name.get(),FILE_PATH_N)
        print("Book successfully added")
        
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

def submit():
    home.quit()

if __name__=='__main__':
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    home = customtkinter.CTk()  # create CTk window like you do with the Tk window
    home.geometry("400x400")
    home.title("Leeds Beckett Library")

    #Taking input from user
    book_name=tk.StringVar()
    user_name=tk.StringVar()

    title=customtkinter.CTkLabel(master=home,width=120,text="Enter Book Name",height=25,fg_color=("white", "black"),corner_radius=8)
    title.pack(padx=20, pady=10)
    entry1 = customtkinter.CTkEntry(master=home,textvariable=book_name)
    entry1.pack(padx=20, pady=10)
    title=customtkinter.CTkLabel(master=home,width=120,text="Enter User Name",height=25,fg_color=("white", "black"),corner_radius=8)
    title.pack(padx=20, pady=10)
    entry2 = customtkinter.CTkEntry(master=home,textvariable=user_name)
    entry2.pack(padx=20, pady=10)

    button = customtkinter.CTkButton(master=home, text="SUBMIT", command=submit)
    button.pack(padx=20, pady=10)

    home.mainloop()

    li = Library(book_name,user_name)                                       #class with its objects
    af = Additional_Function(object,user_name)                              #inheriting another class object
    dd = Display(book_name,user_name)

# def show_books():
#     new=customtkinter.CTk()
#     new.geometry("400x600")
#     new.title("New Window")
#     label1 = label = customtkinter.CTkLabel(master=new,width=120,text="Library Record",height=25,fg_color=("white", "black"),corner_radius=8)
#     label1.pack(padx=20, pady=10)
#     textbox1 = customtkinter.CTkTextbox(new,height=200,width=200)
#     textbox1.pack(pady=20)
#     text_file=open(r'C:\Users\User\Desktop\Library GUI\LBU_LIB-main\lib.txt','r')
#     content = text_file.read()
#     textbox1.insert("0.0",content)
#     label1 = label = customtkinter.CTkLabel(master=new,width=120,text="Lending Record",height=25,fg_color=("white", "black"),corner_radius=8)
#     label1.pack(padx=20, pady=10)
#     textbox2 = customtkinter.CTkTextbox(new)
#     textbox2.pack(pady=20)
#     text_file2=open(r'C:\Users\User\Desktop\Library GUI\LBU_LIB-main\lendrec.txt','r')
#     content2 = text_file2.read()
#     textbox2.insert("0.0",content2)
#     new.mainloop()

def button_function():
    pass

def exit_window():
    app.quit()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x400")
app.title("Leeds Beckkett Library")

title=customtkinter.CTkLabel(master=app,width=120,text="CHOOSE A FUNCTION",height=30,fg_color=("white", "black"),corner_radius=8)
title.pack(padx=20, pady=40)


button = customtkinter.CTkButton(master=app, text="Show Books", command=dd._showBooks)
button.pack(padx=20, pady=10,anchor=tk.CENTER)

button = customtkinter.CTkButton(master=app, text="Add Books", command=dd._addBooks)
button.pack(padx=20, pady=10)

button = customtkinter.CTkButton(master=app, text="Lend Books", command=button_function)
button.pack(padx=20, pady=10)

button = customtkinter.CTkButton(master=app, text="Return Books", command=button_function)
button.pack(padx=20, pady=10)

button = customtkinter.CTkButton(master=app, text="Exit", command=exit_window)
button.pack(padx=20, pady=10)

app.mainloop()
