from school_mgt import Person, Student, Teacher


def test_person():
    person = Person("John", "Doe", 30)
    assert person.first_name == "John"
    assert person.last_name == "Doe"
    assert person.age == 30


def test_get_courses_for_grade_5():
    student = Student("John", "Doe", 10, 5)
    result = student.get_courses()
    assert "Math" in result
    assert "English" in result
    assert "Grade level: 5" in result or "grade 5" in result.lower()


def test_check_fees_paid():
    student = Student("Jane", "Smith", 12, 6, True)
    assert student.check_fees() == "Jane Smith : has paid fees"


def test_check_fees_unpaid():
    student = Student("Ali", "Khan", 11, 4)
    assert student.check_fees() == "Ali Khan : has not paid fees"


def test_update_and_publish_grades():
    student = Student("Sara", "Lee", 13, 8)
    student.update_grade("Math", 90)
    student.update_grade("History", 85)
    output = student.publish_grade()
    assert "Math: 90" in output
    assert "History: 85" in output


def test_str_representation():
    student = Student("Eric", "Stone", 14, 9, True)
    output = str(student)
    assert "Eric Stone" in output
    assert "Grade Level: 9" in output
    assert "Fees Paid: Yes" in output


def test_add_and_list_students():
    teacher = Teacher("Mrs", "Adams", 35, "Science")
    teacher.add_student("John Doe")
    teacher.add_student("Jane Smith")
    output = teacher.list_students()
    assert "John Doe" in output
    assert "Jane Smith" in output


def test_remove_student():
    teacher = Teacher("Mr", "Brown", 40, "English")
    teacher.add_student("Amy Blue")
    teacher.remove_student("Amy Blue")
    assert "Amy Blue" not in teacher.list_students()


def test_list_students_empty():
    teacher = Teacher("Ms", "Green", 30, "French")
    assert teacher.list_students() == "No students assigned."


def test_calculate_pay():
    teacher = Teacher("Dr", "Grey", 45, "Math")
    monthly = teacher.calculate_pay(60000)
    assert "5000.0" in monthly
