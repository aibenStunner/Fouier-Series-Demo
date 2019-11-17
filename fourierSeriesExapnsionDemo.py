__author__ = '8.Ball'

from tkinter import *
import tkinter as tk
from math import *



class Applet:
    def __init__(self):
        global circleNumber, temp
        circleNumber, temp = 1, 1


        self.height = 300
        self.width = 700

        self.window = Tk()
        self.window.title("Fourier Series Visualiser")
        self.window.geometry(str(self.width)+"x"+str(self.height)+"+0+0")

        self.canvas = Canvas(self.window, bg = "black")
        self.canvas.place(x=0,y=70, width = self.width, height = self.height)

        self.centerX, self.centerY = 100, 115
        self.startX = 300

        self.squareStartX = 300

        self.angle = 0
        self.points = []
        self.aRefresh = []

        self.squarePoints = []
        self.squareRefresh = []


        self.update_label=\
                        tk.Label(self.window,
                                 text="Enter number of terms(n)",
                                 )
        self.update_label.grid(row=0, column=0)


        self.update=tk.Entry(self.window)
        self.update.grid(row=0, column=3)


        self.quit_button=tk.Button\
                          (self.window, text='QUIT',
                           command=lambda *args:
                           [self.window.quit(), self.window.destroy()])
        self.quit_button.grid(row=4, column=6)


        self.slider_label=tk.Label(self.window, text="Select number of terms(n)")
        self.slider_label.grid(row=0, column=9)

        self.slider=tk.Scale(self.window,from_=1, to=30,
                                   orient=tk.HORIZONTAL,
                                   length=200,
                                   command=self.sliderGet)
        self.slider.grid(row=0, column=10)
        self.slider.set(1)


        self.start()

    def get(self):
        try:
            circleNumber = int(self.update.get())
        except:
            circleNumber = 1
        return circleNumber

    def sliderGet(self,event):
        global temp
        temp = self.slider.get()
        circleNumber = temp
        return circleNumber

    def start(self):
        for i in self.aRefresh:
            self.canvas.delete(i)
        self.aRefresh.clear()

        for i in self.points:
            self.canvas.move(i, 1, 0)

        nX, nY = self.centerX, self.centerY
        sX, sY = nX, nY


        if self.update.get():
            circleNumber = self.get()
        else:
            circleNumber = temp


        for i in range(circleNumber):

            n = 2*i + 1
            radius = 60 * 4 / (n*pi)
            self.aRefresh.append( self.canvas.create_oval(nX - radius, nY - radius, nX + radius, nY+ radius, outline = "chartreuse" ) )
            self.aRefresh.append( self.canvas.create_oval(nX - 2, nY - 2, nX + 2, nY + 2, fill = "red") )
            nX += radius * cos(n * self.angle)
            nY += radius * sin(n * self.angle)

            sX += self.angle
            sY += self.angle


        self.aRefresh.append( self.canvas.create_oval(nX - 2, nY - 2, nX + 2, nY + 2, fill = "red") )
        self.points.append( self.canvas.create_line(self.startX, nY, self.startX+1, nY+1, fill = "red") ) #Image


        # self.points.append( self.canvas.create_line(self.startX+radius, sY+radius, self.startX+1+radius, sY+1+radius, fill = "red") ) #Image

        self.aRefresh.append( self.canvas.create_oval(self.startX-3, nY-3, self.startX+3, nY+3, fill = "chartreuse") ) #boutLigne
        self.aRefresh.append( self.canvas.create_line(nX, nY, self.startX, nY, fill = "chartreuse") ) #Ligne reliant




        self.angle += 0.025
        self.canvas.after(1, self.start)

        if len(self.points) > 1000:
            self.canvas.delete(self.points[0])
            self.points.pop(0)

App = Applet()
tk.mainloop()
