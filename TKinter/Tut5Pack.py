# Import tkinter 
import tkinter

# Create the GUI window 
window = tkinter.Tk()
window.title("Fill In")
window.geometry("600x400")
########################### Frames Using the Pack ###########################

suff_width = tkinter.Label(window, text="Sufficient Width", fg="white", bg="orange").pack()
all_X = tkinter.Label(window, text="Expand X", fg="white", bg="green").pack(fill='x')
all_Y = tkinter.Label(window, text="Expand Y", fg="white", bg="black").pack(side="left", fill='y')

# enter the main event loop 
window.mainloop()