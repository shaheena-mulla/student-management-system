# ____________________________________________
#Student Management System
#Created By:Shaheena
#Language=Python
#Project No.: 1
# _____________________________________________
students =[]
def save_students():
    with open("students.txt","w")as file:
        for student in students:
            file.write(f"{student['name']},{student['age']},{student['branch']}\n")
def load_students():
    try:
        with open("students.txt","r")as file:
            for line in file:
                name, age ,branch =line.strip().split(",")
                student={
                    "name":name,
                    "age":int(age),
                    "branch":branch
                }

                students.append(student)
    except FileNotFoundError:
        pass
        load_students()
while True:  
    print("\n=========Student Management System=========")
    print("1.Add student")
    print("2.view students")
    print("3.Search student")
    print("4.update student")
    print("5.delete student")
    print("6.Exit")
    print("========================================================")
    choice=input("Enter your choice:")
    if choice=="1":
        name=input("Enter name:")
        age=int(input("Enter age:"))
        branch=input("Enter branch:")


        student={
            "name":name,
            "age": age,
            "branch":branch,
         }
        students.append(student)
        save_students()
        print("\nSaved successfully!\n")
    elif choice=="2":
        if len(students)==0:
            print("Students not found")
        else :
            for student in students:
                print("____________________")
                print("Name:",student["name"])
                print("Age:",student["age"])
                print("Branch:",student["branch"])
                print("____________________")
    elif choice=="3":
        search_name=input("Enter the name to search:")
        found=False
        for student in students:
            if student["name"].lower()==search_name.lower():
                print("\nStudent Found!")
                print("____________________")
                print("Name:",student["name"])
                print("Age:",student["age"])
                print("BRANCH:",student["branch"])
                print("____________________")
                found=True
                break
        if found==False:
            print("Student not found")
    elif choice=="4":
        update=input("Enter the student name to update the details:")
        found=False
        for student in students:
            if student["name"].lower()==update.lower():
                update_name=input("Enter the new name:")
                update_age=int(input("Enter the new age:"))
                update_branch=input("Enter the new branch:")
                student["name"]=update_name
                student["age"]=update_age
                student["branch"]=update_branch
                save_students()
                print("Student details updated successfully!")
                found=True
                break
        if found==False:
            print("Student not found")
    elif choice=="5":
        remove_name=input("Enter the name to remove:")
        found=False
        for student in students:
            if student["name"].lower()==remove_name.lower():
                students.remove(student)
                save_students()
                print("Student deleted successfully!")
                found=True
                break
        if found==False:
            print("student not found")

    elif choice=="6":
        print("Thanks for using Student Management System")
        break
