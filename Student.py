from Validators import check_digit
from Person import Person

class Student(Person):
    def __init__(self):
        super().__init__()
        while True:
            try:
                self.fild_of_study = input("Enter fild of study: ")
                if not self.fild_of_study: raise ValueError("Fild of study empty")
                if not self.fild_of_study.isalpha(): raise ValueError("Fild of study must be letters")
                break
            except ValueError as e:
                print(f"Error: {e}")
        while True:
            try:
                self.year_of_study = input("Enter year of study: ")
                check_digit(self.year_of_study)
                break
            except ValueError as e:
                print(f"Error: {e}")
        while True:
            try:
                self.score_average = input("Enter score average: ")
                check_digit(self.score_average)
                break
            except ValueError as e:
                print(f"Error: {e}")
                
    @property
    def fild_of_study(self) -> str:
        return self._fild_of_study
   
    @fild_of_study.setter
    def fild_of_study(self, fild_of_study:str):
        self._fild_of_study = fild_of_study
   
    @property
    def year_of_study(self) -> str:
        return self._year_of_study
   
    @year_of_study.setter
    def year_of_study(self, year_of_study:str):
        self._year_of_study = year_of_study
   
    @property
    def score_average(self) -> str:
        return self._score_average
   
    @score_average.setter
    def score_average(self, score_average:str):
        self._score_average = score_average
    
    
    
    def get_info(self) -> str:
        return super().get_info() + ", fild study: " + self.fild_of_study + ", year study: " + self.year_of_study + ", score average: " + self.score_average

if __name__ == "__main__":
    try:
        print("Testing Student class...")
        student = Student()
        print("Student created successfully!")
        print(student.get_info())
    except ValueError as e:
        print(f"Error during test: {e}") 