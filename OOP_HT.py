class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


lecturer_num_1 = Lecturer('Владимир', 'Овчинкин')
reviewer_num_1 = Reviewer('Алексей', 'Голдин')
lazy_student = Student('Павел', 'Кириллов', 'alien')
lazy_student.courses_in_progress += ['Git']
lazy_student.courses_in_progress += ['Phyton3', 'Physics']
lazy_student.grades['Git'] = [1, 5, 3, 10]
lazy_student.grades['Phyton3'] = [7, 4, 0]
reviewer_num_1.rate_hw(lazy_student, 'Phyton3', 10)
lecturer_num_1.courses_attached += ['Physics']
lazy_student.rate_lecture(lecturer_num_1, 'Physics', 10)
print(lazy_student.grades)
print(lecturer_num_1.grades)

