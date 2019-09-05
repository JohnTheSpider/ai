import numpy as np
from tkinter import *
from util.color import Color

canvas_wight = 8
canvas_height = 8
brush_size = 10
color = "black"

def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_rectangle(x1,y1,x2,y2,fill=color,outline=color)



root = Tk()
root.title("Paint для смайликов(грустный или веселый)")
#root.minsize(700,700)
#root.geometry("700x700")
w = Canvas(root, width=canvas_wight,height=canvas_height,bg="white")
#w.scale(700, 700)
w.bind("<B1-Motion>", paint)
w.grid(row=2, column=0,
       columnspan=7,padx=5,pady=5, sticky=E+W+S+N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)
w.pack

root.mainloop()


def sigmoid(x):
    return  1 / (1 + np.exp(-x))


training_inputs = np.array([[w],
                            ])
training_outputs = np.array([[1]]).T
np.random.seed(1)
synaptic_weights = 2 * np.random.random((3,1)) - 1
print ("Случайные веса: ")
print  (synaptic_weights)
for i in range(20000):
 input_layer = training_inputs
 outputs = sigmoid(np.dot(input_layer, synaptic_weights))

 err = training_outputs - outputs
 adjustments = np.dot( input_layer.T, err * (outputs * (1 - outputs)))
 synaptic_weights += adjustments;
print ("Веса после обучения :")
print (synaptic_weights)
print ("Результат:")
print (outputs)

new_inputs = np.array([1,1,0])
outputs = sigmoid(np.dot(new_inputs, synaptic_weights))
print("Новая ситуация:")
print (outputs)
