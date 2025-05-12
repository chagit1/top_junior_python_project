from Validators import check_digit
class Person:
    def __init__(self):
       
        while True:
            try:
                self._TZ = input("Enter TZ: ")
                check_digit(self._TZ)
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                self._name = input("Enter name: ")
                if not self._name: raise ValueError("Name empty")
                if not self._name.isalpha(): raise ValueError("Name must be letters")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                self._age = input("Enter age: ")
                check_digit(self._age)
                break
            except ValueError as e:
                print(f"Error: {e}")

    @property
    def TZ(self) -> str:
        return self._TZ
    
    @TZ.setter
    def TZ(self, TZ:str):
            self._TZ = TZ

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name:str):
        self._name = name

    @property  
    def age(self)-> str:
        return self._age
    
    @age.setter
    def age(self, age:str):
            self._age = age

    def get_info(self) -> str:
        return f"TZ: {self.TZ} Name: {self.name}, Age: {self.age}"

if __name__ == "__main__":
    try:
        print("Testing Person class...")
        person = Person()
        print("Person created successfully!")
        print(person.get_info())
    except ValueError as e:
        print(f"Error during test: {e}")
        