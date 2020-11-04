#import statements
from tkinter import *
#create gui
#create root window
app = Tk()
#add title to window
app.title("GYM MANAGEMENT SYSTEM")
#add geometry for the window
app.geometry('480x348')
#adding picture as desktop with the help of label
p=PhotoImage(file="hello.png")
#using label for using the picture
root=Label(app,image=p,height=350)
root.place(x=0,y=0)
#from PIL import ImageTk,Image
#creating a class and constructor and a function for making a menubar
class SP:
    def __init__(self, wood):


#create menu bar
        self.menubar=Menu(wood)

        wood.config(menu=self.menubar)
        #creating file menu
        self.filemenu=Menu(wood, tearoff=1)
        #creating tearoff to tear
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.filemenu.add_command(label="Open",command=abc)
        self.filemenu.add_command(label="Save")
        #using a seperator to seperate
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=wood.destroy)
        self.emenu=Menu(wood, tearoff=1)
        self.menubar.add_cascade(label="Edit",menu=self.emenu)
        self.emenu.add_command(label="Cut",command=abc)
        self.emenu.add_command(label="copy")
        self.emenu.add_command(label="Paste")
        self.emenu.add_separator()
        self.emenu.add_command(label="Exit", command=wood.destroy)
        self.emenu = Menu(wood, tearoff=1)
        self.menubar.add_cascade(label="view",menu=self.emenu)
        self.emenu.add_command(label="list ",command=abc)
        self.emenu.add_command(label="offers")
        self.emenu.add_separator()
        self.emenu.add_command(label="Exit", command=wood.destroy)
        self.emenu = Menu(wood, tearoff=1)
        self.menubar.add_cascade(label="help",menu=self.emenu)
        self.emenu.add_command(label="brower help")
        self.emenu.add_command(label="customer servies")


def abc():
    print("hi Filemenu clicked!!")

o=SP(app)

#using label to create title to the window
l=Label(root,text='welcome to fitness gym',font=('arial bold',12),fg='red',bg='black')
l.place(x=130,y=0)

#label used to use username
l2=Label(root,text='username:-',font=('arial bold',12))
l2.place(x=70,y=100)

#text box to fill the username
t = Entry(root, width=30,bg='white')
t.place(x=170,y=100)

l3=Label(root,text='password:-',font=('arial bold',12))
l3.place(x=70,y=140)
#text box to fill password
t2 = Entry(root,width=30,bg='white',show="*")
t2.place(x=170,y=140)

#created checkbutton to inform keeping the user to be sign in
chk=BooleanVar()
chk.set(True)
ch=Checkbutton(root, text='keep me sign-in',font=('arial',6),width='20',var=chk)
ch.place(x=160,y=190)

#wgen the user click to register for the gym management then the function given to it take him to the next module
def sing_in():
    #creating database connectivity as to store the user details which helps in login in
    import mysql.connector
    NEWLY_register = Toplevel(app)
    NEWLY_register.geometry("400x630")
    NEWLY_register.title("FOR NEWLY REGISTER")
    #here comes the database
    mb = mysql.connector.connect(host="localhost", user="root", password="Mahesh@123", database="spipl")
    mycursor = mb.cursor()
    #we have created table name cALLED FITTABLE
    #mycursor.execute("create table fitlogin (Firstname VARCHAR(100),lastname VARCHAR(100),phonenumber INT(100),email VARCHAR(100),username VARCHAR(100))")
    #this function fill the details of the user in the database
    def filling():
        mb = mysql.connector.connect(host="localhost", user="root", password="Mahesh@123", database="spipl")
        mycursor = mb.cursor()

        mycursor.execute("insert into fitlogin values (%s,%s,%s,%s,%s)",(firstname.get(),lastname.get(),phonenumber.get(),email.get(),username.get()))
        mb.commit()
    #here p1 is the image as the background to the window
    p1 = PhotoImage(file="block.PNG")

    l4 = Label(NEWLY_register, image=p1, height=600, width=400)
    l4.propagate(0)
    l4.place(x=0, y=0)
    #title of the window
    Label(NEWLY_register, text="NEW REGISTRATION", font=('times', 26), bg='RED', fg="BLACK", width=20).place(x=8, y=0)

    Label(NEWLY_register, text="  Frist Name   ", font=('times', 14), bg='black', fg="red").place(x=35, y=55)
    Label(NEWLY_register, text="  Last Name    ", font=('times', 14), bg='black', fg="red").place(x=35, y=105)
    firstname=StringVar()
    Entry(NEWLY_register, bd=7, width=30,textvariable=firstname).place(x=170, y=55)
    lastname = StringVar()
    Entry(NEWLY_register, bd=7, width=30,textvariable=lastname).place(x=170, y=105)
    Label(NEWLY_register, text="Phone Number", font=('times', 14), bg='black', fg="red").place(x=35, y=150)
    Label(NEWLY_register, text="Email Address", font=('times', 14), bg='black', fg="red").place(x=35, y=200)
    phonenumber = IntVar()
    Entry(NEWLY_register, bd=7, width=30,textvariable=phonenumber).place(x=170, y=150)
    email = StringVar()
    Entry(NEWLY_register, bd=7, width=30,textvariable=email).place(x=170, y=200)
    Label(NEWLY_register, text=" Date of Birth  ", font=('times', 14), bg='black', fg="red").place(x=35, y=250)
    Label(NEWLY_register, text="required package", font=('times', 14), bg='black', fg="red").place(x=35, y=310)

    def read():
        x = var1.get()
        y = var2.get()
        z = var3.get()
        lb1 = Label(text=str(x) + "/", bg='yellow').place(x=250, y=282)
        lb2 = Label(text=y + "/", bg='yellow').place(x=265, y=282)
        lb3 = Label(text=str(z), bg='yellow').place(x=310, y=282)
   #here we have used spinbox for date of biirths and the selection of the programm
    var1 = IntVar()
    var2 = StringVar()
    var3 = IntVar()
    var4 = StringVar()
    s1 = Spinbox(NEWLY_register, from_=1, to=31, textvariable=var1, width=4, fg="black", bg="lightgreen",
                 font=('Arial', 12, 'bold'))
    s2 = Spinbox(NEWLY_register,
                 values=('jan', 'Feb', 'March', 'April', 'may', 'june', 'july', 'august', 'sept', 'oct', 'nov', 'dec'),
                 textvariable=var2, width=5, fg="black", bg="lightgreen", font=('Arial', 12, 'bold'))
    s3 = Spinbox(NEWLY_register, from_=1999, to=2020, textvariable=var3, width=5, fg="black", bg="lightgreen",
                 font=('Arial', 12, 'bold'))
    s4 = Spinbox(NEWLY_register, values=('weight loss', 'body fitness', 'body building'), textvariable=var4, width=15,
                 fg="red", bg="white", font=('Arial', 14, 'bold'))
    b = Button(NEWLY_register, text="Get date of birth", command=read)
    s1.place(x=170, y=250)
    s2.place(x=230, y=250)
    s3.place(x=300, y=250)
    s4.place(x=170, y=310)
    b.place(x=150, y=280)

    mb = Menubutton(NEWLY_register, text="click here to Select duration", font=("times", 12), bg="yellow", fg="red",
                    width=35)
    mlist = Menu(mb)
    mb.config(menu=mlist)
    mlist.add_checkbutton(label="  1 month  ")
    mlist.add_checkbutton(label=" 3 months  ")
    mlist.add_checkbutton(label=" 6 months  ")
    mlist.add_checkbutton(label="  1 year   ")
    mb.place(x=40, y=350)
    chk1 = BooleanVar()
    chk1.set(False)
    ch2 = Checkbutton(NEWLY_register, text='  amount payment  ', font=('arial', 12), width='30', fg="red", var=chk1)
    ch2.place(x=40, y=390)
    chk2 = BooleanVar()
    chk2.set(False)
    ch3 = Checkbutton(NEWLY_register, text='agree with all terms and conditions ', font=('arial', 8), width='52',
                      fg="blue", var=chk2)
    ch3.place(x=40, y=550)

    Label(NEWLY_register, text="create Username ", font=('times', 14), bg='skyblue', fg="black").place(x=35, y=430)
    Label(NEWLY_register, text="create password ", font=('times', 14), bg='skyblue', fg="black").place(x=35, y=470)
    Label(NEWLY_register, text="reenter password", font=('times', 14), bg='skyblue', fg="black").place(x=35, y=510)
    username=StringVar()
    Entry(NEWLY_register, bd=7, width=30,textvariable=username).place(x=180, y=430)

    Entry(NEWLY_register, bd=7, width=30, show='*').place(x=180, y=470)
    Entry(NEWLY_register, bd=7, width=30, show='*').place(x=180, y=510)

    exit = PhotoImage(file='exit2.png')
    q = exit.subsample(4, 4)
    exit.height()
    exit.width()
    b3 = Button(NEWLY_register, image=q, height=40, width=80, command=NEWLY_register.destroy)
    b3.propagate(0)
    b3.place(x=50, y=580)

    conti = PhotoImage(file='continue2.png')
    r = conti.subsample(2, 2)
    conti.height()
    conti.width()


    b4 = Button(NEWLY_register, image=r, height=40, width=190,command=filling)
    b4.propagate(0)
    b4.place(x=170, y=580)

    NEWLY_register.mainloop()
#this function defines when the user complete his details entering in the registration form
#and give the imformation to login to the gym manamement
#here we have used the database connectivity to execute as to show all the details of the user here
def touch():
    import mysql.connector
    dbms = Toplevel(app)
    import mysql.connector
    dbms.geometry("600x620")
    dbms.title("details")
    mb = mysql.connector.connect(host="localhost", user="root", password="Mahesh@123", database="spipl")
    mycursor = mb.cursor()
    mycursor.execute("select * from fitlogin")
    x = mycursor.fetchall()
    Label(dbms, text="WELCOME TO FITNESS GYM", font=("times", 20), bg="green", fg="black").place(x=110, y=0)
    Frame(dbms, bg="gray", bd=2, cursor="arrow", height=180, width=600).place(x=0, y=30)
    Label(dbms, text="first name", font=("times,3"), bg="skyblue").place(x=10, y=40)
    Label(dbms, text="last name ", font=("times,3"), bg="skyblue").place(x=10, y=90)
    Label(dbms, text="phone number", font=("times,3"), bg="skyblue").place(x=270, y=40)
    Label(dbms, text="email address", font=("times,3"), bg="skyblue").place(x=270, y=90)
    Label(dbms, text="user name", font=("times,3"), bg="skyblue").place(x=10, y=150)
    v = 6
    for i in x:
        Label(dbms, text=i[0]).place(x=150, y=40)
        Label(dbms, text=i[1]).place(x=150, y=90)
        Label(dbms, text=i[2]).place(x=450, y=40)
        Label(dbms, text=i[3]).place(x=450, y=90)
        Label(dbms, text=i[4]).place(x=120, y=155)
        v = v
    pic1 = PhotoImage(file="Bodybuilding.png").subsample(3, 3)
    Button(dbms, image=pic1, height=200, width=300).place(x=0, y=210)
    pic2 = PhotoImage(file="WeightLoss.png").subsample(4, 4)
    Button(dbms, image=pic2, height=200, width=300).place(x=300, y=210)
    pic3 = PhotoImage(file="first.png").subsample(4, 4)
    Button(dbms, image=pic3, height=200, width=300).place(x=0, y=410)
    pic4 = PhotoImage(file="fit.png").subsample(3, 3)
    Button(dbms, image=pic4, height=200, width=300).place(x=300, y=410)
    dbms.mainloop()
#here we have created login button which take the user to the other window
#where the user login to the fit ness gym AND CHEAK details and perform operations
login=PhotoImage(file="member.png")
x=login.subsample(2,2)
login.height()
login.width()
b1=Button(root,image=x,height=40,width=175,command=touch).place(x=45, y=240)
#here when the user click the this register now button the gui hepls the user to get register
register=PhotoImage(file="register.png")
y=register.subsample(4,4)
register.height()
register.width()
b2= Button (root,image=y,height=40,width=175,command=sing_in)
b2.propagate(0)
b2.place(x=240,y=240)
#closing of the windows
#this mainloop will wait for any action to be done
app.mainloop()
