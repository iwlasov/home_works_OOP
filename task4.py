class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []     # список пройденных курсов для каждого студента
        self.courses_in_progress = []  # список курсов которые сейчас изучаются
        self.grades = {} # словарь оценок студентов по курсам

    def add_courses(self, course_name): # метод для добавления пройденных курсов
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade): # метод выставления оценок лекторам
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades: # if course in lecturer.courses_attached
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка при выставлении оценок лекторам'

    def average_rating(self): # метод вычисления средней оценки
        total_subject_grades = 0
        count_subject_grades = 0
        for value in self.grades.values():
            total_subject_grades += sum(value)
            count_subject_grades += len(value)
        return total_subject_grades / count_subject_grades

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_rating():.1f}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка при сравнении студентов'
        return self.average_rating() > other.average_rating()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка при сравнении студентов'
        return self.average_rating() < other.average_rating()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка при сравнении студентов'
        return self.average_rating() == other.average_rating()

class Mentor: # класс преподаватели

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] # список курсов закрепленный за каждым преподавателем

class Lecturer(Mentor): # класс лекторы

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} # словарь оценок лекторов по курсам

    def average_rating(self): # метод вычисления средней оценки
        total_subject_grades = 0
        count_subject_grades = 0
        for value in self.grades.values():
            total_subject_grades += sum(value)
            count_subject_grades += len(value)
        return total_subject_grades / count_subject_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating():.1f}\n'
        return res

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка при сравнении лекторов'
        return self.average_rating() > other.average_rating()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка при сравнении лекторов'
        return self.average_rating() < other.average_rating()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка при сравнении лекторов'
        return self.average_rating() == other.average_rating()

class Reviewer(Mentor): # класс эксперты

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade): # метод выставления преподавателями оценок студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка при выставления оценок студентам'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

# функция подсчета средней оценки в рамках курса
# (в качестве аргументов принимаем список студентов / лекторов и название курса)

def average_grades(incoming_list, course):
    average_rating = 0
    counter = 0
    for incom in incoming_list:
        if course in incom.grades.keys():
            average_rates = 0
            for grade in incom.grades[course]:
                average_rates += grade
            overall_average_rates = average_rates / len(incom.grades[course])
            average_rating += overall_average_rates
            counter += 1
    return average_rating / counter

best_student = Student('Вадим', 'Власов', 48)
best_student.courses_in_progress += ['Java-разработчик с нуля', 'Fullstack-разработчик на Python', 'Python-разработчик с нуля', 'Frontend-разработчик с нуля']
best_student.finished_courses += ['Основы языка программирования Python', 'Git — система контроля версий']
best_student_2= Student('Алексей', 'Германов', 45)
best_student_2.courses_in_progress += ['Java-разработчик с нуля', 'Fullstack-разработчик на Python', 'Python-разработчик с нуля', 'Frontend-разработчик с нуля']
best_student_2.finished_courses += ['Основы языка программирования Python', 'Git — система контроля версий']

cool_lec = Lecturer('Елена', 'Никитина')
cool_lec.courses_attached += ['Fullstack-разработчик на Python', 'Python-разработчик с нуля']
cool_lec_2 = Lecturer('Алена', 'Батицкая')
cool_lec_2.courses_attached += ['Fullstack-разработчик на Python', 'Python-разработчик с нуля']

cool_rev = Reviewer('Олег', 'Булыгин')
cool_rev.courses_attached += ['Java-разработчик с нуля', 'Frontend-разработчик с нуля']
cool_rev_2 = Reviewer('Евгений', 'Шмаргунов')
cool_rev_2.courses_attached += ['Java-разработчик с нуля', 'Frontend-разработчик с нуля']

best_student.rate_lecturer(cool_lec, 'Fullstack-разработчик на Python', 6)
best_student.rate_lecturer(cool_lec, 'Fullstack-разработчик на Python', 4)
best_student.rate_lecturer(cool_lec, 'Fullstack-разработчик на Python', 5)
best_student.rate_lecturer(cool_lec, 'Python-разработчик с нуля', 8)
best_student.rate_lecturer(cool_lec, 'Python-разработчик с нуля', 6)
best_student.rate_lecturer(cool_lec, 'Python-разработчик с нуля', 9)

best_student_2.rate_lecturer(cool_lec_2, 'Fullstack-разработчик на Python', 3)
best_student_2.rate_lecturer(cool_lec_2, 'Fullstack-разработчик на Python', 4)
best_student_2.rate_lecturer(cool_lec_2, 'Fullstack-разработчик на Python', 6)
best_student_2.rate_lecturer(cool_lec_2, 'Python-разработчик с нуля', 7)
best_student_2.rate_lecturer(cool_lec_2, 'Python-разработчик с нуля', 4)
best_student_2.rate_lecturer(cool_lec_2, 'Python-разработчик с нуля', 9)

cool_rev.rate_hw(best_student_2, 'Java-разработчик с нуля', 2)
cool_rev.rate_hw(best_student_2, 'Java-разработчик с нуля', 3)
cool_rev.rate_hw(best_student_2, 'Java-разработчик с нуля', 4)
cool_rev.rate_hw(best_student_2, 'Frontend-разработчик с нуля', 1)
cool_rev.rate_hw(best_student_2, 'Frontend-разработчик с нуля', 5)
cool_rev.rate_hw(best_student_2, 'Frontend-разработчик с нуля', 6)

cool_rev_2.rate_hw(best_student, 'Java-разработчик с нуля', 10)
cool_rev_2.rate_hw(best_student, 'Java-разработчик с нуля', 9)
cool_rev_2.rate_hw(best_student, 'Java-разработчик с нуля', 10)
cool_rev_2.rate_hw(best_student, 'Frontend-разработчик с нуля', 8)
cool_rev_2.rate_hw(best_student, 'Frontend-разработчик с нуля', 10)
cool_rev_2.rate_hw(best_student, 'Frontend-разработчик с нуля', 7)

students_list = [best_student, best_student_2]
lecturer_list = [cool_lec, cool_lec_2]

print('Студенты:')
print(best_student)
print(best_student_2)
print('словарь оценок студентов по курсам')
print(best_student.grades)
print(best_student_2.grades)

print('\nЛекторы:')
print(cool_lec)
print(cool_lec_2)
print('словарь оценок лекторов по курсам')
print(cool_lec.grades)
print(cool_lec_2.grades)

print('\nПроверяющие:')
print(cool_rev)
print(cool_rev_2)

print('Сравнение студентов по средним оценкам за дз:')
if best_student > best_student_2:
    print(f'{best_student.name} учится лучше чем {best_student_2.name}')
else:
    print(f'{best_student_2.name} учится лучше чем {best_student.name}')


print('Сравнение лекторов по средним оценкам за лекции:')
if cool_lec > cool_lec_2:
    print(f'{cool_lec.name} {cool_lec.surname} преподает лучше чем {cool_lec_2.name} {cool_lec_2.surname}')
else:
    print(f'{cool_lec_2.name} {cool_lec_2.surname} преподает лучше чем {cool_lec.name} {cool_lec.surname}')


print(f'\nСредняя оценка студентов по курсу "Java-разработчик с нуля": {average_grades(students_list, "Java-разработчик с нуля"):.1f}')
print(f'Средняя оценка студентов по курсу "Frontend-разработчик с нуля": {average_grades(students_list, "Frontend-разработчик с нуля"):.1f}')

print(f'Средняя оценка лекторов по курсу "Fullstack-разработчик на Python": {average_grades(lecturer_list, "Fullstack-разработчик на Python"):.1f}')
print(f'Средняя оценка лекторов по курсу "Python-разработчик с нуля": {average_grades(lecturer_list, "Python-разработчик с нуля"):.1f}')
