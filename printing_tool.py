"Developer: Krishna Aggarwal & Dhruv Kalra; Class-section: 12th-A; RollNo. : 16 & 10"
"Submodule:- Printing Tool (completed)"

def dtool(string):
     from time import sleep
     for i in string:
          print(i,end='')
          sleep(0.003)
     print()

def dtool_loading(string):
     from time import sleep
     for i in range(10):
          print('.',end='')
          sleep(0.03)
     print()

#For printing data
def formatting(field1,row1):
        Max=0
        a=0
        d=0
        field=[]
        row=[]
        temp=[]
        for i in field1:
            if type(i)!=str:
                field.append(str(i))
            else:
                field.append(i)
        for j in row1:
            for k in j:
                if type(k)!=str:
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
            d=d+Max+3
            Max=0
        print()
        d-=1
        print('','-'*d)
        for i in field:
            print('|',i,end=' ')
        print('|')
        print('','-'*d)
        for i in row:
            for j in i:
                print('|',j,end=' ')
            print('|')
        print('','-'*d)
        print()