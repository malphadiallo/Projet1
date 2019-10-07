from tkinter import*
import math
fen = Tk()
fen.title("astroide")
fond=Canvas(fen,width=400,height=400,bg="white")
fond.grid()
t= -math.pi
while t<= math.pi:
    x=math.cos(t)**3
    y=math.sin(t)**3
    X=200+200*x
    Y=200-200*y
    fond.create_line(x,y,X+1,Y+1)
    t=t+0.01
fen.mainloop()



fen.mainloop()
