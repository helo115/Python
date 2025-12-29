# Hands-on exercise on List and its built-in methods (append, index, remove, sort)

# Task: Write a menu-driven program to create a Student Records Management System using
#               List and Dic methods
#  1. Add Student - Take name, roll number, subject and marks as input and store them in a list
#  2. Display students - show all stored students in a readable format
#  3. Search Student - Search for a student by roll number and display if found
#  4. update record - Update the marks of student using roll number
#  5. Delete Record - Delete a student record using roll number
#  6. Sort Record - Sorting students records by marks or name
#  7. Exit

# initalize list for store student record.
dics=[]
# add function
def add_dic():
    n=input("Enter the name")
    r=input("Enter the roll no")
    c=input("Enter the course ")
    m=int(input("Enter the Marks "))
    dics.append({"name":n,"roll_no":r,"course":c,"marks":m})
        

# Display function
def Display_dics():
    
    if dics:
        for i in dics:
            print("-------------------------")
            print(f"name:{i['name']}")
            print(f"Rollno:{i['roll_no']}")
            print(f"course:{i['course']}")
            print(f"Marks:{i['marks']}")
            print("-------------------------")
    else:
        print("-------------------------")
        print("list is Empty ")
        print("-------------------------")
# Search Function
def Search_dics():
    if dics:
        roll_no=input("Enter the roll no :")
        for index,found in enumerate( dics):
           if roll_no==found['roll_no']:
               return found,index
                
        return None,None 
    else:
        print("-------------------------")
        print("List is empty")
        print("-------------------------")
        return None,None
    
# for repeat user the menu we need loop so we done while loop because we didnot need to tell to run how many time.
while True:
    print("1. Add Student ")
    print("2. Display students ")
    print("3. Search Student")
    print("4. update record")
    print("5. Delete Record")
    print("6. sort Record")
    print("7. Exit")

 #declare variable which ask user to enter the choice.
    choose=input("Enter Your Choose")
    #Add student.
    if choose=='1':
        add_dic()
    if choose=='2':
        Display_dics()
    if choose=='3':
        record,_=Search_dics()
        if record is not None:
            print("-------------------------")
            print(f"name:{record['name']}")
            print(f"Rollno:{record['roll_no']}")
            print(f"course:{record['course']}")
            print(f"Marks:{record['marks']}")
            print("-------------------------")
        else:
            print("-------------------------")
            print("Record not found")
            print("-------------------------")

    if choose=='4':
        record,index=Search_dics()
        if record is not None:
            marks=int(input("Enter the marks:"))
            dics[index]['marks']=marks
            print("-------------------------")
            print("Successfully updated")
            print("-------------------------")
        else:
            print("-------------------------")
            print("Record not found")
            print("-------------------------")
    if choose=='5':
        record,index=Search_dics()
        if record is not None:
            dics.remove(record)
            print("-------------------------")
            print("Successfully Deleted")
            print("-------------------------")
        else:
            print("-------------------------")
            print("Record not found")
            print("-------------------------")
    if choose=='6':
        if dics:
            st=input("Type 'Asscending'or'Descending':")
            if st=="Asscending":
                dics.sort(key=lambda x:x['marks'],)
                print("-------------------------")
                print("Successfully sorted")
                print("-------------------------")
            if st=='Descending':
                dics.sort(key=lambda x:x['marks'],reverse=True)
                print("-------------------------")
                print("Successfully updated")
                print("-------------------------")
        else:
            print("-------------------------")
            print("Record is empty")
            print("-------------------------")

    if choose=='7':
        break

