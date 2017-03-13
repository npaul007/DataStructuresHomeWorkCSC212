class Student:
    def __init__(self,name,attend,grades):
          self.name = name
          self.attend = attend
          self.grades = grades

    def getName(self):
        return self.name

    def attendClass(self):
        self.attend = self.attend + 1

    def addGrade(self,grade):
        self.grades.append(grade)
        
    def gradeAverage(self):
        gradeAvg = sum(self.grades) / len(self.grades)

        return gradeAvg

nate = Student('Nathanael Paulemon',0,[90,67,75])
print(nate.gradeAverage())
