import tkinter
from tkinter import Tk
from tkinter import ttk
from tkinter import *

root = Tk()
root.geometry("300x300")
root.title('First GUI using Python')
ttk.Button(root, text="Hello Team!!").grid()


frame1=Frame(root)

labelText= StringVar()

label= Label(frame1, textvariable=labelText)
button= Button(frame1, text='Hey')
labelText.set("hey whatsup!!")

label.pack()
button.pack()
frame1.grid()



#tkinter._test()

frame2=Frame(root)
Label(frame2,text='hey').pack()
Button(frame2,text='B1').pack(side=LEFT,fill=Y)
Button(frame2,text='B1').pack(side=RIGHT,fill=X)
Button(frame2,text='B1').pack(side=TOP,fill=Y)
Button(frame2,text='B1').pack(side=BOTTOM,fill=X)
frame2.grid()



Label(root,text="Name").grid(row=0, column=0, sticky=N)
Entry(root, width=50).grid(row=0,column=1)
Button(root, text="submit").grid(row=0,column=5)


Label(root,text="Name").grid(row=0, column=0, sticky=N)
Entry(root, width=10).grid(row=0,column=1)
Button(root, text="submit").grid(row=0,column=2)
Label(root,text="Gender").grid(row=1, column=0, sticky=N)
Radiobutton(root,text="Male",value=1).grid(row=1, column=1, sticky=N)
Radiobutton(root,text="FeMale",value=2).grid(row=1, column=2, sticky=N)

Label(root,text="courses").grid(row=3, column=0,sticky=N)
Checkbutton(root,text="Python").grid(row=3,column=1,sticky=N)
Checkbutton(root,text="Dango").grid(row=3,column=2,sticky=N)
Checkbutton(root,text="Flask").grid(row=3,column=3,sticky=N)




name = input("enter your name : ")
age = input("enter your age : ")
print("hello " + name + " ! you are " + age)

num1 = input("enter a number: ")
num2 = input("enter another number: ")
result = int(num1) + int(num2)
print(result)


root.mainloop()
