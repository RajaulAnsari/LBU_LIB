from FileHandling import *                                                 #custom library imported from Filehandling.py
from testfinal import b_name
from testfinal import u_name

FILE_PATH = "/home/exzyle/ProjectMD/Ongoing/lib.txt"                       #universal filepath location for library data
FILE_PATH_N = "/home/exzyle/ProjectMD/Ongoing/lendrec.txt"                 #universal filepath location for lending book records

class Library():
    
    def __init__(self,book_name.get(),user_name.get()):
        
        booklst_data=(open(FILE_PATH,"r")).read()                           #txt file data into list form
        self._bookList=list(booklst_data.split('\n'))                    
        (open(FILE_PATH,"r")).close()
        
        self.book = book_name.get()
        self._name = user_name.get()

class Additional_Function(Library):                                         #use case of inheritance 
    
    def __init__(self, book_name.get(), user_name.get()):
        self._lendrecord = {}
        super().__init__(book_name.get(), user_name.get())
        
    def _lendBooks(self):                                                  
        
        if book_name.get() not in self._bookList:
            print(f"{book_name.get()} is not in the Library!")
        
        else:
            indx = int((self._bookList).index(book_name.get()))                   #abstraction of data from list 
            self._lendrecord[user_name.get()] = self._bookList.pop(indx)                        
            
            book_add(str(self._lendrecord),FILE_PATH_N)
            replace(((list(self._lendrecord.values()))[0]),FILE_PATH)
            
            print("Successfully lend!")

    def _returnBooks(self):
        
        booklst_data=(open(FILE_PATH_N,"r")).read()                         #txt file data into list form
        self._lendrecord=booklst_data
        (open(FILE_PATH_N,"r")).close() 
        
        book_add(book_name.get(),FILE_PATH)                                       #use case of custom library
        replace(self._lendrecord,FILE_PATH_N)                               #use case of custom library
        
        print("Book Returned!!!")

class Display(Library):
    
    def __init__(self, book_name.get(),user_name.get()):
        super().__init__(book_name.get(),user_name.get())
        
    def _addBooks(self):
        book_add(book_name.get(),FILE_PATH)
        print("Book successfully added")
    
    def _showBooks(self):
        dxply(FILE_PATH_N)
        dxply(FILE_PATH)




if __name__=='__main__':
    book_name.get() = b_name
    user_name.get() = u_name
    
    li = Library(book_name.get(),user_name.get())                                       #class with its objects
    af = Additional_Function(object,user_name.get())                              #inheriting another class object
    dd = Display(book_name.get(),user_name.get())