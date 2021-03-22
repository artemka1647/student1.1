from pprint import pprint

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
        self.finished_courses = ['Зельеварение', 'Заклинания']
        self.courses_in_progress = ['Защита от темных искусств', 'Трансфигурация']
        self.grades = {'Зельеварение':6 ,'Заклинания': 8 }

    def rate_lect(self, lecturer, course, rate):

        if isinstance(lecturer, Lecturer):
            if course in self.courses_in_progress and course in lecturer.course_lect:
                if course in lecturer.rate:
                    lecturer.rate[course] = [rate]
                else:
                    lecturer.rate[course] = [rate]
            else:
                raise ('Ошибка')
        else:
            raise ('Это не лектор')



    def __str__(self, *args, **kwargs):
        return f'Имя:{self.name}, Фамилия:{self.surname},Средняя оценка за ДЗ:{student1.average_grade},Изучаемые курсыы: {self.courses_in_progress}, Пройденные курсы: {self.finished_courses}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name}, Фамилия:{self.surname},'

    def average_grade(self, student, course, grade):
        if isinstance(student, Student):
            if course in self.finished_courses:
                if self.grades in student.grades:
                    av_grade = sum(student.grades) / len(student.finished_courses)
                else:
                    raise ValueError('Сообщение об ошибке')
            else:
                raise ValueError('Сообщение об ошибке')
        else:
            raise ValueError('Сообщение об ошибке')


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.rate = {'Защита от темных искусств': 10, 'Трансфигурация' : 9}
        self.course_lect = ['Защита от темных искусств', 'Трансфигурация']

lecturer1 = Lecturer('Альбус', 'Дамблдор')
lecturer2 = Lecturer('Минерва', 'Макгонагалл')
lecturer_list = [lecturer1, lecturer2]

def ave_rate(course):
    average_rate = 0
    counter = 0
    for lecturer in lecturer_list:
        if course in lecturer.course_lect:
            average_rate += sum(lecturer.rate[course]) / len(lecturer.rate[course])
            counter += 1
        else:
            pass
    return round(average_rate/counter)

def __str__(self):
    return f'Имя:{self.name}, Фамилия:{self.surname},Средняя оценка за лекции:{self.ave_rate}'

student1 = Student('Гарри', 'Поттер', 'мужской')
student1.finished_courses += ['Зельеварение', 'Заклинания']

student2 = Student('Рон', 'Уизли', 'мужской')
student2.finished_courses += ['Зельеварение', 'Заклинания']


lecturer1.course_lect += ['Защита от темных искусств']

student1.rate_lect(lecturer1, 'Защита от темных искусств', 10)
student2.rate_lect(lecturer1, 'Защита от темных искусств', 8)

lecturer2 = Lecturer('Минерва', 'Макгонагалл')
lecturer2.course_lect += ['Трансфигурация']

reviewer1 = Reviewer('Северус', 'Снегг')
reviewer1.rate_hw(student1, 'Зельеварение', 6)
reviewer1.rate_hw(student2, 'Зельеварение', 5)

reviewer2 = Reviewer('Филиас', 'Флитвик')
reviewer2.rate_hw(student1, 'Заклинания', 9)
reviewer2.rate_hw(student2, 'Заклинания', 5)


pprint(student1.__str__())
pprint(lecturer1.__str__())

print(ave_rate('Защита от темных искусств'))