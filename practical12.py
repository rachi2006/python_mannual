class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course.course_name}")

    def display(self):
        print("\n--- Student Details ---")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Courses Enrolled:")
        for c in self.courses:
            print("-", c.course_name)


class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def display(self):
        print("\n--- Teacher Details ---")
        print("ID:", self.teacher_id)
        print("Name:", self.name)
        print("Subject:", self.subject)


class Course:
    def __init__(self, course_id, course_name, teacher):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} added to {self.course_name}")

    def display(self):
        print("\n--- Course Details ---")
        print("Course ID:", self.course_id)
        print("Course Name:", self.course_name)
        print("Teacher:", self.teacher.name)
        print("Students Enrolled:")
        for s in self.students:
            print("-", s.name)


# Creating objects
teacher1 = Teacher("T01", "Ms. Smith", "Mathematics")
course1 = Course("C01", "AI & DS", teacher1)
student1 = Student("S01", "Rachith", 15)

# Enroll student
student1.enroll(course1)
course1.add_student(student1)

# Display details
teacher1.display()
course1.display()
student1.display()
