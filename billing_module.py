"Developer: Krishna Aggarwal & Dhruv Kalra; Class-section: 12th-A; RollNo. : 16 & 10"
"Submodule:- Billing_module (completed)"

def formatting(field1,row1,chk=0):
        Max=0
        a=0
        global d
        d=0
        field=[]
        row=[]
        temp=[]
        for i in field1:
            if type(i)==int:
                field.append(str(i))
            else:
                field.append(i)
        for j in row1:
            for k in j:
                if type(k)==int:
                    temp.append(str(k))
                else:
                    temp.append(k)
            row.append(temp)
            temp=[]
        for i in range(len(field)):
            for j in row:
                if Max<len(j[a]):
                    Max=len(j[a])
            if Max-len(field[i])<=0:
                Max=len(field[i])
            field[i]=field[i]+' '*(Max-len(field[i]))
            for j in row:
                j[a]=j[a]+' '*(Max-len(j[a]))
            a+=1
            d=d+Max+1
            Max=0
        print()
        d-=1
        if chk==1:
            return d
        else:
            for i in field:
                print(i,end=' ')
            print()
            print('-'*d,end=' ')
            print()
            for i in row:
                for j in i:
                    print(j,end=' ')
                print()
            print()
            
def bill_layout1(mycursor,mydb,hour,minute,sec,date,invoice_no):
    mycursor.execute('Select * from account where status=\'active\';')
    for (ID,NAME,GENDER,EMAIL,PHONE,COMPANY_NAME,COMPANY_ADD,GSTIN,STATUS) in mycursor:
        cname=COMPANY_NAME
        cad=COMPANY_ADD
        p=PHONE
        e=EMAIL
        g=GSTIN
    print('-'*(d))
    print((int((d-len(cname)-1)/2))*' ',cname)
    print((int((d-len(cad)-1)/2))*' ',cad)
    print('-'*(d))
    print(' Phno:',p)
    print(' Email:',e)
    print(' GSTIN:',g)
    print(d*'-')
    print((int((d-12)/2))*' ','TAX INVOICE')
    print(d*'-')
    print(' Invoice no:',invoice_no)
    print(' DATE:',date)
    print(f' TIME: {hour}:{minute}:{sec}')
    print(d*'-')

def bill_layout1_for_c2(mycursor,mydb,time,date,invoice_no):
    mycursor.execute('Select * from account where status=\'active\';')
    for (ID,NAME,GENDER,EMAIL,PHONE,COMPANY_NAME,COMPANY_ADD,GSTIN,STATUS) in mycursor:
        cname=COMPANY_NAME
        cad=COMPANY_ADD
        p=PHONE
        e=EMAIL
        g=GSTIN
    print(d*'-')
    print((int((d-len(cname)-1)/2))*' ',cname)
    print((int((d-len(cad)-1)/2))*' ',cad)
    print(d*'-')
    print(' Phno:',p)
    print(' Email:',e)
    print(' GSTIN:',g)
    print(d*'-')
    print((int((d-12)/2))*' ','TAX INVOICE')
    print(d*'-')
    print(' Invoice no:',invoice_no)
    print(' DATE:',date)
    print(f' TIME: {time}')
    print(d*'-')

def billing_layout2(data_1,l_name,l_amount,l_qty,l_dis,sno=0):
    field1=['S.No.','Product Name','Cost Price','Quantity','Discount']
    formatting(field1,data_1)
    print(d*'=')

def billing_layout3(sno,sub_total,total_dis):
    print((int((d-(15+len(str(sub_total))))/2))*' ','SUB TOTAL : ',sub_total)
    print((int((d-(18+len(str(total_dis))))/2))*' ','YOU HAVE SAVED: ',total_dis)
    print(d*'=')
    print((int((d-23)/2))*' ','Thanks for your vist!!')
    print(d*'-')
    
def bill_saving(invoice_no,l_id,l_name,l_qty,l_dis,sno,l_amount,date,hour,minute,sec,mydb,mycursor):

    for i in range(sno):
        ID=l_id[i];qty=l_qty[i];dis=l_dis[i];p=l_amount[i];name=l_name[i]
        query=f"INSERT INTO billing_details VALUES('{date}','{hour}:{minute}:{sec}',{invoice_no},{ID},\'{name}\',{p},{qty},{dis});"
        mycursor.execute(query)
        mydb.commit()
    print(f'\n\n**BILL WITH ID {invoice_no} RECORD SAVED**')
        
def invoice_no_generator(mydb,mycursor):
    query='SELECT IN_ID FROM billing_details;'
    mycursor.execute(query)
    data=mycursor.fetchall()
    l_no=[]
    if data==[]:
        return '1'
    else:
        for i in data:
            l_no.append(i)
        length=len(l_no)
        result=l_no[length-1][0]
        result=int(result)
        result=str(result+1)
        return result