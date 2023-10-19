from pico2d import *

import game_world
from grass import Grass
from boy import Boy


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def create_world():
    global running
    global grass
    global team
    global boy

    running = True

    grass = Grass(60)
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)
    grass = Grass(30)
    game_world.add_object(grass, 2)


open_canvas()
create_world()

# game loop
while running:
    clear_canvas()
    handle_events()
    game_world.Update()
    game_world.Render()
    update_canvas()
    delay(0.01)
# finalization code
close_canvas()
