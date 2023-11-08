

import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import font as ff
from tkinter import messagebox
from PIL import ImageTk, Image
from time import sleep
import threading
import os
from tkinter import filedialog
from tkcalendar import *
import datetime
import re
import csv


a = tk.Tk()



a.title(
    "                                                                                                                                                                                       Login to Akill laptop and spare parts services")
window_width=1365
window_height=452

screen_width=a.winfo_screenwidth()
screen_height=a.winfo_screenheight()

x_cordinate=int((screen_width/3)-(window_width/3))
y_cordinate=int((screen_height/3)-(window_height/3))

# a.iconbitmap("images\SS.ico")
a.geometry("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
a.configure(background='white')
a.resizable(0, 0)


def login():
    # mydb = mysql.connector.connect(

    #     host="localhost",
    #     user="root",
    #     passwd="admin",
    #     database="laptop"
    # )


    user1 = useren.get()
    password1 = passen.get()
    # cur = mydb.cursor()
    # cur.execute("select username,password FROM login")
    # for (username, password) in cur:
    #     if user1 == "" or password1 == "":
    #         msg3=tk.messagebox.showwarning('Warning',"The Field is empty")
    #     else:
    #         if str.isupper(useren.get())==str.islower(useren.get()) or (str.isupper(passen.get()))==str.islower(passen.get()) or str.isdigit(useren.get()) or str.isdigit(passen.get()) or str.isupper(useren.get()) or str.isupper(passen.get()):
    #             msg4=messagebox.showwarning('Warning',"Numbers should not be allowed for both fields \n Capitalize characters should not be alowed")
    #         else:
    if user1=="mkd" and password1=="mkd":
        passen.delete(0, 'end')
        prorun()
        msg1 = tk.messagebox.showinfo('sign in ', "sucessfully sign in")
        logged_window()
    else:
        passen.delete(0, 'end')
        prorun()
        msg2 = tk.messagebox.showwarning('sign in error', "UserName or Password is wrong")


def clear1():
    useren.delete(0, 'end')
    passen.delete(0, 'end')


def cancel1():
    msg3 = tk.messagebox.askquestion('Warning', "Are You Sure You Want To Close")
    if msg3 == 'yes':
        a.destroy()
    else:
        print("")


def prorun():
    for i in range(101):
        sleep(0.01)
        prog['value'] = i
        prog.update()
        prog['value'] = 0


# lap = Image.open('images\Repair.jpg')
# lap1 = ImageTk.PhotoImage(lap)
# lab = tk.Label(a, image=lap1)
# lab.place(x=0, y=0)

f1 = ff.Font(size=20, family='arial', weight='bold', underline=1)
f2 = ff.Font(size=16, family='arial', weight='normal', slant='italic')
f11 = ff.Font(size=13, family='Arial', weight='bold', underline=1)

title = tk.Label(a, text='Akill Laptop And Spare Parts Service', bg='white', fg='dark blue')
title['font'] = f1
title.place(x=800, y=0)

user = tk.Label(a, text='UserName ', bg='white', fg='dark blue')
user['font'] = f2
user.place(x=820, y=100)

# useric = tk.PhotoImage(file='images\ser1.png')
# labuseric = tk.Label(a, image=useric)
# labuseric.place(x=930, y=105)

passw = tk.Label(a, text='Password ', bg='white', fg='dark blue')
passw['font'] = f2
passw.place(x=820, y=200)

# passric = tk.PhotoImage(file='images\key2.png')
# labpass = tk.Label(a, image=passric)
# labpass.place(x=930, y=205)


def mark():
    if var.get() == 1:
        passen.configure(show="")
    elif var.get() == 0:
        passen.configure(show="*")


def hoverhide(e):
    hide['bg'] = 'white'


def hoverhideleave(e):
    hide['bg'] = 'white'


var = tk.IntVar()

hide = tk.Checkbutton(a, relief=tk.FLAT, activebackground='white', command=mark, offvalue=0, onvalue=1, variable=var,
                      bg='white', bd=0, cursor='hand2')
hide.bind("<Enter>", hoverhide)
hide.bind("<Leave>", hoverhideleave)
hide.place(x=1180, y=203)

useren = tk.Entry(a, width=35, highlightbackground='blue', highlightthickness=1)
useren.focus()
useren.place(x=950, y=105)

passen = tk.Entry(a, width=35, highlightbackground='blue', highlightthickness=1, show="*")
passen.place(x=950, y=205)

prog = ttk.Progressbar(a, orient="horizontal", length=220, mode="determinate")
prog.place(x=950, y=285)


def hover(e):
    signin['bg'] = 'sky blue'


def hover_leave(e):
    signin['bg'] = 'white'


def hover1(e):
    clear['bg'] = 'sky blue'


def hover_leave1(e):
    clear['bg'] = 'white'


def hover2(e):
    cancel['bg'] = 'sky blue'


def hover_leave2(e):
    cancel['bg'] = 'white'


signin = tk.Button(a, text="Sign in", activebackground='white', bg='white', fg='blue', relief=tk.FLAT, bd=0,
                   cursor="hand2", command=login)
signin['font'] = f2
signin.bind("<Enter>", hover)
signin.bind("<Leave>", hover_leave)
signin.place(x=820, y=350)

clear = tk.Button(a, text="Clear All", activebackground='white', bg='white', fg='blue', relief=tk.FLAT, bd=0,
                  cursor="hand2", command=clear1)
clear.bind("<Enter>", hover1)
clear.bind("<Leave>", hover_leave1)
clear['font'] = f2
clear.place(x=950, y=350)

cancel = tk.Button(a, text="Cancel", activebackground='white', bg='white', fg='blue', relief=tk.FLAT, bd=0,
                   cursor="hand2", command=cancel1)
cancel.bind("<Enter>", hover2)
cancel.bind("<Leave>", hover_leave2)
cancel['font'] = f2
cancel.place(x=1095, y=350)


def logged_window():
    a.withdraw()
    home = tk.Toplevel(a)
    home.title("Sign in Window")
    # home.iconbitmap("images\SS.ico")

    window_width = 1365
    window_height = 600

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 3) - (window_height / 3))

    home.geometry("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
    home.configure(bg='white')
    home.resizable(0, 0)

    import time

    def upadte_clock():
        now1 = time.strftime("%Y-%m-%d %I:%M:%S:%p")
        time1.configure(text=now1)

    def resf():
        upadte_clock()
        threading.Timer(1, resf).start()

    frame = tk.Frame(home, relief=tk.SUNKEN, borderwidth=2, width=50, height=50)
    frame.pack(side='left', fill='both', expand=False)

    frame1 = tk.Frame(home, relief=tk.SUNKEN, borderwidth=1, bg='white')
    frame1.pack(side='top', fill='both', expand=False)

    f1 = ff.Font(size=20, family='arial', slant='italic')
    f2 = ff.Font(size=22, family='arial', weight='bold', underline=1)
    f3 = ff.Font(size=15, family='arial', weight='bold')
    f4 = ff.Font(size=30, family='arial', weight='bold')
    f5 = ff.Font(size=15, family='arial', weight='bold', underline=1)
    f6 = ff.Font(size=18, family='arial', weight='bold', underline=1)
    f7 = ff.Font(size=35, family='arial', weight='bold', underline=1)
    f10 = ff.Font(size=20, family='arial', weight='bold')

    title1 = tk.Label(home, text='Welcome to Akill Spare Parts And Services', bg='white', fg='green')
    title1['font'] = f7
    title1.place(x=300, y=250)

    now1 = time.strftime("%Y-%m-%d %I:%M:%S:%p")
    time2 = tk.Label(home)
    time2.configure(bg='white', fg='green')
    time2['font'] = f1
    time2.place(x=750, y=400)
    time2.configure(text=now1)

    logged = tk.Label(home, text='Logged by @@ :' + useren.get(), bg='white', fg='green')
    logged['font'] = f1
    logged.place(x=450, y=400)

    title1 = tk.Label(frame1, text="Akill Services", bg="white", fg="blue")
    title1['font'] = f2
    title1.pack()

    # whoic = tk.PhotoImage(file="images\ser45.png")
    # whoicl = tk.Label(frame1, image=whoic)
    # whoicl.place(x=0, y=0)

    who = tk.Label(frame1)
    who['font'] = f1
    who.configure(text=useren.get(), fg='blue', bg='white')
    who.place(x=50, y=5)

    # times = tk.PhotoImage(file="images\cal45.png")
    # timeic = tk.Label(frame1, image=times)
    # timeic.place(x=920, y=0)

    time1 = tk.Label(frame1)
    time1.configure(bg='white', fg='blue')
    time1['font'] = f3
    time1.place(x=990, y=8)
    resf()

    akill = tk.Label(frame)
    akill['font'] = f1
    akill.pack(padx=25, pady=30)

    wholog = open("./log_histroy.txt", "a")
    wholog.write(  useren.get()  )
    wholog.write(time.strftime(  " %Y-%m-%d %I:%M:%S:%p /"  ))
    wholog.close()


    def mouse(label1):

        b = tk.Toplevel(home)
        # b.iconbitmap("images\SS.ico")

        window_width = 1365
        window_height = 600

        screen_width = b.winfo_screenwidth()
        screen_height = b.winfo_screenheight()

        x_cordinate = int((screen_width / 3) - (window_width / 3))
        y_cordinate = int((screen_height / 3) - (window_height / 3))

        b.geometry("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
        b.configure(bg='white')
        b.resizable(0, 0)

        frameright = tk.Frame(b, relief=tk.SUNKEN, borderwidth=2, width=50, height=50, bg='white')
        frameright.pack(side='left', fill='both', expand=False)

        frametop = tk.Frame(b, relief=tk.SUNKEN, borderwidth=1, bg='white')
        frametop.pack(side='top', fill='both', expand=False)

        # whoic = tk.PhotoImage(file="images\ser45.png")
        # whoicl = tk.Label(frametop, image=whoic)
        # whoicl.place(x=0, y=0)

        who = tk.Label(frametop)
        who['font'] = f1
        who.configure(text=useren.get(), fg='blue', bg='white')
        who.place(x=50, y=5)

        # times = tk.PhotoImage(file="images\cal45.png")
        # timeic = tk.Label(frametop, image=times)
        # timeic.place(x=920, y=0)

        def upadte_clock():
            now1 = time.strftime("%Y-%m-%d %I:%M:%S:%p")
            time1.configure(text=now1)

        def resf():
            upadte_clock()
            threading.Timer(1, resf).start()

        time1 = tk.Label(frametop)
        time1.configure(bg='white', fg='blue')
        time1['font'] = f3
        time1.place(x=990, y=8)
        resf()

        title1 = tk.Label(frametop, text="Akill Services", bg="white", fg="blue")
        title1['font'] = f2
        title1.pack()

        akill = tk.Label(frameright, text='Akill', bg='white', fg='white')
        akill['font'] = f1
        akill.pack(padx=25, pady=30)

        titlemc = tk.Label(b, text="Akill Laptop And Spare Parts Service", bg='white', fg='blue')
        titlemc['font'] = f4
        titlemc.place(x=450, y=100)

        infor = tk.Label(b,
                         text="Our Services........\n\n1.Laptop hardware repair\n2.Laptop software update\n3.Os installization\n4.Game store\n5.spare parts available",
                         fg='blue', bg='white')
        infor['font'] = f3
        infor.place(x=200, y=200)

        disclaimer = tk.Label(b,
                              text="Disclaimer........\n\nIf you see any error in this application immediately\ncall the programmer",
                              bg='white', fg='blue')
        disclaimer['font'] = f3
        disclaimer.place(x=880, y=200)

        # now1 = time.strftime("%Y-%m-%d %I:%M:%S:%p")
        # time2 = tk.Label(b)
        # time2.configure(bg='white', fg='blue')
        # time2['font'] = f1
        # time2.place(x=780, y=500)
        # time2.configure(text=now1)

        logged = tk.Label(b, text='Logged by @@ :' + useren.get(), bg='white', fg='green')
        logged['font'] = f1
        logged.place(x=600, y=350)

        def file_open():
            msg11 = tk.messagebox.askquestion("Open a File", 'You Want To Open')
            if msg11 == 'yes':
                fileopen1 = filedialog.askopenfilename(initialdir='properties\log_histroy')
                os.system('"%s"' % fileopen1)
            else:
                print("")

        def hover16(e):
            filebtn['bg'] = 'sky blue'

        def hover_leave16(e):
            filebtn['bg'] = 'white'

        filebtn = tk.Button(b, text="Log Histroy", activebackground='red', bg='white', fg='blue', cursor='hand2', bd=0,
                            relief=tk.FLAT, command=file_open)
        filebtn['font'] = f6
        filebtn.bind("<Enter>", hover16)
        filebtn.bind("<Leave>", hover_leave16)
        filebtn.place(x=600, y=450)

        b.mainloop()

    def userinfo1(label1):
        global entry0, entry1, entry2, entry3, entry4,entry5,valide_email

        # mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", db="laptop")

        # cursor = mydb.cursor()


        from tkinter import filedialog

        c=tk.Toplevel(home)

        window_width = 1365
        window_height = 600

        screen_width = c.winfo_screenwidth()
        screen_height = c.winfo_screenheight()

        x_cordinate = int((screen_width / 3) - (window_width / 3))
        y_cordinate = int((screen_height / 3) - (window_height / 3))

        c.geometry("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))

        # c.iconbitmap("images\SS.ico")
        c.configure(bg='white')
        c.resizable(0, 0)

        frameright = tk.Frame(c, relief=tk.SUNKEN, borderwidth=2, width=50, height=50, bg='white')
        frameright.pack(side='left', fill='both', expand=False)

        frametop = tk.Frame(c, relief=tk.SUNKEN, borderwidth=1, bg='white')
        frametop.pack(side='top', fill='both', expand=False)

        # whoic = tk.PhotoImage(file="images\ser45.png")
        # whoicl = tk.Label(frametop, image=whoic)
        # whoicl.place(x=0, y=0)

        who = tk.Label(frametop)
        who['font'] = f1
        who.configure(text=useren.get(), fg='blue', bg='white')
        who.place(x=50, y=5)

        # times = tk.PhotoImage(file="images\cal45.png")
        # timeic = tk.Label(frametop, image=times)
        # timeic.place(x=920, y=0)

        def upadte_clock():
            now1 = time.strftime("%Y-%m-%d %I:%M:%S:%p")
            time1.configure(text=now1)

        def resf():
            upadte_clock()
            threading.Timer(1, resf).start()

        time1 = tk.Label(frametop)
        time1.configure(bg='white', fg='blue')
        time1['font'] = f3
        time1.place(x=990, y=8)
        resf()

        serialnumber = tk.StringVar()
        username = tk.StringVar()
        userphone = tk.StringVar()
        useraddress = tk.StringVar()
        laptopname = tk.StringVar()
        email_id_address=tk.StringVar()

        valide_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


        def onselected(event):
            cur = tree.focus()
            content = tree.item(cur)
            select = content['values']
            serialnumber.set("")
            username.set("")
            userphone.set("")
            useraddress.set("")
            laptopname.set("")
            email_id_address.set("")
            serialnumber.set(select[0])
            username.set(select[1])
            userphone.set(select[2])
            useraddress.set(select[3])
            laptopname.set(select[4])
            email_id_address.set(select[5])
            updatewindow = tk.Toplevel()
            updatewindow.title("Contact list")
            updatewindow.iconbitmap("images\SS.ico")
            updatewindow.geometry('600x630')
            updatewindow.resizable(0, 0)
            updatewindow.configure(background='white')

            labels1 = tk.Label(updatewindow, text='Updating contact', bg='white', fg='green')
            labels1['font'] = f1
            labels1.place(x=250, y=0)

            labels2 = tk.Label(updatewindow, text='Serial (N) : ', bg='white', fg='blue')
            labels2['font'] = f3
            labels2.place(x=50, y=100)

            labels3 = tk.Label(updatewindow, text='User Name : ', bg='white', fg='blue')
            labels3['font'] = f3
            labels3.place(x=50, y=200)

            labels4 = tk.Label(updatewindow, text='User Phone(N) : ', bg='white', fg='blue')
            labels4['font'] = f3
            labels4.place(x=50, y=300)

            labels5 = tk.Label(updatewindow, text='User Address : ', bg='white', fg='blue')
            labels5['font'] = f3
            labels5.place(x=50, y=400)

            labels6 = tk.Label(updatewindow, text='LapTop Name : ', bg='white', fg='blue')
            labels6['font'] = f3
            labels6.place(x=50, y=500)


            labels7 = tk.Label(updatewindow, text='Email ID : ', bg='white', fg='blue')
            labels7['font'] = f3
            labels7.place(x=50, y=580)


            entrys1 = tk.Entry(updatewindow, width=25, textvariable=serialnumber, highlightbackground='blue',
                               highlightthickness=1)
            entrys1.place(x=200, y=105)

            entrys2 = tk.Entry(updatewindow, width=25, textvariable=username, highlightbackground='blue',
                               highlightthickness=1)
            entrys2.place(x=200, y=205)

            entrys3 = tk.Entry(updatewindow, textvariable=userphone, width=25, highlightbackground='blue',
                               highlightthickness=1)
            entrys3.place(x=206, y=305)

            entrys4 = tk.Entry(updatewindow, textvariable=useraddress, width=25, highlightbackground='blue',
                               highlightthickness=1)
            entrys4.place(x=200, y=405)

            entrys5 = tk.Entry(updatewindow, textvariable=laptopname, width=25, highlightbackground='blue',
                               highlightthickness=1)
            entrys5.place(x=200, y=505)

            entrys6 = tk.Entry(updatewindow, textvariable=email_id_address, width=25, highlightbackground='blue',
                               highlightthickness=1)
            entrys6.place(x=200, y=585)

            def pdfnew():
                from fpdf import FPDF
                psf = FPDF()
                psf.add_page()
                psf.set_font("Arial", size=15, )
                psf.cell(200, 15, txt="Akill LapTop And Spare Parts Services", ln=1, align='C')
                psf.cell(200, 20, txt="Serial Number : " + entrys1.get(), ln=2, align='C')
                psf.cell(200, 20, txt="User Name : " + entrys2.get(), ln=3, align='C')
                psf.cell(200, 20, txt="User Phone(N) : " + entrys3.get(), ln=4, align='C')
                psf.cell(200, 20, txt="User Address :  " + entrys4.get(), ln=5, align='C')
                psf.cell(200, 20, txt="LapTop Name : " + entrys5.get(), ln=6, align='C')
                psf.cell(200, 20, txt="Email ID: " + entrys6.get(), ln=7, align='C')

                now=datetime.datetime.now()
                now_str = now.strftime(" %Y-%m-%d-%I-%M-%S-%p")
                psf.output(r'properties\\userinfo\\userinfo{}.pdf'.format(now_str))
                msg8 = tk.messagebox.askquestion('Open', "Are You Sure You Want To Open")
                if msg8 == "yes":
                    filename = filedialog.askopenfilename(initialdir=r"properties\\userinfo", title="Select A File",
                                                          filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
                    os.system('"%s"' % filename)
                else:
                    print("")

            def Updates():
                global meme
                serialnumber = entrys1.get()
                username = entrys2.get()
                userphone = entrys3.get()
                useraddress = entrys4.get()
                laptopname = entrys5.get()
                email_id_address=entrys6.get()

                if (serialnumber == "" or username == "" or userphone == "" or useraddress == "" or laptopname == "" or email_id_address==""):
                    msg6 = tk.messagebox.showwarning('Warning', "First Enter The Items")

                else:
                    if str.isdigit(entrys1.get()) == str.isalpha(entrys1.get()) or str.isalpha(
                            entrys1.get()) or str.isalpha(entrys2.get()) == str.isdigit(entrys2.get()) or str.isdigit(
                        entrys2.get()) or str.isdigit(
                        entrys3.get()) == str.isalpha(entrys3.get() or str.isalpha(entrys3.get())):
                        msg1 = tk.messagebox.showerror('Error',
                                                       "only numbers should be used for serial number \n \n only characters should be used for user name \n \n only numbers should be used for phone number ")
                    else:
                        if len(entrys2.get()) > 16 or len(entrys3.get()) > 10 or len(entrys3.get()) < 10 or len(
                                entrys5.get()) > 10:
                            msg2 = tk.messagebox.showerror('Error',
                                                           "user name should be allowed below 16 \n \n phone number should be allowed above or below 10 \n \n laptop name should be allowed below 10")
                        else:
                            if (re.search(valide_email,entrys6.get())):

                                mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="admin",
                                    db="laptop")
                                cursor = mydb.cursor()
                                cursor.execute(
                                    "update userinformation set username='" + username + "',userphone='" + userphone + "',useraddress='" + useraddress + "',laptop='" + laptopname + "',Email_id='" + email_id_address + "'  where sno='" + serialnumber + "'")

                                mydb.commit()
                                # entrys1.delete(0, 'end')
                                # entrys2.delete(0, 'end')
                                # entrys3.delete(0, 'end')
                                # entrys4.delete(0, 'end')
                                # entrys5.delete(0, 'end')

                                tree.delete(*tree.get_children())
                                show()
                            else:
                                msg=messagebox.showwarning('Warning',"Please check the Email ID")

            def hover3(e):
                btns['bg'] = 'sky blue'

            def hover_leave3(e):
                btns['bg'] = 'white'

            def hover4(e):
                btnpdf['bg'] = 'sky blue'

            def hover_leave4(e):
                btnpdf['bg'] = 'white'

            btns = tk.Button(updatewindow, text='Update', activebackground='white', bg='white', fg='blue',
                             relief=tk.FLAT, bd=0, cursor="hand2", command=Updates)
            btns['font'] = f3
            btns.bind("<Enter>", hover3)
            btns.bind("<Leave>", hover_leave3)
            btns.place(x=430, y=250)

            btnpdf = tk.Button(updatewindow, text='Print', activebackground='white', bg='white', fg='blue',
                               relief=tk.FLAT, bd=0, cursor="hand2", command=pdfnew)
            btnpdf['font'] = f3
            btnpdf.bind("<Enter>", hover4)
            btnpdf.bind("<Leave>", hover_leave4)
            btnpdf.place(x=430, y=350)

        title1 = tk.Label(frametop, text="Akill Services", bg="white", fg="blue")
        title1['font'] = f2
        title1.pack()

        akill = tk.Label(frameright, text='Akill', bg='white', fg='white')
        akill['font'] = f1
        akill.pack(padx=25, pady=30)

        titleuse = tk.Label(c, text='USER INFORMATION', bg='white', fg='blue')
        titleuse['font'] = f2
        titleuse.place(x=585, y=50)

        serial = tk.Label(c, text='Serial (N) : ', bg='white', fg='blue')
        serial['font'] = f3
        serial.place(x=150, y=100)

        email_id_lab=tk.Label(c,text="Email ID : ",bg='white',fg='blue')
        email_id_lab['font']=f3
        email_id_lab.place(x=600,y=105)

        userl = tk.Label(c, text='User Name : ', bg='white', fg='blue')
        userl['font'] = f3
        userl.place(x=150, y=150)

        user2 = tk.Label(c, text='User Phone(N) : ', bg='white', fg='blue')
        user2['font'] = f3
        user2.place(x=150, y=250)

        entry0 = tk.StringVar()
        entry1 = tk.StringVar()
        entry2 = tk.StringVar()
        entry3 = tk.StringVar()
        entry4 = tk.StringVar()
        entry5 = tk.StringVar()
        search_get=tk.StringVar()

        userinfoen0 = tk.Entry(c, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry0)
        userinfoen0.focus()
        userinfoen0.place(x=350, y=105)

        userinfoemail=tk.Entry(c,width=25,highlightbackground='blue',highlightthickness=1,textvariable=entry5)
        userinfoemail.place(x=800,y=105)

        userinfoen1 = tk.Entry(c, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry1)
        userinfoen1.place(x=350, y=155)

        userinfoen2 = tk.Entry(c, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry2)
        userinfoen2.place(x=350, y=255)

        user3 = tk.Label(c, text='User Address : ', bg='white', fg='blue')
        user3['font'] = f3
        user3.place(x=600, y=150)

        user4 = tk.Label(c, text='LapTop Name : ', bg='white', fg='blue')
        user4['font'] = f3
        user4.place(x=600, y=250)

        search=tk.Label(c,text="Search : ",bg='white',fg='blue')
        search['font']=f3
        search.place(x=150,y=300)

        search_entry=tk.Entry(c,width=25,highlightbackground='blue',highlightthickness=1,textvariable=search_get)
        search_entry.place(x=300,y=305)

        userinfoen3 = tk.Entry(c, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry3)
        userinfoen3.place(x=800, y=155)

        userinfoen4 = tk.Entry(c, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry4)
        userinfoen4.place(x=800, y=255)

        table = tk.Frame(c, width=500)
        table.pack(side='bottom')

        scrollx = tk.Scrollbar(table, orient='horizontal')
        scrolly = tk.Scrollbar(table, orient='vertical')
        tree = ttk.Treeview(table,
                            columns=("Serial Number", "User Name", "User Address", "User Phone(N)", "LapTop Name","Email ID"),
                            selectmode='extended', yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.config(command=tree.yview)
        scrolly.pack(side="right", fill="y")
        scrollx.config(command=tree.xview)
        scrollx.pack(side="bottom", fill="x")

        tree['column'] = ('1', '2', '3', '4', '5','6')
        tree['show'] = 'headings'
        tree.heading('1', text='                      Serial Number', anchor='w')
        tree.heading('2', text='                      User Name', anchor='w')
        tree.heading('3', text='                      User Phone(N)', anchor='w')
        tree.heading('4', text='                      User Address', anchor='w')
        tree.heading('5', text='                      LapTop Name', anchor='w')
        tree.heading('6', text='                      Email ID', anchor='w')
        tree.column('1', stretch='0', minwidth=0, anchor='c')
        tree.column('2', stretch='0', minwidth=0, anchor='c')
        tree.column('3', stretch='0', minwidth=0, anchor='c')
        tree.column('4', stretch='0', minwidth=0, anchor='c')
        tree.column('5', stretch='0', minwidth=0, anchor='c')
        tree.column('6', stretch='0', minwidth=0, anchor='c')
        tree.bind('<Double-Button-1>', onselected)
        tree.pack()



        def add1():

            userserial = userinfoen0.get()
            userenname = userinfoen1.get()
            userenphone = userinfoen2.get()
            userenaddress = userinfoen3.get()
            userenlaptop = userinfoen4.get()
            email_id_address=userinfoemail.get()

            if (userserial == "" or userenname == "" or userenphone == "" or userenaddress == "" or userenlaptop == "" or email_id_address==""):
                msg1 = tk.messagebox.showwarning('Warning', "First Enter The Items ", icon='warning')
            else:
                if str.isdigit(userinfoen0.get()) == str.isalpha(userinfoen0.get()) or str.isalpha(
                        userinfoen0.get()) or str.isdigit(userinfoen1.get()) or str.isdigit(
                        userinfoen2.get()) == str.isalpha(userinfoen2.get() or str.isalpha(userinfoen2.get())):
                    msg1 = tk.messagebox.showerror('Error',
                                                   "only numbers should be used for serial number \n \n only characters should be used for user name \n \n only numbers should be used for phone number ")
                else:
                    if len(userinfoen1.get()) > 16 or len(userinfoen2.get()) > 10 or len(userinfoen2.get()) < 10 or len(
                            userinfoen4.get()) > 10:
                        msg2 = tk.messagebox.showerror('Error',
                                                       "user name should be allowed below 16 \n \n phone number should be allowed above or below 10 \n \n laptop name should be allowed below 10")
                    else:
                        if(re.search(valide_email,userinfoemail.get())):

                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="admin",
                                db="laptop")

                            cursor = mydb.cursor()
                            cursor.execute(
                                "insert into userinformation values('" + userserial + "','" + userenname + "','" + userenphone + "','" + userenaddress + "','" + userenlaptop + "','" + email_id_address + "')")

                            mydb.commit()

                            # userinfoen0.delete(0, 'end')
                            # userinfoen1.delete(0, 'end')
                            # userinfoen2.delete(0, 'end')
                            # userinfoen3.delete(0, 'end')
                            # userinfoen4.delete(0, 'end')
                            show()

                            msg2 = tk.messagebox.showinfo('ADD', "ADD sucessfully")
                            cursor.close()
                            mydb.close()
                        else:
                            msg=messagebox.showwarning('Warning',"please check your Email ID")

        def show():

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="admin",
                db="laptop")
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM userinformation ORDER BY sno ASC")
            rows = cursor.fetchall()
            tree.delete(*tree.get_children())

            for row in rows:
                tree.insert('', 'end', values=(row))

            # msg3 = tk.messagebox.showinfo('View', "Viewed  sucessfully")
            mydb.close()

        def delete():

            if userinfoen0.get() == "":
                msg13 = tk.messagebox.showwarning('Serial Number', "For delete Serial Number is compulsory")
            else:
                if str.isalpha(userinfoen0.get()) or str.isdigit(userinfoen1.get()) or str.isalpha(userinfoen2.get()):
                    msg1 = tk.messagebox.showerror('Error',
                                                   "only numbers should be used for serial number \n \n only characters should be used for user name \n \n only numbers should be used for phone number ")

                else:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="admin",
                        db="laptop")
                    cursor = mydb.cursor()
                    cursor.execute("delete from userinformation where sno='" + userinfoen0.get() + "'")
                    mydb.commit()

                    userinfoen0.delete(0, 'end')
                    userinfoen1.delete(0, 'end')
                    userinfoen2.delete(0, 'end')
                    userinfoen3.delete(0, 'end')
                    userinfoen4.delete(0, 'end')
                    userinfoemail.delete(0,'end')
                    show()

                    msg14 = tk.messagebox.showinfo('Delete', "Deleted sucessfully")
                    mydb.close()

        def update():

            userserial = userinfoen0.get()
            userenname = userinfoen1.get()
            userenphone = userinfoen2.get()
            userenaddress = userinfoen3.get()
            userenlaptop = userinfoen4.get()
            email_id_address=userinfoemail.get()

            if (
                    userserial == " " or userenname == "" or userenphone == "" or userenaddress == "" or userenlaptop == "" or email_id_address==""):
                msg1 = tk.messagebox.showwarning('Warning', "First Enter The Item ", icon='warning')
            else:
                if str.isdigit(userinfoen0.get()) == str.isalpha(userinfoen0.get()) or str.isalpha(
                        userinfoen0.get()) or str.isdigit(userinfoen1.get()) or str.isdigit(
                        userinfoen2.get()) == str.isalpha(userinfoen2.get() or str.isalpha(userinfoen2.get())):
                    msg1 = tk.messagebox.showerror('Error',
                                                   "only numbers should be used for serial number \n \n only characters should be used for user name \n \n only numbers should be used for phone number ")
                else:
                    if len(userinfoen1.get()) > 16 or len(userinfoen2.get()) > 10 or len(userinfoen2.get()) < 10 or len(
                            userinfoen4.get()) > 10:
                        msg2 = tk.messagebox.showerror('Error',
                                                       "user name should be allowed below 16 \n \n phone number should be allowed above or below 10 \n \n laptop name should be allowed below 10")
                    else:
                        if (re.search(valide_email,userinfoemail.get())):

                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="admin",
                                db="laptop")

                            cursor = mydb.cursor()
                            cursor.execute(
                                "update userinformation set username='" + userenname + "',userphone='" + userenphone + "',useraddress='" + userenaddress + "',laptop='" + userenlaptop + "',Email_id='" + email_id_address +"' where sno='" + userserial + "'")

                            mydb.commit()

                            userinfoen0.delete(0, 'end')
                            userinfoen1.delete(0, 'end')
                            userinfoen2.delete(0, 'end')
                            userinfoen3.delete(0, 'end')
                            userinfoen4.delete(0, 'end')
                            userinfoemail.delete(0,'end')
                            show()

                            msg2 = tk.messagebox.showinfo('Update', "Update sucessfully")
                            cursor.close()
                            mydb.close()
                        else:
                            msg=messagebox.showwarning('Warning',"Please check the Email ID")

        def clear1():

            userserial = userinfoen0.get()
            userenname = userinfoen1.get()
            userenphone = userinfoen2.get()
            userenaddress = userinfoen3.get()
            userenlaptop = userinfoen4.get()
            email_id=userinfoemail.get()

            if (
                    userserial == "" and userenname == "" and userenphone == "" and userenaddress == "" and userenlaptop == "" and email_id==""):
                msg4 = tk.messagebox.showwarning('Clear', "All Ready Cleared")
            else:
                userinfoen0.delete(0, 'end')
                userinfoen1.delete(0, 'end')
                userinfoen2.delete(0, 'end')
                userinfoen3.delete(0, 'end')
                userinfoen4.delete(0, 'end')
                userinfoemail.delete(0,'end')
                msg19 = tk.messagebox.showinfo('Clear', "Cleared sucessfully")

        def search_for_update(rows):

            tree.delete(*tree.get_children())
            for i in rows:
                tree.insert("",'end',values=i)

            query = "select sno,username,userphone,useraddress,laptop,Email_id from userinformation"
            # cursor.execute(query)
            # rows = cursor.fetchall()
            search_for_update()


        def search_find():

            if len(tree.get_children()) < 1:
                msg=messagebox.showerror('Error'," No Records found !!! ")
            else:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="admin",
                    db="laptop")

                cursor = mydb.cursor()
                search_give = search_get.get()
                query = "select sno ,username,userphone,useraddress,laptop,Email_id FROM userinformation WHERE  username LIKE '%" + search_give + "%' OR userphone LIKE '%" + search_give + "%' OR Email_id LIKE '%" + search_give + "%' "
                cursor.execute(query)
                global rows
                rows = cursor.fetchall()
                search_for_update(rows)

        def con_to_excel():

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="admin",
                db="laptop")
            cursor = mydb.cursor()
            now = datetime.datetime.now()
            now_str = now.strftime(" %Y-%m-%d-%I-%M-%S-%p")
            cursor.execute("select * from userinformation ORDER by sno ASC")
            result=cursor.fetchall()
            with open('properties/userinfo/userinformation_excel{}.csv'.format(now_str),'a') as f:
                w=csv.writer(f,dialect='excel')
                for records in result:
                    w.writerow(records)
            msg5 = tk.messagebox.showinfo('Excel', "Sucessfully Converted")
            msgnew = tk.messagebox.askquestion('Open', "You Want To Open")
            if msgnew == 'yes':
                        file = filedialog.askopenfilename(initialdir=r"properties\\userinfo",
                                                          title="Select A File",
                                                          filetypes=(("excel files", "*.csv"), ("all files", "*.*")))
                        os.system('"%s"' % file)
            else:
                print("")

        def hover5(e):
            add['bg'] = 'sky blue'

        def hover_leave5(e):
            add['bg'] = "white"

        def hover6(e):
            update1['bg'] = 'sky blue'

        def hover_leave6(e):
            update1['bg'] = "white"

        def hover7(e):
            delete1['bg'] = 'sky blue'

        def hover_leave7(e):
            delete1['bg'] = "white"

        def hover8(e):
            view['bg'] = 'sky blue'

        def hover_leave8(e):
            view['bg'] = "white"

        def hover9(e):
            clearc['bg'] = 'sky blue'

        def hover_leave9(e):
            clearc['bg'] = "white"

        def hover10(e):
            excel['bg'] = 'sky blue'

        def hover_leave10(e):
            excel['bg'] = "white"

        def hover_enter_search(e):
            search_btn['bg'] = 'sky blue'

        def hover_leave_search(e):
            search_btn['bg'] = "white"

        add = tk.Button(c, text="Add", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                        cursor="hand2", command=add1)
        add['font'] = f6
        add.bind("<Enter>", hover5)
        add.bind("<Leave>", hover_leave5)
        add.place(x=1200, y=50)

        update1 = tk.Button(c, text="Update", activebackground='red', fg='black', bg='white', bd=0, relief=tk.FLAT,
                            cursor="hand2", command=update)
        update1['font'] = f6
        update1.bind("<Enter>", hover6)
        update1.bind("<Leave>", hover_leave6)
        update1.place(x=1200, y=100)

        delete1 = tk.Button(c, text="Delete", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                            cursor="hand2", command=delete)
        delete1['font'] = f6
        delete1.bind("<Enter>", hover7)
        delete1.bind("<Leave>", hover_leave7)
        delete1.place(x=1200, y=150)

        view = tk.Button(c, text="View All", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                         cursor="hand2", command=show)
        view['font'] = f6
        view.bind("<Enter>", hover8)
        view.bind("<Leave>", hover_leave8)
        view.place(x=1200, y=200)

        clearc = tk.Button(c, text="Clear All", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                           cursor="hand2", command=clear1)
        clearc['font'] = f6
        clearc.bind("<Enter>", hover9)
        clearc.bind("<Leave>", hover_leave9)
        clearc.place(x=1200, y=300)

        excel = tk.Button(c, text="Con to Excel", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                          cursor="hand2", command=con_to_excel)
        excel['font'] = f6
        excel.bind("<Enter>", hover10)
        excel.bind("<Leave>", hover_leave10)
        excel.place(x=1200, y=250)

        search_btn=tk.Button(c,text='Search',activebackground='red',fg='blue',bg='white',relief=tk.FLAT,bd=0,cursor='hand2',command=search_find)
        search_btn['font']=f6
        search_btn.bind("<Enter>",hover_enter_search)
        search_btn.bind("<Leave>", hover_leave_search)
        search_btn.place(x=500,y=290)


        c.mainloop()

    def spare(label1):

        d = tk.Toplevel(home)

        window_width = 1365
        window_height = 600

        screen_width = d.winfo_screenwidth()
        screen_height =d.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 3) - (window_height / 3))

        d.geometry("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
        d.iconbitmap("images\SS.ico")
        d.configure(bg='white')
        d.resizable(0, 0)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", db="laptop")

        cursor = mydb.cursor()

        frameright = tk.Frame(d, relief=tk.SUNKEN, borderwidth=2, width=50, height=50, bg='white')
        frameright.pack(side='left', fill='both', expand=False)

        frametop = tk.Frame(d, relief=tk.SUNKEN, borderwidth=1, bg='white')
        frametop.pack(side='top', fill='both', expand=False)

        whoic = tk.PhotoImage(file="images\ser45.png")
        whoicl = tk.Label(frametop, image=whoic)
        whoicl.place(x=0, y=0)

        who = tk.Label(frametop)
        who['font'] = f1
        who.configure(text=useren.get(), fg='blue', bg='white')
        who.place(x=50, y=5)

        times = tk.PhotoImage(file="images\cal45.png")
        timeic = tk.Label(frametop, image=times)
        timeic.place(x=920, y=0)

        def upadte_clock():
            now1 = time.strftime("%Y-%m-%d %I:%M:%S:%p")
            time1.configure(text=now1)

        def resf():
            upadte_clock()
            threading.Timer(1, resf).start()

        time1 = tk.Label(frametop)
        time1.configure(bg='white', fg='blue')
        time1['font'] = f3
        time1.place(x=990, y=8)
        resf()

        serialnumber = tk.StringVar()
        laptopname = tk.StringVar()
        laptopmodel = tk.StringVar()
        laptopsn = tk.StringVar()
        ratemrp = tk.StringVar()
        search_get = tk.StringVar()


        def onselected(event):
            cur = tree.focus()
            content = tree.item(cur)
            select = content['values']
            serialnumber.set("")
            laptopname.set("")
            laptopmodel.set("")
            laptopsn.set("")
            ratemrp.set("")
            serialnumber.set(select[0])
            laptopname.set(select[1])
            laptopmodel.set(select[2])
            laptopsn.set(select[3])
            ratemrp.set(select[4])
            updatewindow = tk.Toplevel()
            updatewindow.title("Contact list")
            updatewindow.iconbitmap("images\SS.ico")
            updatewindow.geometry('600x600')
            updatewindow.resizable(0, 0)
            updatewindow.configure(background='white')

            labels1 = tk.Label(updatewindow, text='Updating Spare', bg='white', fg='green')
            labels1['font'] = f1
            labels1.place(x=250, y=0)

            labels2 = tk.Label(updatewindow, text='Serial (N)             : ', bg='white', fg='blue')
            labels2['font'] = f3
            labels2.place(x=50, y=100)

            labels3 = tk.Label(updatewindow, text='LapTop Name      : ', bg='white', fg='blue')
            labels3['font'] = f3
            labels3.place(x=50, y=200)

            labels4 = tk.Label(updatewindow, text='LapTop Model(N) : ', bg='white', fg='blue')
            labels4['font'] = f3
            labels4.place(x=50, y=300)

            labels5 = tk.Label(updatewindow, text='Spare Name         : ', bg='white', fg='blue')
            labels5['font'] = f3
            labels5.place(x=50, y=400)

            labels6 = tk.Label(updatewindow, text='Rate Mrp             : ', bg='white', fg='blue')
            labels6['font'] = f3
            labels6.place(x=50, y=500)

            entrys1 = tk.Entry(updatewindow, width=25, textvariable=serialnumber, highlightbackground='blue',
                               highlightthickness=1)
            entrys1.place(x=240, y=105)

            entrys2 = tk.Entry(updatewindow, width=25, textvariable=laptopname, highlightbackground='blue',
                               highlightthickness=1)
            entrys2.place(x=240, y=205)

            entrys3 = tk.Entry(updatewindow, textvariable=laptopmodel, width=25, highlightbackground='blue',
                               highlightthickness=1)
            entrys3.place(x=240, y=305)

            entrys4 = tk.Entry(updatewindow, textvariable=laptopsn, width=25, highlightbackground='blue',
                               highlightthickness=1)
            entrys4.place(x=240, y=405)

            entrys5 = tk.Entry(updatewindow, textvariable=ratemrp, width=25, highlightbackground='blue',
                               highlightthickness=1)
            entrys5.place(x=240, y=505)

            def pdfnew():
                from fpdf import FPDF
                psf = FPDF()
                psf.add_page()
                psf.set_font("Arial", size=15, )
                psf.cell(200, 15, txt="Akill LapTop And Spare Parts Services", ln=1, align='C')
                psf.cell(200, 20, txt="Serial Number : " + entrys1.get(), ln=2, align='C')
                psf.cell(200, 20, txt="LapTop Name : " + entrys2.get(), ln=3, align='C')
                psf.cell(200, 20, txt="LapTop Model(N) : " + entrys3.get(), ln=4, align='C')
                psf.cell(200, 20, txt="Spare Name :  " + entrys4.get(), ln=5, align='C')
                psf.cell(200, 20, txt="Rate Mrp : " + entrys5.get(), ln=6, align='C')

                now = datetime.datetime.now()
                now_str = now.strftime(" %Y-%m-%d-%I-%M-%S-%p")

                psf.output('properties\spareinfo\spareinfo{}.pdf'.format(now_str))
                msg8 = tk.messagebox.askquestion('Open', "Are You Sure You Want To Open")
                if msg8 == "yes":
                    filename = filedialog.askopenfilename(initialdir="properties\spareinfo", title="Select A File",
                                                          filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
                    os.system('"%s"' % filename)

                else:
                    print("")

            def Updates():
                global meme
                serialnumber = entrys1.get()
                laptopnameen = entrys2.get()
                laptopmodelen = entrys3.get()
                sparenameen = entrys4.get()
                ratemrpen = entrys5.get()

                if (
                        serialnumber == "" or laptopnameen == "" or laptopmodelen == "" or sparenameen == "" or ratemrpen == ""):
                    msg6 = tk.messagebox.showwarning('Warning', "First Enter The Item")
                else:
                    if str.isdigit(entrys1.get()) == str.isalpha(entrys1.get()) or str.isalpha(
                            entrys1.get()) or str.isalpha(entrys2.get()) == str.isdigit(entrys2.get()) or str.isdigit(
                        entrys2.get()) or str.isdigit(
                        entrys5.get()) == str.isalpha(entrys5.get() or str.isalpha(entrys5.get())):
                        msg1 = tk.messagebox.showerror('Error',
                                                       "only numbers should be used for serial number \n \n only characters should be used for user name \n \n only numbers should be used for Rate Mrp ")
                    else:
                        if len(entrys2.get()) > 16:
                            msg2 = tk.messagebox.showerror('Error',
                                                           "user name should be allowed below 16 ")  # \n \n phone number should be allowed above or below 10 \n \n laptop name should be allowed below 10")
                        else:
                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="admin",
                                db="laptop")
                            cursor = mydb.cursor()
                            cursor.execute(
                                "update spareinformation set laptopname='" + laptopnameen + "',laptopmodel='" + laptopmodelen + "',sparename='" + sparenameen + "',ratemrp='" + ratemrpen + "' where sno='" + serialnumber + "'")

                            mydb.commit()
                            # entrys1.delete(0, 'end')
                            # entrys2.delete(0, 'end')
                            # entrys3.delete(0, 'end')
                            # entrys4.delete(0, 'end')
                            # entrys5.delete(0, 'end')

                            tree.delete(*tree.get_children())
                            show()

            def hover3(e):
                btns['bg'] = 'sky blue'

            def hover_leave3(e):
                btns['bg'] = 'white'

            def hover4(e):
                btnpdf['bg'] = 'sky blue'

            def hover_leave4(e):
                btnpdf['bg'] = 'white'

            btns = tk.Button(updatewindow, text='Update', activebackground='white', bg='white', fg='blue',
                             relief=tk.FLAT, bd=0, cursor="hand2", command=Updates)
            btns['font'] = f3
            btns.bind("<Enter>", hover3)
            btns.bind("<Leave>", hover_leave3)
            btns.place(x=430, y=250)

            btnpdf = tk.Button(updatewindow, text='Print', activebackground='white', bg='white', fg='blue',
                               relief=tk.FLAT, bd=0, cursor="hand2", command=pdfnew)
            btnpdf['font'] = f3
            btnpdf.bind("<Enter>", hover4)
            btnpdf.bind("<Leave>", hover_leave4)
            btnpdf.place(x=430, y=350)

        title1 = tk.Label(frametop, text="Akill Services", bg="white", fg="blue")
        title1['font'] = f2
        title1.pack()

        akill = tk.Label(frameright, text='Akill', bg='white', fg='white')
        akill['font'] = f1
        akill.pack(padx=25, pady=30)

        titleuse = tk.Label(d, text='SPARE INFORMATION', bg='white', fg='blue')
        titleuse['font'] = f2
        titleuse.place(x=585, y=50)

        serial = tk.Label(d, text='Serial (N) : ', bg='white', fg='blue')
        serial['font'] = f3
        serial.place(x=150, y=100)

        userl = tk.Label(d, text='Laptop Name : ', bg='white', fg='blue')
        userl['font'] = f3
        userl.place(x=150, y=150)

        user2 = tk.Label(d, text='Laptop Model(N) : ', bg='white', fg='blue')
        user2['font'] = f3
        user2.place(x=150, y=250)

        search = tk.Label(d, text="Search : ", bg='white', fg='blue')
        search['font'] = f3
        search.place(x=150, y=300)

        search_entry = tk.Entry(d, width=25, highlightbackground='blue', highlightthickness=1, textvariable=search_get)
        search_entry.place(x=300, y=305)

        userinfoen0 = tk.Entry(d, width=25, highlightbackground='blue', highlightthickness=1)
        userinfoen0.focus()
        userinfoen0.place(x=350, y=105)

        userinfoen1 = tk.Entry(d, width=25, highlightbackground='blue', highlightthickness=1)
        userinfoen1.place(x=350, y=155)

        userinfoen2 = tk.Entry(d, width=25, highlightbackground='blue', highlightthickness=1)
        userinfoen2.place(x=350, y=255)

        user3 = tk.Label(d, text='Spare Name : ', bg='white', fg='blue')
        user3['font'] = f3
        user3.place(x=600, y=150)

        user4 = tk.Label(d, text=' Rate Mrp : ', bg='white', fg='blue')
        user4['font'] = f3
        user4.place(x=600, y=250)

        userinfoen3 = tk.Entry(d, width=25, highlightbackground='blue', highlightthickness=1)
        userinfoen3.place(x=800, y=155)

        userinfoen4 = tk.Entry(d, width=25, highlightbackground='blue', highlightthickness=1)
        userinfoen4.place(x=800, y=255)

        table = tk.Frame(d, width=500)
        table.pack(side='bottom')

        scrollx = tk.Scrollbar(table, orient='horizontal')
        scrolly = tk.Scrollbar(table, orient='vertical')
        tree = ttk.Treeview(table,
                            columns=("Serial Number", "LapTop Name", "LapTop Model(N)", "Spare Name", "Rate Mrp"),
                            selectmode='extended', yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.config(command=tree.yview)
        scrolly.pack(side="right", fill="y")
        scrollx.config(command=tree.xview)
        scrollx.pack(side="bottom", fill="x")

        tree['column'] = ('1', '2', '3', '4', '5')
        tree['show'] = 'headings'
        tree.heading('1', text='                      Serial Number', anchor='w')
        tree.heading('2', text='                      LapTop Name', anchor='w')
        tree.heading('3', text='                      LapTop Model(N)', anchor='w')
        tree.heading('4', text='                      Spare Name', anchor='w')
        tree.heading('5', text='                      Rate Mrp', anchor='w')
        tree.column('1', stretch='0', minwidth=0, anchor='c')
        tree.column('2', stretch='0', minwidth=0, anchor='c')
        tree.column('3', stretch='0', minwidth=0, anchor='c')
        tree.column('4', stretch='0', minwidth=0, anchor='c')
        tree.column('5', stretch='0', minwidth=0, anchor='c')
        tree.bind('<Double-Button-1>', onselected)
        tree.pack()

        def add1():

            userserial = userinfoen0.get()
            laptopnameen = userinfoen1.get()
            laptopmodelen = userinfoen2.get()
            sparenameen = userinfoen3.get()
            ratemrpen = userinfoen4.get()

            if (userserial == "" or laptopname == "" or laptopmodel == "" or sparenameen == "" or ratemrp == ""):
                msg1 = tk.messagebox.showwarning('Warning', "First Enter The Item ", icon='warning')
            else:
                if str.isdigit(userinfoen0.get()) == str.isalpha(userinfoen0.get()) or str.isalpha(
                        userinfoen0.get()) or str.isalpha(userinfoen1.get()) == str.isdigit(
                        userinfoen1.get()) or str.isdigit(userinfoen1.get()) or str.isdigit(
                        userinfoen4.get()) == str.isalpha(userinfoen4.get()) or str.isalpha(
                        userinfoen4.get()) or userinfoen0.get() == 'sno':
                    msg1 = tk.messagebox.showerror('Error',
                                                   "only numbers should be used for serial number \n \n only characters should be used for Laptop name \n \n only numbers should be used for Rate Mrp ")
                else:
                    if len(userinfoen1.get()) > 16:
                        msg2 = tk.messagebox.showerror('Error',
                                                       "Laptop name should be allowed below 16")  # \n \n phone number should be allowed above or below 10 \n \n laptop name should be allowed below 10")
                    else:
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="admin",
                            db="laptop")

                        cursor = mydb.cursor()
                        cursor.execute(
                            "insert into spareinformation values('" + userserial + "','" + laptopnameen + "','" + laptopmodelen + "','" + sparenameen + "','" + ratemrpen + "')")

                        mydb.commit()

                        userinfoen0.delete(0, 'end')
                        userinfoen1.delete(0, 'end')
                        userinfoen2.delete(0, 'end')
                        userinfoen3.delete(0, 'end')
                        userinfoen4.delete(0, 'end')
                        show()

                        msg2 = tk.messagebox.showinfo('ADD', "ADD sucessfully")
                        cursor.close()
                        mydb.close()

        def show():

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="admin",
                db="laptop")
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM spareinformation ORDER BY sno ASC")
            rows = cursor.fetchall()
            tree.delete(*tree.get_children())

            for row in rows:
                tree.insert('', 'end', values=(row))

            # msg3 = tk.messagebox.showinfo('View', "Viewed  sucessfully")
            mydb.close()

        def delete():

            if userinfoen0.get() == "":
                msg13 = tk.messagebox.showwarning('Serial Number', "For delete Serial Number is compulsory")
            else:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="admin",
                    db="laptop")
                cursor = mydb.cursor()
                # query="insert into login2(id,username,password)"
                cursor.execute("delete from spareinformation where sno='" + userinfoen0.get() + "'")
                mydb.commit()

                userinfoen0.delete(0, 'end')
                userinfoen1.delete(0, 'end')
                userinfoen2.delete(0, 'end')
                userinfoen3.delete(0, 'end')
                userinfoen4.delete(0, 'end')
                show()

                msg14 = tk.messagebox.showinfo('Delete', "Deleted sucessfully")
                mydb.close()

        def update():

            userserial = userinfoen0.get()
            laptopnameen = userinfoen1.get()
            laptopmodelen = userinfoen2.get()
            sparenameen = userinfoen3.get()
            ratemrpen = userinfoen4.get()

            if (userserial == " " or laptopnameen == "" or laptopmodelen == "" or sparenameen == "" or ratemrpen == ""):
                msg1 = tk.messagebox.showwarning('Warning', "First Enter The Item ", icon='warning')
            else:
                if str.isdigit(userinfoen0.get()) == str.isalpha(userinfoen0.get()) or str.isalpha(
                        userinfoen0.get()) or str.isalpha(userinfoen1.get()) == str.isdigit(
                    userinfoen1.get()) or str.isdigit(userinfoen1.get()) or str.isdigit(
                    userinfoen4.get()) == str.isalpha(userinfoen4.get()) or str.isalpha(userinfoen4.get()):
                    msg1 = tk.messagebox.showerror('Error',
                                                   "only numbers should be used for serial number \n \n only characters should be used for Laptop name \n \n only numbers should be used for Rate Mrp ")
                else:
                    if len(userinfoen1.get()) > 16:
                        msg2 = tk.messagebox.showerror('Error', "Laptop name should be allowed below 16")
                    else:
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="admin",
                            db="laptop")

                        cursor = mydb.cursor()
                        cursor.execute(
                            "update spareinformation set laptopname='" + laptopnameen + "',latopmodel='" + laptopmodelen + "',sparename='" + sparenameen + "',ratemrp='" + ratemrpen + "' where sno='" + userserial + "'")

                        mydb.commit()

                        userinfoen0.delete(0, 'end')
                        userinfoen1.delete(0, 'end')
                        userinfoen2.delete(0, 'end')
                        userinfoen3.delete(0, 'end')
                        userinfoen4.delete(0, 'end')
                        show()

                        msg2 = tk.messagebox.showinfo('Update', "Update sucessfully")
                        cursor.close()
                        mydb.close()

        def search_for_update(rows):

            tree.delete(*tree.get_children())
            for i in rows:
                tree.insert("",'end',values=i)

            query = "select sno,laptopname,laptopmodel,sparename,ratemrp from spareinformation"
            cursor.execute(query)
            rows = cursor.fetchall()
            search_for_update()

        def search_find():

            if len(tree.get_children()) < 1:
                msg=messagebox.showerror('Error'," No Records found !!! ")
            else:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="admin",
                    db="laptop")

                cursor = mydb.cursor()
                search_give = search_get.get()
                query = "select sno ,laptopname,laptopmodel,sparename,ratemrp FROM spareinformation WHERE  laptopname LIKE '%" + search_give + "%' OR laptopmodel LIKE '%" + search_give + "%' OR sparename LIKE '%" + search_give + "%' "
                cursor.execute(query)
                global rows
                rows = cursor.fetchall()
                search_for_update(rows)



        def clear1():

            userserial = userinfoen0.get()
            laptopnameen = userinfoen1.get()
            laptopmodelen = userinfoen2.get()
            sparenameen = userinfoen3.get()
            ratemrpen = userinfoen4.get()

            if (
                    userserial == "" and laptopnameen == "" and laptopmodelen == "" and sparenameen == "" and ratemrpen == ""):
                msg4 = tk.messagebox.showwarning('Clear', "All Ready Cleared")
            else:
                userinfoen0.delete(0, 'end')
                userinfoen1.delete(0, 'end')
                userinfoen2.delete(0, 'end')
                userinfoen3.delete(0, 'end')
                userinfoen4.delete(0, 'end')
                msg19 = tk.messagebox.showinfo('Clear', "Cleared sucessfully")

        def con_to_excel():

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="admin",
                db="laptop")
            cursor = mydb.cursor()
            now = datetime.datetime.now()
            now_str = now.strftime(" %Y-%m-%d-%I-%M-%S-%p")
            cursor.execute("select * from spareinformation ORDER by sno ASC")
            result = cursor.fetchall()
            with open('properties/spareinfo/spareinformation{}.csv'.format(now_str), 'a') as f:
                w = csv.writer(f, dialect='excel')
                for records in result:
                    w.writerow(records)
            msg5 = tk.messagebox.showinfo('Excel', "Sucessfully Converted")
            msgnew = tk.messagebox.askquestion('Open', "You Want To Open")
            if msgnew == 'yes':
                        file = filedialog.askopenfilename(initialdir="properties\spareinfo",
                                                          title="Select A File",
                                                          filetypes=(("excel files", "*.csv"), ("all files", "*.*")))
                        os.system('"%s"' % file)
            else:
                print("")

        def hover5(e):
            add['bg'] = 'sky blue'

        def hover_leave5(e):
            add['bg'] = "white"

        def hover6(e):
            update1['bg'] = 'sky blue'

        def hover_leave6(e):
            update1['bg'] = "white"

        def hover7(e):
            delete1['bg'] = 'sky blue'

        def hover_leave7(e):
            delete1['bg'] = "white"

        def hover8(e):
            view['bg'] = 'sky blue'

        def hover_leave8(e):
            view['bg'] = "white"

        def hover9(e):
            clearc['bg'] = 'sky blue'

        def hover_leave9(e):
            clearc['bg'] = "white"

        def hover10(e):
            excel['bg'] = 'sky blue'

        def hover_leave10(e):
            excel['bg'] = "white"

        def hover_enter_search(e):
            search_btn['bg'] = 'sky blue'

        def hover_leave_search(e):
            search_btn['bg'] = "white"

        add = tk.Button(d, text="Add", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                        cursor="hand2", command=add1)
        add['font'] = f6
        add.bind("<Enter>", hover5)
        add.bind("<Leave>", hover_leave5)
        add.place(x=1200, y=50)

        update1 = tk.Button(d, text="Update", activebackground='red', fg='black', bg='white', bd=0, relief=tk.FLAT,
                            cursor="hand2", command=update)
        update1['font'] = f6
        update1.bind("<Enter>", hover6)
        update1.bind("<Leave>", hover_leave6)
        update1.place(x=1200, y=100)

        delete1 = tk.Button(d, text="Delete", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                            cursor="hand2", command=delete)
        delete1['font'] = f6
        delete1.bind("<Enter>", hover7)
        delete1.bind("<Leave>", hover_leave7)
        delete1.place(x=1200, y=150)

        view = tk.Button(d, text="View All", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                         cursor="hand2", command=show)
        view['font'] = f6
        view.bind("<Enter>", hover8)
        view.bind("<Leave>", hover_leave8)
        view.place(x=1200, y=200)

        clearc = tk.Button(d, text="Clear All", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                           cursor="hand2", command=clear1)
        clearc['font'] = f6
        clearc.bind("<Enter>", hover9)
        clearc.bind("<Leave>", hover_leave9)
        clearc.place(x=1200, y=300)

        excel = tk.Button(d, text="Con to Excel", activebackground='red', fg='black', bg='white', relief=tk.FLAT, bd=0,
                          cursor="hand2", command=con_to_excel)
        excel['font'] = f6
        excel.bind("<Enter>", hover10)
        excel.bind("<Leave>", hover_leave10)
        excel.place(x=1200, y=250)


        search_btn=tk.Button(d,text='Search',activebackground='red',fg='blue',bg='white',relief=tk.FLAT,bd=0,cursor='hand2',command=search_find)
        search_btn['font']=f6
        search_btn.bind("<Enter>",hover_enter_search)
        search_btn.bind("<Leave>", hover_leave_search)
        search_btn.place(x=500,y=290)


        d.mainloop()

    def services(label):

        e = tk.Toplevel(home)

        window_width = 1365
        window_height = 730

        screen_width = e.winfo_screenwidth()
        screen_height = e.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 3) - (window_height / 3))

        e.geometry("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
        e.iconbitmap("images\SS.ico")
        e.configure(bg='white')
        e.resizable(0, 0)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="admin", db="laptop")

        cursor = mydb.cursor()

        f8 = ff.Font(size=15, family='Arial', weight='bold', underline=1)
        f9 = ff.Font(size=13, family='Times New Roman', weight='bold')

        frameright = tk.Frame(e, relief=tk.SUNKEN, borderwidth=2, width=50, height=50, bg='white')
        frameright.pack(side='left', fill='both', expand=False)

        frametop = tk.Frame(e, relief=tk.SUNKEN, borderwidth=1, bg='white')
        frametop.pack(side='top', fill='both', expand=False)

        whoic = tk.PhotoImage(file="images\ser45.png")
        whoicl = tk.Label(frametop, image=whoic)
        whoicl.place(x=0, y=0)

        who = tk.Label(frametop)
        who['font'] = f1
        who.configure(text=useren.get(), fg='blue', bg='white')
        who.place(x=50, y=5)

        times = tk.PhotoImage(file="images\cal45.png")
        timeic = tk.Label(frametop, image=times)
        timeic.place(x=920, y=0)

        def upadte_clock():
            now1 = time.strftime("%Y-%m-%d %I:%M:%S:%p")
            time1.configure(text=now1)

        def resf():
            upadte_clock()
            threading.Timer(1, resf).start()

        time1 = tk.Label(frametop)
        time1.configure(bg='white', fg='blue')
        time1['font'] = f3
        time1.place(x=990, y=8)
        resf()

        title1 = tk.Label(frametop, text="Akill Services", bg="white", fg="blue")
        title1['font'] = f2
        title1.pack()

        akill = tk.Label(frameright, text='Akill', bg='white', fg='white')
        akill['font'] = f1
        akill.pack(padx=25, pady=30)

        titleuse = tk.Label(e, text='Billing INFORMATION', bg='white', fg='blue')
        titleuse['font'] = f8
        titleuse.place(x=585, y=50)

        serialnumber = tk.StringVar()
        laptopname = tk.StringVar()
        laptopmodel = tk.StringVar()
        laptopsn = tk.StringVar()
        ratemrp = tk.StringVar()
        search_get = tk.StringVar()

        def onselected1(event):
            cur = tree.focus()
            content = tree.item(cur)
            select = content['values']
            serialnumber.set("")
            laptopname.set("")
            laptopmodel.set("")
            laptopsn.set("")
            ratemrp.set("")
            serialnumber.set(select[0])
            laptopname.set(select[1])
            laptopmodel.set(select[2])
            laptopsn.set(select[3])
            ratemrp.set(select[4])

        serial = tk.Label(e, text='Serial (N) : ', bg='white', fg='blue')
        serial['font'] = f9
        serial.place(x=150, y=100)

        userl = tk.Label(e, text='Laptop Name : ', bg='white', fg='blue')
        userl['font'] = f9
        userl.place(x=150, y=150)

        user2 = tk.Label(e, text='Laptop Model(N) : ', bg='white', fg='blue')
        user2['font'] = f9
        user2.place(x=150, y=200)

        userinfoen0 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=serialnumber)
        userinfoen0.focus()
        userinfoen0.place(x=350, y=105)

        userinfoen1 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=laptopname)
        userinfoen1.place(x=350, y=155)

        userinfoen2 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=laptopmodel)
        userinfoen2.place(x=350, y=205)

        user3 = tk.Label(e, text='Spare Name : ', bg='white', fg='blue')
        user3['font'] = f9
        user3.place(x=600, y=150)

        user4 = tk.Label(e, text=' Rate Mrp : ', bg='white', fg='blue')
        user4['font'] = f9
        user4.place(x=600, y=200)

        userinfoen3 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=laptopsn)
        userinfoen3.place(x=800, y=155)

        userinfoen4 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=ratemrp)
        userinfoen4.place(x=800, y=205)

        serial1 = tk.Label(e, text='Serial User (N) : ', bg='white', fg='blue')
        serial1['font'] = f9
        serial1.place(x=150, y=300)

        userl1 = tk.Label(e, text='User Name : ', bg='white', fg='blue')
        userl1['font'] = f9
        userl1.place(x=150, y=350)

        user12 = tk.Label(e, text='User Phone(N) : ', bg='white', fg='blue')
        user12['font'] = f9
        user12.place(x=150, y=400)

        userinfoen01 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry0)
        userinfoen01.focus()
        userinfoen01.place(x=350, y=305)

        userinfoen11 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry1)
        userinfoen11.place(x=350, y=355)

        userinfoen12 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry2)
        userinfoen12.place(x=350, y=405)

        user13 = tk.Label(e, text='User Address : ', bg='white', fg='blue')
        user13['font'] = f9
        user13.place(x=600, y=300)

        user14 = tk.Label(e, text='LapTop Name : ', bg='white', fg='blue')
        user14['font'] = f9
        user14.place(x=600, y=350)

        user_email=tk.Label(e,text='Email ID : ',bg='white',fg='blue')
        user_email['font']=f9
        user_email.place(x=600,y=260)

        user_email_entry=tk.Entry(e,width=25,highlightbackground='blue',highlightthickness=1,textvariable=entry5)
        user_email_entry.place(x=800,y=260)

        search = tk.Label(e, text="Search : ", bg='white', fg='blue')
        search['font'] = f9
        search.place(x=150, y=445)

        search_entry = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=search_get)
        search_entry.place(x=350, y=450)

        userinfoen13 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry4)
        userinfoen13.place(x=800, y=355)

        userinfoen14 = tk.Entry(e, width=25, highlightbackground='blue', highlightthickness=1, textvariable=entry3)
        userinfoen14.place(x=800, y=300)

        datereceived = tk.Label(e, text='Item Received : ', fg='blue', bg='white')
        datereceived['font'] = f9
        datereceived.place(x=600, y=400)

        datesent = tk.Label(e, text='Item Sent : ', fg='blue', bg='white')
        datesent['font'] = f9
        datesent.place(x=850, y=400)


        def calendar():

            calwin = tk.Tk()
            calwin.iconbitmap("images\SS.ico")
            calwin.geometry('230x230')
            calwin.overrideredirect(True)
            calwin.eval('tk::PlaceWindow . center')
            calwin.resizable(0, 0)
            calwin.configure(bg='white')
            cal = Calendar(calwin, selectmode="day", year=2020, month=6, day=28)
            cal.pack()

            def grab_date(e):
                cal1 = cal.get_date()
                dateentry.delete(0, tk.END)
                dateentry.insert(0, cal1)
                calwin.destroy()

            calwin.bind("<Double Button-1>", grab_date)

            def hovercal1(e):
                btncal11['bg'] = 'sky blue'

            def cal_leave1(e):
                btncal11['bg'] = 'white'

            btncal11 = tk.Button(calwin, text="ok", activebackground='red', fg='black', bg='white', bd=0,
                                 cursor='hand2', command=grab_date)
            btncal11['font'] = f9
            btncal11.bind("<Enter>", hovercal1)
            btncal11.bind("<Leave>", cal_leave1)
            btncal11.pack(pady=10)

        dateentry = tk.Entry(e, width=15, highlightbackground='blue', highlightthickness=1, fg='green', bg='white')
        dateentry.place(x=730, y=403)

        def calendar2():

            calwin1 = tk.Tk()
            calwin1.iconbitmap("images\SS.ico")
            calwin1.overrideredirect(True)
            calwin1.eval('tk::PlaceWindow . center')
            calwin1.geometry('230x230')
            calwin1.resizable(0, 0)
            calwin1.configure(bg='white')
            cal = Calendar(calwin1, selectmode="day", year=2020, month=6, day=28)
            cal.pack()

            def grab_date1(e):
                cal1 = cal.get_date()
                dateentry1.delete(0, tk.END)
                dateentry1.insert(0, cal1)
                calwin1.destroy()

            calwin1.bind("<Double Button-1>", grab_date1)

            def hovercal1(e):
                btncal11['bg'] = 'sky blue'

            def cal_leave1(e):
                btncal11['bg'] = 'white'

            btncal11 = tk.Button(calwin1, text="ok", activebackground='red', fg='black', bg='white', bd=0,
                                 cursor='hand2', command=grab_date1)
            btncal11['font'] = f9
            btncal11.bind("<Enter>", hovercal1)
            btncal11.bind("<Leave>", cal_leave1)
            btncal11.pack(pady=10)

        dateentry1 = tk.Entry(e, width=15, highlightbackground='blue', highlightthickness=1, fg='green', bg='white')
        dateentry1.place(x=950, y=403)

        btncal1 = tk.Button(e, text="C", width=2, height=2, fg='green', bg='white', bd=0, cursor='hand2',
                            command=calendar2)
        btncal1['font'] = f9
        btncal1.place(x=975, y=425)

        btncal2 = tk.Button(e, text="C", width=2, height=2, fg='green', bg='white', bd=0, cursor='hand2',
                            command=calendar)
        btncal2['font'] = f9
        btncal2.place(x=775, y=425)

        table = tk.Frame(e, width=500)
        table.pack(side='bottom')
        scrollx = tk.Scrollbar(table, orient='horizontal')
        scrolly = tk.Scrollbar(table, orient='vertical')
        tree = ttk.Treeview(table,
                            columns=("Serial Number", "LapTop Name", "LapTop Model(N)", "Spare Name", "Rate Mrp"),
                            selectmode='extended', yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.config(command=tree.yview)
        scrolly.pack(side="right", fill="y")
        scrollx.config(command=tree.xview)
        scrollx.pack(side="bottom", fill="x")

        tree['column'] = ('1', '2', '3', '4', '5')
        tree['show'] = 'headings'
        tree.heading('1', text='                      Serial Number', anchor='w')
        tree.heading('2', text='                      LapTop Name', anchor='w')
        tree.heading('3', text='                      LapTop Model(N)', anchor='w')
        tree.heading('4', text='                      Spare Name', anchor='w')
        tree.heading('5', text='                      Rate Mrp', anchor='w')
        tree.column('1', stretch='0', minwidth=0, anchor='c')
        tree.column('2', stretch='0', minwidth=0, anchor='c')
        tree.column('3', stretch='0', minwidth=0, anchor='c')
        tree.column('4', stretch='0', minwidth=0, anchor='c')
        tree.column('5', stretch='0', minwidth=0, anchor='c')
        tree.bind('<Double-Button-1>', onselected1)
        tree.pack()

        def add1():

            userserial = userinfoen01.get()
            userenname = userinfoen11.get()
            userenphone = userinfoen12.get()
            userenaddress = userinfoen13.get()
            userenlaptop = userinfoen14.get()
            laptopenserial = userinfoen0.get()
            laptopenname = userinfoen1.get()
            laptopenmodel = userinfoen2.get()
            spareenname = userinfoen3.get()
            rateenmrp = userinfoen4.get()
            datereceived = dateentry.get()
            datesent = dateentry1.get()
            email_entry=user_email_entry.get()


            if (
                    userserial == "" or userenname == "" or userenphone == "" or userenaddress == "" or userenlaptop == "" or laptopenserial == "" or laptopenname == "" or laptopenmodel == "" or spareenname == "" or rateenmrp == "" or datereceived == "" or datesent == "" or email_entry==""):
                msg1 = tk.messagebox.showwarning('Warning', "First Enter The Item ", icon='warning')
            else:
                if str.isdigit(userinfoen01.get()) == str.isalpha(userinfoen01.get()) or str.isalpha(
                        userinfoen01.get()) or str.isalpha(userinfoen11.get()) == str.isdigit(
                        userinfoen11.get()) or str.isdigit(userinfoen11.get()) or str.isdigit(
                        userinfoen12.get()) == str.isalpha(userinfoen12.get()) or str.isalpha(
                        userinfoen12.get()) or str.isalpha(userinfoen14.get()) == str.isdigit(
                        userinfoen14.get()) or str.isdigit(userinfoen14.get()) or str.isdigit(
                        userinfoen0.get()) == str.isalpha(userinfoen0.get()) or str.isalpha(
                        userinfoen0.get()) or str.isalpha(userinfoen1.get()) == str.isdigit(
                        userinfoen1.get()) or str.isdigit(userinfoen1.get()) or str.isdigit(
                        userinfoen4.get()) == str.isalpha(userinfoen4.get() or str.isalpha(userinfoen4.get())):
                    msg1 = tk.messagebox.showerror('Error',
                                                   "only numbers should be used for serial number \n \n only characters should be used for User name \n \n only numbers should be used for User Phone \n \n only characters should be used for Laptop name \n \n only numbers should be used for Rate Mrp")
                else:
                    if len(userinfoen11.get()) > 16 or len(userinfoen12.get()) > 10 or len(
                            userinfoen12.get()) < 10 or len(userinfoen1.get()) > 16:
                        msg2 = tk.messagebox.showerror('Error',
                                                       "user name should be allowed below 16 \n \n phone number should be allowed 10 \n \n Laptop name should be allowed below 16")
                    else:
                        if (re.search(valide_email,user_email_entry.get())):
                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="admin",
                                db="laptop")

                            cursor = mydb.cursor()
                            cursor.execute(
                                "insert into billinghistroy values('" + userserial + "','" + userenname + "','" + userenphone + "','" + userenaddress + "','" + userenlaptop + "','" + laptopenserial + "','" + laptopenname + "','" + laptopenmodel + "','" + spareenname + "','" + rateenmrp + "','" + datereceived + "','" + datesent + "','" + email_entry + "')")

                            mydb.commit()

                            userinfoen01.delete(0, 'end')
                            userinfoen11.delete(0, 'end')
                            userinfoen12.delete(0, 'end')
                            userinfoen13.delete(0, 'end')
                            userinfoen14.delete(0, 'end')
                            userinfoen0.delete(0, 'end')
                            userinfoen1.delete(0, 'end')
                            userinfoen2.delete(0, 'end')
                            userinfoen3.delete(0, 'end')
                            userinfoen4.delete(0, 'end')
                            dateentry.delete(0, 'end')
                            dateentry1.delete(0, 'end')
                            user_email_entry.delete(0,'end')

                            msg2 = tk.messagebox.showinfo('ADD', "Add to Billing Histroy sucessfully")
                            cursor.close()
                            mydb.close()
                        else:
                            msg=messagebox.showwarning('Warning',"Please check Email ID")

        def show():

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="admin",
                db="laptop")
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM spareinformation ORDER BY sno ASC")
            rows = cursor.fetchall()
            tree.delete(*tree.get_children())

            for row in rows:
                tree.insert('', 'end', values=(row))

            # msg3 = tk.messagebox.showinfo('View', "Viewed  sucessfully")
            mydb.close()

        def delete():

            if userinfoen0.get() == "":
                msg13 = tk.messagebox.showwarning('Serial Number', "For delete Serial Number is compulsory")
            else:

                if str.isalpha(userinfoen01.get()) or str.isdigit(userinfoen11.get()) or str.isalpha(
                        userinfoen12.get()) or str.isdigit(userinfoen14.get()) or str.isalpha(
                        userinfoen0.get()) or str.isdigit(userinfoen1.get()) or str.isalpha(userinfoen4.get()):
                    msg1 = tk.messagebox.showerror('Error',
                                                   "only numbers should be used for serial number \n \n only characters should be used for User name \n \n only numbers should be used for User Phone \n \n only characters should be used for Laptop name \n \n only numbers should be used for Rate Mrp")
                else:

                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="admin",
                        db="laptop")
                    cursor = mydb.cursor()
                    cursor.execute("delete from spareinformation where sno='" + userinfoen0.get() + "'")
                    mydb.commit()

                    userinfoen0.delete(0, 'end')
                    userinfoen1.delete(0, 'end')
                    userinfoen2.delete(0, 'end')
                    userinfoen3.delete(0, 'end')
                    userinfoen4.delete(0, 'end')
                    show()

                    msg14 = tk.messagebox.showinfo('Delete', "Deleted sucessfully")
                    mydb.close()

        def update():

            userserial = userinfoen0.get()
            laptopnameen = userinfoen1.get()
            laptopmodelen = userinfoen2.get()
            sparenameen = userinfoen3.get()
            ratemrpen = userinfoen4.get()

            if (userserial == " " or laptopnameen == "" or laptopmodelen == "" or sparenameen == "" or ratemrpen == ""):
                msg1 = tk.messagebox.showwarning('Warning', "First Enter The Item ", icon='warning')
            else:
                if str.isdigit(userinfoen0.get()) == str.isalpha(userinfoen0.get()) or str.isalpha(
                        userinfoen0.get()) or str.isalpha(userinfoen1.get()) == str.isdigit(
                        userinfoen1.get()) or str.isdigit(userinfoen1.get()) or str.isdigit(
                        userinfoen4.get()) == str.isalpha(userinfoen4.get()) or str.isalpha(userinfoen4.get()):
                    msg1 = tk.messagebox.showerror('Error',
                                                   "only numbers should be used for serial number \n \n only characters should be used for Laptop name \n \n only numbers should be used for Rate Mrp ")
                else:
                    if len(userinfoen1.get()) > 16:
                        msg2 = tk.messagebox.showerror('Error', "Laptop name should be allowed below 16")
                    else:
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="admin",
                            db="laptop")

                        cursor = mydb.cursor()
                        cursor.execute(
                            "update spareinformation set laptopname='" + laptopnameen + "',latopmodel='" + laptopmodelen + "',sparename='" + sparenameen + "',ratemrp='" + ratemrpen + "' where sno='" + userserial + "'")

                        mydb.commit()

                        userinfoen0.delete(0, 'end')
                        userinfoen1.delete(0, 'end')
                        userinfoen2.delete(0, 'end')
                        userinfoen3.delete(0, 'end')
                        userinfoen4.delete(0, 'end')
                        show()

                        msg2 = tk.messagebox.showinfo('Update', "Update sucessfully")
                        cursor.close()
                        mydb.close()

        def search_for_update(rows):

            tree.delete(*tree.get_children())
            for i in rows:
                tree.insert("",'end',values=i)

            query = "select sno,laptopname,laptopmodel,sparename,ratemrp from spareinformation"
            cursor.execute(query)
            rows = cursor.fetchall()
            search_for_update()

        def search_find():

            if len(tree.get_children()) < 1:
                msg=messagebox.showerror('Error'," No Records found !!! ")
            else:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="admin",
                    db="laptop")

                cursor = mydb.cursor()
                search_give = search_get.get()
                query = "select sno ,laptopname,laptopmodel,sparename,ratemrp FROM spareinformation WHERE  laptopname LIKE '%" + search_give + "%' OR laptopmodel LIKE '%" + search_give + "%' OR sparename LIKE '%" + search_give + "%' "
                cursor.execute(query)
                global rows
                rows = cursor.fetchall()
                search_for_update(rows)






        def clear1():

            userserial = userinfoen0.get()
            laptopnameen = userinfoen1.get()
            laptopmodelen = userinfoen2.get()
            sparenameen = userinfoen3.get()
            ratemrpen = userinfoen4.get()
            datereceived1 = dateentry.get()
            datesent1 = dateentry1.get()
            usercl1 = userinfoen01.get()
            usercl2 = userinfoen11.get()
            usercl3 = userinfoen12.get()
            usercl4 = userinfoen13.get()
            usercl5 = userinfoen14.get()
            email_id=user_email_entry.get()

            if (
                    userserial == "" and laptopnameen == "" and laptopmodelen == "" and sparenameen == "" and ratemrpen == "" and datereceived1 == "" and datesent1 == "" and usercl1 == "" and usercl2 == "" and usercl3 == "" and usercl4 == "" and usercl5 == "" and email_id==""):
                msg4 = tk.messagebox.showwarning('Clear', "All Ready Cleared")
            else:
                userinfoen0.delete(0, 'end')
                userinfoen1.delete(0, 'end')
                userinfoen2.delete(0, 'end')
                userinfoen3.delete(0, 'end')
                userinfoen4.delete(0, 'end')
                dateentry.delete(0, 'end')
                dateentry1.delete(0, 'end')
                userinfoen01.delete(0, 'end')
                userinfoen11.delete(0, 'end')
                userinfoen12.delete(0, 'end')
   

    home.mainloop()


a.mainloop()
