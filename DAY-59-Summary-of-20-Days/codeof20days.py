# 🌟 Advanced Student Management System 🌟
# Concepts: OOP, inheritance, decorators, static/class methods, lambda, map/filter/reduce, file I/O, introspection

import json
from functools import reduce

# --- Global variable (Day 41) ---
student_file = "students.json"

# --- Decorator to log actions (Day 50) ---
def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Action '{func.__name__}' executed ✅")
        return result
    return wrapper

# --- Base class (Day 47, 48, 52, 53) ---
class Person:
    _species = "Human"  # Protected variable (Day 53)
    __population = 0    # Private variable (Day 53)

    def __init__(self, name, age):
        self.name = name          # Public attribute
        self.age = age            # Public attribute
        Person.__population += 1

    @classmethod
    def get_population(cls):      # Class method (Day 57)
        return cls.__population

# --- Student class inheriting from Person ---
class Student(Person):
    school_name = "ABC School"   # Static/Class variable (Day 54, 55)

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade       # Private variable (Day 53)

    # Getter and setter (Day 51)
    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("Invalid grade! Must be 0-100.")

    @staticmethod                   # Static method (Day 54)
    def is_passing(grade):
        return grade >= 50

    @log_action                     # Using decorator
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.__grade}, School: {Student.school_name}")

# --- Helper functions for file I/O (Day 42) ---
def save_students_to_file(students):
    data = [{"name": s.name, "age": s.age, "grade": s.grade} for s in students]
    with open(student_file, "w") as f:
        json.dump(data, f)
    print("All students saved to file! 📂")

def load_students_from_file():
    students = []
    try:
        with open(student_file, "r") as f:
            data = json.load(f)
            for item in data:
                students.append(Student(item["name"], item["age"], item["grade"]))
    except FileNotFoundError:
        pass
    return students

# --- Program Main Loop ---
students = load_students_from_file()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Students (by name)")
    print("4. View Average Grade")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        grade = int(input("Grade (0-100): "))
        s = Student(name, age, grade)
        students.append(s)
        print(f"Student {name} added! ✅")
        
    elif choice == "2":
        if not students:
            print("No students found! ❌")
        else:
            for s in students:
                s.display_info()
                
    elif choice == "3":
        keyword = input("Enter name to search: ")
        # Using lambda and filter (Day 43, 44)
        found = list(filter(lambda s: s.name.lower() == keyword.lower(), students))
        if found:
            print(f"{len(found)} student(s) found:")
            for s in found:
                s.display_info()
        else:
            print("No student found with that name! ❌")
            
    elif choice == "4":
        if students:
            grades = list(map(lambda s: s.grade, students))
            average = reduce(lambda a, b: a + b, grades) / len(grades)
            print(f"Average Grade of all students: {average:.2f}")
            passing_count = len(list(filter(Student.is_passing, grades)))
            print(f"Passing Students: {passing_count}/{len(students)}")
        else:
            print("No students to calculate average! ❌")
            
    elif choice == "5":
        save_students_to_file(students)
        print("Exiting program... Goodbye! 👋")
        break
        
    else:
        print("Invalid choice! ⚠️")

# --- Object introspection (Day 58) ---
if students:
    print("\n--- Object Introspection Example ---")
    first_student = students[0]
    print(f"type: {type(first_student)}")
    print(f"dir: {dir(first_student)}")
    print(f"vars: {vars(first_student)}")
    print(f"Is instance of Student? {isinstance(first_student, Student)}")
    print(f"Population via class method: {Student.get_population()}")