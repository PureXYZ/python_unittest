class Student:
    
    def __init__(self):
        self.grades = []
    
    def add_grade(self, grade):
        if grade <= 100 and grade >= 0:
            self.grades.append(grade)
        else:
            raise ValueError("grade out of range")
        
    def boost_grades(self):
        new_grades = []
        for grade in self.grades:
            if grade + 10 <= 100:
                new_grade = grade + 10
            else:
                new_grade = 100
            new_grades.append(new_grade)
        self.grades = new_grades
          