students = []

for i in range(3):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    major = input("Enter your major: ")
    
    student = {"name": name, "age": age, "major": major}
    students.append(student)

print("---- Info of Students ----")
for student in students:
    
    print(f"name: {student['name']} | age: {student['age']} | major: {student['major']}")

search_name = input("Enter name the student to search : ")

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("the student was found")
        print(f"name: {student['name']} | age: {student['age']} | major: {student['major']}")
        found = True
        break

if not found:
    print("the student was not found ")

delete_name = input("Enter name the student to delete :")
delete = False
for student in students:
     if student["name"].lower() == delete_name.lower():
         students.remove(student)
         print("the student has been deleted")
         delete = True
         break
if not delete :
         print("the student was not delete ")
    