from FileHandling import *                                                 #custom library imported from Filehandling.py
from testfinal import b_name
from testfinal import u_name

FILE_PATH = "/home/exzyle/ProjectMD/Ongoing/lib.txt"                       #universal filepath location for library data
FILE_PATH_N = "/home/exzyle/ProjectMD/Ongoing/lendrec.txt"                 #universal filepath location for lending book records

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