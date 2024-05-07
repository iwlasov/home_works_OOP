class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # список пройденных курсов для каждого студента
        self.courses_in_progress = []  # список курсов которые сейчас изучаются
        self.grades = {}  # словарь оценок студентов по курсам

    def add_courses(self, course_name):  # метод для добавления пройденных курсов
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):  # метод выставления оценок лекторам
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:  # if course in lecturer.courses_attached
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:  # класс преподаватели

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # список курсов закрепленный за каждым преподавателем


class Lecturer(Mentor):  # класс лекторы

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # словарь оценок лекторов по курсам


class Reviewer(Mentor):  # класс эксперты

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):  # метод выставления преподавателями оценок студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Вадим', 'Власов', 48)
best_student.courses_in_progress += ['Java-разработчик с нуля', 'Fullstack-разработчик на Python',
                                     'Python-разработчик с нуля', 'Frontend-разработчик с нуля']

cool_lec = Lecturer('Елена', 'Никитина')
cool_lec.courses_attached += ['Fullstack-разработчик на Python', 'Python-разработчик с нуля']

cool_rev = Reviewer('Олег', 'Булыгин')
cool_rev.courses_attached += ['Java-разработчик с нуля', 'Frontend-разработчик с нуля']

best_student.rate_lecturer(cool_lec, 'Fullstack-разработчик на Python', 6)
best_student.rate_lecturer(cool_lec, 'Fullstack-разработчик на Python', 4)
best_student.rate_lecturer(cool_lec, 'Fullstack-разработчик на Python', 5)
best_student.rate_lecturer(cool_lec, 'Python-разработчик с нуля', 8)
best_student.rate_lecturer(cool_lec, 'Python-разработчик с нуля', 6)
best_student.rate_lecturer(cool_lec, 'Python-разработчик с нуля', 9)

cool_rev.rate_hw(best_student, 'Java-разработчик с нуля', 10)
cool_rev.rate_hw(best_student, 'Java-разработчик с нуля', 9)
cool_rev.rate_hw(best_student, 'Java-разработчик с нуля', 10)
cool_rev.rate_hw(best_student, 'Frontend-разработчик с нуля', 8)
cool_rev.rate_hw(best_student, 'Frontend-разработчик с нуля', 10)
cool_rev.rate_hw(best_student, 'Frontend-разработчик с нуля', 7)

print(cool_lec.grades)
print(best_student.grades)
