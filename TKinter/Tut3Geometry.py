# Import tkinter 
import tkinter
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.ttk
# Create the GUI window 
window = tkinter.Tk()

# Set the window size
window.geometry("600x400")

# Name the window
window.title("Introduction to TKinter Gemoetry Managers (Grid, Pack, Place)")

# There are many widgets in Tkinter , let's explore them 
# 1- Labels (as we've seen in the first program)
# l1 = tkinter.Label(window, text = "Label with Pack ", font=("Times New Romans",10))
# l1.pack() #enforces pack on all next slaves

l2 = tkinter.Label(window, text = "Label with Grid at row = 0 , col = 0 ", font=("Times New Romans",10))
l2.grid(row=0, column=0)

l3 = tkinter.Label(window, text = "Label with Place at (300,200) ", font=("Times New Romans",10))
l3.place(x=300, y=200)

window.mainloop()

