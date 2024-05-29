# Import tkinter 
import tkinter
import tkinter.messagebox

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

#create a submit button
def submit():
    # clear the entry fields
    def quit_button_clicked():
    # 11- Message Box 
        tkinter.messagebox.showinfo("Submitted", "Your entry was successfully submitted! ") 
        window.quit()
    if e1.get() == "" or e2.get() == "":
        tkinter.messagebox.showinfo("Error", "Please enter both username and password")
    else:
        quit_button_clicked()
    return

submit_btn = tkinter.Button(window, text="Submit", command=submit, bg="orange", fg="white", font=("Times New Romans",9), width=10, height=1)
submit_btn.grid(columnspan=4)


# enter the main event loop 
window.mainloop()