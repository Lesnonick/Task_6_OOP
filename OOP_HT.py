from statistics import mean
from decimal import Decimal


class bcolors:
    ATTENTION = '\033[93m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


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

    def add_course(self, course_name):
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


def avg_hw_rating(students, course):
    all_grades = []
    for student in students:
        all_grades += student.grades[course]
    return mean(all_grades)


def avg_lect_rating(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        all_grades += lecturer.grades[course]
    return mean(all_grades)


# Объявления переменных

lecturer_num_1 = Lecturer('Владимир', 'Овчинкин')
lecturer_num_1.courses_attached += ['Physics', 'Math']
lecturer_num_1.grades['Physics'] = [10, 10, 10, 8, 2, 9]
lecturer_num_1.grades['Math'] = [7, 7, 7]

lecturer_num_2 = Lecturer('Яков', 'Дымарский')
lecturer_num_2.courses_attached += ['Math', 'Physics']
lecturer_num_2.grades['Math'] = [10, 7, 10, 8, 8, 5]
lecturer_num_2.grades['Physics'] = [6, 8, 4, 6]

reviewer_num_1 = Reviewer('Алексей', 'Голдин')
reviewer_num_1.courses_attached += ['Physics', 'Phyton3']
reviewer_num_2 = Reviewer('Светлана', 'Иванова')
reviewer_num_2.courses_attached += ['Math']

lazy_student = Student('Павел', 'Кириллов', 'alien')
lazy_student.finished_courses += ['Git']
lazy_student.courses_in_progress += ['Phyton3', 'Physics']
lazy_student.grades['Git'] = [1, 5, 3, 10]
lazy_student.grades['Phyton3'] = [7, 4, 0]

good_student = Student('Кирилл', 'Суслов', 'man')
good_student.finished_courses += ['Git', 'Java']
good_student.courses_in_progress += ['Phyton3', 'Physics', 'Math']
good_student.grades['Git'] = [10, 10, 9, 10]
good_student.grades['Java'] = [8, 10, 10, 10, 9, 10, 10]
good_student.grades['Phyton3'] = [9, 9, 10]

# Проверка методов и функций

print(bcolors.ATTENTION + 'Методы лекторов: срднее и печать' + bcolors.ENDC)
print('%.2f' % lecturer_num_1.avg_grade())
print(lecturer_num_1)
print('%.2f' % lecturer_num_2.avg_grade())
print(lecturer_num_2)
print(bcolors.ATTENTION + 'Методы лекторов: сравнение' + bcolors.ENDC)
print(f'Лектор 1 >  Лектор 2: {lecturer_num_1 > lecturer_num_2}')
# print(lecturer_num_1 >= lecturer_num_2)
# print(lecturer_num_1 == lecturer_num_2)
# print(lecturer_num_1 != lecturer_num_2)
# print(lecturer_num_1 < lecturer_num_2)
print(f'Лектор 1 <= Лектор 2: {lecturer_num_1 <= lecturer_num_2}')

print(bcolors.ATTENTION + 'Методы проверяющих: добавление оценок ученикам' + bcolors.ENDC)
print(bcolors.BOLD + 'ДО' + bcolors.ENDC)
print(f'Ученик 1: {lazy_student.grades}')
print(f'Ученик 2: {good_student.grades}')
reviewer_num_1.rate_hw(lazy_student, 'Physics', 10)
reviewer_num_1.rate_hw(lazy_student, 'Phyton3', 8)
reviewer_num_2.rate_hw(lazy_student, 'Math', 2)
reviewer_num_2.rate_hw(good_student, 'History', 4)
reviewer_num_2.rate_hw(good_student, 'Phyton3', 7)
print(bcolors.BOLD + 'ПОСЛЕ' + bcolors.ENDC)
print(f'Ученик 1: {lazy_student.grades}')
print(f'Ученик 2: {good_student.grades}')
print(bcolors.ATTENTION + 'Методы проверяющих: печать' + bcolors.ENDC)
print(reviewer_num_1)
print(reviewer_num_2)

print(bcolors.ATTENTION + 'Методы студентов: добавление оценок лекторам' + bcolors.ENDC)
print(bcolors.BOLD + 'ДО' + bcolors.ENDC)
print(f'Лектор 1: {lecturer_num_1.grades}')
print(f'Лектор 2: {lecturer_num_2.grades}')
lazy_student.rate_lecture(lecturer_num_1, 'Physics', 10)
lazy_student.rate_lecture(lecturer_num_2, 'Math', 1)
good_student.rate_lecture(lecturer_num_2, 'Math', 7)
good_student.rate_lecture(lecturer_num_2, 'Literacy', 10)
print(bcolors.BOLD + 'ПОСЛЕ' + bcolors.ENDC)
print(f'Лектор 1: {lecturer_num_1.grades}')
print(f'Лектор 2: {lecturer_num_2.grades}')
print(bcolors.ATTENTION + 'Методы студентов: среднее и печать' + bcolors.ENDC)
print('%.2f' % lazy_student.avg_grade())
print(lazy_student)
print('%.2f' % good_student.avg_grade())
print(good_student)
print(bcolors.ATTENTION + 'Методы студентов: добавление курса' + bcolors.ENDC)
print(bcolors.BOLD + 'ДО' + bcolors.ENDC)
print(f'Ученик 1: {lazy_student.finished_courses}')
print(f'Ученик 2: {good_student.finished_courses}')
lazy_student.add_course('Literacy')
good_student.add_course('History')
print(bcolors.BOLD + 'ПОСЛЕ' + bcolors.ENDC)
print(f'Ученик 1: {lazy_student.finished_courses}')
print(f'Ученик 2: {good_student.finished_courses}')
print(bcolors.ATTENTION + 'Методы студентов: сравнение' + bcolors.ENDC)
print(f'Студент 1 >= Студент 2: {lazy_student >= good_student}')
# print(lecturer_num_1 > lecturer_num_2)
print(f'Студент 1 == Студент 2: {lazy_student == good_student}')
# print(lecturer_num_1 != lecturer_num_2)
print(f'Студент 1 >= Студент 2: {lazy_student < good_student}')
# print(f'Лектор 1 <= Лектор 2: {lecturer_num_1 <= lecturer_num_2}')

print(bcolors.ATTENTION + 'Функции средней оценки' + bcolors.ENDC)
students = [lazy_student, good_student]
lecturers = [lecturer_num_1, lecturer_num_2]
print('Средняя оценка лекторов по математике: ' + '%.2f' % avg_lect_rating(lecturers, 'Math'))
print('Средняя оценка студентов по Питону: ' + '%.2f' % avg_hw_rating(students, 'Phyton3'))
