class Library():
    def __init__(self,bookList,book):
        self._bookList=bookList
        self.add={}
        self.book=book

class Additional_Function(Library):
    def __init__(self, bookList, book,name):
        self._name = name
        self._lendrecord = {}
        super().__init__(bookList, book)
        
    def _lendBooks(self):
        if book not in self._bookList:
            print(f"{self.book} is not in the Library!")
        else:
            indx = int((self._bookList).index(book))            
            self._lendrecord[self._name] = self._bookList.pop(indx)
            print("Successfully lend!")

    def _returnBooks(self):
        self._bookList.append(book)
        print("Book Returned!!!")

class Display(Additional_Function,Library):
    def __init__(self, bookList, book, name):
        super().__init__(bookList, book, name)
    def _addBooks(self,book):
        self._bookList.append(book)
        print("Book successfully added")
    def _showBooks(self):
        for i in self._bookList:
            print(i)
        for j in self._lendrecord:
            print(j)

if __name__=='__main__':
    raja=Library(['a','b','c'],'book')
    af = Additional_Function(['a','b','c'],'book','antony')
    dd = Display(['a','b','c'],'book','antony')
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
            af._lendBooks()
        elif(CHOICE=='4'):
            book=input("Enter name of book u want to return: ")
            raja._returnBooks()
        else:
            print("INVALID CHOICE!!!")