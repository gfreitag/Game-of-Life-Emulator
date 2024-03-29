#Game of Life
#Author: Greta Freitag
#

import tkinter
import random

##########################################################

class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title=tkinter.Label(text="Game of Life", background="light blue").pack(fill=tkinter.X)
        self.run = tkinter.Button(self, text="run", command=self.play)
        self.random = tkinter.Button(self, text="randomize", command=self.initialState)
        self.canvas = tkinter.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.run.pack(padx=90, pady=10, side=tkinter.RIGHT)
        self.random.pack(padx=90, pady=10, side=tkinter.LEFT)
        self.rows=100
        self.columns=100
        self.cells={}

    def initialState(self):
        for x in range(0,self.rows):
            for y in range(0,self.columns):
                val=random.randint(0,1)
                self.cells[x,y] = val
                if(val==0):
                    self.canvas.create_rectangle(x*5,y*5,x*5+5,y*5+5, fill="white", tags=("rect","dead"))
                if(val==1):
                    self.canvas.create_rectangle(x*5,y*5,x*5+5,y*5+5, fill="black", tags=("rect","live"))


    def update(self):
        liveCount=0
        newcells={}
        #First two loops for rows and columns, last two for checking surrounding
        #cells without excessive if statements.
        for i in range(0,self.rows):
            for j in range(0,self.columns):
                for m in range(-1,2):
                    for n in range(-1,2):
                        if (i+m,j+n) in self.cells:
                            if(self.cells[(i+m,j+n)]==1):
                                liveCount+=1;
                        if((m==0 and n==0) and self.cells[(i,j)]==1):
                            liveCount-=1;
                #Update live or dead
                if(self.cells[(i,j)]==0):
                    if(liveCount==3):
                        newcells[(i,j)]=1
                    else:
                        newcells[(i,j)]=0

                elif(self.cells[(i,j)]==1):
                    if(liveCount<2):
                        newcells[(i,j)]=0
                    if(liveCount==2 or liveCount==3):
                        newcells[(i,j)]=1
                    if(liveCount>3):
                        newcells[(i,j)]=0
                liveCount=0
        self.cells=newcells

    #Draws on canvas
    def display(self):
        for x in range(0,self.rows):
            for y in range(0,self.columns):
                if(self.cells[(x,y)]==0):
                    self.canvas.create_rectangle(x*5,y*5,x*5+5,y*5+5, fill="white", tags=("rect","dead"))
                if(self.cells[(x,y)]==1):
                    self.canvas.create_rectangle(x*5,y*5,x*5+5,y*5+5, fill="black", tags=("rect","live"))

    #Clears the canvas so I'm not just drawing rectangles on top of more rectangles
    def clearCanvas(self):
        self.canvas.delete("all")

    #one generation of life
    def play(self):
        self.update()
        self.clearCanvas()
        self.display()
        self.canvas.after(1, self.play)


##########################################################
if __name__ == "__main__":

    app = App()
    app.initialState()
    app.mainloop()
