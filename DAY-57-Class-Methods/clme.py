class Student:
    # Class variable
    school_name = "Green Valley School"
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1

    # Class method to change school name
    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

    # Class method to get total students
    @classmethod
    def get_total_students(cls):
        return cls.total_students

    # Class method as a factory method
    @classmethod
    def create_student_from_string(cls, data):
        name, grade = data.split(",")
        return cls(name.strip(), grade.strip())


# Creating student objects
s1 = Student("Alice", "A")
s2 = Student("Bob", "B")

# Display class-level data
print("School Name:", Student.school_name)
print("Total Students:", Student.get_total_students())

# Change class variable using class method
Student.change_school_name("Blue Ridge School")
print("Updated School Name:", Student.school_name)

# Create object using factory class method
s3 = Student.create_student_from_string("Charlie, A+")

print("New Student:", s3.name, s3.grade)
print("Updated Total Students:", Student.get_total_students())
