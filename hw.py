# Template for "Stopwatch: The Game"
import simplegui

# define global variables
game_data = {
    "is running?": False,
    "counter": 0,
    "stop": 0,
    "total stop": 0
  }

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = (t / 600)
    B = (t / 100) % 6
    C = (t / 10) % 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    

# define helper function score that returns current score
def score():
    return str(game_data["stop"]) + "/" + str(game_data["total stop"])
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global game_data
    timer.start()
    game_data["is running?"] = True

def stop():
    global game_data
    timer.stop()
    if game_data["is running?"]:
        game_data["total stop"] += 1
        if game_data["counter"] % 10 == 0:
            game_data["stop"] += 1
    game_data["is running?"] = False

def reset():
    global game_data
    timer.stop()
    game_data["is running?"] = False
    game_data["counter"] = game_data["stop"] = game_data["total stop"] = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global game_data
    game_data["counter"] += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(game_data["counter"]), [60, 85], 36, "White")
    canvas.draw_text(score(), [155, 25], 26, "Green")

# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)

# register event handlers
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
