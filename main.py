from pyray import *

init_window(800,450, "Mon jeu")
set_target_fps(10)
SIDE = 40
WIDTH  = 20 
HEIGHT = 10

vitesse = [1,0]

snake = [[1,1], [2,1], [3,1]]

while not window_should_close() : 
    begin_drawing()
    clear_background(RAYWHITE)

    #ANIMATION DU SERPENT
    vx, vy = vitesse
    hx, hy = snake[-1]
    new_head = [hx+ vx, hy+vy]
    snake = snake[1:] + [new_head]


    for (x,y) in snake : 
        draw_rectangle(x*SIDE+1,y*SIDE+1,SIDE-2,SIDE-2,GREEN)

    end_drawing()

close_window()

