"Developer: Krishna Aggarwal & Dhruv Kalra; Class-section: 12th-A; RollNo. : 16 & 10"
"Submodule:- Setting_module (completed)"

import datetime
import csv
def copy_master(mydb,mycursor,table_name):
    copied_date = []
    mycursor.execute(f'SELECT * FROM {table_name}_copy;')
    data = mycursor.fetchall()
    for i in data:
        for j in i:
            copied_date.append(j)
            break
    mycursor.execute('SELECT CURDATE();')
    data = mycursor.fetchall()
    for i in data:
        for j in i:
            current_date = j
    length = len(copied_date)
    if copied_date == []:
        chk_copied_date = 0
    else:
        chk_copied_date = copied_date[length-1]
    query = f'SELECT * FROM {table_name};'
    mycursor.execute(query)
    data = mycursor.fetchall()
    if data!=[]:
        if current_date == chk_copied_date:
            mycursor.execute(f'DELETE FROM {table_name}_copy WHERE CDATE=\'{current_date}\';')
            mydb.commit()
    for i in data:
        query = f"INSERT INTO {table_name}_copy VALUES(\'{current_date}\',"
        sno = 0
        for j in i:
            sno += 1
            if sno == len(i):
                if type(j) == int:
                    query = query+str(j)+');'
                else:
                    query = query+"\'"+str(j)+"\'"+');'
            else:
                if type(j) == int:
                    query = query+str(j)+','
                else:
                    query = query+"\'"+str(j)+"\'"+','
        mycursor.execute(query)
        mydb.commit()

def bin_master(mydb,mycursor,data,table_name):
    mycursor.execute('SELECT CURDATE();')
    date_data = mycursor.fetchall()
    for i in date_data:
        for j in i:
            current_date = j
    for i in data:
        query = f"INSERT INTO {table_name}_bin VALUES(\'{current_date}\',"
        sno = 0
        for j in i:
            sno += 1
            if sno == len(i):
                if type(j) == int:
                    query = query+str(j)+');'
                else:
                    query = query+"\'"+str(j)+"\'"+');'
            else:
                if type(j) == int:
                    query = query+str(j)+','
                else:
                    query = query+"\'"+str(j)+"\'"+','
        mycursor.execute(query)
        mydb.commit()

def isNotEmpty(c='_copy'):
        with open(f'Employee_details{c}.csv','r') as file:
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

def copy_master_csv():
    data=[]
    cdata=[]
    date=str(datetime.date.today())
    file_data3=['CDATE','ID','NAME','WORKING HOURS','SALARY','INFORMATION']
    with open('Employee_details_copy.csv','r') as file:
        read=csv.reader(file)
        file.seek(0)
        field=next(read)
        for i in read:
            if i!=[]:
                data.append(i)
        if isNotEmpty():
            chk_date=data[-1][0]
        else:
            chk_date=0
        filec=open('Employee_details.csv','r')
        filec1=open('Employee_details_copy.csv','r')
        read=csv.reader(filec)
        readc=csv.reader(filec1)
        filec.seek(0)
        filec1.seek(0)
        field=next(filec)
        fieldc=next(filec1)
        for j in readc:
            if j!=[]:
                if date==chk_date:
                    if j[0]!=date:
                        cdata.append(j)
                else:
                    cdata.append(j)
        for i in read:
            if i!=[]:
                cdata.append([date]+i)
        with open('Employee_details_copy.csv','w') as file2:
            write=csv.writer(file2)
            write.writerow(file_data3)
            write.writerows(cdata)

def create_account(mydb,mycursor,cms=False):
    #CODE TO CREATE ACCOUNT
    primary_acc=True
    mycursor.execute('SELECT * FROM ACCOUNT;')
    data = mycursor.fetchall()

    if data==[]:
        if cms==False:
            print('\nNo account present currently..')
            print('CREATE AN ACCOUNT TO CONTINUE')
        else:
            primary_acc=False

    if primary_acc==False or cms==False:
        query='SELECT ID FROM ACCOUNT;'
        mycursor.execute(query)
        data=mycursor.fetchall()
        l_no=[]
        if data==[]:
            account_id='1'
        else:
            for i in data:
                l_no.append(i)
            length=len(l_no)
            result=l_no[length-1][0]
            result=int(result)
            result=str(result+1)
            account_id=result
        column = []
        query = f'DESC ACCOUNT;'
        mycursor.execute(query)
        data = mycursor.fetchall()
        for i in data:
            for j in i:
                column.append(j)
                break
        column = column[1:8]
        query = f'INSERT INTO ACCOUNT VALUES ({account_id},'
        print(' Account ID:',account_id)
        for i in range(1):
            no = 0
            for j in column:
                if j.upper()=='COMPANY_NAME':
                    query+='\'TECHNETIUMM\','
                elif j.upper()=='COMPANY_ADD':
                    query+='\'INDIA\','
                elif j.upper()=='GSTIN':
                    query+='\'03AADFG180E34\''
                else:
                    while True:
                        no += 1
                        if j.upper()=='GENDER':
                            value = input(' Enter GENDER(male[M]/female[F]/other[O]): ')
                        else:
                            value = input(f' Enter {j}: ')
                        if no == len(column):
                            if type(value) == str:
                                value=value.upper()
                                if j.upper()=='EMAIL':
                                    if '@' in value and '.' in value:
                                        query += f'\'{value}\''
                                        break
                                    else:
                                        print(' ::Invalid EMAIL::')
                                        no-=1
                                elif j.upper()=='PHONE':
                                    try:
                                        value = int(value)
                                        if len(str(value)) == 10:
                                            query += f'\'{value}\''
                                            break
                                        else:
                                            print(' ::Invalid PHONE NO::')
                                            no-=1
                                    except:
                                        print(' ::Invalid PHONE NO::')
                                        no-=1
                                elif j.upper()=='GENDER':
                                    if value == 'M' or value == 'F' or value == 'O':
                                        query += f'\'{value}\''
                                        break
                                    else:
                                        print(' ::Invalid GENDER::')
                                        no-=1
                                else:
                                    query += f'\'{value}\''
                                    break
                            else:
                                if j.upper()=='EMAIL':
                                    if '@' in value and '.' in value:
                                        query += f'\'{value}\''
                                        break
                                    else:
                                        print(' ::Invalid EMAIL::')
                                        no-=1
                                elif j.upper()=='PHONE':
                                    try:
                                        value = int(value)
                                        if len(str(value)) == 10:
                                            query += f'\'{value}\''
                                            break
                                        else:
                                            print(' ::Invalid PHONE NO::')
                                            no-=1
                                    except:
                                        print(' ::Invalid PHONE NO::')
                                        no-=1
                                else:
                                    query += f'{value}'
                                    break
                        else:
                            if type(value) == str:
                                value=value.upper()
                                if j.upper()=='EMAIL':
                                    if '@' in value and '.' in value:
                                        query += f'\'{value}\','
                                        break
                                    else:
                                        print(' ::Invalid EMAIL::')
                                        no-=1
                                elif j.upper()=='PHONE':
                                    try:
                                        value = int(value)
                                        if len(str(value)) == 10:
                                            query += f'\'{value}\','
                                            break
                                        else:
                                            print(' ::Invalid PHONE NO::')
                                    except:
                                        print(' ::Invalid PHONE NO::')
                                        no-=1
                                elif j.upper()=='GENDER':
                                    if value == 'M' or value == 'F' or value == 'O':
                                        query += f'\'{value}\','
                                        break
                                    else:
                                        print(' ::Invalid GENDER::')
                                        no-=1
                                else:
                                    query += f'\'{value}\','
                                    break
                            else:
                                if j.upper()=='EMAIL':
                                    if '@' in value and '.' in value:
                                        query += f'\'{value}\','
                                        break
                                    else:
                                        print(' ::Invalid EMAIL::')
                                        no-=1
                                elif j.upper()=='PHONE':
                                    try:
                                        value = int(value)
                                        if len(str(value)) == 10:
                                            query += f'\'{value}\','
                                            break
                                        else:
                                            print(' ::Invalid PHONE NO::')
                                    except:
                                        no-=1
                                else:
                                    query += f'{value},'
                                    break
            query += ',\'ACTIVE\');'
            print(' STATUS: ACTIVE')
        mycursor.execute(query)
        mydb.commit()
        mycursor.execute(f'UPDATE ACCOUNT SET STATUS=\'DEACTIVE\' WHERE ID<>{account_id};');mydb.commit()