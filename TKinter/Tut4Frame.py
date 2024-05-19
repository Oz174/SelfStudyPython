# Import tkinter 
import tkinter
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.ttk
# Create the GUI window 
window = tkinter.Tk()

# Set the window size
window.geometry("600x400")
window.title("Frames in TKinter")

# Name the window
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")

button1 = tkinter.Button(top_frame, text="Button 1", fg="red").pack()
button2 = tkinter.Button(top_frame, text="Button 2", fg="green").pack()

button3 = tkinter.Button(bottom_frame, text="Button 3", fg="purple").pack(side="left")
button4 = tkinter.Button(bottom_frame, text="Button 4", fg="orange").pack(side="left")


window.mainloop()

