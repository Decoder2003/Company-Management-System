"Developer: Krishna Aggarwal & Dhruv Kalra; Class-section: 12th-A; RollNo. : 16 & 10"
"Submodule:- Setting (completed)"

def run(mycursor, mydb):
    import main_menu
    from time import sleep
    import setting_module
    from printing_tool import formatting
    import csv
    cont = 'y'
    while cont == 'y':
        main_menu.setting_menu()
        print("Enter your choice(1-6): ")
        choice = input('➥ ')

        # ---/Account/--choice-->
        if choice == '1':
            print('\nAccount present-->')
            mycursor.execute('SELECT * FROM ACCOUNT;')
            data = mycursor.fetchall()
            L = []
            rows = []
            for i in data:
                for j in i:
                    L.append(j)
                rows.append(L)
                L = []
            if rows == []:
                print('No account currently.')
            else:
                column = []
                query = 'DESC ACCOUNT;'
                mycursor.execute(query)
                data = mycursor.fetchall()
                for i in data:
                    for j in i:
                        column.append(j)
                        break
                formatting(column, rows)

            inner_loop = 'y'
            while inner_loop == 'y':
                print('What you want?')
                print('1.Update status')
                print('2.Add account')
                print('3.Remove account')
                print('4.Back')
                print('Enter your choice(1-4):')
                choice = input('➥ ')

                # CODE TO UPDATE STATUS
                if choice == '1':
                    try:
                        value = input('Enter ACCOUNT ID:')
                        value=int(value);value=str(value)
                        mycursor.execute(f'SELECT * FROM ACCOUNT WHERE ID={value};')
                        data =mycursor.fetchall()
                        if data==[]:
                            print(f'::No ACCOUNT with ID {value}::')
                        else:
                            mycursor.execute(f'UPDATE ACCOUNT SET STATUS=\'ACTIVE\' WHERE ID={value};');mydb.commit()
                            mycursor.execute(f'UPDATE ACCOUNT SET STATUS=\'DEACTIVE\' WHERE ID<>{value};');mydb.commit()
                            print('STATUS UPDATED.')
                    except:
                        mydb.rollback()
                        print('::Invalid Value Input Detected::')
                    key = input('Press ENTER key to contniue:')
                    print('')

                # CODE TO ADD ACCOUNT
                elif choice == '2':
                    try:
                        setting_module.create_account(mydb,mycursor)    
                        inner_loop='n'
                    except:
                        print('::Something Went Wrong::Pls retry::')
                    key = input('Press ENTER key to contniue:')
                    print('')
                
                # CODE TO REMOVE ACCOUNT
                elif choice == '3':
                    try:
                        condition = input('Enter the ID:')
                        condition = int(condition);condition = str(condition)
                        mycursor.execute(f'SELECT STATUS FROM ACCOUNT WHERE ID={condition};')
                        data = mycursor.fetchall()
                        if data==[]:
                            print(f'::No ACCOUNT with ID {condition}::')
                        else:
                            for i in data:
                                for j in i:
                                    check_status=j
                            query = f'DELETE FROM ACCOUNT WHERE ID={condition};'
                            mycursor.execute(query)
                            mydb.commit()
                            print(f'**ACCOUNT WITH ID {condition} DELETED SUCCESSFULLY**')
                            if check_status.upper()=='ACTIVE':
                                mycursor.execute(f'SELECT * FROM ACCOUNT;')
                                data = mycursor.fetchall()
                                if data==[]:
                                    setting_module.create_account(mydb,mycursor)    
                                else:
                                    for i in  data:
                                        for j in i:
                                            account_id=j
                                            break
                                        break
                                    mycursor.execute(f'UPDATE ACCOUNT SET STATUS=\'ACTIVE\' WHERE ID={account_id};');mydb.commit()
                                    print('STATUS UPDATED.')
                    except:
                        print('::Invalid Value Input Detected::')
                    key = input('Press ENTER key to contniue:')
                    print('')
                # CODE TO GO BACK
                elif choice == '4':
                    inner_loop = 'n'
                    print('Going back...');sleep(1)
                    break
                else:
                    try:
                        choice=int(choice)
                        print('::Invalid option::')
                    except:
                        print('::Invalid Value Input Detected::')
                    key = input('Press ENTER key to contniue:')
                    print('')

        # ---/BackUp/--choice-->
        elif choice == '2':
            inner_loop = 'y'
            while inner_loop == 'y':
                print('Which you want?')
                print('1.Employee')
                print('2.Stock House')
                print('3.Billing')
                print('4.Back')
                print("Enter your choice(1-4): ")
                choice = input('➥ ')

                # CODE TO DISPLAY EMPLOYEE DETAILS BACKUP DATA
                if choice == '1':
                    inner_choice='y'
                    while inner_choice.upper()=='Y':
                        row=[]
                        with open('Employee_details_copy.csv','r') as file:
                            read=csv.reader(file)
                            if setting_module.isNotEmpty():
                                file.seek(0)
                                field=next(read)
                                value=input('Enter the DATE(YYYY-MM-DD): ')
                                for i in read:
                                    if i!=[]:
                                        if i[0]==value:
                                            row.append(i)
                                if row!=[]:
                                    formatting(field,row)
                                else:
                                    print(f'::No Backup found on DATE {value}::')

                                while True:
                                    inner_choice=input("Do you want to search more data(y/n)? ")
                                    if inner_choice.upper()=='Y':
                                        inner_choice='y'
                                        break
                                    elif inner_choice.upper()=='N':
                                        inner_choice='n';inner_loop='n'
                                        break
                                    else:
                                        print('::Invalid Option::')
                            else:
                                print('NO BACKUP')
                                inner_choice='n';inner_loop='n'
                    key = input('Press ENTER key to contniue:')
                    print('')

                # CODE TO DISPLAY STOCK HOUSE DETAILS BACKUP DATA
                elif choice == '2':
                    try:
                        inner_choice='y'
                        while inner_choice.upper()=='Y':
                            query = f'SELECT * FROM STOCK_HOUSE_COPY;'
                            mycursor.execute(query)
                            data = mycursor.fetchall()
                            if data==[]:
                                print('::NO BACKUP::')                            
                            else:
                                value = input('Enter the date (YYYY-MM-DD): ')
                                search_date=value
                                value = '\''+value+'\''
                                query = f'SELECT * FROM STOCK_HOUSE_COPY WHERE CDATE={value};'
                                mycursor.execute(query)
                                data = mycursor.fetchall()
                                L = []
                                row = []
                                for i in data:
                                    for j in i:
                                        L.append(j)
                                    row.append(L)
                                    L = []
                                if row == []:
                                    print(f'::No Backup found on {value}::')
                                else:
                                    row=[];date=[];new_L=[]
                                    date.append(search_date)
                                    for i in data:
                                        for j in i:
                                            L.append(j)
                                        L=L[1:]
                                        new_L=date+L
                                        row.append(new_L)
                                        L = []
                                    column = []
                                    query = 'DESC STOCK_HOUSE_COPY;'
                                    mycursor.execute(query)
                                    data = mycursor.fetchall()
                                    for i in data:
                                        for j in i:
                                            column.append(j)
                                            break
                                    formatting(column, row)
                            while True:
                                #continuation
                                inner_choice=input("Do you want to search more data(y/n)? ")
                                if inner_choice.upper()=='Y':
                                    inner_choice='y'
                                    break
                                elif inner_choice.upper()=='N':
                                    inner_choice='n';inner_loop='n'
                                    break
                                else:
                                    print('::Invalid Option::')
                    except:
                        print('::Invalid input detected::')
                    key = input('Press ENTER key to contniue:')
                    print('')

                # CODE TO DISPLAY BILLING DETAILS BACKUP DATA
                elif choice == '3':
                    try:
                        inner_choice='y'
                        while inner_choice.upper()=='Y':
                            query = f'SELECT * FROM BILLING_DETAILS_COPY;'
                            mycursor.execute(query)
                            data = mycursor.fetchall()
                            if data==[]:
                                print('::NO BACKUP::')                            
                            else:
                                value = input('Enter the Date(yyyy/mm/dd):')
                                search_date=value
                                value = '\''+value+'\''
                                query = f'SELECT * FROM BILLING_DETAILS_COPY WHERE CDATE={value};'
                                mycursor.execute(query)
                                data = mycursor.fetchall()
                                L = []
                                row = []
                                for i in data:
                                    for j in i:
                                        L.append(j)
                                    row.append(L)
                                    L = []
                                if row == []:
                                    print(f'::No Backup found on {value}::')
                                else:
                                    row=[];date=[]
                                    date.append(search_date)
                                    for i in data:
                                        for j in i:
                                            L.append(j)
                                        L=L[1:]
                                        new_L=date+L
                                        row.append(new_L)
                                        L = []
                                    column = []
                                    query = 'DESC BILLING_DETAILS_COPY;'
                                    mycursor.execute(query)
                                    data = mycursor.fetchall()
                                    for i in data:
                                        for j in i:
                                            column.append(j)
                                            break
                                    formatting(column, row)
                            while True:
                                #continuation
                                inner_choice=input("Do you want to search more data(y/n)? ")
                                if inner_choice.upper()=='Y':
                                    inner_choice='y'
                                    break
                                elif inner_choice.upper()=='N':
                                    inner_choice='n';inner_loop='n'
                                    break
                                else:
                                    print('::Invalid Option::')
                    except:
                        print('::Invalid input detected::Pls check::')
                    key = input('Press ENTER key to contniue:')
                    print('')

                # BACK
                elif choice == '4':
                    inner_loop = 'n'
                    print('Going back.....')
                else:
                    print('::Invalid option::')
                    key = input('Press ENTER key to contniue:')
                    print('')

        # ---/Bin/--choice-->
        elif choice == '3':
            inner_loop = 'y'
            while inner_loop == 'y':
                print('Which Bin you want to see?')
                print('1.Employee')
                print('2.Stock House')
                print('3.Billing')
                print('4.Back')
                print("Enter your choice(1-4): ")
                choice = input('➥ ')

                # CODE TO DISPLAY EMPLOYEE DETAILS BIN DATA
                if choice == '1':
                    row=[]
                    c='_bin'
                    with open('Employee_details_bin.csv','r') as file:
                        read=csv.reader(file)
                        if setting_module.isNotEmpty(c):
                            file.seek(0)
                            field=next(read)
                            for i in read:
                                if i!=[]:
                                    row.append(i)
                            formatting(field,row)
                            
                        else:
                            print('::NO DATA FOUND IN BIN::')
                    key = input('Press ENTER key to contniue:')
                    print('')

                # CODE TO DISPLAY STOCK HOUSE DETAILS BACKUP DATA
                elif choice == '2':
                    mycursor.execute('SELECT * FROM STOCK_HOUSE_BIN;')
                    data = mycursor.fetchall()
                    L = []
                    rows = []
                    for i in data:
                        for j in i:
                            L.append(j)
                        rows.append(L)
                        L = []
                    if rows == []:
                        print('::NO DATA FOUND IN BIN::')
                    else:
                        column = []
                        query = 'DESC STOCK_HOUSE_BIN;'
                        mycursor.execute(query)
                        data = mycursor.fetchall()
                        for i in data:
                            for j in i:
                                column.append(j)
                                break
                        formatting(column, rows)
                    key = input('Press ENTER key to contniue:')
                    print('')

                # CODE TO DISPLAY BILLING DETAILS BACKUP DATA
                elif choice == '3':
                    mycursor.execute('SELECT * FROM BILLING_DETAILS_BIN;')
                    data = mycursor.fetchall()
                    L = []
                    rows = []
                    for i in data:
                        for j in i:
                            L.append(j)
                        rows.append(L)
                        L = []
                    if rows == []:
                        print('::NO DATA FOUND IN BIN::')
                    else:
                        column = []
                        query = 'DESC BILLING_DETAILS_BIN;'
                        mycursor.execute(query)
                        data = mycursor.fetchall()
                        for i in data:
                            for j in i:
                                column.append(j)
                                break
                        formatting(column, rows)
                    key = input('Press ENTER key to contniue:')
                    print('')

                # BACK
                elif choice == '4':
                    inner_loop = 'n'
                    cont='y'
                    print('Going back....')
                else:
                    print('::Invalid option::')
                    key = input('Press ENTER key to contniue:')
                    print('')

        # ---/AboutUs/--choice-->
        elif choice == '4':
            with open('aboutUs.txt','r') as about:
                about.seek(0)
                r=about.read()
            print(r)
            print()
            key = input('Press ENTER key to contniue:')
            print('')

        #--/Factory Reset/--choice-->
        elif choice == '5':
            confirm=input('Confirm to reset(y/n):')
            if confirm.upper()=='Y':
                print('Ok! Resetting...')
                file_data=['ID','NAME','WORKING HOURS','SALARY','INFORMATION']#official
                file_data2=['DDATE','ID','NAME','WORKING HOURS','SALARY','INFORMATION']#bin
                file_data3=['CDATE','ID','NAME','WORKING HOURS','SALARY','INFORMATION']#copy
                mycursor.execute('TRUNCATE TABLE billing_details;');mydb.commit()
                mycursor.execute('TRUNCATE TABLE billing_details_copy;');mydb.commit()
                mycursor.execute('TRUNCATE TABLE billing_details_bin;');mydb.commit()
                mycursor.execute('TRUNCATE TABLE stock_house;');mydb.commit()
                mycursor.execute('TRUNCATE TABLE stock_house_copy;');mydb.commit()
                mycursor.execute('TRUNCATE TABLE stock_house_bin;');mydb.commit()
                with open('Employee_details.csv','w') as file1:
                    write=csv.writer(file1)
                    write.writerow(file_data)
                with open('Employee_details_copy.csv','w') as file1:
                    write=csv.writer(file1)
                    write.writerow(file_data3)
                with open('Employee_details_bin.csv','w') as file1:
                    write=csv.writer(file1)
                    write.writerow(file_data2)
                print('Software reset completed....')
                sleep(1)
            else:
                print('Aborting process....')
                sleep(1)
        
        # ---/Exit/--choice-->
        elif choice == '6':
            print('Going back....')
            sleep(2)
            cont = 'n'
        else:
            try:
                choice=int(choice)
                print('::Invalid option::')
            except:
                print('::Invalid Value Input Detected::')
            key = input('Press ENTER key to contniue:')
            print('')