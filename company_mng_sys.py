"Developer: Krishna Aggarwal & Dhruv Kalra; Class-section: 12th-A; RollNo. : 16 & 10"
"Submodule:- Company Management System (completed)"

# IMPORTING ALL SUB_MODULES
import main_menu
import employee_details
import billing
import printing_tool
import stock_house
import setting
from setting_module import copy_master, bin_master, copy_master_csv , create_account
import csv

# IMPORTING BUILT-IN MODULES
import mysql.connector
from time import sleep

# CREATING CONNECTION BTW DBMS
connection = 'y'
try:
    mysqlusr = input('Please enter your mysql user: ')
    mysqlpaswd = input('Please enter your mysql password: ')
    mydb = mysql.connector.connect(
        host='localhost', user=mysqlusr, passwd=mysqlpaswd)  # PUT YOUR SYSTEM PASSWD
    mycursor = mydb.cursor()
except:
    print('ERROR: conection not sucsess...Pls check passwd/user/host or other issues:')
    connection = 'n'

# CREATING/CHECKING DBMS
if connection == 'y':
    try:
        print('Creating company_mng_ sys database......')
        sleep(1)
        mycursor.execute('create database company_management_system;')
        mydb.commit()
        print('Database successfully created.')
    except:
        mydb.rollback()
        print('Database already present......')

    # Using company_management_system database---->
    mycursor.execute('use company_management_system;')

    try:
        print('\nCreating table for stock house details....')
        sleep(1)
        mycursor.execute('create table stock_house(ID integer primary key not null, \
                            NAME varchar(100), PERPC integer, \
                            AVAILABILITY integer, INFO varchar(250));')
        mydb.commit()
        print('Table successfully created.....')
    except:
        mydb.rollback()
        print('Table already present.....')
    try:
        print('\nCreating table for billing details....')
        sleep(1)
        mycursor.execute('create table billing_details(BDATE date, BTIME time,IN_ID integer not null, ID integer not null,NAME varchar(100), \
            AMOUNT integer,QTY integer not null, DIS integer not null);')
        mydb.commit()
        print('Table successfully created.....')
    except:
        mydb.rollback()
        print('Table already present.....')

    try:
        print('\nCreating table for Account details....')
        sleep(1)
        mycursor.execute('create table account(ID integer primary key not null,NAME varchar(20) not null,GENDER char(1), \
            EMAIL varchar(30) not null,PHONE varchar(11) not null,COMPANY_NAME varchar(50) not null,COMPANY_ADD varchar(50) not null,\
            GSTIN varchar(20) not null,STATUS varchar(20) not null);')
        mydb.commit()
        print('Table successfully created.....')
    except:
        mydb.rollback()
        print('Table already present.....')

    try:
        print('\nSetting up files for Employee Details......')
        file_data=['ID','NAME','WORKING HOURS','SALARY','INFORMATION']
        with open('Employee_details.csv','r') as file:
            read=csv.reader(file)
            file.seek(0)
            for i in read:
                if i==file_data:
                    break
                else:
                    with open('Employee_details.csv','w') as file:
                        wrt=csv.writer(file)
                        wrt.writerow(file_data)
    except:
        with open('Employee_details.csv','w') as file:
            wrt=csv.writer(file)
            wrt.writerow(file_data)

    # CODE TO CREATE BACKUP TABLES
    print('\nSetting up back up files', end='')
    for i in range(5):
        print('.', end='')
        sleep(0.1)
    print()

    try:
        file_data3=['CDATE','ID','NAME','WORKING HOURS','SALARY','INFORMATION']
        with open('Employee_details_copy.csv','r') as file3:
            read3=csv.reader(file3)
            file3.seek(0)
            
            for i in read3:
                if i==file_data3:
                    break
                else:
                    with open('Employee_details_copy.csv','w') as file:
                        wrt=csv.writer(file)
                        wrt.writerow(file_data3)
    except:
        
        with open('Employee_details_copy.csv','w') as file3:
            wrt=csv.writer(file3)
            wrt.writerow(file_data3)

    try:
        mycursor.execute('create table billing_details_copy(CDATE date,BDATE date, BTIME time,IN_ID integer not null, ID integer not null, NAME varchar(100),\
            AMOUNT integer,QTY integer not null, DIS integer not null);')
        mydb.commit()
    except:
        mydb.rollback()
    try:
        mycursor.execute('create table stock_house_copy(CDATE date,ID integer not null, \
                            NAME varchar(100), PERPC integer, \
                            AVAILABILITY integer, INFO varchar(250));')
        mydb.commit()
    except:
        mydb.rollback()
    
    # CODE TO CREATE BIN TABLES
    print('Setting up bin files', end='')
    for i in range(5):
        print('.', end='')
        sleep(0.1)
    print()

    try:
        file_data2=['DDATE','ID','NAME','WORKING HOURS','SALARY','INFORMATION']
        with open('Employee_details_bin.csv','r') as file2:
            read2=csv.reader(file2)
            file2.seek(0)
            
            for i in read2:
                if i==file_data2:
                    break
                else:
                    with open('Employee_details_bin.csv','w') as file:
                        wrt=csv.writer(file)
                        wrt.writerow(file_data2)
    except:
        
        with open('Employee_details_bin.csv','w') as file2:
            wrt=csv.writer(file2)
            wrt.writerow(file_data2)

    try:
        mycursor.execute('create table billing_details_bin(DDATE date,BDATE date,BTIME time,IN_ID integer not null,ID integer not null, NAME varchar(100),\
            AMOUNT integer,QTY integer not null, DIS integer not null);')
        mydb.commit()
    except:
        mydb.rollback()
    try:
        mycursor.execute('create table stock_house_bin(DDATE date,ID integer not null, \
                            NAME varchar(100), PERPC integer, \
                            AVAILABILITY integer, INFO varchar(250));')
        mydb.commit()
    except:
        mydb.rollback()

# CODE TO SETUP APPLICATION/ACCOUNT
    print('\nSetting up the application...')
    create_account(mydb,mycursor,cms=True)
    print('Setup Completed.')

    # MAIN MENU_DRIVEN PROGRAM
    cont = 'y'
    while cont == 'y' and connection == 'y':
        main_menu.main_menu()
        print("Enter your choice(1-5): ")
        choice = input('➥ ')
        if choice == '1':
            print('\n Showing employee_details sub menu...')
            sleep(2)
            employee_details.run()
        elif choice == '2':
            print('\n Showing stock house sub menu...')
            sleep(2)
            stock_house.run(mycursor, mydb)
        elif choice == '3':
            print('\n Showing billing sub menu...')
            sleep(2)
            billing.run(mycursor, mydb)
        elif choice == '4':
            print('\n Showing Setting sub menu...')
            sleep(2)
            setting.run(mycursor, mydb)
        elif choice == '5':
            print(' YOU CHOOSE TO EXIT...')
            sleep(0.5)
            print('Creating backup files.....')
            # CODE TO BACK UP DATA
            table_name = 'stock_house'
            copy_master(mydb, mycursor, table_name)
            table_name = 'billing_details'
            copy_master(mydb, mycursor, table_name)
            copy_master_csv()
            sleep(0.5)
            print('Logging off...')
            sleep(1)
            # print('\n\nCredits:-')
    #         print('''NAME OF DEVELOPERS: DHRUV KALRA AND KRISHNA AGGARWAL 
    # ROLL NOS: 10 & 16
    # SCHOOL: RYAN INTERNATIONAL SCHOOL, MAYUR VIHAR - III''')
            sleep(0.1)
            print('Shutting down...')
            sleep(2)
            print('Exit process successful!!')
            sleep(1)
            print('Powered by Technetiumm.')
            cont = 'n'
        else:
            try:
                choice=int(choice)
                print('::Invalid Option::')
            except:
                print('::Invalid Value Input Detected::')
            key = input('Press ENTER key to contniue:')
            print('')
    if connection == 'y':
        mycursor.close()
        mydb.close()