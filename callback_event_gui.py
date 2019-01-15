from tkinter import *
root = Tk()
my_string = StringVar()
ticked_yes = BooleanVar()
group_choice = IntVar()
volumn = DoubleVar()


Entry(root, textvariable=my_string)
Checkbutton(root, text="Remeber Me", variable=ticked_yes)
Radiobutton(root, tet="Option1", variable=group_choice, value='option1')
Scale(root, label="Volume Control", variable=volumn, from=0, to=10)

# Label(root, text="Click at differet\n locations in the frame below").pack()


# def callback(event):
#     print(dir(event))
#     print()

# frame = Frame(root, bg='khaki', width=130, height=80)
# frame.bind("<KeyPress-B>", callback)
# frame.pack()
root.mainloop()
