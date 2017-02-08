import simplegui
import random
x = 500
y = 500
screen_text = "Khoa doesn't do homework"

#change screensaver text input field handler
def change_text(screensaver):
    global screen_text
    screen_text = screensaver
    
    
def draw(canvas):
    canvas.draw_text(screen_text,(x,y),20,"Red")

def timer_handler():
    global x,y
    x = random.randrange(100,900)
    y = random.randrange(100,900)
    
frame = simplegui.create_frame("Screensaver",1000,1000)
inp = frame.add_input('enter text', change_text,100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000,timer_handler)
frame.start()
timer.start()
    