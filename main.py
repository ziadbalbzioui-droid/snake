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
score = 0 

screen_width = get_monitor_width(0)
screen_height = get_monitor_height(0)

while not window_should_close() : 
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
    if not perdu : 
        vx, vy = vitesse
        hx, hy = snake[-1]
        new_head = [hx+ vx, hy+vy]

        if new_head == fruit : 
            snake = snake + [new_head]
            fruit = [random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)]
            score += 1
        else : 
            snake = snake[1:] + [new_head]
        
        draw_rectangle(fruit[0]*SIDE,fruit[1]*SIDE,SIDE-2,SIDE-2,RED)
        draw_text("Score : "+ str(score), 10, 10, 30, GRAY)



    if new_head[0] >= WIDTH :  
        new_head[0] = 0
    if new_head[0] < 0 : 
        new_head[0] = WIDTH - 1
    if new_head[1] >= HEIGHT : 
        new_head[1] = 0
    if new_head[1] < 0 : 
        new_head[1] = HEIGHT 

    #Condition de fin de partie
    if new_head in snake[:-1] : 
        perdu = True
        
    
    if perdu : 

        draw_rectangle(0,0,screen_width,screen_height,BLACK)
        draw_text("Votre score est de : " + str(score),10,  10, 50, WHITE)
        draw_text("Presser sur entrer pour réessayer",10,  60, 20, WHITE)

        if is_key_pressed(KEY_ENTER) : 
            perdu = False
            snake = snake[len(snake)-4:]
            score = 0
            
    #Dessin du serpent
    for (x,y) in snake : 
        draw_rectangle(x*SIDE+1,y*SIDE+1,SIDE-2,SIDE-2,GREEN)
    draw_rectangle(new_head[0]*SIDE +1, new_head[1]*SIDE + 1, SIDE-2, SIDE- 2, DARKGREEN)


    end_drawing()

close_window()

