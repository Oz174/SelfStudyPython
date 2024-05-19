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
window.title("Introduction to TKinter Widgets")

# There are many widgets in Tkinter , let's explore them 
# 1- Labels (as we've seen in the first program)
label = tkinter.Label(window, text = "Enter Text: ", font=("Times New Romans",10))
label.grid(row=0, column=0)

l2 = tkinter.Label(window)
l2.grid(row=3, column=0)

l3 = tkinter.Label(window, text = "Selected Option :  ", font=("Times New Romans",10))
l3.grid(row=1, column=0)

# 2- Buttons
def button_click():
    res = entry.get()
    l2.config(text = f"Welcome , {res}!")
    l3.config(text = f"Selected: {combo_box.get()}")

def quit_button_clicked():
    # 11- Message Box 
    tkinter.messagebox.showinfo("Quit", "There's nothing we can do ! ") 
    window.quit()


button = tkinter.Button(window, text = "Submit",bg="orange",fg="white", font=("Times New Romans",9), command=button_click)
button.grid(row=0, column=2)
quit_button = tkinter.Button(window, text = "Quit",bg="red",fg="white", font=("Times New Romans",9), command=quit_button_clicked)
quit_button.grid(row=10, column=10)
# 3- Radio Buttons
radio_button_1 = tkinter.Radiobutton(window, text = "Python ", value=1)
radio_button_2 = tkinter.Radiobutton(window, text = "Java",value=2)
radio_button_3 = tkinter.Radiobutton(window, text = "C++", value=3)
radio_button_1.grid(row=2, column=1)
radio_button_2.grid(row=2, column=2)
radio_button_3.grid(row=2, column=3)
radio_button_1.select()

# 4- Entry
entry = tkinter.Entry(window, width=20)
entry.grid(row=0, column=1)
# 5- Check Buttons
chk_state = tkinter.BooleanVar()
chk_state.set(False) # set check state
chk = tkinter.Checkbutton(window, text='Choose', var=chk_state)
chk.grid(row=2, column=0)
# 6- Combo Boxes
combo_box = tkinter.ttk.Combobox(window)
combo_box['values'] = ("Option 1", "Option 2", "Option 3") #tuple 
combo_box.current(0) # set the default value
combo_box.grid(row=1, column=1)
# 7- Spin Boxes
spin = tkinter.Spinbox(window, from_=0, to=10, width=5,wrap=True)
spin.grid(row=4,column=0)
# 8- Menu Bars
# 9- Notebook 
# 10- scrolled Text , specify length and width to not overlay the whole window 
# scrolled_txt = tkinter.scrolledtext.ScrolledText(window, width=20, height=20)
# scrolled_txt.grid(row=4, column=0)
# enter the main event loop 
window.mainloop()