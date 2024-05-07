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

class Mentor: # класс преподаватели
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = [] # список курсов закрепленный за каждым преподавателем

  def rate_hw(self, student, course, grade): # метод выставления преподавателями оценок студентам
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

class Lecturer(Mentor): # класс лекторы
    pass

class Reviewer(Mentor): # класс эксперты
    pass

best_student = Student('Вадим', 'Власов', 48)
best_student.courses_in_progress += ['Java-разработчик с нуля', 'Fullstack-разработчик на Python', 'Python-разработчик с нуля', 'Frontend-разработчик с нуля']

cool_mentor = Mentor('Олег', 'Булыгин')
cool_mentor.courses_attached += ['Fullstack-разработчик на Python', 'Python-разработчик с нуля']

cool_mentor.rate_hw(best_student, 'Fullstack-разработчик на Python', 10)
cool_mentor.rate_hw(best_student, 'Fullstack-разработчик на Python', 9)
cool_mentor.rate_hw(best_student, 'Fullstack-разработчик на Python', 10)
cool_mentor.rate_hw(best_student, 'Python-разработчик с нуля', 8)
cool_mentor.rate_hw(best_student, 'Python-разработчик с нуля', 10)
cool_mentor.rate_hw(best_student, 'Python-разработчик с нуля', 7)

print(best_student.grades)
