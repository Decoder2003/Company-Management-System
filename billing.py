"Developer: Krishna Aggarwal & Dhruv Kalra; Class-section: 12th-A; RollNo. : 16 & 10"
"Submodule:- Billing (completed)"

def run(mycursor,mydb):
    import billing_module
    import datetime
    import main_menu as menu
    from time import sleep
    from setting_module import bin_master

    cont='y'
    while cont=='y':
        menu.billing_menu()
        print("Enter your choice(1-4): ")
        choice=input('➥ ')
        
        #Creates gst bills.
        if choice=='1':
            loop_0='y'
            while loop_0=='y':
                #Gives current date
                date=datetime.date.today()
                #Give current time
                time=datetime.datetime.now()
                hour,minute,sec=time.hour,time.minute,time.second
                loop='y'
                step1,step2,step3=True,True,True
                l_name,l_stock,l_amount,l_qty,l_dis,l_id=[],[],[],[],[],[]
                sno=0
                invoice_no=billing_module.invoice_no_generator(mydb,mycursor)
                while loop=='y':
                    if step2==True and step3==True:
                        try:
                            sno+=1
                            product_ID=input('Enter the product ID: ')
                            product_ID=int(product_ID)
                            query=f"select * from stock_house where ID={product_ID};"
                            mycursor.execute(query)
                            data1 = mycursor.fetchall()
                            if data1==[]:
                                print(f'::Product with ID {product_ID} not available::')
                                step1=False;sno-=1
                            else:
                                for(ID,NAME,PERPC,AVIALABILITY,INFO) in data1:
                                    name=NAME
                                    stock=AVIALABILITY
                                    amount=PERPC
                                    print('  NAME->',name,'\n  STOCK->',stock,'\n  AMOUNT->',amount)
                                    l_name.append(name);l_stock.append(stock);l_amount.append(amount)
                                l_id.append(product_ID)
                                step1=True
                        except:
                            mydb.rollback()
                            print('::Invalid Value Input Detected::')
                            step1=False;sno-=1
                    if step1==True and step3==True:
                        try:
                            qty=int(input('Enter the quantity: '));step2=True
                            l_qty.append(qty)
                            if qty>stock:
                                print("::Quantity not valid::It exceed the Availability::Pls enter again::")
                                step2=False
                                l_qty.pop(sno-1)
                        except:
                            print('::Invalid Value Input Detected::')
                            step2=False
                    if step1==True and step2==True:
                        try:
                            dis=int(input('Enter the Discount: '));step3=True
                            l_dis.append(dis)
                            if dis>amount:
                                    print("::Discount not valid::It exceed the cost::Pls enter again::")
                                    step3=False
                                    l_dis.pop(sno-1)
                        except:
                            print('::Invalid value input Detected::')
                            step3=False
                    try:
                        loop=input('Press ANY key to continue or type E/e to quit: ')
                        if loop=='e' or loop=='E' or loop=='exit':
                            print('ok!');sleep(1)
                        else:
                            loop='y'
                    except:
                        loop='y'

                #Prints the invoice in 3 parts (layout1,layout2,layout3)
                if l_name!=[] and l_amount!=[] and l_qty!=[] and l_dis!=[] and sno!=0:
                    print('Creating your bill....');sleep(1)
                    rows=[]
                    for i in range(0,len(l_name)):
                        rows.append([i+1,l_name[i],l_amount[i],l_qty[i],l_dis[i]])
                    # print(rows)
                    field1=['S.No.','Product Name','Quantity','Cost Price','Discount']
                    billing_module.formatting(field1,rows,chk=1)
                    billing_module.bill_layout1(mycursor,mydb,hour,minute,sec,date,invoice_no)
                    billing_module.billing_layout2(rows,l_name,l_amount,l_qty,l_dis,sno)

                    #Totaling Amount
                    sub_total=0
                    Sub_total_discount=0
                    for i in range(sno):
                        cp=l_amount[i]*l_qty[i]
                        discount=l_dis[i]*l_qty[i]
                        Sub_total_discount+=l_dis[i]*l_qty[i]
                        sub_total+=cp
                        sub_total-=discount
                    billing_module.billing_layout3(sno,sub_total,Sub_total_discount)

                    #Bill_saving CODE
                    try:
                        billing_module.bill_saving(invoice_no,l_id,l_name,l_qty,l_dis,sno,l_amount,date,hour,minute,sec,mydb,mycursor)
                        #Updating Stock_house
                        for i in  range(sno):
                            product=l_name[i];product='\''+product+'\''
                            new_qty=l_stock[i]-l_qty[i]
                            query=f'update stock_house set availability={new_qty} where name={product}'
                            mycursor.execute(query)
                            mydb.commit()

                    except:
                        mydb.rollback()
                        print('\nBill record not saved....')
                        break
                        
                else:
                    print('::Aborting Process::Details are not complete for creating bill........')

                while True:
                    loop_0=input('\nDo you want to create more bills[y/n]?')
                    if loop_0.lower()=='y':
                        loop_0='y';break
                    elif loop_0.lower()=='n':
                        loop_0='n';break
                    else:
                        print('::Invalid Option::')

        #Search an invoice record.
        elif choice=='2':
            mycursor.execute('SELECT * FROM BILLING_DETAILS;')
            data = mycursor.fetchall()
            if data == []:
                loop2='n'
                print('NO DATA EXIST...')
            else:
                loop2='y'
            while loop2=='y':
                l_name,l_stock,l_amount,l_qty,l_dis,l_id=[],[],[],[],[],[]
                sno=0;
                NR=False
                try:
                    E_name=input('Enter the BILL ID: ')
                    #Extracting data from billing_details.
                    query=f"select * from billing_details where IN_ID={E_name};"
                    mycursor.execute(query)
                    data_0=mycursor.fetchall()
                    if data_0==[]:
                        print(f" No invoice record with ID-{E_name}....")
                        NR=True
                    else:
                        for i in data_0:
                            sno+=1
                            product_ID=i[3]
                            time=i[1]
                            invoice_no=i[2]
                            product_name=i[4]
                            amount=i[5]
                            qty=i[6]
                            dis=i[7]
                            date=i[0]

                            l_name.append(product_name);l_amount.append(amount);l_id.append(product_ID)
                            l_qty.append(qty);l_dis.append(dis)
                except:
                    mydb.rollback()
                    print('::Invalid value input detected::')
                    sleep(1)
                    break
                
                #Prints the invoice in 3 parts (layout1,layout2,layout3)
                if l_name!=[] and l_amount!=[] and l_qty!=[] and l_dis!=[] and sno!=0:
                    field1=['S.No.','Product Name','Quantity','Cost Price','Discount']
                    data_1=[]
                    for i in range(0,len(l_name)):
                        data_1.append([i+1,l_name[i],l_amount[i],l_qty[i],l_dis[i]])
                    billing_module.formatting(field1,data_1,chk=1)
                    billing_module.bill_layout1_for_c2(mycursor,mydb,time,date,invoice_no)
                    billing_module.billing_layout2(data_1,l_name,l_amount,l_qty,l_dis,sno)

                    #Totaling Amount
                    sub_total=0
                    Sub_total_discount=0
                    for i in range(sno):
                        cp=l_amount[i]*l_qty[i]
                        discount=l_dis[i]*l_qty[i]
                        Sub_total_discount+=l_dis[i]*l_qty[i]
                        sub_total+=cp
                        sub_total-=discount
                    billing_module.billing_layout3(sno,sub_total,Sub_total_discount)

                else:
                    if NR==False:
                        print('::Something went wrong::Pls retry::')

                #for continuation.                
                while True:
                    loop2=input('\nDo you want to search more records[y/n]?')
                    if loop2.lower()=='y':
                        loop2='y';break
                    elif loop2.lower()=='n':
                        loop2='n';break
                    else:
                        print('::Invalid Option::')
            key = input('Press ENTER key to contniue:')
            print('')

        #Delete an invoice record.
        elif choice=='3':
            mycursor.execute('SELECT * FROM BILLING_DETAILS;')
            data = mycursor.fetchall()
            if data == []:
                loop3='n'
                print('NO DATA EXIST...')
            else:
                loop3='y'
            while loop3=='y':
                try:
                    E_name=input('Enter the BILL ID: ')

                    #Extracting data from billing_details.
                    query=f"select * from billing_details where IN_ID={E_name};"
                    mycursor.execute(query)
                    data_0=mycursor.fetchall()
                    if data_0==[]:
                        print(f"No invoice record with ID-{E_name}....")
                    else:
                        #BIN_MASTER
                        table_name='billing_details'
                        bin_master(mydb,mycursor,data_0,table_name)
                        #Drop that column 
                        query=f"DELETE FROM billing_details where IN_ID={E_name};" 
                        mycursor.execute(query)
                        mydb.commit()
                        print(f'**BILL RECORD WITH ID {E_name} SUCCESSFULLY DELETED**')    
                except:
                    mydb.rollback()
                    print('::Invalid value input detected::')
                    break

                #for continuation.                
                while True:
                    loop3=input('Do you want to delete more records[y/n]?')
                    if loop3.lower()=='y':
                        loop3='y';break
                    elif loop3.lower()=='n':
                        loop3='n';break
                    else:
                        print('::Invalid Option::')
            key = input('Press ENTER key to contniue:')
            print('')
        elif choice=='4':
            print(' Going back....')
            sleep(2) ; cont='n'
            break
        else:
            try:
                choice=int(choice)
                print('::Invalid option::')
            except:
                print('::Invalid value input detected::')
            key = input('Press ENTER key to contniue:')
            print('')