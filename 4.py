class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка: неверный лектор или курс'

    def average_grade(self):
        if self.grades:
            return sum([sum(grades) for grades in self.grades.values()]) / sum([len(grades) for grades in self.grades.values()])
        return 0

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average_grade():.1f}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершённые курсы: {', '.join(self.finished_courses)}"
        )

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if self.grades:
            return sum([sum(grades) for grades in self.grades.values()]) / sum([len(grades) for grades in self.grades.values()])
        return 0

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average_grade():.1f}"
        )

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Создание экземпляров классов
best_student1 = Student('Ruoy', 'Eman', 'male')
best_student1.courses_in_progress += ['Python', 'Git']
best_student1.finished_courses += ['Введение в программирование']

best_student2 = Student('John', 'Smith', 'male')
best_student2.courses_in_progress += ['Python', 'Java']
best_student2.finished_courses += ['Анализ данных']

cool_lecturer1 = Lecturer('Some', 'Buddy')
cool_lecturer1.courses_attached += ['Python', 'Git']

cool_lecturer2 = Lecturer('Alice', 'Johnson')
cool_lecturer2.courses_attached += ['Java', 'Python']

cool_reviewer1 = Reviewer('John', 'Doe')
cool_reviewer1.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Ann', 'Brown')
cool_reviewer2.courses_attached += ['Java']

# Оценки от рецензентов для студентов
cool_reviewer1.rate_hw(best_student1, 'Python', 9)
cool_reviewer1.rate_hw(best_student2, 'Python', 8)

cool_reviewer2.rate_hw(best_student1, 'Java', 9)
cool_reviewer2.rate_hw(best_student2, 'Java', 10)

# Оценки от студентов для лекторов
best_student1.rate_lecturer(cool_lecturer1, 'Python', 10)
best_student1.rate_lecturer(cool_lecturer1, 'Git', 9)
best_student2.rate_lecturer(cool_lecturer2, 'Java', 6)
best_student2.rate_lecturer(cool_lecturer2, 'Python', 7)

# Вывод информации о студентах, лекторах и рецензентах
print(best_student1)
print(best_student2)
print(cool_lecturer1)
print(cool_lecturer2)
print(cool_reviewer1)
print(cool_reviewer2)

# Функция для подсчёта среднего балла за домашние задания по всем студентам по курсу
def average_student_grade(students_list, course):
    total_grade = 0
    count = 0
    for student in students_list:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grade / count if count > 0 else 0

# Функция для подсчёта среднего балла за лекции по всем лекторам по курсу
def average_lecturer_grade(lecturers_list, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grade / count if count > 0 else 0

# Пример использования функций
students = [best_student1, best_student2]
lecturers = [cool_lecturer1, cool_lecturer2]

avg_student_grade_python = average_student_grade(students, 'Python')
avg_lecturer_grade_python = average_lecturer_grade(lecturers, 'Python')

print(f"Средний балл за домашние задания по курсу 'Python': {avg_student_grade_python:.1f}")
print(f"Средний балл за лекции по курсу 'Python': {avg_lecturer_grade_python:.1f}")