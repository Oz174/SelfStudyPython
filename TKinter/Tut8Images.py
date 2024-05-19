# Import tkinter 
import tkinter
import tkinter.messagebox

# Create the GUI window 
window = tkinter.Tk()

# Set the window size
window.geometry("800x400")

# Name the window
window.title("Images")

icon = tkinter.PhotoImage(file="./sql.png")

grid_params = {"row":0 , "column":0}
label = tkinter.Label(window, image=icon).grid(**grid_params)


# enter the main event loop 
window.mainloop()