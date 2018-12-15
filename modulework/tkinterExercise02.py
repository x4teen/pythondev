try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

root = tkinter.Tk()

root.title("Hello, World")
root.geometry('640x480+8+200')
label_message = "Hello, World"

label = tkinter.Label(root, text=label_message)
label.grid(row=0, column=0)

left_frame = tkinter.Frame(root)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief='sunken', borderwidth=1)
canvas.grid(row=1, column=0)

right_frame = tkinter.Frame(root)
right_frame.grid(row=1, column=2)

button_start = tkinter.Button(right_frame, text="Start >")
button_start.grid(row=0, column=0)
button_pause = tkinter.Button(right_frame, text="Pause ||")
button_pause.grid(row=1, column=0)
button_stop = tkinter.Button(right_frame, text="Stop <>")
button_stop.grid(row=2, column=0)

# Column configuration
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

left_frame.config(relief='raised', borderwidth=1)
right_frame.config(relief='raised', borderwidth=1)
left_frame.grid(sticky='ns')
right_frame.grid(sticky='new')


root.mainloop()

