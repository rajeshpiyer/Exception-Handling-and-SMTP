#Handling ZeroDivisionError exception
def execute():
    try:
        print("-- DIVISION --")
        a=int(input("Enter a Number : "))
        b=int(input("Enter the Divisor : "))
        c=a/b
        print("Quotient : ",c)
    except ZeroDivisionError:
        print("Error : Division by zero is not possible.")

execute()