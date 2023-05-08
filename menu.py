import calender
import tkinter as tk
from tkinter import *


root = Tk()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        #filemenu creation
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)



    def exitProgram(self):
        exit()

#picker data for time
class TimePicker(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.oneDay_string = StringVar()
        self.twoDay_string = StringVar()
        self.hour_string = StringVar()
        self.min_string = StringVar()
        self.last_value_sec = ""
        self.last_value = ""
        self.f = ('Helvetica', 20)

        self.create_widgets()

    def create_widgets(self):
        fone = Frame(self)
        ftwo = Frame(self)
        fthree = Frame(self)
        fone.pack(pady=10)
        ftwo.pack(pady=10)
        fthree.pack(pady=20)

        self.min_sb = Spinbox(
            ftwo,
            from_=0,
            to=23,
            wrap=True,
            textvariable=self.hour_string,
            width=2,
            state="readonly",
            font=self.f,
            justify=CENTER
        )
        self.sec_hour = Spinbox(
            ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.min_string,
            font=self.f,
            width=2,
            justify=CENTER
        )

        self.sec = Spinbox(
            ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.sec_hour,
            width=2,
            font=self.f,
            justify=CENTER
        )

        self.sec_day = Spinbox(
            ftwo,
            from_=0,
            to=3,
            wrap=True,
            textvariable=self.twoDay_string,
            font=self.f,
            width=2,
            justify=CENTER
        )

        self.day = Spinbox(
            ftwo,
            from_=0,
            to=9,
            wrap=True,
            textvariable=self.oneDay_string,
            width=2,
            font=self.f,
            justify=CENTER
        )

        self.sec_day.pack(side=LEFT, fill=X, expand=True)
        self.day.pack(side=LEFT, fill=X, expand=True)
        self.min_sb.pack(side=LEFT, fill=X, expand=True)
        self.sec_hour.pack(side=LEFT, fill=X, expand=True)
        self.sec.pack(side=LEFT, fill=X, expand=True)

        self.msg = Label(
            self,
            text="Hour  Minute  Seconds",
            font=("Helvetica", 12),
            bg="#F79AC0"
        )
        self.msg.pack(side=TOP)

        self.actionBtn = Button(
            self,
            text="Create Event",
            padx=10,
            pady=10,
            command=self.display_msg
        )
        self.actionBtn.pack(pady=10)

        self.msg_display = Label(
            self,
            text="",
            bg="#F79AC0"
        )
        self.msg_display.pack(pady=10)

    def display_msg(self):
        dayone = self.day.get()
        daytwo = self.sec_day.get()
        m = self.min_sb.get()
        h = self.sec_hour.get()
        s = self.sec.get()
        t = f"Your appointment is booked for  {daytwo}{dayone}   {m}:{h}:{s}."
        self.msg_display.config(text=t)



#create time picker
hour_string=StringVar()
min_string=StringVar()
last_value_sec = ""
last_value = ""        
f = ('Times', 20)

def display_msg():
    #date = cal.get_date()
    m = min_sb.get()
    h = sec_hour.get()
    s = sec.get()
    #t = f"Your appointment is booked for {date} at {m}:{h}:{s}."
    msg_display.config(text=t)


if last_value == "59" and min_string.get() == "0":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)   
    last_value = min_string.get()

if last_value_sec == "59" and sec_hour.get() == "0":
    min_string.set(int(min_string.get())+1 if min_string.get() !="59" else 0)
if last_value == "59":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)            
    last_value_sec = sec_hour.get()

fone = Frame(root)
ftwo = Frame(root)

fone.pack(pady=10)
ftwo.pack(pady=10)

min_sb = Spinbox(
    ftwo,
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=2,
    state="readonly",
    font=f,
    justify=CENTER
    )
sec_hour = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    font=f,
    width=2,
    justify=CENTER
    )


sec = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=sec_hour,
    width=2,
    font=f,
    justify=CENTER
    )

min_sb.pack(side=LEFT, fill=X, expand=True)
sec_hour.pack(side=LEFT, fill=X, expand=True)
sec.pack(side=LEFT, fill=X, expand=True)

msg = Label(
    root, 
    text="Hour  Minute  Seconds",
    font=("Helvetica", 12),
    bg="#F79AC0"
    )
msg.pack(side=TOP)

actionBtn =Button(
    root,
    text="Create Event",
    padx=10,
    pady=10,
    command=display_msg
)
actionBtn.pack(pady=10)

msg_display = Label(
    root,
    text="Birthday party",
    bg="#F79AC0"
)
msg_display.pack(pady=10)



turn_on = Button(root, text="select time")
turn_on.pack()
        

app = Window(root)
root.geometry("300x300")
root.wm_title("Personal Schedule")
root.mainloop()


