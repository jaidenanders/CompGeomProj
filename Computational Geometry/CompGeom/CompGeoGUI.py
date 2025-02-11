import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#import functions
from closest_pair import Closest_Pair
from convex_hull import Convex_Hull
from largest_empty_circle import Largest_Empty_Circle
from intersection import Intersection
#main application window
root = tk.Tk()
root.title("Computational Geometry")
root.geometry("600x450")

#label widget
label = ttk.Label(root, text="Computational Geometry GUI", font=("Arial", 14))
label.pack(pady=10)

#frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(side="left", padx=10, pady=10, anchor="n")


buttons = [
    ("Closest Pair", Closest_Pair),
    ("Convex Hull", Convex_Hull),
    ("Largest Empty Circle", Largest_Empty_Circle),
    ("Intersection", Intersection)
]

#create buttons inside the frame
for name, command in buttons:
    btn = ttk.Button(button_frame, text=name, command=command)
    btn.pack(fill="x", pady=2)
    
#exit button
exit_button = ttk.Button(button_frame, text="Exit", command=root.destroy)
exit_button.pack(side="left", anchor="s", pady=20)  # Stick to bottom left

# frame to hold the scatter plot and results text
plot_frame = tk.Frame(root)
plot_frame.pack(side="right", padx=20, pady=10, anchor="n")

#matplotlib figure
fig, ax = plt.subplots(figsize=(4, 3))  # Figure size

#generate random scatter points
x = np.random.rand(10)
y = np.random.rand(10)

#create scatter plot
ax.scatter(x, y, color='blue')
ax.set_title("Random Scatter Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

#put the Matplotlib figure inside Tkinter
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=5)  # Align the plot properly

#create a text box for displaying results
result_text = tk.Text(plot_frame, height=5, width=40, wrap="word")
result_text.pack(pady=5

#insert scatter point data into the text box
result_text.insert(tk.END, "Scatter Plot Points (x, y):\n")
for i in range(len(x)):
    result_text.insert(tk.END, f"({x[i]:.2f}, {y[i]:.2f})\n")
result_text.config(state="disabled")

#start the GUI loop
root.mainloop()

