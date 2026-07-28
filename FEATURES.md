# 🎯 Student Management System - Features

This project is a **menu-driven Student Management System** developed using **Python**. It allows users to manage student records efficiently while storing data permanently in a JSON file.

---

# 👨‍🎓 Student Management Features

## ➕ Add Student

- Add a new student record.
- Stores:
  - Student ID
  - Student Name
  - Student Age
  - Student Course
- Prevents duplicate Student IDs.
- Saves data automatically to `students.json`.

---

## 📋 View All Students

- Displays all student records.
- Shows:
  - Student ID
  - Name
  - Age
  - Course
- Displays the total number of students.

---

## 🔍 Search Student

- Search a student using the Student ID.
- Displays complete student information.
- Shows an appropriate message if the student is not found.

---

## ✏️ Update Student

- Update existing student information.
- Editable fields:
  - Name
  - Age
  - Course
- Saves updated information automatically.

---

## 🗑️ Delete Student

- Delete a student record using Student ID.
- Automatically updates the JSON file.
- Displays a success message after deletion.

---

## 👥 Total Students

Displays:

- Total number of students currently stored.

---

## 🧹 Clear Students

- Removes all student records.
- Clears the JSON file automatically.
- Useful for resetting the application.

---

# 💾 Data Storage

- Permanent data storage using **JSON**.
- Automatically loads student records when the application starts.
- Automatically saves every change.
- Handles missing or corrupted JSON files gracefully.

---

# 🛡️ Input Validation

The application validates:

- Student ID must be numeric.
- Student Name cannot be empty.
- Student Age must be between **1 and 120**.
- Student Course cannot be empty.
- Duplicate Student IDs are not allowed.

---

# ⚠️ Error Handling

The system handles:

- Invalid numeric inputs
- Missing student records
- Duplicate Student IDs
- Empty fields
- Missing JSON file
- Corrupted JSON file

---

# 🧠 Python Concepts Used

- Functions
- Loops
- Conditional Statements
- Lists
- Dictionaries
- CRUD Operations
- JSON File Handling
- Exception Handling (`try-except`)
- Input Validation
- File Handling

---

# 🚀 Future Enhancements

- 🔐 Login Authentication
- 📊 Student Grade Management
- 📄 Export Student Data to CSV
- 📈 Student Performance Reports
- 📅 Admission Date Management
- 🗄️ SQLite/MySQL Database Integration
- 🖥️ GUI using Tkinter
- 🌐 Web Version using Flask or Django

---

# ✅ Project Highlights

- Menu-Driven CLI Application
- Beginner-Friendly Python Project
- Persistent JSON Data Storage
- CRUD Functionality
- Strong Input Validation
- Exception Handling
- Clean and Readable Code
- Easy to Extend and Maintain