#Handling ValueError exception
def execute():
    try:
        a=int(input("Enter a Number : "))
        print("The entered number is : ",a)
    except ValueError:
        print("Error : A Value other than integer is found.")

execute()