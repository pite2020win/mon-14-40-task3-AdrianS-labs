# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class Student:
    grades = []
    presences = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def add_new_grade(self,grade):
        self.grades.append(grade)

    def calculate_avg(self):
        sum=0
        amount_of_grades = len(self.grades)
        for i in self.grades:
            sum += i
        avg_grade = sum / amount_of_grades
        return avg_grade
    
    

class Subject:
    list_of_students = []
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def add_student(self, student):
        list_of_students.append(student)

    def add_presence(self, precence, student):
        if presence == "present":
            student.presences.append("present")
        elif presence == "absent":
            student.presences.append("absent")

    def check_presence(self,student):
        amount_of_lessons = len(student.presences)
        sum = 0
        for i in student.presences:
            if i == "present":
                sum += 1
        precentage_of_presence = sum / amount_of_lessons
        return precentage_of_presence


if __name__ == '__main__':  
    student = Student("A", "S")
    student.add_new_grade(1)
    student.add_new_grade(4)
    student.add_new_grade(5)
    avg = student.calculate_avg()
    print(avg)
