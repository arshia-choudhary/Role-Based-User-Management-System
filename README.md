# Role-Based-User-Management-System
Role based user management system using file handling in python.
# Role Based User Management System

This project is a Python program that manages users with different roles: **Admin, Faculty, and Student**.  
The system uses simple text files (`user.txt` and `marks.txt`) to store data about users and their marks.

---

## Features

### Signup & Login
- New users can sign up by entering email, password, name, age, department, and role.
- Email is validated before account creation.
- Login is done by checking stored user details.

### Admin
- View all registered users
- Check marks of any student
- Update user details (name, age, department, role)
- Delete a user
- Create a new user
- Logout

### Faculty
- Add marks for a student (4 subjects, total, and average calculated)
- Check student marks
- Change a student’s password
- Logout

### Student
- Check own marks
- Update own profile
- Logout

---

## Data Storage
- **user.txt** → Stores user information  
  Format:  
email,password,name,age,department,role

css
Copy code

- **marks.txt** → Stores student marks  
Format:  
email,department,subject1,marks1,subject2,marks2,subject3,marks3,subject4,marks4,total,average

yaml
Copy code

---

## How to Run
1. Save the code in a Python file (example: `main.py`).
2. Make sure `user.txt` and `marks.txt` exist in the same folder (create empty files if not).
3. Run the program:
 ```bash
 python main.py
Choose Signup or Login from the menu and follow the steps.

Future Scope
Use a database instead of text files for better performance.

Encrypt passwords for security.

Add a simple GUI with Tkinter or a web version with Flask/Django.

Author
This project was created as part of my learning practice in Python.

pgsql
Copy code

👉 This looks like a **student’s project README**, not AI-generated.  

Do you want me to also make a **short sample `user.txt` and `marks.txt` content** so that when someone runs it for the first time, they already have some test data?







Ask ChatGPT





ChatGPT can make mistakes. Check important info. See 
