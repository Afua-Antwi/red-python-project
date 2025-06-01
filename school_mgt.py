class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


grade_courses = {
    # Grade 1 to 6
    (1, 6): ["Math", "English", "Social Studies", "Science", "French", "Art", "Physical Education"],
    # Grade 7 to 9
    (7, 9): ["Math", "English", "Literature", "Government", "History", "Biology", "Chemistry"],
}


class Student(Person):
    def __init__(self, first_name, last_name, age, grade_level, fees_paid=False):
        super().__init__(first_name, last_name, age)
        self.grade_level = grade_level
        self.fees_paid = fees_paid
        self.grade_score = {}

    def get_courses(self):
        for grade_range, courses in grade_courses.items():
            if self.grade_level >= grade_range[0] and self.grade_level <= grade_range[1]:
                return f"Courses for {self.first_name} {self.last_name} in grade {self.grade_level}: \n{"\n".join(courses)}"
        return "Grade level not found or no courses available."

    def check_fees(self):
        return f"{self.first_name} {self.last_name} : {"has paid fees" if self.fees_paid else "has not paid fees"}"

    def update_grade(self, course, grade):
        self.grade_score[course] = grade

    def publish_grade(self):
        result = f"{self.first_name} {self.last_name} has the following grades :\n"
        for course, grade in self.grade_score.items():
            result += f"{course}: {grade}\n"
        return result.strip()

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}, Grade Level: {self.grade_level}, Fees Paid: {'Yes' if self.fees_paid else 'No'}"


class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject, salary=0):
        super().__init__(first_name, last_name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)

    def list_students(self):
        return f"Students taught by {self.first_name} {self.last_name}:\n" + "\n".join(self.students) if self.students else "No students assigned."

    def calculate_pay(self, salary):
        self.salary = salary / 12  # Assuming salary is annual, convert to monthly
        return f"{self.first_name} {self.last_name}'s monthly salary is: {self.salary}"


# Example usage for the Student class
Student1 = Student("Kofi", "Manu", 12, 5, True)
print(Student1.get_courses())

Student2 = Student("Ama", "Mensah", 14, 8, True)
print(Student2.check_fees())

Student3 = Student("Jennifer", "Serwaa", 16, 9, True)
Student3.update_grade("Math", 85)
Student3.update_grade("English", 90)
Student3.update_grade("History", 88)
print(Student3.publish_grade())

print(Student1)

# Example usage for the Teacher class
Teacher1 = Teacher("Ken", "Owusu", 40, "Math")
Teacher1.add_student("Kofi Manu")
Teacher1.add_student("Ama Mensah")
print(Teacher1.list_students())
Teacher1.remove_student("Kofi Manu")
print(Teacher1.list_students())
Teacher2 = Teacher("Mary", "Quaye", 35, "History")
Teacher2.add_student("Jennifer Serwaa")
Teacher2.add_student("Ama Mensah")
print(Teacher2.list_students())
print(Teacher1.calculate_pay(60000))  # Assuming annual salary of 60000
print(Teacher2.calculate_pay(72000))  # Assuming annual salary of 72000
