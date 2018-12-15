try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()
mainWindow = tkinter.Tk()

mainWindow.title("Hello, World")
mainWindow.geometry('640x480+8+400')
label_message = "Hello, World"

label = tkinter.Label(mainWindow, text=label_message)
label.pack(side='top')

left_frame = tkinter.Frame(mainWindow)
left_frame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

right_frame = tkinter.Frame(mainWindow)
right_frame.pack(side='right', anchor='n', fill=tkinter.Y, expand=True)

button_start = tkinter.Button(right_frame, text="Start >")
button_start.pack(side="top")
button_pause = tkinter.Button(right_frame, text="Pause ||")
button_pause.pack(side="top")
button_stop = tkinter.Button(right_frame, text="Stop <>")
button_stop.pack(side="top")






mainWindow.mainloop()

