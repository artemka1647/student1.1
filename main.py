class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []
    def rate_lect(self,lecturer,course,rate):
        if isinstance(lecturer, Lecturer):
            if course in self.courses_in_progress and course in lecturer.course_lect:
                if course in lecturer.rate :
                    lecturer.rate[course] += [rate]
                else:
                   lecturer.rate[course] = [rate]
            else:
                raise ('Ошибка')
        else:
            raise ('Это не лектор')

    def average_grade(self, student, course, grades):
        if isinstance(student, Student):
            if course in self.finished_courses:
                if self.grades in student.grades:
                    av_grade = student.grades / len(student.list)
                else:
                    raise ValueError('Сообщение об ошибке')
            else:
                raise ValueError('Сообщение об ошибке')
        else:
            raise ValueError('Сообщение об ошибке')


    def __str__(self):
        return f'Имя:{self.name}, Фамилия:{self.surname},Средняя оценка за ДЗ:{self.grades},Изучаемые курсыы: {self.courses_in_progress}, Пройденные курсы: {self.finished_courses}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



    def __str__(self):
        return f'Имя:{self.name}, Фамилия:{self.surname},'

class Lecturer(Mentor):
    def __init__(self, name, surname, **kwargs):
        super().__init__(**kwargs):
        self.name = name
        self.surname = surname
        self.rate = []
        self.course_lect = []
    def ave_rate(self, lecturer, course, rate):
        if isinstance(lecturer,Lecturer):
            if course in lecturer.course_lect:
                average_rate = lecturer.rate / len(course_lect)

    def __str__(self):
        return f'Имя:{self.name}, Фамилия:{self.surname},Средняя оценка за лекции:{self.rate}'



student1 = Student('Гарри', 'Поттер', 'мужской')
student2 = Student('Рон', 'Уизли', 'мужской')
lecturer1 = Lecturer('Альбус', 'Дамблдор')
lecturer2 = Lecturer('Минерва', 'Макгонагалл')
reviewer1 = Reviewer('Северус', 'Снегг')
reviewer2 = Reviewer('Филиас', 'Флитвик')






best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
