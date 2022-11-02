FILE_PATH = "/home/exzyle/ProjectMD/Ongoing/lib.txt"
        
def book_add(x,y):
    try:
        file_op=open(y,"a")
        file_op.write(x+"\n")
        file_op.close()
    except:
        print("File Not Found!!!")

def replace(x,xpath):
    try:
        file = open(xpath,"r")
        word = (file.read()).replace(x,".")
        file = open(xpath,"w")
        file.write(word)
        file.close()
    except:
        print("File Not Found!!!")
    
def dxply(xfilepath):
    try:
        datas=(open(xfilepath,"r")).readlines()
        for i in datas:
            print(i)
        (open(xfilepath,"r")).close()
    except:
        print("File Not Found!!!")