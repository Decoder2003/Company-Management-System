"Developer: Krishna Aggarwal & Dhruv Kalra; Class-section: 12th-A; RollNo. : 16 & 10"
"Submodule:- Employee Details (completed)"

def run():
    from printing_tool import formatting
    import datetime
    date=datetime.date.today()
    def isNotEmpty():
        with open('Employee_details.csv','r') as file:
            read=csv.reader(file)
            file.seek(0)
            field=next(read)
            chk=0
            for i in read:
                if i==[]:
                    chk=1
                else:
                    chk=0
                    break
        if chk==0:
            return True
        else:
            return False
    def employee_details():
        ch='y'
        while ch=="Y" or ch=="y":
            mm.employee_menu()
            print('Enter your choice(1-6): ')
            c=input('➥ ')
            if c=='1':#To display all employee records.
                row=[]
                with open('Employee_details.csv','r') as file:
                    read=csv.reader(file)
                    if isNotEmpty():
                        file.seek(0)
                        field=next(read)
                        for i in read:
                            if i!=[]:
                                row.append(i)
                        formatting(field,row)
                        
                    else:
                        print('\nNO DATA EXIST...')
            elif c=='2':#To search for an employee.
                cont='y'
                while cont=='Y' or cont=='y':
                    row=[]
                    chk=0
                    with open('Employee_details.csv','r') as file:
                        read=csv.reader(file)
                        if isNotEmpty():
                            file.seek(0)
                            field=next(read)
                            while True:
                                try:
                                    emp_id=int(input(' Enter the employee id: '))
                                    emp_id = str(emp_id)
                                    break
                                except:
                                    print(' ::Invalid Value Input Detected::')
                            for i in read:
                                if i!=[]:
                                    if i[0]==emp_id:
                                        chk=1
                                        row.append(i)
                                        break
                                    else:
                                        chk=0
                                else:
                                    continue
                            if chk==1:
                                formatting(field,row)
                            else:
                                print(f' Employee with ID {emp_id} not found')
                            cont=input("Enter 'y' to display more data: ")
                        else:
                            print(' NO DATA EXIST...')
                            cont='n'
            elif c=='3':#To add an employee
                cont='y'
                while cont=='y' or cont=='Y':
                    while True:
                        try:
                            n=int(input('How many employees do you want to add?: '))
                            break
                        except:
                            print('::Invalid Value Input Detected::')
                    data=[]
                    file=open('Employee_details.csv','r')
                    read=csv.reader(file)
                    file.seek(0)
                    for i in read:
                        if i!=[]:
                            data.append(i)
                    try:
                        for i in range(n):
                            print('%d entries left to enter'%(n-i))
                            if isNotEmpty():
                                Id=int(data[-1][0])+1
                            else:
                                Id=1
                            file.close()
                            print('Employee ID:',Id)
                            name=input('Enter the name of employee: ')
                            wh=int(input('Enter working hours: '))
                            salary=int(input('Enter salary: '))
                            info=input('Enter some information: ')
                            print('**DATA SUCCESSFULLY ADDED**')
                            print('--------------')
                            data.append([str(Id),name,str(wh),str(salary),info])
                            with open('Employee_details.csv','w') as file:
                                write=csv.writer(file)
                                write.writerows(data)
                            
                    except:
                        print('::Invalid Value::')
                    cont=input("Enter 'y' to add more data: ")

            elif c=='4': #To update details
                cont='y'
                while cont=='y' or cont=="Y":
                    ck=0
                    data=[]
                    with open('Employee_details.csv','r') as file:
                            read=csv.reader(file)
                            if isNotEmpty():
                                file.seek(0)
                                field=next(read)
                                while True:
                                    try:
                                        emp_id=int(input('Enter employee id to edit: '))
                                        break
                                    except:
                                        print('Invalid value enterd!!')
                                for i in read:
                                    if i!=[]:
                                        data.append(i)
                                for i in data:
                                    if i[0]==str(emp_id):
                                        ck=1
                                        for j in range(len(field)-1):
                                            print(j+1,')',field[j+1])
                                        while True:  
                                            try:
                                                c=int(input('Enter column number to edit: '))
                                                break
                                            except:
                                                print('Invalid value entered!!')
                                        if c>=0 and c<=4:
                                            if c==1 or c==4:
                                                value=input('Enter new value: ')
                                                i[c]=value
                                            elif c==2 or c==3:
                                                while True:
                                                    try:
                                                        value=int(input('Enter new value: '))
                                                        i[c]=str(value)
                                                        break
                                                    except:
                                                        print('Invalid value enter again')
                                            with open('Employee_details.csv','w') as file:
                                                file=csv.writer(file)
                                                file.writerow(field)
                                                file.writerows(data)
                                                print('**DATA SUCCESSFULLY UPDATED**')
                                            break
                                        else:
                                            print('Column not found')
                                            break
                                    else:
                                        ck=0
                                if ck==0:
                                    print('Employee Not Found')
                                cont=input("Enter 'y' to update more details: ")
                            else:
                                print('\nNO DATA EXIST...')     
                                cont='n'
            elif c=='5': #To remove employee
                cont='y'
                ck=0
                while cont=='y' or cont=='Y':
                    data=[]
                    data2=[]
                    with open('Employee_details.csv','r') as file:
                            read=csv.reader(file)
                            if isNotEmpty():
                                while True:
                                    try:
                                        emp_id=int(input('Enter employee id to delete: '))
                                        break
                                    except:
                                        print('Invalid value!!')
                                file.seek(0)
                                for i in read:
                                    if i!=[]:
                                        if i[0]!=str(emp_id):
                                            ck=1
                                        else:
                                            ck=0
                                            break
                                if ck==0:
                                    file.seek(0)
                                    for i in read:
                                        if i!=[]:
                                            if i[0]!=str(emp_id):
                                                data.append(i)
                                            else:
                                                i=[str(date)]+i
                                                data2.append(i)
                                    with open('Employee_details_bin.csv','a') as file2:
                                        write=csv.writer(file2)
                                        write.writerows(data2)
                                    with open('Employee_details.csv','w') as file:
                                        write=csv.writer(file)
                                        write.writerows(data)
                                        print('**DATA SUCCESSFULLY REMOVED**')
                                else:
                                    print('Employee not found.')
                                cont=input("\nEnter 'y' to delete more data: ")
                            else:
                                print('\nNO DATA EXIST...')
                                cont='n'
            elif c=='6':
                print(' Going back.....')
                break
            else:
                try:
                    c=int(c)
                    print('::Invalid option::')
                except:
                    print('::Invalid Value Input Detected::')
            key = input('Press ENTER key to contniue:')
            print('')

    import csv
    import main_menu as mm
    from time import sleep
    employee_details()