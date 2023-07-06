#! /usr/bin/env python3

import turtle
import tkinter as tk

# A class to manage the app
class ControlFrame():
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame.grid(row=1, column=0)
        self.canvas = tk.Canvas(parent, background="white", width=800, height=800)
        self.canvas.grid(row=0, column=0)
        
        # Defining variables for the entry fields
        self.num_sides = tk.IntVar(self.frame, 3)
        self.side_length = tk.IntVar(self.frame, 100)
        
        # Creating labels, entry fields, and draw button
        tk.Label(self.frame, text="N").pack()
        tk.Entry(self.frame, width=50, textvariable=self.num_sides).pack()
        tk.Label(self.frame, text="Side Length").pack()
        tk.Entry(self.frame, width=50, textvariable=self.side_length).pack()
        tk.Button(self.frame, width=50, text="Draw", command=lambda: self.render()).pack()
        
    def render(self):
        self.t = turtle.RawTurtle(self.canvas)
        self.t.hideturtle()
        exterior_angle = 360 / self.num_sides.get()
        for i in range(self.num_sides.get()):
            self.t.forward(self.side_length.get())
            self.t.right(exterior_angle)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Turtle and Tkinter")
    ControlFrame(root)
    root.mainloop()