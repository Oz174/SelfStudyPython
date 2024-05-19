# Import tkinter 
import tkinter

# Create the GUI window 
window = tkinter.Tk()
window.title("Login Form")

# Set the window size
window.geometry("200x100")
l1 = tkinter.Label(window, text = "Username", font=("Times New Romans",10))
l1.grid(row=0, column=0)
l2 = tkinter.Label(window, text = "Password", font=("Times New Romans",10))
l2.grid(row=1, column=0)
e1 = tkinter.Entry(window)
e1.grid(row=0, column=1)
# make the password as astericks or dots 
e2 = tkinter.Entry(window,show="*")
e2.grid(row=1, column=1)

#check box 
chk_state = tkinter.BooleanVar()
chk_state.set(False)
chk_btn = tkinter.Checkbutton(window,text="Keep me logged in", var=chk_state)
chk_btn.grid(columnspan=2)

# enter the main event loop 
window.mainloop()