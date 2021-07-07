import pgzrun
import random
FONT_COLOR = (255, 255, 255) #màu RGB
WIDTH = 1300
HEIGHT = 700
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
START_SPEECH=10
COLOR=["orange","blue"]
curren_level=1
final_level=5
game_over=False
game_complete=False
impostors=[]
animation=[]
def draw():
    global impostors,curren_level,game_over,game_complete
    screen.clear()
    screen.blit("dark",(0,0))
    if game_over:
        display_message("Game Over","Press Space to play again")
    elif game_complete:
        display_message("You won","Press Space to play again")
    else:
      for im in impostors:
            im.draw()

def update():
    global impostors,curren_level,game_over,game_complete
    if len(impostors)==0:
        impostors=make_impostors(curren_level)
    if (game_over or game_complete) and keyboard.space:
        impostors=[]
        curren_level=1
        game_complete=False
        game_over=False

def make_impostors(number_of_impostors):
    colors_to_create=get_colors_to_create(number_of_impostors)
    new_impostors=create_impostors(colors_to_create)
    layout_impostors(new_impostors)
    animate_impostors(new_impostors)
    return new_impostors

def get_colors_to_create(number_of_impostors):
    colors_to_create=["red"]
    for i in range(0,number_of_impostors):
        random_color=random.choice(COLOR)
        colors_to_create.append(random_color)
    return colors_to_create    

def create_impostors(colors_to_create):
    new_impostors=[]
    for color in colors_to_create:
        impostors=Actor(color + "-im")
        new_impostors.append(impostors)
    return new_impostors

def layout_impostors(impostors_to_layout):
    number_of_gaps = len(impostors_to_layout) + 1
    gap_size= WIDTH/number_of_gaps
    random.shuffle(impostors_to_layout)
    for index,impostors in enumerate(impostors_to_layout):
        new_x_pos= (index+1)*gap_size
        impostors.x=new_x_pos

def animate_impostors(impostors_to_animate):
    for impostors in impostors_to_animate:
        duration = START_SPEED = current_level
        impostors= Actor('impostors', anchor=('centre', 'bottom'))
        animation = animate(impostors, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animation.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global impostors, curren_level
    for impostors in impostors:
        if impostors.collidepoint(pos):
            if "red" in impostors.image:
                red_impostor_click()
            else:
                handle_game_over()

def red_impostor_click():
    global curren_level, impostors, animation, game_complete
    stop_animations(animation)
    if curren_level == final_level:
        game_complete = True
    else:
        curren_level = current_level + 1
        impostors = []
        animation = []



def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER)
    screen.draw.text(sub_heading_text,
    fontsize=30,
    center=(CENTER_X, CENTER_Y + 30),
    color=FONT_COLOR)   
pgzrun.go()
