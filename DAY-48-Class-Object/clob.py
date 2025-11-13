
# 🧩 Example of Class and Object in Python (With User Input)

# -----------------------------
# 🏗️ Defining a Class
# -----------------------------
class Car:
    # Constructor: initializes attributes
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    # Method to display car information
    def car_info(self):
        print(f"\n🚗 Car Details:")
        print(f"   Brand: {self.brand}")
        print(f"   Model: {self.model}")
        print(f"   Color: {self.color}")

    # Method to start the engine
    def start_engine(self):
        print(f"🔑 The {self.brand} {self.model}'s engine has started!")

    # Method to stop the engine
    def stop_engine(self):
        print(f"🛑 The {self.brand} {self.model}'s engine has stopped.")


# -----------------------------
# 🎭 Taking User Input
# -----------------------------
print("=== 🚘 Create Your Car Object ===")
brand = input("Enter car brand: ")
model = input("Enter car model: ")
color = input("Enter car color: ")

# Create an object using user input
user_car = Car(brand, model, color)

# -----------------------------
# ⚙️ Using the Object
# -----------------------------
user_car.car_info()
user_car.start_engine()
user_car.stop_engine()
