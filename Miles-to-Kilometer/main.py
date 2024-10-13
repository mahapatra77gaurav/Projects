from tkinter import *


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20,pady=20)
window.size()

#Entry
miles = Entry(width=10)
miles.grid(column=1,row=0)

#Label1
label1 = Label(text="Miles")
label1.grid(column=2,row=0)

#Label2
label2 = Label(text="is equal to")
label2.grid(column=0,row=1)

#Label3
label3 = Label(text="0")
label3.grid(column=1,row=1)

#Label4
label4 = Label(text="Km")
label4.grid(column=2,row=1)

def miles_to_km():
    mile = float(miles.get())
    km = round(mile*1.609,2)
    label3.config(text=km)

#Button
button = Button(text="Calculate", command= miles_to_km)
button.grid(column=1,row=2)


window.mainloop()

