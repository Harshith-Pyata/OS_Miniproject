from tkinter import *
from PIL import Image, ImageTk

import weatherml

def weather_window():

    global weather_type
    global Temperature
    global Humidity
    global Wind_speed
    global precipitation
    global cloud_cover
    global atmospheric
    global uv_index
    global season
    global visibility
    global location

    
    def prediction():
        print(atmospheric.get())
        res = weatherml.mlpred(Temperature.get(),Humidity.get(),Wind_speed.get(),precipitation.get(),cloud_cover.get(),atmospheric.get(),uv_index.get(),season.get(),visibility.get(),location.get())
        weather_type.set(res[0])
        result.update()

    # Initialize Tkinter window
    root = Toplevel()
    root.geometry("700x700")

    # for i in range(0,36,3):
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    root.columnconfigure(3,weight=1)

    root.title("Weather Prediction")
    root.configure(bg="light blue")

    # wi=Image.open("weather_background.jpg")
    # wiphoto=ImageTk.PhotoImage(wi)
    # wi_face=Label(root,image=wiphoto)
    # wi_face.place(relheight=1,relwidth=1)

    for i in range(0,15,1):
        root.rowconfigure(i,weight=1)

    title=Label(root,text="Weather Classifier",background="light blue",font="lucida 15 bold")
    title.grid(row=0,column=1, columnspan=2)

    Temperature=IntVar()
    Temperature.set(0)
    Humidity = IntVar()
    Humidity.set(0)
    Wind_speed = IntVar()
    Wind_speed.set(0)
    precipitation = IntVar()
    precipitation.set(0)
    cloud_cover= StringVar()
    cloud_cover.set("")
    atmospheric=IntVar()
    atmospheric.set(0)
    uv_index=IntVar()
    uv_index.set(0)
    season= StringVar()
    season.set("")
    visibility=IntVar()
    visibility.set(0)
    location=StringVar()
    location.set("")
    weather_type=StringVar()
    weather_type.set("")

    Label(root,text="Temperature",background="light blue",font="lucida 10 bold").grid(row=1,column=1,sticky='w')
    Label(root,text="Humidity",background="light blue",font="lucida 10 bold").grid(row=2,column=1,sticky='w')
    Label(root,text="Wind Speed",background="light blue",font="lucida 10 bold").grid(row=3,column=1,sticky='w')
    Label(root,text="Precipitation(%)",background="light blue",font="lucida 10 bold").grid(row=4,column=1,sticky='w')
    Label(root,text="Cloud Cover",background="light blue",font="lucida 10 bold").grid(row=5,column=1,sticky='w')
    Label(root,text="Atmospheric Pressure",background="light blue",font="lucida 10 bold").grid(row=6,column=1,sticky='w')
    Label(root,text="UV Index",background="light blue",font="lucida 10 bold").grid(row=7,column=1,sticky='w')
    Label(root,text="Season",background="light blue",font="lucida 10 bold").grid(row=8,column=1,sticky='w')
    Label(root,text="Visibility(km)",background="light blue",font="lucida 10 bold").grid(row=9,column=1,sticky='w')
    Label(root,text="Location",background="light blue",font="lucida 10 bold").grid(row=10,column=1,sticky='w')

    input1=Entry(root,textvariable=Temperature,font="lucida 12 bold",width=20)
    input1.grid(row=1,column=2,padx=10,pady=5)
    input2=Entry(root,textvariable=Humidity,font="lucida 12 bold",width=20)
    input2.grid(row=2,column=2,padx=10,pady=5)
    input3=Entry(root,textvariable=Wind_speed,font="lucida 12 bold",width=20)
    input3.grid(row=3,column=2,padx=10,pady=5)
    input4=Entry(root,textvariable=precipitation,font="lucida 12 bold",width=20)
    input4.grid(row=4,column=2,padx=10,pady=5)
    input5=OptionMenu(root,cloud_cover,"overcast","partly cloudy","clear","cloudy")
    input5.grid(row=5,column=2)
    input6=Entry(root,textvariable=atmospheric,font="lucida 12 bold",width=20)
    input6.grid(row=6,column=2,padx=10,pady=5)
    input7=Entry(root,textvariable=uv_index,font="lucida 12 bold",width=20)
    input7.grid(row=7,column=2,padx=10,pady=5)
    input8=OptionMenu(root,season,"Winter","Summer","Autumn","Spring")
    input8.grid(row=8,column=2)
    input9=Entry(root,textvariable=visibility,font="lucida 12 bold",width=20)
    input9.grid(row=9,column=2,padx=10,pady=5)
    input10=OptionMenu(root,location,"inland","mountain","coastal")
    input10.grid(row=10,column=2)

    result = Button(root,text="Predict",command=prediction,width=25).grid(row=11,column=2)

    Label(root,textvariable=weather_type,background="light blue",font="lucida 10 bold").grid(row=12,column=1,columnspan=2,sticky="s")

    # root.mainloop()
