from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if userEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Feilds Cannot be empty')
    elif userEntry.get()=="Rajat Gupta" and passwordEntry.get()=="12345":
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import next_page
    else:
        messagebox.showerror('Error','Invalid Credentials')

window = Tk()
window.geometry('1440x720+0+0')
window.title('Login Window')
window.resizable(False,False)
background = ImageTk.PhotoImage(file = '1695702.jpg')
bglabel = Label(window,image = background)
bglabel.place(x=0,y=0)

loginFrame=Frame(window,background='green')
loginFrame.place(x=600,y=250)
logoImage = PhotoImage(file='student.png')
logolabel=Label(loginFrame,image=logoImage)
logolabel.grid(row=0,column=0,columnspan=2,pady=10)

user = PhotoImage(file = 'username.png')
usernamelabel = Label(loginFrame,image=user,text = "Username",compound=LEFT,font=('times new roman',20,'bold'))
usernamelabel.grid(row=1,column=0,pady=10,padx=20)
userEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=8)
userEntry.grid(row=1,column=1,pady=10,padx=20)

password = PhotoImage(file = 'password.png')
passwordlabel = Label(loginFrame,image=password,text = "Password",compound=LEFT,font=('times new roman',20,'bold'))
passwordlabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=8)
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginbutton = Button(loginFrame,text="Login",font=('times new roman',20,'bold'),width=15,bg='cornflowerblue',cursor='hand2',command=login)
loginbutton.grid(row=3,column=1)

window.mainloop()

