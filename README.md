# Student Notice Board (Django)

A simple, university-syllabus-based web application for a Student Notice Board. Built strictly according to the 5-module Django syllabus.

## 🚀 Tech Stack
- **Backend:** Python, Django
- **Database:** SQLite (Relational Database)
- **Frontend:** HTML5, CSS3 (Bootstrap 5)
- **Scripting:** JavaScript (jQuery)
- **Format:** JSON (for AJAX responses)

## 📚 Syllabus Features Implemented
- **Module 1:** MVT Pattern, URL Conf, Loose Coupling, Wildcard URLs.
- **Module 2:** SQLite Integration, Template Inheritance, Custom Filters, ORM CRUD.
- **Module 3:** Django Admin Interface, Model Forms with Custom Validation.
- **Module 4:** Class-Based Generic Views (ListView, DetailView, CreateView, etc.), Authentication, Sessions, Feed Framework (RSS).
- **Module 5:** AJAX Implementation using jQuery for a "Like" toggle system.

## 🛠️ Step-by-Step Installation

1. **Clone the Repo:**
   ```bash
   git clone <your-repo-url>
   cd django_student_project
   ```

2. **Create & Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Django:**
   ```bash
   pip install django
   ```

4. **Initialize Database:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Users (Admin & Students):**
   - Create an Admin: `python manage.py createsuperuser`
   - Create Students: Log in to `/admin` and add users, or use the command again with different names.

6. **Run Server:**
   ```bash
   python manage.py runserver
   ```
   Visit: `http://127.0.0.1:8000/`

## 🎓 Exam/Viva Quick Reference

### 1. MVC vs MVT
- **Model:** Handles data logic (SQLite).
- **View:** Handles business logic (connects Model to Template).
- **Template:** Handles presentation logic (HTML/Bootstrap).

### 2. CRUD Operations
- **Insert:** Handled by `NoticeCreateView` and `NoticeForm`.
- **Select:** Handled by `NoticeListView` and `NoticeDetailView`.
- **Update:** Handled by `NoticeUpdateView`.
- **Delete:** Handled by `NoticeDeleteView`.

### 3. AJAX Logic
Used for the "Like" button to update the like count without reloading the page. It sends a **POST** request with a **CSRF token**, gets a **JSON response**, and updates the DOM using **jQuery**.

### 4. Sessions
Used to store the 'last visit' time of a user, demonstrating how data persists across requests.
