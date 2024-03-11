from tkinter import*
import sqlite3
from PIL import Image,ImageTk
from tkinter import messagebox

mainwin=Tk()
mainwin.title("Student Management System")
#mainwin.geometry("600x500")

p1=PhotoImage(file='icon.png')
mainwin.iconphoto(False,p1)

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
        if len(sph.get())==10:

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
                messagebox.showinfo("Done","Added successfully")
            except:
                messagebox.showerror("Wrong!","Oops! Something went wrong. Please ry again later.")
        else:
            messagebox.showerror("Wrong"," Phone number should be 10 digits")

        #root.destroy()
        #mainwin.deiconify()

        cnt.commit()
        cnt.close()

        sname.delete(0,END)
        sroll.delete(0,END)
        sdept.delete(0,END)
        sfname.delete(0,END)
        sph.delete(0,END)
        saddress.delete(0,END)

        a=messagebox.askquestion("More data","Do you want to add more student?")
        if a=="yes":
            return
        else:
            root.destroy()


def addnew():
    global sname,sroll,saddress,sdept,sfname,sph,root
    root=Tk()
    root.title("Add New Student")
    #root.geometry("600x500")
    #mainwin.withdraw()
    

    cnt=sqlite3.connect("Student_data.db")
    c=cnt.cursor()

    heading=Label(root,text="STUDENT MANAGEMENT SYSTEM",font=('bodoni mt black',25),fg='green')
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
    submit_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=50)

    #button_quit=Button(root,text="Exit",command=root.quit)
    #button_quit.grid(row=7,column=1,pady=10,padx=10,ipadx=70)
    
    cnt.commit()
    cnt.close()

    root.mainloop()


def updatelist():
    cnt=sqlite3.connect("Student_data.db")
    c=cnt.cursor()

    record_id=id_text.get()

    if len(sph2.get())==10:
        c.execute("""UPDATE student SET
            name=:name,
            roll=:roll,
            dept=:dept,
            father_name=:father_name,
            ph_no=:ph_no,
            address=:address

            WHERE roll=:roll""",
            {
            'name':sname2.get(),
            'roll':sroll2.get(),
            'dept':sdept2.get(),
            'father_name':sfname2.get(),
            'ph_no':sph2.get(),
            'address':saddress2.get(),
            'roll':record_id
            })

        messagebox.showinfo("Done","Updated successfully")
    
    else:
        messagebox.showerror("Wrong","Phone number should be 10 digits")
    
    sname2.delete(0,END)
    sroll2.delete(0,END)
    sdept2.delete(0,END)
    sfname2.delete(0,END)
    sph2.delete(0,END)
    saddress2.delete(0,END)

    cnt.commit()
    cnt.close()

    a=messagebox.askquestion("More data","Do you want to modify more data?")
    if a=="yes":
        return
    else:
        win5.destroy()


def modify():
    global win5
    win5=Tk()
    win5.title("Modify Student Data")

    heading2=Label(win5,text="STUDENT MANAGEMENT SYSTEM",font=('bodoni mt black',25),fg='green')
    heading2.grid(row=0,column=0,padx=20,pady=10,columnspan=3)

    show(win5)

    updatebtn=Button(win5,text="Update",command=updatelist)
    updatebtn.grid(row=1,column=3,pady=10,padx=10)

    
def deletestudent():
    cnt=sqlite3.connect("Student_data.db")
    c=cnt.cursor()

    #record_id=id_text.get()

    c.execute("DELETE from student WHERE roll="+id_text.get())
    sname2.delete(0,END)
    sroll2.delete(0,END)
    sdept2.delete(0,END)
    sfname2.delete(0,END)
    sph2.delete(0,END)
    saddress2.delete(0,END)

    messagebox.showinfo("Done","Deleted successfully !!!!")
    
    cnt.commit()
    cnt.close()

    a=messagebox.askquestion("More Delete","Do you want to delete more student?")
    if a=="yes":
        return
    else:
        win4.destroy()
    
    
def deleterecord():
    global win4
    win4=Tk()
    win4.title("Delete Student Details")

    heading3=Label(win4,text="STUDENT MANAGEMENT SYSTEM",font=('bodoni mt black',25),fg='green')
    heading3.grid(row=0,column=0,padx=20,pady=10,columnspan=2)

    show(win4)

    deletebtn=Button(win4,text="Delete",command=deletestudent)
    deletebtn.grid(row=1,column=3,pady=10,padx=10)
    
def details(a):
    cnt=sqlite3.connect("Student_data.db")
    c=cnt.cursor()

    record_id=id_text.get()

    try:
        c.execute("SELECT* FROM student WHERE roll="+record_id)
        records=c.fetchall()
    
        sname_label=Label(a,text="Student Name:")
        sname_label.grid(row=2,column=0,pady=20)
        sroll_label=Label(a,text="Student Roll:")
        sroll_label.grid(row=3,column=0,pady=20)
        sdept_label=Label(a,text="Student Department:")
        sdept_label.grid(row=4,column=0,pady=20)
        sfname_label=Label(a,text="Father's Name:")
        sfname_label.grid(row=5,column=0,pady=20)
        sph_label=Label(a,text="Student Phone no:")
        sph_label.grid(row=6,column=0,pady=20)
        saddress_label=Label(a,text="Student address:")
        saddress_label.grid(row=7,column=0,pady=20)
    

        global sname2,sroll2,sdept2,sfname2,sph2,saddress2
    
        sname2=Entry(a,width=60)
        sname2.grid(row=2,column=1)
        sroll2=Entry(a,width=60)
        sroll2.grid(row=3,column=1)
        sdept2=Entry(a,width=60)
        sdept2.grid(row=4,column=1)
        sfname2=Entry(a,width=60)
        sfname2.grid(row=5,column=1)
        sph2=Entry(a,width=60)
        sph2.grid(row=6,column=1)
        saddress2=Entry(a,width=60)
        saddress2.grid(row=7,column=1)
    

        for record in records:
            sname2.insert(0,record[0])
            sroll2.insert(0,record[1])
            sdept2.insert(0,record[2])
            sfname2.insert(0,record[3])
            sph2.insert(0,record[4])
            saddress2.insert(0,record[5])
    except:
        messagebox.showerror("ERROR","Something went wrong, Please try again")
    cnt.commit()
    cnt.close()

def seedetails():
    global win3
    win3=Tk()
    win3.title("Student Information")

    heading4=Label(win3,text="STUDENT MANAGEMENT SYSTEM",font=('bodoni mt black',25),fg='green')
    heading4.grid(row=0,column=0,padx=20,pady=10,columnspan=2)

    show(win3)
    
def show(b):
    global id_text
    
    cnt=sqlite3.connect("Student_data.db")
    c=cnt.cursor()

    id_label=Label(b,text="Enter Roll No:")
    id_label.grid(row=1,column=0,pady=20)
    id_text=Entry(b,width=30)
    id_text.grid(row=1,column=1)
    searchbtn=Button(b,text="SEARCH",command=lambda:details(b))
    searchbtn.grid(row=1,column=2,pady=10)

    cnt.commit()
    cnt.close()


heading=Label(mainwin,text="STUDENT MANAGEMENT SYSTEM",font=('bodoni mt black',25),fg='green')
heading.grid(row=0,column=0,padx=20,pady=10,columnspan=2)

b1=Button(mainwin,text="Add New Student",font=('arial',15),fg='red',command=addnew)
b1.grid(row=1,column=0,columnspan=2,pady=10,padx=10,ipadx=140)
b2=Button(mainwin,text="Modify Existing Student",font=('arial',15),fg='red',command=modify)
b2.grid(row=2,column=0,columnspan=2,pady=10,padx=10,ipadx=114)
b3=Button(mainwin,text="Delete Student Records",font=('arial',15),fg='red',command=deleterecord)
b3.grid(row=3,column=0,columnspan=2,pady=10,padx=10,ipadx=113)
b4=Button(mainwin,text="Show Student Details",font=('arial',15),fg='red',command=seedetails)
b4.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=124)
b5=Button(mainwin,text="Exit",font=('arial',15),fg='red',command=mainwin.quit)
b5.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=30)

cnt.commit()
cnt.close()

mainwin.mainloop()