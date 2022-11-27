from tkinter import Tk, Canvas, Button
from PIL import Image, ImageDraw

X = 0
Y = 0

app = Tk()


def set_xy(click):
    global X, Y
    X, Y = click.x, click.y


def draw_line(drag):
    global X, Y
    draw_panel.create_line((X, Y, drag.x, drag.y), fill="black", capstyle="round", smooth=True)
    draw.line([(X, Y), (drag.x, drag.y)], fill="black", joint="curve")
    X, Y = drag.x, drag.y


def save(event=None):
    # ATTENTION: This is not working properly
    image.save("image.png", "png")


# App's drawing panel
draw_panel = Canvas(app, background="white", cursor="dot")
draw_panel.place(x=0, relwidth=1.0, y=0, relheight=1.0)

# Invisible canvas for saving as an image later on
image = Image.new("RGB", (draw_panel.winfo_width(), draw_panel.winfo_height()), "white")
draw = ImageDraw.Draw(image)

# Mouse and Key bindings
draw_panel.bind('<Button-1>', set_xy)
draw_panel.bind('<B1-Motion>', draw_line)
app.bind('<s>', save)  # press 's' to save the drawing as .png

app.mainloop()
