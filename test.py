### TEST TASK
# class Person:
#     def __init__(self, id):
#         self.id = id
#
# some_person = Person(100)
# some_person.__dict__['age'] = 30
# print(some_person.age + len(some_person.__dict__))
#
# class Income:
#     def __init__(self, id_):
#         self.id_ = id_
#         id_=100
# income_1 = Income(1000)
# print(income_1.id_)
#
# print(isinstance(some_person, Person))

## Quiz TASK

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

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Phyton']
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Phyton'] = [10, 10]

# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Phyton']
# print(cool_mentor.courses_attached)

cool_mentor.rate_hw(best_student, 'Phyton', 8)
cool_mentor.rate_hw(best_student, 'Phyton', 9)
cool_mentor.rate_hw(best_student, 'Phyton', 10)

print(best_student.grades)

# Nikolai = Student('Nikolai', 'Seliverstov', 'male')
# Mariya = Student('Mariya', 'Simakina', 'female')
# Nikolai.finished_courses.append('Phyton')
# print(Nikolai.finished_courses)
# print(Mariya.finished_courses)

