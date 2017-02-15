import simplegui
screensaver_text = "Khoa still didn't do his homework"

def draw_handler(canvas):
    canvas.draw_text(screensaver_text, (200, 200), 22, 'Red')
def input_handler(text):
    global screensaver_text
    screensaver_text=text
    
def keydown_handler(key):
    global screensaver_text
    if (key == simplegui.KEY_MAP['space']):
        screensaver_text = ""
    
frame = simplegui.create_frame('Testing', 1000, 1000)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)
frame.add_input('test', input_handler, 50)
frame.start()