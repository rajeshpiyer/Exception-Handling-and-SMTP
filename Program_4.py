#Handling HTTP Request exception
import requests

def website(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Failed to connect to the website:", e)
    else:
        print("Connection Successful")
        print("-- Website Content --")
        print(response.text)


link = "http://"+input("Enter the URL to the website : ")
website(link)