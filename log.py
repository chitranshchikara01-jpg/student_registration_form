from tkinter import *

from PIL import ImageTk # first run pip install pillow in terminal

m=Tk()
m.geometry("1400x700")
m.title("welcome")

def Loginfetch():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='@veerumysql1234', db='python_project')
    cur = db.cursor()
    cur.execute("select * from details where ID=%s and password=%s",(E1.get(),E2.get()))
    row =cur.fetchone()
    if row == None:
        messagebox.showerror("Error","Invalid ID and Password")
    else:
        m.destroy()
        import first

def showpassword():
    if E2.cget('show') =="*":
        E2.config(show='')
    else:
        E2.config(show='*')

img=ImageTk.PhotoImage(file=r"D:\download\3146-3840x2160-desktop-4k-mercedes-benz-background-image.jpg")
I=Label(m,image=img)
I.pack()

L=Label(m,text='Login',fg='sky blue',bg='black',font='Arial 25 bold')
L.place(x=500,y=100)

L1=Label(m,text='ID',bg='purple',font='Arial 20 bold')
L1.place(x=100,y=250)
E1=Entry(m,font='Arial 20 bold')
E1.place(x=250,y=250)

L2=Label(m,text='Password',font='Arial 20 bold')
L2.place(x=100,y=350)
E2=Entry(m,font='Arial 20 bold',show="*")
E2.place(x=250,y=350)
C1=Checkbutton(m,font='Arial 15 bold',command=showpassword)
C1.place(x=560,y=350)

B=Button(m,text='Submit',font='Arial 20 bold',command=Loginfetch)
B.place(x=300,y=400)

m.mainloop()