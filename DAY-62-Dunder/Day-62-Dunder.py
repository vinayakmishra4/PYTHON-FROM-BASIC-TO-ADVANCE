class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    # String Representation
    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, Marks: {self.marks})"

    # Length of Name
    def __len__(self):
        return len(self.name)

    # Comparison
    def __gt__(self, other):
        return self.marks > other.marks

    # Addition of Marks
    def __add__(self, other):
        return self.marks + other.marks

    # Callable Object
    def __call__(self):
        return f"Hello {self.name}! Welcome to Python."

    # Container Method
    def __getitem__(self, key):
        data = {
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }
        return data[key]


# ----------- User Input -----------

print("Enter Details for Student 1")
name1 = input("Name : ")
age1 = int(input("Age : "))
marks1 = int(input("Marks : "))

print("\nEnter Details for Student 2")
name2 = input("Name : ")
age2 = int(input("Age : "))
marks2 = int(input("Marks : "))

# Creating Objects
s1 = Student(name1, age1, marks1)
s2 = Student(name2, age2, marks2)

# ----------- Dunder Method Demonstration -----------

print("\n===== Dunder Methods Output =====")

print("\n1. __str__()")
print(s1)

print("\n2. __len__()")
print("Length of Name:", len(s1))

print("\n3. __add__()")
print("Total Marks:", s1 + s2)

print("\n4. __gt__()")
print("Student 1 has more marks than Student 2:", s1 > s2)

print("\n5. __call__()")
print(s1())

print("\n6. __getitem__()")
print("Name :", s1["name"])
print("Age  :", s1["age"])
print("Marks:", s1["marks"])