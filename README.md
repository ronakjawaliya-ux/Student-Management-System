# 🎓 Student Management System (Python)

A simple **Student Management System** built using **Python** that allows users to manage student records through a command-line interface (CLI). Student records are stored permanently using **JSON**, ensuring data remains available even after the program is closed.

---

## 📌 Features

### 👨‍🎓 Student Management

- ✅ Add New Student
- ✅ View All Students
- ✅ Search Student by ID
- ✅ Update Student Details
- ✅ Delete Student Record
- ✅ Display Total Number of Students
- ✅ Clear All Student Records

### 💾 Data Management

- ✅ Automatic JSON Data Saving
- ✅ Automatic JSON Data Loading

### 🛡️ Validation & Error Handling

- ✅ Student ID Validation
- ✅ Duplicate Student ID Prevention
- ✅ Name Validation
- ✅ Age Validation
- ✅ Course Validation
- ✅ Exception Handling using `try-except`
- ✅ Handles Missing or Corrupted JSON Files

---

## 🛠️ Technologies Used

- Python 3
- JSON (Data Storage)

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py              # Main application
├── students.json        # Stores student records
├── README.md            # Project documentation
├── FEATURES.md          # Project features
├── .gitignore           # Ignore unnecessary files
└── screenshots/         # Application screenshots
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ronakjawaliya-ux/Student-Management-System.git
```

### 2. Open the project folder

```bash
cd Student-Management-System
```

### 3. Run the application

```bash
python main.py
```

---

## 📋 Menu Options

```text
===== Student Management System =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Total Students
7. Clear Students
8. Exit
```

---

## 💡 Features Explained

### ➕ Add Student

- Adds a new student record.
- Prevents duplicate Student IDs.
- Validates:
  - Student ID
  - Student Name
  - Student Age
  - Student Course

### 📋 View Students

- Displays all student records.
- Shows:
  - Student ID
  - Name
  - Age
  - Course

### 🔍 Search Student

- Search a student using the Student ID.
- Displays complete student information.

### ✏️ Update Student

- Update an existing student's information.
- Editable fields:
  - Name
  - Age
  - Course
- Saves updated information automatically.

### 🗑️ Delete Student

- Deletes a student record using Student ID.
- Automatically updates the JSON file.

### 👥 Total Students

Displays the total number of students currently stored.

### 🧹 Clear Students

- Deletes all student records.
- Automatically updates the JSON file.

---

## ⚠️ Input Validation

The application validates:

- Student ID
- Duplicate Student IDs
- Student Name
- Student Age (1–120)
- Student Course

The application prevents:

- Invalid numeric inputs
- Empty names
- Empty course names
- Invalid age values
- Duplicate Student IDs
- Operations on non-existing students

---

## 📄 Sample JSON

```json
[
    {
        "id": 101,
        "name": "Ronak",
        "age": 22,
        "course": "B.Tech CSE (AI & ML)"
    },
    {
        "id": 102,
        "name": "Aman",
        "age": 21,
        "course": "BCA"
    }
]
```

---

## 📷 Sample Output

```text
Student Details

-----------------------------------
ID        : 101
Name      : Ronak
Age       : 22
Course    : B.Tech CSE (AI & ML)
-----------------------------------
```

---

## 📸 Screenshots

Application screenshots are available in the **screenshots/** folder.

- Main Menu
- Add Student
- View Students
- Search Student
- Update Student
- Delete Student

---

## 🎯 Future Improvements

- 🔐 Login Authentication
- 📊 Student Grade Management
- 📄 Export Student Records to CSV
- 📈 Student Performance Reports
- 📅 Admission Date Management
- 🗄️ SQLite/MySQL Database Integration
- 🖥️ Graphical User Interface (Tkinter)
- 🌐 Web Version using Flask or Django

---

## 📚 What I Learned

This project helped me strengthen my understanding of:

- Python Fundamentals
- Functions
- Loops & Conditional Statements
- Lists & Dictionaries
- CRUD Operations
- JSON File Handling
- Exception Handling (`try-except`)
- Input Validation
- Data Persistence
- Problem-Solving
- Building Complete CLI Applications

---

## 👨‍💻 Author

**Ronak Jawalia**

- B.Tech CSE (AI & ML)
- Python Developer
- Learning Data Structures & Algorithms
- Building projects to strengthen programming skills

### GitHub

- **Profile:** https://github.com/ronakjawaliya-ux
- **Repository:** https://github.com/ronakjawaliya-ux/Student-Management-System

---

## ⭐ Support

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub. It motivates me to keep learning, improve my programming skills, and build more exciting projects.