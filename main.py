import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Main window Configuration
window = tk.Tk()
window.title("Simple Plot Generator")
window.config(bg = "lightgoldenrod1")
window.geometry("800x500")

# Functions
x_points = StringVar()
y_points = StringVar()

x_points.set("")
y_points.set("")

def submit():
    x = x_points.get()
    y = y_points.get()
    plots = choosed.get()
    mark_choosed = mark_choice.get()
    color_choosed = color_choice.get()
    line_choosed = line_choice.get()
    size_choosed = size_choice.get()
    mec_choosed = mec_choice.get()

    x_1 = x.split()
    map_x = map(int, x_1)
    final_x = list(map_x)

    y_1 = y.split()
    map_y = map(int, y_1)
    final_y = list(map_y)

    xaxis = np.array(final_x)
    yaxis = np.array(final_y)

    # Empty Field Checkings
    if not x:
        messagebox.showwarning("X-Plot", "X-Axis field is Empty!")
    elif not y:
        messagebox.showwarning("Y-plot", "Y-Axis field is Empty!")
    else:
        if plots == "Plots":
            plt.plot(xaxis, yaxis, marker = mark_choosed, color = color_choosed, linestyle = line_choosed, ms = size_choosed, mec = mec_choosed, mfc = mec_choosed)
            plt.show()
        elif plots == "Scatters":
            plt.scatter(xaxis, yaxis, marker = mark_choosed, color = color_choosed, linestyle = line_choosed, ms = size_choosed, mec = mec_choosed, mfc = mec_choosed)
            plt.show()
        elif plots == "Bars":
            plt.bar(xaxis, yaxis, color = color_choosed)
            plt.show()
        elif plots == "Histograms":
            plt.hist(xaxis, color = color_choosed)
            plt.show()
        elif plots == "Pie Charts":
            plt.pie(xaxis)
            plt.show()
        else:
            messagebox.showwarning("Field Empty", "Choose any type from the Plots")


# Placement of X-Axis and Y-Axis
xaxis = Label(window, text = "Enter your X-Axis Points (Histograms or Pie Charts points) ", font = ("Times New Roman", 15, "bold"), wraplength = 250).place(x = 50, y = 70)
xaxis_entry = Entry(window, textvariable = x_points, width = 30).place(x = 300, y = 96)
x_ins = Label(window, text = "(Enter your x-axis points followed SPACE at each point)", font = ("Times New Roman", 12), fg = "red").place(x = 120, y = 155)
yaxis = Label(window, text = "Enter your Y-Axis points: ", font = ("Times New Roman", 15, "bold")).place(x = 50, y = 200)
yaxis_entry = Entry(window, textvariable = y_points, width=30, state = "normal").place(x=300, y=206)
y_inst = Label(window, text = "(Enter your y-axis points followed by SPACE at each point)", font = ("Times New Roman", 12), fg = "red").place(x = 120, y = 235)
prop = Label(window, text = "Plot Properties", font = ("Times New Roman", 12, "bold")).place(x = 600, y = 40)

# Marker Tab
mark = Label(window, text = "Choose Marker:", font = ("Times New Roman", 15, "bold")).place(x = 580, y = 70)
mark_list = ["o", "*", ".", ",", "x", "X", "+", "P", "s", "D", "d", "p", "H", "h", "v", "^", "<", ">", "1", "2", "3", "4", "|", "_"]
mark_choice = StringVar(window)
mark_choice.set("o")
mark_option = OptionMenu(window, mark_choice, *mark_list).place(x = 625, y = 100)

# Line Color Tab
color = Label(window, text = "Line color:", font = ("Times New Roman", 15, "bold")).place(x = 600, y = 150)
color_list = {"C0":"C0","r":"Red", "b":"Blue", "g":"Green", "c":"Cyan", "m":"Magenta", "y":"Yellow", "k":"Black", "w":"White"}
color_choice = StringVar(window)
color_choice.set("C0")
color_option = OptionMenu(window, color_choice, *color_list.values()).place(x = 625, y = 180)

#Line Type Tab
line = Label(window, text = "Line Type:", font = ("Times New Roman", 15, "bold")).place(x = 600, y = 230)
line_list = {"-":"Solid Line", ":":"Dotted Line", "--":"Dashed Line", "-.":"Dashed/Dotted Line"}
line_choice = StringVar(window)
line_choice.set("")
line_option = OptionMenu(window, line_choice, *line_list.keys()).place(x = 625, y = 260)

# Marker Size Tab
size_choice = IntVar(window)
size = Label(window, text = "Marker Size:", font = ("Times New Roman", 15, "bold")).place(x = 590, y = 310)
size_entry = Entry(window, textvariable = size_choice, width = 10).place(x = 615, y = 340)

# Marker Color Tab
mec = Label(window, text = "Marker Color:", font = ("Times New Roman", 15, "bold")).place(x = 585, y = 380)
mec_list = color_list
mec_choice = StringVar(window)
mec_choice.set("C0")
mec_option = OptionMenu(window, mec_choice, *mec_list.values()).place(x = 615, y = 414)

# Details of Plots
t_plots = Label(window, text = "Choose your plots: ", font = ("Times New Roman", 15, "bold")).place(x = 110, y = 300)
ddlist = ["Plots", "Scatters", "Bars", "Histograms", "Pie Charts"]
choosed = StringVar(window)
choosed.set("Select an Option")
user_pick = StringVar()
t_plots_option = OptionMenu(window, choosed, *ddlist).place(x = 300, y = 300)
submit = Button(window, text = "Generate", command = submit, width = 15, font = ("Times New Roman", 11, "bold"), activebackground = "Green").place(x = 300, y = 350)

window.mainloop()