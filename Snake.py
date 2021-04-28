from Snake_Class import *
from Snake_Functions import *
from time import sleep
import os


def run_game():
    ai_screen = Setting()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (45, 45)
    pygame.init()
    screen = pygame.display.set_mode((ai_screen.width, ai_screen.height))
    pygame.display.set_caption('SNAKE')
    snake = Snake(screen)
    body = []
    mouse = Mouse(screen)
    score = Score(screen)
    mouse_update(ai_screen, snake, mouse, body)

    while snake.active:
        events(snake, body)
        snake_update(snake, body)
        collide(snake, mouse, body, ai_screen, score)
        display(screen, ai_screen, snake, mouse, body, score)

    screen.fill((128, 0, 128))
    score.prep_image()
    score.prep_score(True)
    score.draw()
    pygame.display.flip()
    sleep(3)


run_game()
