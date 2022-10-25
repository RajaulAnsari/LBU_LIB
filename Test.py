
class Library:
    def __init__(self,name,book):
        self.name=name
        self.lend={"Anamol":"Development"}
        self.book_list=["HarryPoter","Environment"]
        self.book = book

    def display(self):
        for i in self.book_list:
            print(i)

    def lendBook(self):
        if self.book not in self.book_list:
            print(f"{self.book} is not in the Library!")
        else:
            self.lend[self.name]=self.book
            (self.book_list).remove(self.book)
            print("Successfully lend!")

    def addBook(self):
        self.book_list.append(self.book)
        print("self.book added successfully!")

    def returnBook(self):
        if list(self.lend.keys()) == self.name and self.book == ((self.lend).get(self.name)):
            self.book_list.append(self.lend([self.name]))
            print("Book returned!!!")
        else:
            print("Can't Return ",f"{self.book}")




L = Library("Anamol","Development")
L.display()
L.returnBook()