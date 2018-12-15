try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def make_window(title="Window"):
    main_window = tkinter.Tk()
    main_window.title(title)
    main_window.geometry('640x480+8+400')
    return main_window


def make_canvas(main_window):
    canvas = tkinter.Canvas(main_window, width=640, height=480)
    canvas.grid(row=0, column=0)
    return canvas


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2

    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin,
                                   y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")


root = make_window("Parabola")
canvas = make_canvas(root)
draw_axes(canvas)

root.mainloop()