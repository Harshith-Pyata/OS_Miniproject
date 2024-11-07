from tkinter import *
from PIL import Image, ImageTk
import math

def calculator_window():

    global scvalue
    global iconc1
    global iconc2
    global iconc3
    def delete(event):
        global scvalue
        text=scvalue.get()
        scvalue.set(text[:-1])
        screen.update()
        
    def squareroot(event):
        global scvalue
        text="√"
        scvalue.set(scvalue.get()+text)
        scvalue.update()
        
    def square(event):
        global scvalue
        text="^2"
        scvalue.set(scvalue.get()+text)
        scvalue.update()
        
        
    def click(event):
        global scvalue
        text=event.widget.cget("text")
        if text=="=":
            if "√" in scvalue.get():
                value=scvalue.get()
                value=value[1:] 
                value=math.sqrt(int(value))
            elif "^2" in scvalue.get():
                value=scvalue.get()
                value=value[:-2] 
                value=math.pow(int(value),2)
            elif "sin" in scvalue.get():
                value=scvalue.get()
                value=value[3:] 
                value=math.sin(int(value))
            elif "cos" in scvalue.get():
                value=scvalue.get()
                value=value[3:] 
                value=math.cos(int(value))
            elif "log" in scvalue.get():
                value=scvalue.get()
                value=value[3:] 
                value=math.log(int(value))
            elif "!" in scvalue.get():
                value=scvalue.get()
                value=value[:-1]
                value=math.factorial(int(value))
                
            elif scvalue.get().isdigit():
                value=int(scvalue.get())
            else:
                try:
                    value=eval(screen.get())
                except Exception as e:
                    print(e)
                    value="Error"
                    
            scvalue.set(value)
            screen.update()
        elif text=="C":
            scvalue.set("")
            screen.update()
        else:
            scvalue.set(scvalue.get()+text)
            screen.update()
        

    cal=Toplevel()
    cal.geometry("550x550")
    cal.title("Calculator")
    # root.wm_iconbitmap("")

    cal.configure(bg="light blue")

    title=Label(cal,text="SCIENTIFIC CALCULATOR",bg="light blue",font="lucida 15 bold")
    title.pack(pady=10)
    scvalue=StringVar()
    scvalue.set("")
    screen=Entry(cal,textvariable=scvalue,font="lucida 25 bold")
    screen.pack(pady=15) 

    f1=Frame(cal, bg="light blue")
    b=Button(f1,text="sin",padx=17,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=10,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f1,text="cos",padx=17,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=10,pady=5)
    b.bind("<Button-1>",click)
    photoc1=Image.open("squareroot.jpg")
    photoc1=photoc1.resize((55,55))
    iconc1=ImageTk.PhotoImage(photoc1)
    b=Button(f1,image=iconc1,padx=20,pady=10)
    b.pack(side=LEFT,padx=10,pady=5)
    b.bind("<Button-1>",squareroot)
    photoc3=Image.open("delete icon1.jpg")
    photoc3=photoc3.resize((55,55))
    iconc3=ImageTk.PhotoImage(photoc3)
    b=Button(f1,image=iconc3,padx=31,pady=10)
    b.pack(side=LEFT,padx=10,pady=5)
    b.bind("<Button-1>",delete)
    f1.pack(padx=15)

    f1=Frame(cal, bg="light blue")
    b=Button(f1,text="log",padx=24,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=7,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f1,text="!",padx=30,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=7,pady=5)
    b.bind("<Button-1>",click)
    photoc2=Image.open("square.jpg")
    photoc2=photoc2.resize((55,55))
    iconc2=ImageTk.PhotoImage(photoc2)
    b=Button(f1,image=iconc2,padx=31,pady=10)
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",square)
    b=Button(f1,text=".",padx=25.5,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    f1.pack(padx=15)

    f1=Frame(cal, bg="light blue")
    b=Button(f1,text="9",padx=26.5,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f1,text="8",padx=26,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f1,text="7",padx=26,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f1,text="+",padx=26.5,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=6,pady=5)
    b.bind("<Button-1>",click)
    f1.pack(padx=15)

    f2=Frame(cal, bg="light blue")
    b=Button(f2,text="6",padx=27,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f2,text="5",padx=28,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f2,text="4",padx=28,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f2,text="-",padx=27,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    f2.pack()

    f3=Frame(cal, bg="light blue")
    b=Button(f3,text="3",padx=27,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f3,text="2",padx=26,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f3,text="1",padx=26,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f3,text="x",padx=27,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    f3.pack()

    f4=Frame(cal, bg="light blue")
    b=Button(f4,text="C",padx=26,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=4,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f4,text="0",padx=27,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=4,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f4,text="/",padx=28,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)
    b=Button(f4,text="=",padx=27,pady=10,font="lucida 15 bold")
    b.pack(side=LEFT,padx=6,pady=5)
    b.bind("<Button-1>",click)
    f4.pack()
