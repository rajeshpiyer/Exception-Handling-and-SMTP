#Implementing try-except-finally
def copyFile(filename1,filename2):
    try:
        file1 = open(filename1,"r")
        file2 = open(filename2,"w")
        for i in file1:
            file2.write(i)
    except FileNotFoundError:
        print(f"Error : {filename1} not found!")
    else:
        print("Copy Successfull!!")
    finally:
        file1.close()
        file2.close()

def filenameInput():
    return input("Enter filename : ")

print("File 1 : ")
filename1 = filenameInput()

print("File 2 : ")
filename2 = filenameInput()

copyFile(filename1,filename2)





