#make sure to complete your gui part mr.sweing nakarmi Thank You!!!

from FileHandling import *                                                 #custom library imported from Filehandling.py

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

class Display(Library):
    
    def __init__(self, book_name,user_name):
        super().__init__(book_name,user_name)
        
    def _addBooks(self):
        book_add(book_name,FILE_PATH)
        print("Book successfully added")
    
    def _showBooks(self):
        dxply(FILE_PATH_N)
        dxply(FILE_PATH)

if __name__=='__main__':
    book_name = input("Enter Book Name: ")
    user_name = input("Enter User Name: ")
    
    li = Library(book_name,user_name)                                       #class with its objects
    af = Additional_Function(object,user_name)                              #inheriting another class object
    dd = Display(book_name,user_name)
    
    while(True):
        
        print('''
              1. SHOW BOOKS
              2. ADD BOOKS
              3. LEND BOOKS
              4. RETURN BOOKS
              5. Exit''')
        
        CHOICE=input("ENTER YOUR CHOICE: ")
        if CHOICE not in ['1','2','3','4']:
            continue
        if(CHOICE=='1'):
            dd._showBooks()
        elif(CHOICE=='2'):
            dd._addBooks()
        elif(CHOICE=='3'):
            af._lendBooks()
        elif(CHOICE=='4'):
            af._returnBooks()
        elif(CHOICE=='5'):
            exit()                                                          #exiting program built-in function
        else:
            print("INVALID CHOICE!!!")