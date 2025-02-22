import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Creative Drawing App")
        
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack()
        
        self.color = "black"
        self.brush_size = 3
        
        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack()
        
        self.clear_button = tk.Button(self.controls_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)
        
        self.color_button = tk.Button(self.controls_frame, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)
        
        self.size_slider = tk.Scale(self.controls_frame, from_=1, to=10, orient=tk.HORIZONTAL, label="Brush Size", command=self.change_brush_size)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT)
        
    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
        
    def clear_canvas(self):
        self.canvas.delete("all")
        
    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]
        
    def change_brush_size(self, size):
        self.brush_size = int(size)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
