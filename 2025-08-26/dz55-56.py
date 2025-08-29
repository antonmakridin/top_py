class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

class School:
    def __init__(self):
        self.students = []
    
    def enroll_student(self, student):
        self.students.append(student)
        print(f"{student.name} зачислен в школу.")
    
    def give_grade(self, student_name, grade):
        for student in self.students:
            if student.name == student_name:
                student.grades.append(grade)
                print(f"{student_name} получил оценку {grade}.")
                return
        print(f"Студент {student_name} не найден.")
    
    def show_students(self):
        print("Студенты школы:")
        for student in self.students:
            print(f"- {student.name}, оценки: {student.grades}")

# работа
school = School() 
alice = Student("Алиса") 
bob = Student("Боб")
school.enroll_student(alice) 
school.enroll_student(bob) 
school.give_grade("Алиса", 5)
school.give_grade("Боб", 4) 
school.give_grade("Алиса", 3) 
school.give_grade("Том", 3) 
school.show_students()