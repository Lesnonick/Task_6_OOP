from statistics import mean
from decimal import Decimal


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        all_grades = []
        for course in self.grades:
            all_grades += self.grades[course]
        return mean(all_grades)

    def __str__(self):
        new_str = 'Имя: ' + self.name + \
                  '\nФамилия: ' + self.surname + \
                  '\nСредняя оценка за лекции: ' + str(Decimal(self.avg_grade()).quantize(Decimal('1.00')))
        return new_str

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __ne__(self, other):
        return self.avg_grade() != other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        new_str = 'Имя: ' + self.name + \
                  '\nФамилия: ' + self.surname
        return new_str


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        all_grades = []
        for course in self.grades:
            all_grades += self.grades[course]
        return mean(all_grades)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        new_str = 'Имя: ' + self.name + \
                  '\nФамилия: ' + self.surname + \
                  '\nСредняя оценка за домашние задания: ' + str(Decimal(self.avg_grade()).quantize(Decimal('1.00'))) + \
                  '\nКурсы в процессе изучения: ' + str(self.courses_in_progress)[1: -1].replace("'", '') + \
                  '\nЗавершенные курсы: ' + str(self.finished_courses)[1: -1].replace("'", '')
        return new_str

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __ne__(self, other):
        return self.avg_grade() != other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()


lecturer_num_1 = Lecturer('Владимир', 'Овчинкин')
lecturer_num_1.courses_attached += ['Physics']
lecturer_num_1.grades['Physics'] = [10, 10, 10, 8, 2, 9]

lecturer_num_2 = Lecturer('Яков', 'Дымарский')
lecturer_num_2.courses_attached += ['Math']
lecturer_num_2.grades['Math'] = [10, 7, 10, 8, 8, 5]

reviewer_num_1 = Reviewer('Алексей', 'Голдин')

lazy_student = Student('Павел', 'Кириллов', 'alien')
lazy_student.finished_courses += ['Git']
lazy_student.courses_in_progress += ['Phyton3', 'Physics']
lazy_student.grades['Git'] = [1, 5, 3, 10]
lazy_student.grades['Phyton3'] = [7, 4, 0]
lazy_student.rate_lecture(lecturer_num_1, 'Physics', 10)

reviewer_num_1.rate_hw(lazy_student, 'Phyton3', 10)

good_student = Student('Кирилл', 'Суслов', 'man')
good_student.finished_courses += ['Git', 'Java']
good_student.courses_in_progress += ['Phyton3', 'Physics']
good_student.grades['Git'] = [10, 10, 9, 10]
good_student.grades['Java'] = [8, 10, 10, 10, 9, 10, 10]
good_student.grades['Phyton3'] = [9, 9, 10]

print(lazy_student.grades)
print()
print(lecturer_num_1.grades)
print()
print(lecturer_num_1)
print()
print(reviewer_num_1)
print()
print(lazy_student)
print()
print(lecturer_num_2 < lecturer_num_1)
print(lazy_student > good_student)

