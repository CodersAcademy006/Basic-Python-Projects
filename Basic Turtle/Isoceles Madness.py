import turtle
import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas
import random

# Create a Tkinter root window
root = tk.Tk()
root.title("Isosceles Triangle Madness - PythonTurtle.Academy")

# Create a canvas with scrolling capability
canvas = ScrolledCanvas(root)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

# Set initial window size
initial_width = 1000
initial_height = 1000
root.geometry(f"{initial_width}x{initial_height}")

# Create the Turtle screen
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")

# Create a turtle to draw the triangles
t = RawTurtle(screen)
t.hideturtle()
t.speed(0)

# Function to draw an isosceles triangle
def IsoscelesTriangle(x, y, width, height, direction, c):
    t.penup()
    t.goto(x, y)
    t.setheading(direction - 90)
    t.forward(width / 2)
    p1x, p1y = t.xcor(), t.ycor()  # first point: bottom right
    t.backward(width)
    p2x, p2y = t.xcor(), t.ycor()  # second point: bottom left
    t.goto(x, y)
    t.setheading(direction)
    t.forward(height)
    p3x, p3y = t.xcor(), t.ycor()  # third point: top
    t.goto(p1x, p1y)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    t.goto(p2x, p2y)
    t.goto(p3x, p3y)
    t.goto(p1x, p1y)
    t.end_fill()

# Function to draw multiple random triangles
def draw_triangles():
    for _ in range(50):
        IsoscelesTriangle(random.uniform(-400, 400), random.uniform(-400, 400),
                          random.uniform(30, 300), random.uniform(30, 300),
                          random.uniform(0, 360),
                          (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    screen.update()

# Function to handle window resizing and redraw the triangles
def on_resize(event):
    width, height = event.width, event.height
    canvas.config(width=width, height=height)
    screen.setworldcoordinates(-width // 2, -height // 2, width // 2, height // 2)
    draw_triangles()

# Function to generate triangles endlessly
def generate_triangles_endlessly():
    draw_triangles()  # Draw 50 random triangles
    screen.ontimer(generate_triangles_endlessly, 1000)  # Keep drawing every 1 second

# Initial drawing of the triangles
draw_triangles()

# Start the endless generation of triangles
generate_triangles_endlessly()

# Bind the resize event to redraw the triangles on resize
root.bind("<Configure>", on_resize)

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_x = (screen_width - initial_width) // 2
window_y = (screen_height - initial_height) // 2
root.geometry(f"+{window_x}+{window_y}")

# Enable window buttons like minimize, maximize, and close
root.update_idletasks()

# Start the Tkinter event loop
root.mainloop()