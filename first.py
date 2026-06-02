from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from PIL import Image,ImageTk # first run pip install pillow in terminal
import datetime
from tkinter import messagebox

m=Tk()
m.geometry("1400x700")
m.title("welcome")
#m.resizable(0,0)

def Updateform():
    m2 = Toplevel()   #for inherite parent properties
    m2.geometry("1400x700")
    m2.title("welcome")
    # m2.resizable(0,0)

    def Update():
        K = int(E1.get())
        K2 = E2.get()
        K3 = E3.get()
        format = '%m/%d/%y'  # convert time format according to sql time format
        K4 = cal.get()
        date = datetime.datetime.strptime(K4, format)
        n = date.strftime('%y-%m-%d')
        K5 = var.get()
        K6 = cb.get()
        K7 = E4.get()
        K8 = E5.get()
        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='@veerumysql1234', db='python_project')
        cur = db.cursor()
        S="update details set Name=%s,Lastname=%s,DOB=%s,Gender=%s,Course=%s, Email=%s, Password=%s where ID=%s"
        A=(K2,K3,n,K5,K6,K7,K8,K)  # tuple
        result=cur.execute(S,A)
        if (result > 0):
            messagebox.showinfo("result", "your record Update successfully")
        else:
            messagebox.showinfo("result", "your record not Updated")
        db.commit()


    img = ImageTk.PhotoImage(file=r"D:\download\pexels-eberhardgross-1624438.jpg")
    I = Label(m2, image=img)
    I.pack()

    var = StringVar()

    c = ['Select', 'Python', 'Java', 'PHP', 'ML', 'AI', 'SQL', 'DA', 'DSA']

    L = Label(m2, text='Student Registration Form', fg='sky blue', bg='black', font=('Arial 25 bold'))
    L.place(x=400, y=50)

    L1 = Label(m2, text='ID', bg='purple', font=('Arial 20 bold'))
    L1.place(x=100, y=150)
    E1 = Entry(m2, font=('Arial 20 bold'))
    E1.place(x=250, y=150)

    L2 = Label(m2, text='Name', font=('Arial 20 bold'))
    L2.place(x=100, y=200)
    E2 = Entry(m2, font=('Arial 20 bold'))
    E2.place(x=250, y=200)

    L3 = Label(m2, text='Lastname', font=('Arial 20 bold'))
    L3.place(x=100, y=250)
    E3 = Entry(m2, font=('Arial 20 bold'))
    E3.place(x=250, y=250)

    L4 = Label(m2, text='DOB', font=('Arial 20 bold'))
    L4.place(x=100, y=300)
    cal = DateEntry(m2, width=19, font=('Arial 20 bold'))
    cal.place(x=250, y=300)

    L5 = Label(m2, text='Gender', font=('Arial 20 bold'))
    L5.place(x=100, y=350)
    r1 = Radiobutton(m2, text='Male', variable=var, value='Male', font=('Arial 15 bold'))
    r1.place(x=250, y=350)
    r2 = Radiobutton(m2, text='Female', variable=var, value='Female', font=('Arial 15 bold'))
    r2.place(x=350, y=350)
    r3 = Radiobutton(m2, text='Others', variable=var, value='Others', font=('Arial 15 bold'))
    r3.place(x=480, y=350)

    L6 = Label(m2, text='Course', font=('Arial 20 bold'))
    L6.place(x=100, y=400)
    cb = ttk.Combobox(m2, values=c, font=('Arial 19 bold'))
    cb.place(x=250, y=400)
    cb.current(0)

    L7 = Label(m2, text='Email', font=('Arial 20 bold'))
    L7.place(x=100, y=450)
    E4 = Entry(m2, font=('Arial 20 bold'))
    E4.place(x=250, y=450)

    L8 = Label(m2, text='Password', font=('Arial 20 bold'))
    L8.place(x=100, y=500)
    E5 = Entry(m2, font=('Arial 20 bold'), show="*")
    E5.place(x=250, y=500)
    C1 = Checkbutton(m2, font=('Arial 15 bold'), command=showpassword)
    C1.place(x=560, y=500)

    B = Button(m2, text='Update', font=('Arial 20 bold'), command=Update)
    B.place(x=300, y=600)

    m2.config(bg='Black')

    m2.mainloop()

def Login(): #For connection b/w both pages
    m.destroy()
    import log

def showpassword():
    if E5.cget('show') =="*":
        E5.config(show='')
    else:
        E5.config(show='*')


def Insert():
    K=int(E1.get())
    K2=E2.get()
    K3=E3.get()
    format = '%m/%d/%y'   # convert time format according to sql time format
    K4=cal.get()
    date = datetime.datetime.strptime(K4,format)
    n = date.strftime('%y-%m-%d')
    K5=var.get()
    K6=cb.get()
    K7=E4.get()
    K8=E5.get()

    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='@veerumysql1234',db='python_project')
    cur=db.cursor() # execute query
    s="insert into details values('%s','%s','%s','%s','%s','%s','%s','%s')"%(K,K2,K3,n,K5,K6,K7,K8)
    result=cur.execute(s)
    if(result>0):
        messagebox.showinfo("result","your record inserted successfully")
    else:
        messagebox.showinfo("result","your record not inserted")
    db.commit()
    E1.delete(0,"end") #record insert karne ke baad previous record ko form se remove karne ke liye
    E2.delete(0, "end")
    E3.delete(0, "end")
    cb.current(0)
    E4.delete(0, "end")
    E5.delete(0, "end")

def delete():
    K=E1.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='@veerumysql1234', db='python_project')
    cur = db.cursor()  # execute query
    s = "delete from details where ID=%s"
    result = cur.execute(s,K)
    if (result > 0):
        messagebox.showinfo("result", "your record delete successfully")
    else:
        messagebox.showinfo("result", "your record not deleted")
    db.commit()

def showdata():
    for i in tv.get_children():
        tv.delete(i) # return result of showdata one time no matter how many time you click for result

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='@veerumysql1234', db='python_project')
    cur = db.cursor()
    p = "select*from details"
    cur.execute(p)
    result=cur.fetchall()
    for col in result:
        ID=col[0]
        Name=col[1]
        Lastname=col[2]
        DOB=col[3]
        Gender=col[4]
        Course=col[5]
        Email=col[6]
        Password=col[7]
        tv.insert("",'end', values=(ID,Name,Lastname,DOB,Gender,Course,Email,Password))
        #print(ID,Name,Lastname,DOB,Gender,Course,Email,Password)

def Search():
    K=E1.get()
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='@veerumysql1234', db='python_project')
    cur = db.cursor()
    p = "select * from details where ID=%s"
    cur.execute(p,K)
    result=cur.fetchall()
    for col in result:
        ID=col[0]
        Name=col[1]
        Lastname=col[2]
        DOB=col[3]
        Gender=col[4]
        Course=col[5]
        Email=col[6]
        Password=col[7]
        tv.insert("",'end', values=(ID,Name,Lastname,DOB,Gender,Course,Email,Password))


img=ImageTk.PhotoImage(file=r"D:\download\pexels-eberhardgross-1624438.jpg")
I=Label(m,image=img)
I.pack()

tv = ttk.Treeview(m,height=15) # for making table
tv['columns'] = ('ID','Name','Lastname','DOB','Gender','Course','Email','Password')

tv.column('#0', width=0, stretch='No')
tv.column('ID', anchor=CENTER, width=90)
tv.column('Name', anchor=CENTER, width=90)
tv.column('Lastname', anchor=CENTER, width=90)
tv.column('DOB', anchor=CENTER, width=90)
tv.column('Gender', anchor=CENTER, width=90)
tv.column('Course', anchor=CENTER, width=90)
tv.column('Email', anchor=CENTER, width=90)
tv.column('Password', anchor=CENTER, width=90)

tv.heading('ID', text='ID', anchor=CENTER)
tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Lastname', text='Lastname', anchor=CENTER)
tv.heading('DOB', text='DOB', anchor=CENTER)
tv.heading('Gender', text='Gender', anchor=CENTER)
tv.heading('Course', text='Course', anchor=CENTER)
tv.heading('Email', text='Email', anchor=CENTER)
tv.heading('Password', text='Password', anchor=CENTER)

tv.place(x=600,y=150)


var=StringVar()

c = ['Select','Python','Java','PHP','ML','AI','SQL','DA','DSA']

L=Label(m,text='Student Registration Form',fg='sky blue',bg='black',font=('Arial 25 bold'))
L.place(x=400,y=50)

L1=Label(m,text='ID',bg='purple',font=('Arial 20 bold'))
L1.place(x=100,y=150)
E1=Entry(m,font=('Arial 20 bold'))
E1.place(x=250,y=150)

L2=Label(m,text='Name',font=('Arial 20 bold'))
L2.place(x=100,y=200)
E2=Entry(m,font=('Arial 20 bold'))
E2.place(x=250,y=200)

L3=Label(m,text='Lastname',font=('Arial 20 bold'))
L3.place(x=100,y=250)
E3=Entry(m,font=('Arial 20 bold'))
E3.place(x=250,y=250)

L4=Label(m,text='DOB',font=('Arial 20 bold'))
L4.place(x=100,y=300)
cal = DateEntry(m,width=19,font=('Arial 20 bold'))
cal.place(x=250,y=300)

L5=Label(m,text='Gender',font=('Arial 20 bold'))
L5.place(x=100,y=350)
r1=Radiobutton(m,text='Male',variable=var,value='Male',font=('Arial 15 bold'))
r1.place(x=250,y=350)
r2=Radiobutton(m,text='Female',variable=var,value='Female',font=('Arial 15 bold'))
r2.place(x=350,y=350)
r3=Radiobutton(m,text='Others',variable=var,value='Others',font=('Arial 15 bold'))
r3.place(x=480,y=350)


L6=Label(m,text='Course',font=('Arial 20 bold'))
L6.place(x=100,y=400)
cb= ttk.Combobox(m,values=c,font=('Arial 19 bold'))
cb.place(x=250,y=400)
cb.current(0)

L7=Label(m,text='Email',font=('Arial 20 bold'))
L7.place(x=100,y=450)
E4=Entry(m,font=('Arial 20 bold'))
E4.place(x=250,y=450)

L8=Label(m,text='Password',font=('Arial 20 bold'))
L8.place(x=100,y=500)
E5=Entry(m,font=('Arial 20 bold'),show="*")
E5.place(x=250,y=500)
C1=Checkbutton(m,font=('Arial 15 bold'),command=showpassword)
C1.place(x=560,y=500)

B=Button(m,text='Submit',font=('Arial 20 bold'),command=Insert)
B.place(x=300,y=600)

B1=Button(m,text='Delete',font=('Arial 20 bold'),command=delete)
B1.place(x=450,y=600)

B2=Button(m,text='Show Data',font=('Arial 20 bold'),command=showdata)
B2.place(x=580,y=600)

B3=Button(m,text='Search',font=('Arial 20 bold'),command=Search)
B3.place(x=780,y=600)

B3=Button(m,text='Login',font=('Arial 20 bold'),command=Login)
B3.place(x=930,y=600)

B3=Button(m,text='Update',font=('Arial 20 bold'),command=Updateform)
B3.place(x=1070,y=600)

m.config(bg='Black')

m.mainloop()
