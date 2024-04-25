"Developer: Krishna Aggarwal & Dhruv Kalra; Class-section: 12th-A; RollNo. : 16 & 10"
"Submodule:- Stock House (completed)"

def run(mycursor,mydb):
    from printing_tool import formatting
    import main_menu as mm
    from time import sleep
    from setting_module import copy_master, bin_master
    ch='y'
    switch=0
    zw=0
    c=0
    prsnt=0
    addi=0
    while ch=='y':
        if switch==0:
            sw=1
            mm.stock_house_menu()
            print('Enter your choice(1-5):')
            c=input('➥ ')
        if c=='1' or switch==1:#to search for items
            try:
                field1=[]
                mycursor.execute('Select * from stock_house;')
                fetch=mycursor.fetchall()
                mycursor.execute('Desc stock_house;')
                fetch2=mycursor.fetchall()
                for i in fetch2:
                    for j in i:
                        field1.append(j)
                        break
                if fetch==[]:
                    print('NO DATA EXIST...')
                    switch=0
                else:
                    z=input('Do you want to display all the records(y/n)?:')
                    if z=='y' or z=='Y':
                        formatting(field1,fetch)
                    elif z=='n' or z=='N':
                        item_id=int(input(' Enter item id to be searched:'))
                        for d in fetch:
                            if item_id!=d[0]:
                                prsnt=0
                            else:
                                prsnt=1
                                break
                        if prsnt==0:
                            print(f' ::Item with ID {item_id} is not present::')
                        else:
                            mycursor.execute(f'Select * from stock_house where ID={item_id};')
                            fetch=mycursor.fetchall()
                            formatting(field1,fetch)
                        again=input('Do you want to display more records(y/n)?:')
                        if again=='y' or again=='Y':
                            switch=1
                            pass
                        else:
                            switch=0
                            pass
                    else:
                        print('::Invalid Option::')
                        switch=1
                        pass
                c=0
            except:
                print('::Invalid Value Input Detected::')
                switch=1
                pass
        elif c=='2' or switch==2:# to add  item
            ID=1
            while True:
                try:
                    n=int(input('How many items do you want to add?'))
                    break
                except:
                    print('::Invalid Value Input Detected::')
            while addi<n:
                if zw==0:                    
                        mycursor.execute('Select * from stock_house;')
                        fetch=mycursor.fetchall()
                        item_id=ID
                        if fetch==[]:
                            zw=1
                        else:
                            for j in fetch:
                                if item_id==j[0]:
                                    ID+=1
                                    zw=0
                                    break
                                else:
                                    zw=1
                if zw==1:
                    name=input(' Enter name:')
                    while True:
                        try:
                            ava=int(input(' Enter availability of the product:'))
                            break
                        except:
                            print('::Invalid Value Input Detected::')
                    while True:
                        try:
                            perpc=int(input(' Enter cost per peice:'))
                            break
                        except:
                            print('::Invalid Value Input Detected::')
                    info=input(' Enter information about the item:')
                    mycursor.execute(f'insert into stock_house values({item_id},\'{name}\',{perpc},{ava},\'{info}\');')
                    mydb.commit()
                    print('**ITEM SUCCESSFULLY INSERTED BY THE NAME OF'+name+'**')
                    addi+=1
                    print('Records left to entered:',n-addi)
                    zw=0
            again=input('Do you want to add more records(y/n)?:')
            addi=0
            if again=='y' or again=='Y':
                switch=2
                zw=0
                pass
            else:
                switch=0
            c=0
        elif c=='3' or switch==3:#update an item
            try:
                mycursor.execute('select * from stock_house;')
                fetch=mycursor.fetchall()
                if fetch==[]:
                    print('NO DATA EXIST...')
                    switch=0
                else:
                    Id=int(input(' Enter the item id:'))
                    for d in fetch:
                            if Id!=d[0]:
                                prsnt=0
                            else:
                                prsnt=1
                                break
                    if prsnt==0:
                        print(f' ::Item with ID {Id} record is not present::')
                        switch=3
                        pass
                    else:
                        print(' Enter column to be edited')
                        print(" 1.Name")
                        print(" 2.Cost per piece")
                        print(" 3.Availability")
                        print(" 4.Information")
                        column=int(input('  Enter column number:'))
                        value=input('  Enter value:')
                        if column==1:
                            mycursor.execute(f'Update stock_house set NAME=\'{value}\' where ID={Id};')
                        elif column==2:
                            mycursor.execute(f'Update stock_house set PERPC={value} where ID={Id};')
                        elif column==3:
                            mycursor.execute(f'Update stock_house set AVAILABILITY={value} where ID={Id};')
                        elif column==4:
                            mycursor.execute(f'Update stock_house set INFO=\'{value}\' where ID={Id};')
                        mydb.commit()
                        print('**RECORD SUCCESSFULLY UPDATED**')
                        again=input('Do you want to update more records(y/n)?:')
                        if again=='y' or again=='Y':
                            switch=3
                            pass
                        else:
                            switch=0
                        c=0
            except:
                mydb.rollback()
                print('::Invalid Value Input Detected::')
                switch=3
                pass
        elif c=='4' or switch==4:#remove an item
            try:
                mycursor.execute('select * from stock_house;')
                fetch=mycursor.fetchall()
                if fetch==[]:
                    print('NO DATA EXIST...')
                    switch=0
                else:
                    if sw==1:
                        y=input('Do you want to delete all the records(y/n)?:')
                    if y=='y' or y=='Y':
                        #BIN_MASTER
                        table_name='stock_house'
                        bin_master(mydb,mycursor,fetch,table_name)
                        mycursor.execute('truncate stock_house;')
                        print("**ALL RECORDS HAVE BEEN SUCCESSFULLY DELETED**")
                        addi=0

                    elif y=='n' or y=='N' or  sw==0:
                        Id=int(input(' Enter ID of the item to be deleted:'))
                        mycursor.execute(f'select * from stock_house where id={Id}')
                        mce=mycursor.fetchall()
                        if mce==[]:
                            print(f'::No Data with ID {Id} Present::')
                        else:
                            #BIN_MASTER
                            table_name='stock_house'
                            bin_master(mydb,mycursor,mce,table_name)
                            mycursor.execute(f'delete from stock_house where id={Id}')
                            mydb.commit()
                            print("**RECORD HAVE BEEN SUCCESSFULLY DELETED**")
                            addi=0
                        again=input('Do you want to delete more records(y/n)?:')
                        if again=='y' or again=='Y':
                            sw=0
                            switch=4
                            pass
                        elif again=='n' or again=='N':
                            switch=0
                        else:
                            print('::Invalid Value Input Detected::')
                            switch=0
                            pass
                    else:
                        print('::Invalid Option::')
                        switch=4
                        pass
                c=0
            except:
                mydb.rollback()
                print('::Invalid Value Input Detected::')
                switch=4
                pass
        elif c=='5':#back to main menu
            print(' Going back....')
            ch='n'
            switch=1
        else:
            print('::Invalid Value Input Detected::')
            switch=0
            pass
        if switch==0:
            key = input('Press ENTER key to contniue:')
            print('')
            ch='y'
            switch=0