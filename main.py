class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
class Lecturer(Mentor):
    courses_lect = []
    grades = {}
minerva = Lecturer('Minerva', 'McGonagall')
albus = Lecturer('Albus','Dumbledore')
lecturer_list = [albus, minerva]
    def lect_average_grade(lecturer_lisg, self.courses.lect)




class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_lect:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
harry = Student('Harry','Potter','male')
harry.finished_courses += ['Magic']
harry.grades += [10]
ronald = Student('Ronald','Weasley', 'male')
ronald.grades += [8]
ronald.finished_courses += ['Magic']
student_list = [ronald, harry]
    def st_average_grade(student_list, self.finished_courses):
        if isinstance(student, Student) and course in self.finished_courses and self.grades in student.grades :
            average_grade = student.grades / len(student.list)
        else:
            return 'Ошибка'
print(harry.name, harry.surname, harry.gender)
print(st_average_grade)
class Reviewer(Mentor):
    courses_revierwer = []

    def Rev(self):
        self.courses_revierwer = []

    def rate_hw(self, student, course, grade):
         if isinstance(student, Student) and course in self.courses_revierwer and course in student.courses_in_progress:
            if course in student.grades:
                    student.grades[course] += [grade]
            else:
                    student.grades[course] = [grade]
         else:
             return 'Ошибка'

severus = Reviewer('Severus', "Snape")
filius = Reviewer('Filius',"Flitvik")

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_lector = Lecturer('John', 'Antony')
best_lector.courses_lect += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_revierwer += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
best_student.rate_lect(best_lector, 'Python', 10)
print(best_student.grades)

