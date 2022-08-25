# Student
# attrs: id, name, birth_year, grade
# methods: set_grade, get_grade, get_age


class Student:
    def __init__(self, s_id, name, birth_year):
        self.student_id = s_id
        self.name = name
        self.birth_year = birth_year
        self.grade = None

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_age(self):
        age = 2022 - self.birth_year
        return age


# s1 = Student(123, "Ofri", 1996)
# s2 = Student(456, "Moshe", 1990)
#
# s1.set_grade(100)
# s2.set_grade(80)
#
#
# print(s1.name + " her age " + str(s1.get_age()) + " and the grage is: " + str(s1.get_grade()))
# print(s2.name + " his age " + str(s2.get_age()) + " and the grage is: " + str(s2.get_grade()))

students = []
for i in range(3):
    s_id = int(input("enter id: "))
    name = input("enter name: ")
    year = int(input("enter birth year: "))

    s = Student(s_id, name, year)
    students.append(s)

for s in students:
    grade = int(input("enter grade for " + s.name + " (" + str(s.student_id) + "):"))
    s.set_grade(grade)


sum_grades = 0
for s in students:
    sum_grades += s.get_grade()

print("the avg is : " + str(sum_grades / len(students)))
