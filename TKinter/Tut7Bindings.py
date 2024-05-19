# Import tkinter 
import tkinter
import tkinter.messagebox

# Create the GUI window 
window = tkinter.Tk()

# Set the window size
window.geometry("600x400")

# Name the window
window.title("Event handling")

# from the events concerning the mouse that we can map is 
# 1- Button 1 : Left click 
# 2- Button 2 : Middle click (wheel )
# 3- Button 3 : Right click

# binding the left click 
def left_click(event):
    tkinter.Label(window, text="Left Click").pack()

def middle_click(event):
    tkinter.Label(window, text="Middle Click").pack()
# binding the right click
def right_click(event):
    tkinter.Label(window, text="Right Click").pack()

# button = tkinter.Button(window, text="Click Me")
# button.bind("<Button-1>", left_click) #bind takes 2 arguments 
# button.bind("<Button-3>", right_click) # the first is event , 2nd is fn
# button.pack() # comes after binding is done

# using window bind instead of btn bind 
window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)


# enter the main event loop 
window.mainloop()