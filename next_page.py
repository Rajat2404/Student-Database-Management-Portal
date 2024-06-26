from tkinter import *
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas
import numpy
#Function


def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = student_table.get_children()
    newlist=[]
    for index in indexing:
        content=student_table.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table = pandas.DataFrame(newlist,columns=['Roll No.','Name','Outlook Id','Mobile No.','Physics','Chemistry','Maths'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data Saved successfully')

def update_student():
    def update_data():
        query = 'update student set Name=%s,OutlookId=%s,MobileNo=%s,Physics=%s,Chemistry=%s,Maths=%s where RollNo=%s'
        mycursor.execute(query,(nameentry.get(),outlookentry.get(),mobileentry.get(),physicsentry.get(),chemistryentry.get(),mathsentry.get(),rollentry.get()))
        con.commit()
        messagebox.showinfo('Success',f'Roll No. {rollentry.get()} if modified successfully',parent=update_window)
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.resizable(0, 0)
    update_window.title('Update Student')
    update_window.grab_set()
    rollnolabel = Label(update_window, text='Roll No.', font=('times new roman', 20, 'bold'))
    rollnolabel.grid(row=0, column=0, pady=15, padx=30)
    rollentry = Entry(update_window, font=('roman', 15, 'bold'))
    rollentry.grid(row=0, column=1, pady=15, padx=10)

    namelabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0, pady=15, padx=30)
    nameentry = Entry(update_window, font=('roman', 15, 'bold'))
    nameentry.grid(row=1, column=1, pady=15, padx=10)

    outlooklabel = Label(update_window, text='Outlook Id', font=('times new roman', 20, 'bold'))
    outlooklabel.grid(row=2, column=0, pady=15, padx=30)
    outlookentry = Entry(update_window, font=('roman', 15, 'bold'))
    outlookentry.grid(row=2, column=1, pady=15, padx=10)

    mobilelabel = Label(update_window, text='Mobile', font=('times new roman', 20, 'bold'))
    mobilelabel.grid(row=3, column=0, pady=15, padx=30)
    mobileentry = Entry(update_window, font=('roman', 15, 'bold'))
    mobileentry.grid(row=3, column=1, pady=15, padx=10)

    physicslabel = Label(update_window, text='Physics', font=('times new roman', 20, 'bold'))
    physicslabel.grid(row=4, column=0, pady=15, padx=30)
    physicsentry = Entry(update_window, font=('roman', 15, 'bold'))
    physicsentry.grid(row=4, column=1, pady=15, padx=10)

    chemistrylabel = Label(update_window, text='Chemistry', font=('times new roman', 20, 'bold'))
    chemistrylabel.grid(row=5, column=0, pady=15, padx=30)
    chemistryentry = Entry(update_window, font=('roman', 15, 'bold'))
    chemistryentry.grid(row=5, column=1, pady=15, padx=10)

    mathslabel = Label(update_window, text='Maths', font=('times new roman', 20, 'bold'))
    mathslabel.grid(row=6, column=0, pady=15, padx=30)
    mathsentry = Entry(update_window, font=('roman', 15, 'bold'))
    mathsentry.grid(row=6, column=1, pady=15, padx=10)

    update_student_button = ttk.Button(update_window, text='UPDATE STUDENT',command=update_data)
    update_student_button.grid(row=7, columnspan=2, pady=15)

    indexing=student_table.focus()
    content=student_table.item(indexing)
    listdata=content['values']
    rollentry.insert(0,listdata[0])
    nameentry.insert(0,listdata[1])
    outlookentry.insert(0,listdata[2])
    mobileentry.insert(0,listdata[3])
    physicsentry.insert(0,listdata[4])
    chemistryentry.insert(0,listdata[5])
    mathsentry.insert(0,listdata[6])

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('',END,values=data)

def delete_student():
    indexing=student_table.focus()
    content=student_table.item(indexing)
    content_rollno=content['values'][0]
    query='delete from student where RollNo=%s'
    mycursor.execute(query,content_rollno)
    con.commit()    
    messagebox.showinfo('Deleted',f'Roll No. {content_rollno} is deleted successfully')
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('',END,values=data)


def search_student():
    def search_data():
        query = 'select * from student where RollNo=%s or Name=%s or OutlookId=%s or MobileNo=%s or Physics=%s or Chemistry=%s or Maths=%s'
        mycursor.execute(query,(rollentry.get(),nameentry.get(),outlookentry.get(),mobileentry.get(),physicsentry.get(),chemistryentry.get(),mathsentry.get()))
        student_table.delete(*student_table.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            student_table.insert('',END,values=data)




    search_window = Toplevel()
    search_window.resizable(0, 0)
    search_window.title('Search Student')
    search_window.grab_set()
    rollnolabel = Label(search_window, text='Roll No.', font=('times new roman', 20, 'bold'))
    rollnolabel.grid(row=0, column=0, pady=15, padx=30)
    rollentry = Entry(search_window, font=('roman', 15, 'bold'))
    rollentry.grid(row=0, column=1, pady=15, padx=10)

    namelabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0, pady=15, padx=30)
    nameentry = Entry(search_window, font=('roman', 15, 'bold'))
    nameentry.grid(row=1, column=1, pady=15, padx=10)

    outlooklabel = Label(search_window, text='Outlook Id', font=('times new roman', 20, 'bold'))
    outlooklabel.grid(row=2, column=0, pady=15, padx=30)
    outlookentry = Entry(search_window, font=('roman', 15, 'bold'))
    outlookentry.grid(row=2, column=1, pady=15, padx=10)

    mobilelabel = Label(search_window, text='Mobile', font=('times new roman', 20, 'bold'))
    mobilelabel.grid(row=3, column=0, pady=15, padx=30)
    mobileentry = Entry(search_window, font=('roman', 15, 'bold'))
    mobileentry.grid(row=3, column=1, pady=15, padx=10)

    physicslabel = Label(search_window, text='Physics', font=('times new roman', 20, 'bold'))
    physicslabel.grid(row=4, column=0, pady=15, padx=30)
    physicsentry = Entry(search_window, font=('roman', 15, 'bold'))
    physicsentry.grid(row=4, column=1, pady=15, padx=10)

    chemistrylabel = Label(search_window, text='Chemistry', font=('times new roman', 20, 'bold'))
    chemistrylabel.grid(row=5, column=0, pady=15, padx=30)
    chemistryentry = Entry(search_window, font=('roman', 15, 'bold'))
    chemistryentry.grid(row=5, column=1, pady=15, padx=10)

    mathslabel = Label(search_window, text='Maths', font=('times new roman', 20, 'bold'))
    mathslabel.grid(row=6, column=0, pady=15, padx=30)
    mathsentry = Entry(search_window, font=('roman', 15, 'bold'))
    mathsentry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='SEARCH STUDENT', command=search_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)

def add_student():
    def add_data():
        if rollentry.get()=='' or mobileentry.get()=='' or outlookentry.get()=='' or nameentry.get()=='' or physicsentry.get()=='' or chemistryentry.get()=='' or mathsentry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=add_window)
        else:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(rollentry.get(),nameentry.get(),outlookentry.get(),mobileentry.get(),physicsentry.get(),chemistryentry.get(),mathsentry.get()))
            con.commit()
            result=messagebox.askyesno('Confirm','Data Added. Do you want to clean the form?',parent=add_window)
            if result:
                rollentry.delete(0,END)
                nameentry.delete(0,END)
                outlookentry.delete(0,END)
                mobileentry.delete(0,END)
                physicsentry.delete(0,END)
                chemistryentry.delete(0,END)
                mathsentry.delete(0,END)
            else:
                pass
            query = 'select * from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for data in fetched_data:
                data_list=list(data)
                student_table.insert('',END,values=data_list)



    add_window=Toplevel()
    add_window.resizable(0,0)
    add_window.grab_set()
    rollnolabel=Label(add_window,text='Roll No.',font=('times new roman',20,'bold'))
    rollnolabel.grid(row=0,column=0,pady=15,padx=30)
    rollentry=Entry(add_window,font=('roman',15,'bold'))
    rollentry.grid(row=0,column=1,pady=15,padx=10)

    namelabel=Label(add_window,text='Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,pady=15,padx=30)
    nameentry=Entry(add_window,font=('roman',15,'bold'))
    nameentry.grid(row=1,column=1,pady=15,padx=10)

    outlooklabel=Label(add_window,text='Outlook Id',font=('times new roman',20,'bold'))
    outlooklabel.grid(row=2,column=0,pady=15,padx=30)
    outlookentry=Entry(add_window,font=('roman',15,'bold'))
    outlookentry.grid(row=2,column=1,pady=15,padx=10)

    mobilelabel=Label(add_window,text='Mobile',font=('times new roman',20,'bold'))
    mobilelabel.grid(row=3,column=0,pady=15,padx=30)
    mobileentry=Entry(add_window,font=('roman',15,'bold'))
    mobileentry.grid(row=3,column=1,pady=15,padx=10)

    physicslabel=Label(add_window,text='Physics',font=('times new roman',20,'bold'))
    physicslabel.grid(row=4,column=0,pady=15,padx=30)
    physicsentry=Entry(add_window,font=('roman',15,'bold'))
    physicsentry.grid(row=4,column=1,pady=15,padx=10)

    chemistrylabel=Label(add_window,text='Chemistry',font=('times new roman',20,'bold'))
    chemistrylabel.grid(row=5,column=0,pady=15,padx=30)
    chemistryentry=Entry(add_window,font=('roman',15,'bold'))
    chemistryentry.grid(row=5,column=1,pady=15,padx=10)

    mathslabel=Label(add_window,text='Maths',font=('times new roman',20,'bold'))
    mathslabel.grid(row=6,column=0,pady=15,padx=30)
    mathsentry=Entry(add_window,font=('roman',15,'bold'))
    mathsentry.grid(row=6,column=1,pady=15,padx=10)

    add_student_button = ttk.Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=15)

count=0
text=''
def slider():
    global  text,count
    if count == len(s):
        count =0
        text = ''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(250,slider)

def connect_to_database():
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host=hostentry.get(), user=userentry.get(), password=passwordentry.get())
            mycursor = con.cursor()
            messagebox.showinfo('Success','Database Connection Successfull',parent=connectwindow)
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectwindow)
        try:
            query ='Create database studentinformationsystem'
            mycursor.execute(query)
            query='use studentinformationsystem'
            mycursor.execute(query)
            query='create table student(RollNo int not null primary key,Name varchar(30),OutlookId varchar(30),MobileNo varchar(10),Physics varchar(3),Chemistry varchar(3),Maths varchar(3))'
            mycursor.execute(query)
        except:
            query='use studentinformationsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection is successful',parent = connectwindow)
        connectwindow.destroy()
        addstudentbutton.config(state=NORMAL)
        searchstudentbutton.config(state=NORMAL)
        updatestudentbutton.config(state=NORMAL)
        showstudentbutton.config(state=NORMAL)
        exportstudentbutton.config(state=NORMAL)
        deletestudentbutton.config(state=NORMAL)

    connectwindow = Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('470x250+730+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(0,0)

    hostnamelabel = Label(connectwindow,text="Host Name",font=('arial',20,'bold'))
    hostnamelabel.grid(row=0,column=0,padx=20)

    hostentry = Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=40,pady=20)

    usernamelabel = Label(connectwindow,text="User Name",font=('arial',20,'bold'))
    usernamelabel.grid(row=1,column=0,padx=20)

    userentry = Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    userentry.grid(row=1,column=1,padx=40,pady=20)

    passwordnamelabel = Label(connectwindow,text="Password",font=('arial',20,'bold'))
    passwordnamelabel.grid(row=2,column=0,padx=20)

    passwordentry = Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    passwordentry.grid(row=2,column=1,padx=40,pady=20)

    connectbutton = ttk.Button(connectwindow,text="CONNECT",command=connect)
    connectbutton.grid(row=3,columnspan=2)



#GUI

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+0+0')
root.title('Student Information System')
root.resizable(0,0)

s = 'Student Information System'
sliderLabel = Label(root,text =s,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectbutton = ttk.Button(root,text='Connect To DataBase',command=connect_to_database)
connectbutton.place(x=990,y=0)

leftframe = Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)

logo_image = PhotoImage(file='studentlogo.png')
logo_label = Label(leftframe,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentbutton = ttk.Button(leftframe,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentbutton.grid(row=1,column=0,pady=20)

searchstudentbutton = ttk.Button(leftframe,text='Search Student',width=25,state=DISABLED,command=search_student)
searchstudentbutton.grid(row=2,column=0,pady=20)

deletestudentbutton = ttk.Button(leftframe,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentbutton.grid(row=3,column=0,pady=20)

updatestudentbutton = ttk.Button(leftframe,text='Update Student',width=25,state=DISABLED,command=update_student)
updatestudentbutton.grid(row=4,column=0,pady=20)

showstudentbutton = ttk.Button(leftframe,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentbutton.grid(row=5,column=0,pady=20)

exportstudentbutton = ttk.Button(leftframe,text='Export Student',width=25,state=DISABLED,command=export_data)
exportstudentbutton.grid(row=6,column=0,pady=20)

exitbutton = ttk.Button(leftframe,text='Exit',width=25,command=iexit)
exitbutton.grid(row=7,column=0,pady=20)

rightframe = Frame(root)
rightframe.place(x=350,y=80,width=820,height=600)

scroll_x=Scrollbar(rightframe,orient=HORIZONTAL)
scroll_y=Scrollbar(rightframe,orient=VERTICAL)

student_table=ttk.Treeview(rightframe,columns=('RollNo','Name','OutlookId','MobileNo','Physics','Chemistry','Maths'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

student_table.pack(fill=BOTH,expand=1)

student_table.heading('RollNo',text='Roll No.')
student_table.heading('Name',text='Name')
student_table.heading('OutlookId',text='Outlook Id')
student_table.heading('MobileNo',text='Mobile No.')
student_table.heading('Physics',text='Physics')
student_table.heading('Chemistry',text='Chemistry')
student_table.heading('Maths',text='Maths')

student_table.config(show='headings')

root.mainloop()