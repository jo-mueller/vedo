"""Create a button using an Image icon to show its state"""
from vedo import *

def button_func(widget, evtname):
    print("button_func called")
    cone.color(button.state)
    
def on_mouse_click(event):
    if event.object:
        print("on_mouse_click", event)
        cone.color(button.state)

# Create a cone
cone = Cone().color(0)

# Create a plotter
plt = Plotter(bg='bb', axes=1)
plt.add_callback('mouse click', on_mouse_click)

plt.add(cone, __doc__)

# Create a button widget
img0 = Image(dataurl+"images/play-button.png")
img1 = Image(dataurl+"images/power-on.png")

button = ButtonWidget(
    button_func, 
    # states=["State 0", "State 1"], 
    states=[img0, img1],
    c=["red4", "blue4"],
    bc=("k9", "k5"),
    size=100,
    plotter=plt,
)
button.pos([0,0]).enable()

plt.show(elevation=-40)
