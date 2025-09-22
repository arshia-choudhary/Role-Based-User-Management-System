
def emailvalidation():
    while True:
        emailresult = input("Enter email: ")
        has_space = 0
        has_invalid_char = 0

        if len(emailresult) >= 6:
            if emailresult[0].isalpha():
                if "@" in emailresult and emailresult.count("@") == 1:
                    if emailresult[-4] == "." or emailresult[-3] == ".":
                        for char in emailresult:
                            if char.isspace():
                                has_space = 1
                            elif char.isalpha() or char.isdigit():
                                continue
                            elif char in "_@.":
                                continue
                            else:
                                has_invalid_char = 1

                        if has_space == 1 or has_invalid_char == 1:
                            print("Invalid! No spaces allowed")
                        else:
                            return emailresult
                    else:
                        print("Invalid! Expected '.'")
                else:
                    print("Invalid! Expected one @.")
            else:
                print("Invalid! Must Start with alphabet")
        else:
            print("Invalid! Enter Again")


def signup():
        email = emailvalidation()
        password = input("Enter password: ")
        name = input("Enter full name: ")
        age = input("Enter age: ")
        dept = input("Enter department: ")
        status_input = int(input("Enter 0 for Admin, 1 for Faculty, 2 for Student: "))
        if status_input == 0:
            status = "Admin"
        elif status_input == 1:
            status = "Faculty"
        else:
            status = "Student"
        data=[email,password,name,age,dept,status]
        with open("user.txt","a") as file:
            file.write(",".join(data)+"\n")


def admin(choice):
    if choice==1:
        with open("user.txt","r"):
            count=1
            print("All users are : ")
            for line in users:
                print("{count}. {line}")
                count+=1
    elif choice==2:
        student_email = input("Enter student email to check marks: ")
        with open("marks.txt","r"):
            for mark in marks:
                marks_data=mark.strip().split(",")
                if marks_data[0]==student_email:
                    print(marks_data[2],marks_data[3])
                else:
                    print("Not found!")    
    elif choice==3:
        change_email = input("Enter email of user to update details: ")
        with open("user.txt", "w") as f:
            for line in users:
                user_data = line.strip().split(",")
                if user_data[0] == change_email:
                    print("Current details:", user_data)
                    user_data[2] = input("Enter new name: ")
                    user_data[3] = input("Enter new age: ")
                    user_data[4] = input("Enter new department: ")
                    user_data[5] = input("Enter new role (Admin/Faculty/Student): ")
                    f.write(",".join(user_data) + "\n")
                    print("User details updated.")
                else:
                    f.write(line)
    elif choice==4:
        delete=input("Enter email of user to delete : ")
        with open("user.txt","w") as f:
            for line in users:
                user_data=line.strip().split(",")
                if user_data[0]==delete:
                    del line
                else:
                    f.write(line)

    elif choice==5:
        signup()
        print("New user created successfuly!")

    elif choice == 6:
        return False
    else:
        print("Invalid Choice!")

def faculty(choice):
    if choice==1:
            semail=input("Enter email")
            dpt=input("Enter department : ")
            subject1=input("Enter 1st subject : ")
            marks1=input("Enter 1st subject marks : ")
            subject2=input("Enter 2st subject : ")
            marks2=input("Enter 2st subject marks : ")
            subject3=input("Enter 3st subject : ")
            marks3=input("Enter 3st subject marks : ")
            subject4=input("Enter 4st subject : ")
            marks4=input("Enter 4st subject marks : ")
            total=marks1+marks2+marks3+marks4
            avg=total/4
            data1=[semail,dpt,subject1,marks1,subject2,marks2,subject3,marks3,subject4,marks4,total,avg]
            with open("marks.txt","a") as f:
                f.write(",".join(data1)+"\n")
            print("Marks added successfully!")
                
    elif choice==2:
        student_email = input("Enter student email to check marks: ")
        with open("marks.txt","r"):
            for mark in marks:
                marks_data=mark.strip().split(",")
                if marks_data[0]==student_email:
                    print(marks_data[2],marks_data[3])
                else:
                    print("Not found!")  

    elif choice==3:
        email_password = input("Enter student email to change password : ")
        with open("user.txt", "w") as f:
            for line in users:
                user_data = line.strip().split(",")
                if user_data[0] == email_password:
                    user_data[1]=input("Enter new password : ")
                    f.write(",".join(user_data) + "\n")
                    print("User password updated.")
                else:
                    f.write(line)
    

    elif choice==4:
        return False
    
    else:
        print("Invalid Choice!")



def student(choice):
    if choice==1:
        with open("marks.txt","r"):
            for mark in marks:
                marks_data=mark.strip().split(",")
                if marks_data[0]==email:
                    print(marks_data[1],marks_data[2])
                else:
                    print("Not marks found!")  


    elif choice==2:

        with open("user.txt", "w") as f:
            for line in users:
                user_data = line.strip().split(",")
                if user_data[0] == email:
                    print("Current details:", user_data)
                    user_data[2] = input("Enter new name: ")
                    user_data[3] = input("Enter new age: ")
                    user_data[4] = input("Enter new department: ")
                    user_data[5] = input("Enter new role (Admin/Faculty/Student): ")
                    f.write(",".join(user_data) + "\n")
                    print("details updated.")
                else:
                    f.write(line)



    elif choice==3:
        return False
    else:
        print("Invalid choice!")
       







print("\n\n-----ROLE-BASED USER MANAGEMENT SYSTEM-----\n")
while True:
    print("\n1. Signup\n2. Login\n3. Exit")
    user = int(input("Choose: "))
    
    if user == 1:
        signup()
        print("Signup successful!")

    elif user == 2:
        email = input("Enter email: ")
        password = input("Enter password: ")
    
        with open("user.txt", "r") as f:
            users = f.readlines()
        for line in users:
            data = line.strip().split(",")
            if data[0] == email:
                if data[1] == password:
                    print("Login successful!\nWelcome,", data[2])
                    role = data[5]
                    dept = data[4]
                    
                    while True:
                        with open("marks.txt", "r") as stuMarks:
                            marks=stuMarks.readlines()

                            
                        if role == "Admin" or role=="admin":
                            print("Admin menu:\n1. View All Users\n2. Check Student Marks by Email\n3. Update User Details\n4. Delete a User\n5. Create a New User\n6. Logout")
                            choice = int(input("Choose: "))
                            result=admin(choice)
                            if result==False:
                                break

                        elif role == "Faculty" or role=="faculty":
                            print("Faculty menu:\n1. Add marks for a student\n2. Check student marks\n3. Change password\n4. Logout")
                            choice =int(input("Choose: "))
                            result=faculty(choice)
                            if result==False:
                                break
                        

                        elif role == "Student" or role=="student":
                            print("Student menu:\n1. Check own marks\n2. Update own Profile\n3. Logout")
                            choice = int(input("Choose: "))
                            result=student(choice)
                            if result==False:
                                break 
        else:
            print("Wrong Email or Password!")
            
                
    elif user == 3:
        print("End of program.Thank You!")
        break

    else:
        print("Invalid choice!")

