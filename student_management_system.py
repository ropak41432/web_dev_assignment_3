# Student Management System using Python OOP concepts
# Author: Ropak

class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email          # Private attribute (Encapsulation)
        self.age = age
        self.department = department
        self.__marks = []             # Private attribute (Encapsulation)

    # Encapsulation: Getter and Setter for __email
    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self.__email = new_email
        else:
            print("Error: Invalid email format.")

    # Encapsulation: Getter and Setter for __marks
    def get_marks(self):
        return self.__marks

    def set_marks(self, *marks):
        self.__marks = list(marks)

    # Method Overloading using variable arguments (*marks) and default parameter
    def calculate_result(self, *marks, passing_grade=40):
        scores = marks if marks else self.__marks
        if not scores:
            return "No marks available"
        
        avg = sum(scores) / len(scores)
        status = "Passed" if avg >= passing_grade else "Failed"
        return f"Average: {avg:.2f} ({status})"

    def get_student_type(self):
        return "General Student"

    def display_info(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Type: {self.get_student_type()}")


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    # Method Overriding
    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}")


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    # Method Overriding
    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")


# Demonstration of OOP Concepts
if __name__ == "__main__":
    print("=" * 50)
    print("1. CLASS & OBJECT CREATION")
    print("=" * 50)
    ug_student = UndergraduateStudent(
        name="Ropak Hasan",
        student_id="UG-2024-001",
        email="ropak@example.com",
        age=21,
        department="Computer Science",
        semester="5th Semester"
    )

    grad_student = GraduateStudent(
        name="Sarah Jenkins",
        student_id="GS-2024-102",
        email="sarah.j@example.com",
        age=25,
        department="Software Engineering",
        research_topic="Automated Code Generation with LLMs"
    )

    print(f"Created: {ug_student.name} ({ug_student.get_student_type()})")
    print(f"Created: {grad_student.name} ({grad_student.get_student_type()})")

    print("\n" + "=" * 50)
    print("2. ENCAPSULATION DEMONSTRATION")
    print("=" * 50)
    print(f"Current Email: {ug_student.get_email()}")
    ug_student.set_email("ropak.updated@example.com")
    print(f"Updated Email: {ug_student.get_email()}")
    # Attempting direct access to private attribute
    try:
        print(ug_student.__email)
    except AttributeError:
        print("Direct access ug_student.__email blocked as expected (private attribute).")

    print("\n" + "=" * 50)
    print("3. METHOD OVERLOADING DEMONSTRATION")
    print("=" * 50)
    # Using stored marks
    ug_student.set_marks(85, 78, 92, 88)
    print("Result using stored marks:", ug_student.calculate_result())
    # Passing marks dynamically via *args
    print("Result passing 3 marks dynamically:", grad_student.calculate_result(75, 80, 85))
    # Passing marks dynamically with custom passing grade
    print("Result with custom passing_grade=80:", grad_student.calculate_result(70, 75, passing_grade=80))

    print("\n" + "=" * 50)
    print("4. POLYMORPHISM & METHOD OVERRIDING DEMONSTRATION")
    print("=" * 50)
    student_list = [ug_student, grad_student]

    for s in student_list:
        print("-" * 35)
        s.display_info()
        print("Result:", s.calculate_result(88, 91, 84))
