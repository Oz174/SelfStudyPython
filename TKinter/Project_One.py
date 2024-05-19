""" A calculator using Tkinter"""
import tkinter

# Create the GUI window
window = tkinter.Tk()

# Set the window size
window.geometry("280x150")

# Name the window
window.title("Calculator")

# Create a text entry box
entry = tkinter.Entry(window)
entry.pack()

# Create a frame to hold the buttons
frame = tkinter.Frame(window)
frame.pack()

# Create the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add the buttons to the frame
for i in range(4):
    for j in range(4):
        b = buttons[i*4 + j]
        tkinter.Button(frame, text=b, width=5).grid(row=i, column=j)

# Enter the main event loop
window.mainloop()

