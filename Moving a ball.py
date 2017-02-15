import simplegui

ball_pos = [500,500]
ball_vel = [5,-5]

def draw(canvas):
    canvas.draw_circle(ball_pos,10,2,'Red','Red')
    
def time_handle():
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
frame = simplegui.create_frame("Moving ball", 1000,1000)
timer = simplegui.create_timer(1,time_handle)
timer.start()
frame.set_draw_handler(draw)
frame.start()