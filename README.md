# Scholarship Management System

## Project Overview
The Scholarship Management System is a web-based application developed using Django. It allows students to explore available scholarships, view detailed information, apply online, and track their application status efficiently.

---

## Features

- User authentication (signup and login)  
- Student profile creation and management  
- View and filter available scholarships  
- Search scholarships by title and description  
- Detailed scholarship view  
- Apply for scholarships with document upload  
- Prevention of duplicate applications  
- Dashboard to track total, approved, and pending applications  

---

## Technology Stack

- Backend: Python, Django  
- Frontend: HTML, CSS, Bootstrap  
- Database: SQLite  

---

## Project Structure

- `accounts` - Authentication and homepage  
- `students` - Student profiles and applications  
- `scholarships` - Scholarship listing and details  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Meghasm10304/scholarship-management-system.git
cd scholarship-management-system
2. Create a virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Apply migrations
python manage.py migrate
5. Run the development server
python manage.py runserver
6. Open in browser
http://127.0.0.1:8000/
Key Learnings
Understanding Django architecture (MVT pattern)
Implementing authentication and authorization
Working with models, views, and templates
Handling file uploads in Django
Debugging and resolving runtime errors
Using Git and GitHub for version control
Acknowledgement

The initial project structure was provided by my internship mentor.
This project includes my implementation, debugging, and feature enhancements built on top of the base structure.

Repository

https://github.com/Meghasm10304/scholarship-management-system
