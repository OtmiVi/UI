from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text='button1', fg='green')
button2 = Button(bottom_frame, text='button2', fg='red')
button3 = Button(bottom_frame, text='button3')
button1.pack()
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
help(Button)
# the_label = Label(root, text="Hello World")
# the_label.pack()


root.mainloop()
