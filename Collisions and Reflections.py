import simplegui
import random
ball_pos = [500,500]
ball_vel = [0,0]



def draw(canvas):
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    canvas.draw_circle(ball_pos,10,5,"Red")
    if (ball_pos[0] < 10 or ball_pos[0] + 10 >1000):
        ball_vel[0] = -ball_vel[0]
    if (ball_pos[1] <10 or ball_pos[1] + 10 > 1000):
        ball_vel[1] = -ball_vel[1]

def keyup(key):
    if (key == simplegui.KEY_MAP['left']):
        ball_vel[0] -= ball_vel[0]
    elif (key == simplegui.KEY_MAP['right']):
        ball_vel[0] -= ball_vel[0]
    elif (key == simplegui.KEY_MAP['up']):
        ball_vel[1] -= ball_vel[1]
    elif (key == simplegui.KEY_MAP['down']):
        ball_vel[1] -= ball_vel[1]
        
def keydown(key):
    if (key == simplegui.KEY_MAP['left']):
        ball_vel[0] -= 2
    elif (key == simplegui.KEY_MAP['right']):
        ball_vel[0] += 2
    elif (key == simplegui.KEY_MAP['up']):
        ball_vel[1] -= 2
    elif (key == simplegui.KEY_MAP['down']):
        ball_vel[1] += 2
    
    
frame = simplegui.create_frame("Ball Physics",1000,1000)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()