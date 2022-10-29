def details():
    book=input("book u want to add: ")
    f=open("/home/rajaul/Documents/raja/File Handling/lib.txt","a")
    f.write(book+"\n")
    f.close()


def show():
    f=open("/home/rajaul/Documents/raja/File Handling/lib.txt","r")
    a=f.readlines()
    for i in a:
        print(i)
    f.close()


def lend():
    book=input("which book do u want: ")
    name=input("enter your name: ")
    lname=f"{book} : Lended BY: {name}"
    f=open("/home/rajaul/Documents/raja/File Handling/lib.txt","r")
    word=(f.read()).replace(book,lname)
    f=open("/home/rajaul/Documents/raja/File Handling/lib.txt","w")
    f.write(word)
    f.close()

def Return():
    book=input("Enter the book u want to return: ")
    name=input("enter your name: ")
    name1=f"{book} : Lended BY: {name}"
    f=open("/home/rajaul/Documents/raja/File Handling/lib.txt","r")
    word=(f.read()).replace(name1,book)
    f=open("/home/rajaul/Documents/raja/File Handling/lib.txt","w")
    f.write(word)
    f.close()

    
while(True):
    print("""
        1. add details
        2. show
        3. lend
        4. Return
""")

    choice=input("Enter choice: ")
    if (choice=="1"):
        details()
    elif (choice=="2"):
        print("Book details here:\n")
        show()
    elif (choice=="3"):
        lend()
    elif (choice=="4"):
        Return()
    else:
        print("invalid!!!")
