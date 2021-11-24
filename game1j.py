import pygame as pg
import  random as r
import  os
x = pg.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
screen_width=900
screen_height=600
pg.display.set_caption("Nikhil First Game")
gameWindow=pg.display.set_mode((screen_width,screen_height))
pg.mixer.init()
clock=pg.time.Clock()

font=pg.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_snk(gameWindow,color,snk_list,size):
    #print(snk_list)
    for x,y in snk_list:
        pg.draw.rect(gameWindow,color, [x, y, size, size])
def welcome():
    exit_game = False
    pg.mixer.music.load('s1.mp3')
    pg.mixer.music.play()
    while not exit_game:
        #gameWindow.fill((233,210,229))
        bgimg = pg.image.load('g2.jpg')
        bgimg = pg.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(bgimg, (0, 0))

        text_screen("Welcome to Snakes", white, 260, 250)
        text_screen("Press Space Bar To Play", white, 232, 290)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    gameloop()

        pg.display.update()
        clock.tick(60)

def gameloop():
    if not os.path.exists("his.txt"):
        with open("his.txt", 'w') as f:
            f.write("0")
    with open("his.txt", 'r') as f:
        hi = f.read()
    pg.mixer.music.load('s1.mp3')
    pg.mixer.music.play()


    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    size = 20
    fps = 30
    velocity_x = 0
    velocity_y = 0
    init_velocity = 10
    food_x = r.randrange(20, screen_width / 2)
    food_y = r.randrange(20, screen_height / 2)
    score = 0
    snk_length = 1
    snk_list = []
    while not exit_game:

        if game_over:
            with open("his.txt", 'w') as f:
                    f.write(str(hi))
            bgimg = pg.image.load('g4.jpg')
            bgimg = pg.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))

            #gameWindow.fill((white))
            text_screen("Game Over Enter enter to continue",red,screen_width/2-300,screen_height/2)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RETURN:
                        gameloop()

        else:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pg.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pg.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    if event.key==pg.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    #if event.key==pg.K_q:
                     #   score+=100
            snake_x+=velocity_x
            snake_y+=velocity_y
            #gameWindow.fill((white))
            bgimg = pg.image.load('g3.jpg')
            bgimg = pg.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=10
                #print(("Score  %d"%(score)))
                food_x = r.randrange(20, screen_width / 2)
                food_y = r.randrange(20, screen_height / 2)

                snk_length+=5

                if int(hi) < score:
                    hi = score


            pg.draw.rect(gameWindow, red, [food_x, food_y, size, size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            text_screen("Score " + str(score)+"High Score"+str(hi), red, 5, 5)
            #print(snk_list)

            if len(snk_list)>snk_length:
                del snk_list[0]
            #print(snk_list)
            if head in snk_list[:-1]:
                game_over=True
                pg.mixer.music.load('s2.mp3')
                pg.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y>screen_height or snake_y<0:
                game_over=True
                pg.mixer.music.load('s2.mp3')
                pg.mixer.music.play()

            plot_snk(gameWindow,black,snk_list,size)

        pg.display.update()
        clock.tick(fps)
    pg.quit()
    quit()
welcome()