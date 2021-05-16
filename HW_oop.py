class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_hw = 0  # точка отсчёта средней оценки
        Student.student_list.append(self)  # добавляем все экземпляры класса в новый список

    def sett_ratings(self, lectorer, course, grade):  # оценки лекторам за лекции
        if isinstance(lectorer,
                      Lecturer) and course in self.courses_in_progress and course in lectorer.courses_attached:
            if course in lectorer.grades:
                lectorer.grades[course] += [grade]
            else:
                lectorer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):  # Подсчёт срденей оценки
        values_list = []
        for value in self.grades.values():  # Проход по всем парамерам и добавление в новый список
            for each in value:
                values_list.append(each)
        if values_list:
            self.average_hw = sum(values_list) / len(values_list)  # Среднее

    def __str__(self):  # магический метод для принта
        self.average_rating()
        text_courses = ', '.join(grade for grade in self.courses_in_progress)  # Вывод без кавычек
        text_finished_courses = ', '.join(grade for grade in self.finished_courses)  # Вывод без кавычек
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_hw} \nКурсы в процессе изучения: {text_courses} \nЗавершенные курсы: {text_finished_courses}'

    def __lt__(self, other):  # больше или меньше
        return self.average_hw < other.average_hw


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.average_lecture = 0  # точка отсчёта средней оценки
        Lecturer.lecturer_list.append(self)

    def average_rating(self):  # Подсчёт срденей оценки
        values_list = []
        for value in self.grades.values():  # Проход по всем парамерам и добавление в новый список
            for each in value:
                values_list.append(each)
        if values_list:
            self.average_lecture = sum(values_list) / len(values_list)  # Среднее

    def __str__(self):
        self.average_rating()
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_lecture}'

    def __lt__(self, other):  # больше или меньше
        return self.average_lecture < other.average_lecture


class Reviewer(Mentor):  # Проверяющий
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


student_1 = Student('Вася', 'Жако', 'man')
student_1.courses_in_progress += ['Python', 'Git']  # Проходит 2 курса!
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Vilat', 'Pip', 'man')
student_2.courses_in_progress += ['Python']  # Проходит только один курс!
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Faust', 'De`moon')
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2 = Lecturer('Mat', 'Hru')
lecturer_2.courses_attached += ['Python', 'Git']

reviewer_1 = Reviewer('Qwerty', 'Klon')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2 = Reviewer('Jiji', 'Jaja')
reviewer_2.courses_attached += ['Python', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)

student_1.sett_ratings(lecturer_1, 'Python', 10)
student_1.sett_ratings(lecturer_1, 'Git', 8)
student_2.sett_ratings(lecturer_2, 'Python', 7)

print(f'Проверяющий: \n{reviewer_1} \n')

for lecturer in Lecturer.lecturer_list:
    print(f'Лектор: \n{lecturer} \n')

for student in Student.student_list:
    print(f'Студент: \n{student} \n')

print(student_1.average_hw > student_2.average_hw)  # сравнение студентов по средней оценке за домашние задания
#
print(
    lecturer_1.average_lecture > lecturer_2.average_lecture)  # сравнение лекторв по средней оценке за домашние задания



