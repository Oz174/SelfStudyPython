# Import tkinter 
import tkinter

# Create the GUI window 
window = tkinter.Tk()

# Set the window size
window.geometry("600x400")

# Name the window
window.title("My First GUI Program")

# put a label in the window
label = tkinter.Label(window, text = "Hello World!").pack() # used to show an object in the window

# enter the main event loop 
window.mainloop()