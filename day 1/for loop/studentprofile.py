student_id = ""
name = ""
age = ""
course = ""
 
 for True:
   print("-----student profile menu------")
   print("1.add student")
   print("2. view student")
   print("3. update student")
   print("4. Delect student")
   print("5. exit")

choice = int(input("enter choice:"))

if choice == "i":
  student_id = input("enter student_id:")
  name = input("enter name:")
  age = input("enter age:")
  course = input("enter course:")

  print("student added succesfully")
elif choice == "2":
  if student_id == "":
    print("no student found")
  else:
    print("\n student details")
    print("id: "student found")

 
 
 
 
