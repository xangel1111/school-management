# 🏫 SCHOOL MANAGER - School magement system

**School Manager** is a web-based school management system built with Django. It helps educational institutions manage students and their courses.

## 🚀 Key Features

- Student Management
- Course Management
- **Course Enrollments**
  - Students can be enrolled in multiple courses
  - Courses can have multiple students

## 🔧 Technologies

- Python 3.x
- Django
- Bootstrap 5
- SQLite (por defecto)

## 📝 Requirements

To run the **School Manager** application, you need the following:

- **Python 3.x**
- **pip** – Python package installer (comes with Python)

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/xangel1111/school-management.git
cd school-management
```

### 2. Create and Activate a Virtual Environment ()

**On Unix/macOS**:

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows**:

```bash
python3 -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Make and Apply Migrations

```bash
cd src
python3 makemigrations
python3 migrate
```

### 5. Seed the Database (Optional)

```bash
python3 seed.py
```

### 6. Start the Development Server

```bash
python3 manage.py runserver
```

### 7. Access the Application

Open your browser and navigate to:
http://localhost:8000/

