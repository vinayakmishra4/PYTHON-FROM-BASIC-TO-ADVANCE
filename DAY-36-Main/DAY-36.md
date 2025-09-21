

# 🌟 DAY-36 — `if __name__ == "__main__"`

In Python, every file has a special built-in variable called **`__name__`**.  
The value of this variable changes depending on **how the file is used**:

---

## 🔎 How it works

- ▶️ **When the file is run directly**  
  `__name__ = "__main__"` → The code inside this block **executes**.  

- 📦 **When the file is imported as a module**  
  `__name__ = "filename"` → The code inside this block **does not run**.  

---

## 🎯 Why use it?

✅ **Prevents unwanted execution** — Keeps print statements, tests, or main logic from running when imported.  
✅ **Encourages reusability** — Functions and classes can be imported freely.  
✅ **Organizes your project** — Separates **library code** from **main program logic**.  

---

## 🛠 Best Practice

Always wrap your entry-point code like this:

```
if __name__ == "__main__":
    # main logic here
```

This ensures your script is both **executable** and **importable**.  

---

## 🎭 Analogy (Easy to Remember)

Think of a Python file as a **play script**:  

- 🎬 Running directly = **Actors perform on stage** (main code runs).  
- 📖 Importing as module = **Reading backstage** (you see the script but no performance happens).  

---

## 🧭 Quick Visual Flow

```
Run directly?  ---> Yes ---> __name__ = "__main__" ---> Run main block
                 |
                 No
                 |
                 V
           Import as module ---> __name__ = "module_name" ---> Skip main block
```

---

✨ In short:  
`if __name__ == "__main__":` lets you write code that’s **both reusable as a module** and **executable as a standalone script**.  