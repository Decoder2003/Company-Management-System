'''Developers:-  
   Name:- Krishna Aggarwal Class:- 12-A RollNo:- 16 
   Name:- Dhruv Kalra Class:- 12-A RollNo:- 10'''
'''File:- Sample Data (completed)'''

# IMPORTING ALL SUB_MODULES
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
        host='localhost', user=mysqlusr, passwd=mysqlpaswd) 
    mycursor = mydb.cursor()
except:
    print('ERROR: conection not sucsess...Pls check passwd/user/host or \
         other issues:')
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
    sampleSH = '''INSERT INTO STOCK_HOUSE VALUES
(1,'Techo core i3',9250,2200,'core i3-11154G:2/4 cores/threads:4.10-GHz Max Turbo Frequency'),
(2,'Techo core i5',14399,2200,'core i5-10504A:6/12 cores/threads:4.30-GHz Max Turbo Frequency'),
(3,'Techo core i7',25999,2200,'core i7-9700F:8/8 cores/threads:4.7-GHz Max Turbo Frequency'),
(4,'Techo Ram TCR2GB',564,5399,'TCRDDR2 800MHz'),
(5,'Techo Ram TCR4GB',1840,5399,'TCRDDR3 1600MHz'),
(6,'Techo Ram TCR8GB',3998,5399,'TCRDDR4 3200MHz'),
(7,'Techo Ram TCR16GB',5599,5399,'TCRDDR4 2666MHz'),
(8,'Techo A320M-S2H',4399,1807,'Supports 8gen+ processors:AM4 Socket:Ultra Durable Motherboard'),
(9,'Techo B450M-DS3H',7179,1200,'Supports 11gen+ processors:AM4 Socket:Gaming Motherboard'),
(10,'Techo Esports-130AG',2690,5080,'Supports HHD/SSD/PCI slots:Black Matte Finish'),
(11,'Techo Esports-225VG',4670,5080,'Supports RGB/SSD/PCLE slots:Tower Base'),
(12,'Techo Esports-780TF',5211,5080,'Supports Cooler/SSD/PCI slots:Gaming Cabinet'),
(13,'Techo HDD-M01TB',3381,7899,'3.5 Inch SATA 6Gb/s 7200 RPM 64 MB Cache'),
(14,'Techo HDD-M0500GB',1609,7899,'2.0 Inch SATA 4Gb/s 5400 RPM 16 MB Cache'),
(15,'Techo SSD-M0120GB',3381,7899,'2.5 Inch SATA 12Gb/s 8200 RPM 54 MB Cache'),
(16,'Techo SSD-M0240GB',2721,7899,'2.5 Inch SATA 12Gb/s 8200 RPM 64 MB Cache'),
(17,'Techo VP450P',2590,3560,'450 Watt Power Supply 85% efficient'),
(18,'Techo VP550P',3590,4760,'550 Watt Power Supply 75% efficient');'''
    try:
        print('\nCreating table for stock house details....')
        sleep(1)
        mycursor.execute('create table stock_house(ID integer primary key\
                            not null,NAME varchar(100), PERPC integer, \
                            AVAILABILITY integer, INFO varchar(250));')
        print('\nAdding sample data.......')
        try:
            mycursor.execute(sampleSH)
            mydb.commit()
        except:
            print('\n')
            
        print('Table successfully created.....')
    except:
        mydb.rollback()
        print('Table already present.....')
        print('Adding sample data.....')
        try:
            mycursor.execute(sampleSH)
            mydb.commit()
        except:
            print('\n')


    sampleBD = '''INSERT INTO BILLING_DETAILS VALUES
('2021-02-01','12:52:42',1,1,'Techo core i3',9250,1,0),
('2021-02-01','12:52:42',1,4,'Techo Ram TCR2GB',564,2,150),
('2021-02-01','12:52:42',1,9,'Techo B450M-DS3H',7179,1,230),
('2021-02-01','12:52:42',1,11,'Techo Esports-225VG',4670,1,19),
('2021-02-01','12:52:42',1,14,'Techo HDD-M0500GB',1609,1,10),
('2021-02-01','12:52:42',1,17,'Techo VP450P',2590,1,199),
('2021-02-02','18:45:12',2,2,'Techo core i5',14399,1,200),
('2021-02-02','18:45:12',2,5,'Techo Ram TCR4GB',1840,2,150),
('2021-02-02','18:45:12',2,9,'Techo B450M-DS3H',7179,1,30),
('2021-02-02','18:45:12',2,12,'Techo Esports-780TF',5211,1,190),
('2021-02-02','18:45:12',2,13,'Techo HDD-M01TB',3381,2,0),
('2021-02-02','18:45:12',2,18,'Techo VP550P',3590,1,199),
('2021-02-03','14:26:58',3,1,'Techo core i3',9250,1,0),
('2021-02-03','14:26:58',3,4,'Techo Ram TCR2GB',564,2,150),
('2021-02-03','14:26:58',3,8,'Techo A320M-S2H',4399,1,230),
('2021-02-03','14:26:58',3,11,'Techo Esports-225VG',4670,1,19),
('2021-02-03','14:26:58',3,14,'Techo HDD-M0500GB',1609,1,10),
('2021-02-03','14:26:58',3,17,'Techo VP450P',2590,1,199),
('2021-02-04','13:01:34',4,3,'Techo core i7',25999,1,0),
('2021-02-04','13:01:34',4,7,'Techo Ram TCR16GB',5599,1,120),
('2021-02-04','13:01:34',4,9,'Techo B450M-DS3H',7179,1,130),
('2021-02-04','13:01:34',4,11,'Techo Esports-130AG',2690,1,0),
('2021-02-04','13:01:34',4,16,'Techo SSD-M0120GB',2721,1,10),
('2021-02-04','13:01:34',4,18,'Techo VP550P',3590,1,199),
('2021-02-05','16:57:39',5,1,'Techo core i5',14399,1,0),
('2021-02-05','16:57:39',5,6,'Techo Ram TCR8GB',3998,2,10),
('2021-02-05','16:57:39',5,9,'Techo A320M-S2H',4399,1,230),
('2021-02-05','16:57:39',5,11,'Techo Esports-225VG',4670,1,99),
('2021-02-05','16:57:39',5,16,'Techo SSD-M0240GB',3871,1,0),
('2021-02-05','16:57:39',5,17,'Techo VP450P',2590,1,299);'''
    try:
        print('\nCreating table for billing details....')
        sleep(1)
        mycursor.execute('create table billing_details(BDATE date, BTIME \
            time,IN_ID integer not null, ID integer not null,NAME \
            varchar(100),AMOUNT integer,QTY integer not null, DIS integer\
            not null);')
        print('Adding sample data.....')
        try:
            mycursor.execute(sampleBD)
            mydb.commit()
        except:
            print('\n')
        mydb.commit()
        print('Table successfully created.....')
    except:
        mydb.rollback()
        print('Table already present.....')
        print('Adding sample data.....')
        try:
            mycursor.execute(sampleBD)
            mydb.commit()
        except:
            print('\n')


    try:
        print('\nCreating table for Account details....')
        sleep(1)
        mycursor.execute('create table account(ID integer primary key not\
            null,NAME varchar(20) not null,GENDER char(1), \
            EMAIL varchar(30) not null,PHONE varchar(11) not null,\
            COMPANY_NAME varchar(50) not null,COMPANY_ADD varchar(50) not \
            null,GSTIN varchar(20) not null,STATUS varchar(20) not null);')
        mydb.commit()
        print('Table successfully created.....')
    except:
        mydb.rollback()
        print('Table already present.....')

        print('\nSetting up files for Employee Details......')
        file_data=['ID','NAME','WORKING HOURS','SALARY','INFORMATION']
        with open('SampleData/Employee_details_sample.csv','r') as sampleEmp:
            readSample = csv.reader(sampleEmp)
            with open('Employee_details.csv','w') as file:
                wrt=csv.writer(file)
                wrt.writerows(readSample)

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
        mycursor.execute('create table billing_details_copy(CDATE date,\
            BDATE date,BTIME time,IN_ID integer not null, ID integer not\
            null, NAME varchar(100),AMOUNT integer,QTY integer not null,\
            DIS integer not null);')
        mydb.commit()
    except:
        mydb.rollback()
    try:
        mycursor.execute('create table stock_house_copy(CDATE date,ID \
                        integer not null,NAME varchar(100), PERPC \
                        integer,AVAILABILITY integer, INFO varchar(250)\
                        );')
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
        mycursor.execute('create table billing_details_bin(DDATE date,\
                        BDATE date,BTIME time,IN_ID integer not null,ID\
                        integer not null, NAME varchar(100),AMOUNT \
                        integer,QTY integer not null, DIS integer not\
                        null);')
        mydb.commit()
    except:
        mydb.rollback()
    try:
        mycursor.execute('create table stock_house_bin(DDATE date,ID \
                        integer not null,NAME varchar(100), PERPC \
                        integer,AVAILABILITY integer, INFO varchar(250)\
                        );')
        mydb.commit()
    except:
        mydb.rollback()
    
    
    print('\n Sample data added successfully!! \n')