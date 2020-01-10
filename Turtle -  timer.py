import turtle
# Alarm clocks, kitchen timers, and thermonuclear bombs in James Bond
# movies are set to create an “automatic” event after a certain interval. The
# turtle module in Python has a timer that can cause an event when its time is up

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)

def h1():
    tess.forward(100)
    tess.left(56)

wn.ontimer(h1, 2000) #On line 16 the
#timer is started and set to explode in 2000 milliseconds (2 seconds).
#When the event does occur, the handler is called, and tess springs into action.
#Unfortunately, when one sets a timer, it only goes off once. 
wn.mainloop()
