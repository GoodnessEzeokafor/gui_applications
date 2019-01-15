"""
Pack Geometry Manager
    - side: LEFT, TOP, RIGHT, BOTTOM
    -fill: X,Y,BOTH,NONE
    -expand: 
    -anchor: NW, N, NE, E, SE, S,SW, W, CENTER

"""
from tkinter import *
root = Tk()

Label(root, text="Username").grid(row=0, sticky=W)
Label(root, text="Password").grid(row=1, sticky=W)
Entry(root).grid(row=0, column=1, sticky=E)
Entry(root).grid(row=1, column=1, sticky=E)
Button(root, text="Login").grid(row=2, column=1, sticky=E)
# parent = Frame(root)
# Button(parent, text="ALL IS WELL").pack(fill=X)
# Button(parent, text="BACK TO BASICS").pack(fill=X)
# Button(parent, text="CATCH ME IF U CAN").pack(fill=X)

#placing the widgets side by side
# Button(parent, text="LEFT").pack(side=LEFT)
# Button(parent, text="CENTER").pack(side=LEFT)
# Button(parent, text="RIGHT").pack(side=RIGHT)
# demo of side and fill options
# Label(frame, text="Pack demo of side and fill").pack() # label
# Button(frame, text="A").pack(side=LEFT, fill=X)
# Button(frame, text="B").pack(side=TOP, fill=X)
# Button(frame, text="C").pack(side=RIGHT, fill=None)
# Button(frame, text="D").pack(side=TOP, fill=BOTH)
# frame.pack()
# Label(root, text="Pack Demo of expand").pack()
# Button(root, text="I do not expand").pack()
# Button(root, text="I do not fill x but i expand").pack(expand=1)
# Button(root, text="I fill x and expand").pack(fill=X, expand=1)
# parent.pack()
root.mainloop()

