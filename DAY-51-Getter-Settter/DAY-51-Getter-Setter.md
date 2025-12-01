# Getters and Setters

## Definition
In object-oriented programming (OOP), **getters** and **setters** are special methods used to access and update the private or protected attributes of a class.

- A **Getter** is a method that allows you to *retrieve* the value of a private attribute.
- A **Setter** is a method that allows you to *modify* the value of a private attribute.

These methods support **encapsulation**, which is one of the core principles of OOP. Encapsulation keeps data safe from unintended or unauthorized access and modification.

---

## Purpose of Getters and Setters

1. **Protect Data:**  
   Prevents direct access to sensitive attributes and keeps internal data safe.

2. **Control Access:**  
   Allows an attribute to be made read-only or write-only by controlling which methods exist.

3. **Data Validation:**  
   Setters can check incoming values before updating an attribute (e.g., preventing negative ages).

4. **Flexibility for Future Changes:**  
   Internal implementation can change without affecting external code because interaction happens through methods.

5. **Maintainability:**  
   Makes the structure of the class clearer and easier to update.

---

## General Syntax (Described, Not Code)
Although the structure differs slightly among programming languages, getters and setters follow a similar pattern:

- A **getter method** generally:
  - Has a name that indicates the attribute it retrieves (for example: "get attribute").
  - Returns the value of the private attribute.

- A **setter method** generally:
  - Has a name that indicates it updates the attribute (for example: "set attribute").
  - Accepts a parameter representing the new value.
  - Updates the private attribute after optional validation.

---

## Example Explanation (No Code)
Imagine a class that represents a Person. The class may have private attributes such as:

- Name  
- Age  

Since these attributes are private, they cannot be accessed directly.  
Therefore, the class provides:

- A **getter** for retrieving the name  
- A **setter** for updating the name  
- A **getter** for retrieving the age  
- A **setter** for updating the age, with validation (e.g., age must be positive)

This allows controlled interaction with the data while maintaining its safety and integrity.

---

## Features of Getters and Setters

### 1. Encapsulation  
They hide the internal representation of an object and expose only controlled access points.

### 2. Data Integrity  
Setters help ensure only valid or safe values are assigned to attributes.

### 3. Read-Only or Write-Only Properties  
- If only a getter is provided → the attribute becomes **read-only**.  
- If only a setter is provided → the attribute becomes **write-only**.

### 4. Enhancing Flexibility  
You can add logic inside getters and setters later without changing how external code interacts with the class.

### 5. Security  
They prevent direct access to the internal state, protecting objects from accidental or malicious changes.

---

## Additional Notes

- Many modern languages offer special syntax for getters and setters:
  - **Python:** Uses property decorators to define getters and setters elegantly.
  - **Java:** Typically uses `getProperty()` and `setProperty()` naming conventions.
  - **C#:** Uses built-in `get` and `set` accessors inside properties.
- Getters and setters are a foundational concept in object-oriented design.
- They promote good programming practices by enforcing **clean**, **structured**, and **safe** class design.

---

## Summary
Getters and setters are essential tools in object-oriented programming. They provide a safe, controlled way to access and modify private attributes. By enforcing data validation, maintaining encapsulation, and offering flexibility, they contribute to maintainable and secure software design.
```

---