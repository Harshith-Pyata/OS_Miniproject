from tkinter import *
from PIL import Image,ImageTk
import os
import webbrowser
import datetime
import tkinter.messagebox as tmsg
import calculatorwindow
import weatherpred

def weather():
    weatherpred.weather_window()

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime("%I:%M %p")
    date=time.strftime("%d-%m-%y,%a,")
    
    time_box.config(text=date+hr)
    time_box.after(200,date_time)
    
# def Vs():
#     os.startfile("C:/Users/yamin/AppData/Local/Programs/Microsoft VS Code/code")
def microsoft():
    os.startfile("C:/Program Files (x86)/Microsoft/Edge/Application/msedge")
def chrome():
    webbrowser.open("https://www.google.co.in/")
def recyclebin():
    os.startfile("C:\$Recycle.Bin\S-1-5-21-3496414530-3704387798-3435682941-1001")
def mypc():
    os.startfile("C:")
def youtube():
    webbrowser.open("https://www.youtube.com/?gl=IN")
def search():
    global var
    text=var.get()
    try:
        # if text=="VS code":
        #     Vs()
        if text=="microsoft":
            microsoft()
        elif text=="chrome":
            chrome()
        elif text=="mypc":
            mypc()
        elif text=="recyclebin":
            recyclebin()
        elif text=="youtube":
            youtube()
        elif text=="calculator":
            calculator()
        else:
            raise ValueError
    except Exception:
        tmsg.showinfo("File","File not found")

def searchenter(event):
    global var
    text=var.get()
    try:
        # if text=="VS code":
        #     Vs()
        if text=="microsoft":
            microsoft()
        elif text=="chrome":
            chrome()
        elif text=="mypc":
            mypc()
        elif text=="recyclebin":
            recyclebin()
        elif text=="youtube":
            youtube()
        elif text=="calculator":
            calculator()
        else:
            raise ValueError
    except Exception:
        tmsg.showinfo("File","File not found")

def calculator():
    calculatorwindow.calculator_window()
    

root=Tk()
root.geometry("1400x750")

root.title("Software interface")
root.resizable(False,False)

wi=Image.open("window interface.jpg")
wiphoto=ImageTk.PhotoImage(wi)
wi_face=Label(root,image=wiphoto)
wi_face.place(relheight=1,relwidth=1)

for i in range(0,36,3):
    root.rowconfigure(i,weight=1)
    root.rowconfigure(i+1,weight=4)
    root.rowconfigure(i+2,weight=1)
    
    root.columnconfigure(i,weight=1)
    root.columnconfigure(i+1,weight=4)
    root.columnconfigure(i+2,weight=1)

original_pcicon1=Image.open("pc-icon-1.png")
resized_pcicon1=original_pcicon1.resize((60,60))
image0=ImageTk.PhotoImage(resized_pcicon1)
Button(root,image=image0,background="light blue",borderwidth=0,command=mypc).grid(row=1,column=1,sticky='n')
Label(root,text="My PC",background="light blue").grid(row=1,column=1,sticky='s')

# original_pcicon1=Image.open("VS.png")
# resized_pcicon1=original_pcicon1.resize((60,60))
# image1=ImageTk.PhotoImage(resized_pcicon1)
# Button(root,image=image1,background="light blue",borderwidth=0,command=Vs).grid(row=4,column=1,sticky='n')
# Label(root,text="VS code",background="light blue").grid(row=4,column=1,sticky='s')


original_pcicon1=Image.open("microsoftedge.png")
resized_pcicon1=original_pcicon1.resize((60,60))
image2=ImageTk.PhotoImage(resized_pcicon1)
Button(root,image=image2,background="light blue",borderwidth=0,command=microsoft).grid(row=4,column=1,sticky='n')
Label(root,text="Microsoft",background="light blue").grid(row=4,column=1,sticky='s')

original_pcicon1=Image.open("chrome.png")
resized_pcicon1=original_pcicon1.resize((60,60))
image3=ImageTk.PhotoImage(resized_pcicon1)
Button(root,image=image3,background="light blue",borderwidth=0,command=chrome).grid(row=7,column=1,sticky='n')
Label(root,text="Chrome",background="light blue").grid(row=7,column=1,sticky='s')

original_pcicon1=Image.open("youtube.png")
resized_pcicon1=original_pcicon1.resize((60,60))
image4=ImageTk.PhotoImage(resized_pcicon1)
Button(root,image=image4,background="light blue",borderwidth=0,command=youtube).grid(row=10,column=1,sticky='n')
Label(root,text="YouTube",background="light blue").grid(row=10,column=1,sticky='s')

original_pcicon1=Image.open("recyclebin.png")
resized_pcicon1=original_pcicon1.resize((60,60))
image5=ImageTk.PhotoImage(resized_pcicon1)
Button(root,image=image5,background="light blue",borderwidth=0,command=recyclebin).grid(row=13,column=1,sticky='n')
Label(root,text="Recycle Bin",background="light blue").grid(row=13,column=1,sticky='s')

sbar=Label(root,bg="light blue")
sbar.rowconfigure(0,pad=1)
sbar.columnconfigure(0,pad=4)
sbar.columnconfigure(1,pad=5)
sbar.columnconfigure(2,pad=1)
sbar.columnconfigure(3,pad=1)
sbar.columnconfigure(4,pad=1)
sbar.columnconfigure(5,pad=5)
sbar.columnconfigure(6,pad=5)
sbar.columnconfigure(7,pad=900)
sbar.columnconfigure(8,pad=5)
var=StringVar()

original_pcicon1=Image.open("windows.png")
resized_pcicon1=original_pcicon1.resize((35,30))
image6=ImageTk.PhotoImage(resized_pcicon1)
Button(sbar,image=image6,background="light blue",borderwidth=0).grid(row=0,column=0,sticky='s')

original_pcicon1=Image.open("search.png")
resized_pcicon1=original_pcicon1.resize((35,30))
image7=ImageTk.PhotoImage(resized_pcicon1)
Button(sbar,image=image7,background="light blue",borderwidth=0,command=search).grid(row=0,column=4,sticky='s')


text=Label(sbar,text="Search",background="light blue")
text.grid(row=0,column=2)
search=Entry(sbar,textvariable=var)
search.grid(row=0,column=3)
search.bind("<Return>",searchenter)

original_pcicon1=Image.open("settings.png")
resized_pcicon1=original_pcicon1.resize((35,30))
image8=ImageTk.PhotoImage(resized_pcicon1)
Button(sbar,image=image8,background="light blue",borderwidth=0).grid(row=0,column=5,sticky='s')

original_pcicon1=Image.open("calculator.png")
resized_pcicon1=original_pcicon1.resize((35,30))
image10=ImageTk.PhotoImage(resized_pcicon1)
b=Button(sbar,image=image10,background="light blue",borderwidth=0,command=calculator).grid(row=0,column=6,sticky='nsw')

original_pcicon1=Image.open("weather.png")
resized_pcicon1=original_pcicon1.resize((30,30))
image11=ImageTk.PhotoImage(resized_pcicon1)
b=Button(sbar,image=image11,background="light blue",borderwidth=0,command=weather).grid(row=0,column=7,sticky='nsw')

original_pcicon1=Image.open("clock.png")
resized_pcicon1=original_pcicon1.resize((35,30))
image9=ImageTk.PhotoImage(resized_pcicon1)
Button(sbar,image=image9,background="light blue",borderwidth=0).grid(row=0,column=7,sticky='nse')

time_box=Label(sbar,text="time",background="light blue")
time_box.grid(row=0,column=8,sticky='nse')

date_time()

sbar.grid(row=35,column=0,rowspan=38,columnspan=38,sticky='nsew')

root.mainloop()