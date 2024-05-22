import mysql.connector

# Global Variable for Report
Clg_name = 'Vidyalankar School of Information Technology'
Clg_Add = 'Wadala'
Clg_Email = 'principle@vsit.edu.in'
Clg_Phone = '123456789'

#conn = mysql.connector.connect(host="localhost",user="root",password="@omkar22")
#cursor = conn.cursor()
#cursor.execute("CREATE DATABASE ReportCard")

def clear():
    for _ in range(65):
        print()

def add_student():
    conn = mysql.connector.connect(host='localhost', database='ReportCard', user='root', password='@omkar22')
    cursor = conn.cursor()
    clear()
    print('Add New Student Screen')
    print('-' * 120)
    name = input('Enter Student Name: ')
    roll_no = input('Enter Student Roll No: ')
    clas = input('Enter Student Class: ')
    division = input('Enter Student Division: ')
    sql = 'INSERT INTO student (Name, Roll_no, Class, Division, Status) VALUES \
        ("' + name + '","' + roll_no + '","' + clas + '","' + division + '","active");'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n New Student Added Successfully.....')
    wait = input('\n\n\nPress any key to Continue...')

def add_marks():
    conn = mysql.connector.connect(host='localhost', database='ReportCard', user='root', password='@omkar22')
    cursor = conn.cursor()
    clear()
    print('Add New Marks Screen')
    print('-' * 120)
    roll_no = input("Enter Roll no: ")
    Semester = input("Enter Semester: ")
    Session = input("Enter Session: ")
    division = input('Enter Division: ')
    PP = input('Enter marks in PP: ')
    DS = input("Enter marks in DS: ")
    DBMS = input('Enter marks in DBMS: ')
    CN = input("Enter marks in CN: ")
    AM = input('Enter marks in AM: ')
    sql = 'INSERT INTO marks(Roll_no, Division,Semester, Session,PP, DS, DBMS, CN, AM)  VALUES (' \
          +roll_no + ',"'+division+'","' + Semester + '","' +Session+'",'+ PP + ',' + DS + ',' + DBMS + ',' + CN + ',' + AM + ');'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n New Marks added successfully.....')
    wait = input('\n\n\nPress any key to continue....')

def modify_student():
    conn = mysql.connector.connect(host='localhost', database='ReportCard', user='root', password='@omkar22')
    cursor = conn.cursor()
    clear()
    print('Modify Student Information - Screen')
    print('-' * 120)
    roll_no = input('Enter Student Roll No: ')
    print('\n1.   Name   ')
    print('\n2.   Class   ')
    print('\n3.   Division   ')
    print('\n\n')
    choice = int(input('Enter Your Choice: '))
    field = ''
    if choice == 1:
        field = 'name'
    if choice == 2:
        field = 'class'
    if choice == 3:
        field = 'division'
    value = input("Enter new Value: ")
    sql ='UPDATE student set '+field+' ="'+value+'" WHERE roll_no ='+roll_no+';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n Student Record Updated.....')
    wait = input('\n\n\nPress any key to continue.....')

def modify_marks():
    conn = mysql.connector.connect(host='localhost', database='ReportCard', user='root', password='@omkar22')
    cursor = conn.cursor()
    clear()
    print('Modify Marks - Screen')
    print('-'*120)
    roll_no = input('Enter Student Roll_no: ')
    print('\n1.   PP   ')
    print('\n2.   DS   ')
    print('\n3.   DBMS   ')
    print('\n4.   CN   ')
    print('\n5.   AM   ')
    print('\n\n')
    choice = int(input('Enter your choice: '))
    field=''
    if choice == 1:
        field ='PP'
    if choice == 2:
        field = 'DS'
    if choice == 3:
        field = 'DBMS'
    if choice == 4:
        field = 'CN'
    if choice == 5:
        field = 'AM'

    value = input('Enter new value: ')
    sql = 'UPDATE marks set '+field+' ="'+value + '"WHERE roll_no = '+roll_no+';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n Marks Updated Successfully.....')
    wait = input('\n\nPress any key to continue.....')

def search_student(field):
    conn = mysql.connector.connect(host='localhost', database='ReportCard', user='root', password='@omkar22')
    cursor = conn.cursor()
    sql = ' SELECT * from student WHERE '
    msg ='Enter '+field+' :'
    value =input(msg)
    if field == 'roll_no':
        sql =sql +field+'='+value+';'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Student for '+field+' :'+value)
    print('-' * 120)
    for record in records:
        print(record)
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')

def search_marks():
    conn = mysql.connector.connect(host='localhost', database='ReportCard', user='root', password='@omkar22')
    cursor=conn.cursor()
    roll_no=input('Enter Roll_no: ')
    Session=input('Enter Session: ')
    sql='SELECT * FROM marks WHERE Roll_no = '+roll_no+' AND Session = "'+Session+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for Roll_no :'+roll_no+' Session : '+Session)
    print('-'*120)
    for record in records:
        print(record)
    conn.close()
    wait = input('\n\n\n Press any key to continue.....')

def search_menu():
    while True:
        clear()
        print('  S E A R C H   M E N U   ')
        print('-'*120)
        print("\n1.  Roll_no")
        print("\n2.  Student Term Marks")
        print("\n3.  Back to main menu")
        print('\n\n')
        choice=int(input("Enter your Choice...."))
        field=''
        if choice == 1:
            field='roll_no'
            search_student(field)
        if choice == 2:
            search_marks()
        if choice == 3:
            break

def report_single_term():
    conn = mysql.connector.connect(host='localhost', database='ReportCard', user='root', password='@omkar22')
    cursor = conn.cursor()
    roll_no = input("Enter Student Roll_no : ")
    Session = input("Enter Session : ")
    Semester = input("Enter Semester : ")
    sql = 'SELECT student.roll_no, name, PP, DS, DBMS, CN, AM from  \
          student, marks WHERE student.roll_no = marks.roll_no and \
          student.roll_no = '+roll_no
    cursor.execute(sql)
    record = cursor.fetchone()
    conn.commit()
    clear()
    print(f"\t\t\t\t\t{Clg_name}")
    print(f"{Clg_Add}")
    print('Phone :', Clg_Phone, ' Email: ', Clg_Email)
    print('-'*120)
    print('Name : ', record[1], ' Roll_no : ', record[0])
    print('Session : ', Session, ' Semester : ', Semester)
    print('-'*120)
    print('Subject', ' Max_marks', '  Min_marks', '   Marks Obtained')
    print('PP', ' \t  100', ' \t\t\t33\t', '\t\t\t',record[2])
    print('DS', ' \t  100', ' \t\t\t33\t', '\t\t\t',record[3])
    print('DBMS', ' \t  100', ' \t\t\t33\t','\t\t\t',record[4])
    print('CN', ' \t  100', ' \t\t\t33\t', '\t\t\t',record[5])
    print('AM', ' \t  100', ' \t\t\t33\t','\t\t\t',record[6])
    print('-'*120)
    total = record[2]+record[3]+record[4]+record[5]+record[6]
    percentage = total*100/500
    print('Total Marks : ', total, ' Percentage : ', percentage)
    conn.close()
    wait = input('\n\n\n Press any key to continue.....')

def report_menu():
    while True:
        clear()
        print(' R E P O R T   M E N U ')
        print("\n1. Student Report Card")
        print("\n2. Back to Main Menu")
        print("\n\n")
        choice = int(input("Enter your Choice: "))
        if choice == 1:
            report_single_term()
        if choice == 2:
            break

def main_menu():
    while True:
        clear()
        print(' R E P O R T   C A R D   M E N U  ')
        print("\n1. Add Student")
        print("\n2. Modify Student Record")
        print("\n3. Add Marks")
        print("\n4. Modify Marks")
        print("\n5. Search Menu")
        print("\n6. Report Menu")
        print("\n7. Close Application")
        print('\n\n')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        if choice == 2:
            modify_student()
        if choice == 3:
            add_marks()
        if choice == 4:
            modify_marks()
        if choice == 5:
            search_menu()
        if choice == 6:
            report_menu()
        if choice == 7:
            break

if __name__ == "__main__":
    main_menu()
