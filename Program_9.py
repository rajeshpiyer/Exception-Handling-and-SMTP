#Age validation using custom exception
class InvalidAgeError(Exception):

    def __init__(self, age: int):
        self.age = age

    def __str__(self) -> str:
        return f"\nInvalid age: {self.age}. Age must be between 0 and 150."
    
def check_age(age: int):
    if not 0 <= age <= 150:
        raise InvalidAgeError(age)
    print("\nAge is valid.")

try:
    age = int(input("Enter an age : "))
    check_age(age)
except InvalidAgeError as e:
    print(e)
