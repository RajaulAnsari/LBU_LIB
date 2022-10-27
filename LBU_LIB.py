class Library():
    def __init__(self,book,name):
        self._bookList=['a','b','c']
        self.book=book
        self._name=name

class Additional_Function(Library):
    def __init__(self,book,name):
        self.var_tempx = None
        self._lendrecord = {}
        super().__init__(book,name)
        
    def _lendBooks(self):
        if book not in self._bookList:
            print(f"{book} is not in the Library!")
        else:
            indx = int((self._bookList).index(book))            
            self._lendrecord[self._name] = self._bookList.pop(indx)
            print("Successfully lend!")

    def _returnBooks(self):
        print(self._lendrecord)
        self._lendrecord.pop(self._name)
        self._bookList.append(book)
        print("Book Returned!!!")
        


class Display(Additional_Function,Library):
    def __init__(self, book, name):
        super().__init__(book, name)
    def _addBooks(self,book):
        self._bookList.append(book)
        print("Book successfully added")
    def _showBooks(self):
        for i in self._bookList:
            print(i)
        print("Lend Record",self._lendrecord)


if __name__=='__main__':
    
    raja=Library('book','Antony')
    af = Additional_Function(object,'Antony')
    dd = Display('book','Antony') 
    
    while(True):
        print('''
            1. SHOW BOOKS
            2. ADD BOOKS
            3. LEND BOOKS
            4. RETURN BOOKS
            ''')
        CHOICE=input("ENTER YOUR CHOICE: ")
        if CHOICE not in ['1','2','3','4']:
            continue
        if(CHOICE=='1'):
            dd._showBooks()
        elif(CHOICE=='2'):
            book=input("Enter name of book u want to add: ")
            dd._addBooks(book)
        elif(CHOICE=='3'):
            book=input("Enter name of book u want to lend: ")
            dd._lendBooks()
        elif(CHOICE=='4'):
            book=input("Enter name of book u want to return: ")
            dd._returnBooks()
        else:
            print("INVALID CHOICE!!!")
