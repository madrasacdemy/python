import tkinter as tk
import time

def change_light():
    while True:
        canvas.itemconfig(red_light, fill="red")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="gray")
        window.update()
        time.sleep(3)
        
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="yellow")
        window.update()
        time.sleep(1)
        
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="green")
        window.update()
        time.sleep(3)
        
        canvas.itemconfig(green_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="yellow")
        window.update()
        time.sleep(1)

window = tk.Tk()
window.title("Traffic Light Simulation")
window.geometry("200x400")

canvas = tk.Canvas(window, width=200, height=400, bg="white")
canvas.pack()

canvas.create_rectangle(50, 50, 150, 250, fill="black")

red_light = canvas.create_oval(75, 60, 125, 110, fill="gray")
yellow_light = canvas.create_oval(75, 120, 125, 170, fill="gray")
green_light = canvas.create_oval(75, 180, 125, 230, fill="gray")

window.after(100, change_light)
window.mainloop()
