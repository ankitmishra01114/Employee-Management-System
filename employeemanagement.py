import mysql.connector as a
con=a.connect(host="localhost", user="root", passwd="root", database="employee")
if con.is_connected():
    print("successfully connected \n")
else:
    print("error")
print("........................................................ Welcome to Employee Details ........................................................ \n")
c=con.cursor()


def new():
    a=int(input('Enter Employee Id :'))
    b=input('Enter Name :')
    c=input('Enter Date  of Birth :')
    d=int(input("Enter Employee's Contact Number:"))
    e=input('Enter Address of employee :')
    f=int(input("Enter Employee's Salary :"))
    val=(a,b,c,d,e,f)
    paas='insert into data values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(paas,val)
    con.commit()
    print("Data Entered successfully")
    print("........................................................................................................................................................")
    main()




def display():
    c.execute('select * from data;')
    d=c.fetchall()
   
    for i in d:
        print(i)
    print("........................................................................................................................................................")
    main()



    
def delete():
  
    a=int(input("Enter emoployee's id :"))
    b=(a,)
    c.execute('delete from data where emp_id =%s',b)
    con.commit()
    print("Data Deleted successfully")
    print("........................................................................................................................................................")
    main()



    
def asc():
    c.execute('SELECT * from data ORDER BY salary desc;')
    d=c.fetchall()
    for i in d:
        print(i)
    print("........................................................................................................................................................")
    main()



    

def update():
    a=input("Enter Employee ID :")
    b=input("Enter New Salary :")
    val=(b,a)
    c.execute('UPDATE data SET salary = %s WHERE emp_id = %s',val)
    con.commit()
    print("successfully updated ")
    print("........................................................................................................................................................")
    main()

def details():
    print('''\t\t Project Developed by \n\n\
             \t Name             Student ID
             \t Chandan          22051592
             \t Ankit Mishra     22050968
             ''')
    print("........................................................................................................................................................")
    print("\n")
    main()


def out():
    exit()
    

    
    
    
    
def main():
   
    print("""\t1. Add new employee details
    \t2. Display employee details
    \t3. Delete employee's data
    \t4. Arrange employee by salary
    \t5. Update salary
    \t6. Project Made By:
    \t7. Exit\n""")
    opt = int(input("\tEnter Task No. :"))
    print()
    print("........................................................................................................................................................")
    while True:
        if(opt==1):
            new()
        elif(opt==2):
            display()
        elif(opt==3):
            delete()
        elif(opt==4):
            asc()
        elif(opt==5):
            update()
        elif(opt==6):
            details()
            break
        elif(opt==7):
            out()
        else:
            print("Please enter valid input")
            break
main()
