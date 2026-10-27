print("Welcome To the Student Data Organizer 1")

students=[
    {"id":1,"name":"Jayraj","age":18,"grade":"A+","subject":"Math,English,Science","Date of Birth":"13-02-2007"},
    {"id":2,"name":"Neev","age":21,"grade":"A","subject":"Math,C Programming,Science","Date of Birth":"03-07-2008"},
    {"id":3,"name":"Hardik,","age":19,"grade":"A","subject":"Math,Gujrati,Science","Date of Birth":"16-10-2006"},
]


print("Select An Opton :")

while True:
    print("1. Add Student ")
    print("2. Display All Student ")
    print("3. Update Student Information ")
    print("4. Delete Student")
    print("5. Display Subject Offered")
    print("6. Exit")

    choice = int (input("Enter Your Choice :"))


    if choice == 1:

        id= int(input("Enter Student ID :"))

        found= False

        for s in students:
            if s["id"]==id:
                found=True
                break

        if found:
                print("Student With This ID Already Exist !")

        if not found:
            name=input("Enter Student Name :")
            age=int(input("Enter Student age :"))
            DoB=input("Enter Student's Date of Birth :")
            grade=input("Enter Student's Grade : ")
            subject=input("Enter Student's Subjects ")

            newstudent={
                "id":id,"name":name,"age":age,"grade":grade,"Date of Birth":DoB,"subject":subject
            }
 

            students.append(newstudent)

            print(students)


    elif choice == 2:
        for s in students:
            print(" ID :",s["id"],"Name :",s["name"],"Age :",s["age"],"Grade :",s["grade"],"Subjects :",s["subject"],"Date of Birth :",s["Date of Birth"],sep="|")
            
                
    elif choice == 3:

        id=int(input("Enter Student's ID :"))

        found= False


        for s in students:
            if s["id"]==id:
                age=int(input("Enter New Age :"))
                s["age"]=age
                print("Age Updated Successfull !")
                subject=input("Enter Student's Subject :")
                s["subject"]=subject
                print("Student's Subject Updated Succesfully !")
                print(s,sep="|")
                found=True

        if not found:
            print("Student Not Found !")

    elif choice == 4:

        id=int(input("Enter Student's Id :"))

        found=False

        for s in students:
           if s["id"]==id:
               found=True
               students.remove(s)
               print("Student ID Succesfully Deleted !")

        if not found:
            print("Student Not Found !")

    elif choice == 5:

        subject={"Math","Science","English","Chemistry","Physics","Python","C-Programing","Gujrati"}


        print(subject)

    elif choice == 6:


        print("Thank You For Checking this Student Organizer !")
        break


              