from tkinter import*
import sqlite3
from PIL import Image,ImageTk
from tkinter import messagebox

root=Tk()
root.title("Student Management System")
root.geometry("600x500")
p1=PhotoImage(file='icon.png')
root.iconphoto(False,p1)

cnt=sqlite3.connect("Student_data.db")
c=cnt.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS student(
    name text,
    roll integer,
    dept text,
    father_name text,
    ph_no integer,
    address text
)

""")


def submit():
    cnt=sqlite3.connect("Student_data.db")
    c=cnt.cursor()

    try:
        c.execute("INSERT INTO student VALUES(:sname, :sroll, :sdept, :sfname, :sph, :saddress)",
            {
                'sname': sname.get(),
                'sroll': sroll.get(),
                'sdept': sdept.get(),
                'sfname': sfname.get(),
                'sph': sph.get(),
                'saddress': saddress.get()
            
            })
    except:
        messagebox.showerror("Wrong!")


    cnt.commit()
    cnt.close()

    sname.delete(0,END)
    sroll.delete(0,END)
    sdept.delete(0,END)
    sfname.delete(0,END)
    sph.delete(0,END)
    saddress.delete(0,END)



heading=Label(root,text="STUDENT MANAGEMENT SYSTEM",font=('arial',25),fg='green')
heading.grid(row=0,column=0,padx=20,pady=10,columnspan=2)
sname_label=Label(root,text="Enter Student Name:")
sname_label.grid(row=1,column=0,pady=20)
sroll_label=Label(root,text="Enter Student Roll:")
sroll_label.grid(row=2,column=0,pady=20)
sdept_label=Label(root,text="Enter Student Department:")
sdept_label.grid(row=3,column=0,pady=20)
sfname_label=Label(root,text="Enter Father's Name:")
sfname_label.grid(row=4,column=0,pady=20)
sph_label=Label(root,text="Enter Student Phone no:")
sph_label.grid(row=5,column=0,pady=20)
saddress_label=Label(root,text="Enter Student address:")
saddress_label.grid(row=6,column=0,pady=20)


sname=Entry(root,width=60)
sname.grid(row=1,column=1)
sroll=Entry(root,width=60)
sroll.grid(row=2,column=1)
sdept=Entry(root,width=60)
sdept.grid(row=3,column=1)
sfname=Entry(root,width=60)
sfname.grid(row=4,column=1)
sph=Entry(root,width=60)
sph.grid(row=5,column=1)
saddress=Entry(root,width=60)
saddress.grid(row=6,column=1)

submit_btn=Button(root,text="Add record to database",command=submit)
submit_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=112)


cnt.commit()
cnt.close()

root.mainloop()