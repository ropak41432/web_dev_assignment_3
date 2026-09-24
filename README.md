# Student Management System

A Python-based Student Management System developed using core Object-Oriented Programming (OOP) principles.

---

## Class Architecture

```
Student (Base Class)
  │
  ├── UndergraduateStudent (Subclass)
  └── GraduateStudent (Subclass)
```

---

## OOP Concepts Demonstrated

1. **Class & Object:**
   - Base `Student` class and specialized subclasses (`UndergraduateStudent`, `GraduateStudent`).
   - Multiple student instances created with unique identities and data.

2. **Attributes:**
   - Common student attributes: `name`, `student_id`, `age`, `department`.
   - Subclass-specific attributes: `semester` for undergraduate students and `research_topic` for graduate students.

3. **Methods:**
   - Methods implementing core student operations: `display_info()`, `calculate_result()`, and `get_student_type()`.

4. **Inheritance:**
   - `UndergraduateStudent` and `GraduateStudent` inherit common attributes and behavior from `Student` using `super().__init__(...)`.

5. **Encapsulation:**
   - Sensitive attributes (`__email`, `__marks`) are declared private using double underscores.
   - Controlled access and modification are enforced through getter (`get_email()`, `get_marks()`) and setter (`set_email()`, `set_marks()`) methods with validation.

6. **Method Overloading:**
   - Python-style method overloading implemented in `calculate_result(*marks, passing_grade=40)` using variable arguments (`*marks`) and default parameters to support different argument counts.

7. **Method Overriding:**
   - Subclasses override `get_student_type()` to return specific student types (`"Undergraduate Student"`, `"Graduate Student"`).
   - Subclasses extend `display_info()` to include subclass-specific fields.

8. **Polymorphism:**
   - Different student objects are stored in a single list and iterated through, invoking the same interface (`display_info()`, `calculate_result()`) with each object executing its specific implementation.

---

## Project Structure

```
├── student_management_system.py      # Main Python script
└── README.md                         # Project documentation
```

---

## How to Run

```bash
python student_management_system.py
```
