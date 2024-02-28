#Handling FileNotFound exception
def execute():
    try:
        filename = input("Enter a filename(Without extension) : ")+".txt"
        file = open(filename,"r")
        for i in file:
            print(i)
    except FileNotFoundError:
        print(f"Error : '{filename}' doesn't exist.")

execute()