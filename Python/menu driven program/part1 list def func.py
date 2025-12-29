# Hands-on exercise on List and its built-in methods (append, index, remove, sort)

# Task: Write a menu-driven program to create a Student Records Management System using
#               List and List methods
#  1. Add Student - Take name, roll number, subject and marks as input and store them in a list
#  2. Display students - show all stored students in a readable format
#  3. Search Student - Search for a student by roll number and display if found
#  4. update record - Update the marks of student using roll number
#  5. Delete Record - Delete a student record using roll number
#  6. Sort Record - Sorting students records by marks or name
#  7. Exit

# initalize list for store student record.
Record=[]
#now def function for each
def add_record():
    
    name=input("Enter the name")
    roll_no=input("Enter the roll no")
    course=input("Enter the course ")
    marks=int(input("Enter the Marks "))
    Record.append([name,roll_no,course,marks])
    
def Display_record():
    
    if Record:
        for i in Record:
            print("-------------------------")
            print(f"name:{i[0]}")
            print(f"Rollno:{i[1]}")
            print(f"course:{i[2]}")
            print(f"Marks:{i[3]}")
            print("-------------------------")
            
    else:
        print("-------------------------")
        print("list is Empty ")
        print("-------------------------")


def Search_record():
   
    if Record:
        roll_no=input("Enter the roll no :")
        for index,found in enumerate( Record):
           if roll_no==found[1]:
               return found,index
                
        return None,None 
    else:
        print("-------------------------")
        print("List is empty")
        print("-------------------------")
        return None,None
# for repeat user the menu we need loop so we done while loop because we didnot need to tell to run how many time.
while True:
    print(" 1. Add Student ")
    print(" 2. Display students ")
    print(" 3. Search Student")
    print("4. update record")
    print("5. Delete Record")
    print("6. sort Record")
    print("7. Exit")

    #declare variable which ask user to enter the choice.
    choice=input("Enter Your Choice :")
    #Add student.
    if choice=='1':
        add_record()
    # Display student
    if choice=='2':
       Display_record()
    # Search student:
    if choice=='3':
        student,_=Search_record()
        if student is not None:
            print("-------------------------")
            print(f"name:{student[0]}")
            print(f"Rollno:{student[1]}")
            print(f"course:{student[2]}")
            print(f"Marks:{student[3]}")
            print("-------------------------")
        else:
            print("-------------------------")
            print("Record not found")
            print("-------------------------")
                
    # update record:
    if choice=='4':
        record,idd=Search_record()
        if record is not None:
            Marks=int(input("Enter the Marks :"))
            Record[idd][3]=Marks
            print("-------------------------")
            print("Record updated Successfully")
            print("-------------------------")
        else:
            print("-------------------------")
            print("Record not found")
            print("-------------------------")
    # Delete record:
    if choice=='5':
        record,idx=Search_record()
        if record is not None:
            Record.remove(record)
            print("-------------------------")
            print("Successfully Deleted")
            print("-------------------------")
        else:
            print("-------------------------")
            print("Record not found")
            print("-------------------------")
    # Sort record:
    if choice=='6':
        if Record:
            s=input("Type 'Assending 'or 'Descending':")
            if s =='Descending':
                Record.sort(key=lambda x:x[3],reverse=True)
                print("-------------------------")
                print("Successfully Updated")
                print("-------------------------")
            if s=='Assending':
                Record.sort(key=lambda x:x[3],)
                print("-------------------------")
                print("Successfully Updated")
                print("-------------------------")
        else:
            print("-------------------------")
            print("Record is empty")
            print("-------------------------")
    # exist loop
    if choice=='7':
        break


