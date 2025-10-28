from pyray import *
import random

init_window(800,450, "Mon jeu")
set_target_fps(10)
SIDE = 40
WIDTH  = 20 
HEIGHT = 10

vitesse = [1,0]

snake = [[1,1], [2,1], [3,1]]

perdu = False
fruit = [random.randint(0,WIDTH),random.randint(0,HEIGHT)]

while not window_should_close() and not perdu: 
    begin_drawing()
    clear_background(RAYWHITE)

    # Detection des touches
    if is_key_pressed(KEY_RIGHT) and vitesse != [-1,0] : 
        vitesse = [1,0]
    if is_key_pressed(KEY_LEFT) and vitesse != [1,0] :
        vitesse = [-1,0]
    if is_key_pressed(KEY_UP) and vitesse != [0,1] :
        vitesse = [0,-1]
    if is_key_pressed(KEY_DOWN) and vitesse != [0,-1]:
        vitesse = [0,1]
    

    #ANIMATION DU SERPENT
    vx, vy = vitesse
    hx, hy = snake[-1]
    new_head = [hx+ vx, hy+vy]


    if new_head == fruit : 
        snake = snake + [new_head]
        fruit = [random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]

    else : 
        snake = snake[1:] + [new_head]
    

    #Condition de fin de partie
    if new_head[0] >= WIDTH or new_head[0] < 0: 
         perdu = True
    if new_head[1] >= HEIGHT or new_head[1] < 0: 
        perdu = True
    if new_head in snake[:-1] : 
        perdu = True
            
    draw_rectangle(fruit[0]*SIDE,fruit[1]*SIDE,SIDE-2,SIDE-2,RED)
    for (x,y) in snake : 
        draw_rectangle(x*SIDE+1,y*SIDE+1,SIDE-2,SIDE-2,GREEN)

    end_drawing()

close_window()

