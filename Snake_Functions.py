import pygame
import sys
import random
from Snake_Class import Body
from time import sleep


def collide(snake, mouse, body, ai_screen, score):
    if pygame.Rect.colliderect(snake.rect, mouse.rect):
        bodies = Body(snake)
        if len(body) > 0:
            body_update(bodies, body[-1])
        else:
            bodies.location(snake, -5, -5)
        body.append(bodies)
        score.stats += 50
        score.prep_score()
        mouse_update(ai_screen, snake, mouse, body)

    collision = pygame.Rect.collidelistall(snake.rect, body)
    if len(collision) >= 4:
        snake.active = False

    if snake.rect.x == 0 or snake.rect.x == ai_screen.width - snake.width - 5:
        snake.active = False
    if snake.rect.y == 0 or snake.rect.y == ai_screen.height - snake.height:
        snake.active = False


def body_update(body_new, body_old):
    if body_old.type_now == 0:
        body_new.x = body_old.x
        body_new.y = body_old.y + 30

    elif body_old.type_now == 1:
        body_new.x = body_old.x - 30
        body_new.y = body_old.y

    elif body_old.type_now == 2:
        body_new.x = body_old.x
        body_new.y = body_old.y - 30

    elif body_old.type_now == 3:
        body_new.x = body_old.x + 30
        body_new.y = body_old.y

    body_new.type_now = body_old.type_now
    body_new.type_new = body_old.type_now


def mouse_update(ai_screen, snake, mouse, body):
    mouse.rect.x = random.randint(100, ai_screen.width - 100)
    mouse.rect.y = random.randint(100, ai_screen.height - 100)
    if pygame.Rect.colliderect(snake.rect, mouse.rect):
        mouse_update(ai_screen, snake, mouse, body)
    if pygame.Rect.collidelist(mouse.rect, body) != -1:
        mouse_update(ai_screen, snake, mouse, body)


def snake_update(snake, body):
    if snake.pause:
        pass

    elif snake.type1 == 1 and snake.rect.right <= snake.screen_rect.right:
        snake.x += snake.speed

    elif snake.type1 == 0 and snake.rect.top >= 0:
        snake.y -= snake.speed

    elif snake.type1 == 2 and snake.rect.bottom <= snake.screen_rect.bottom:
        snake.y += snake.speed

    elif snake.type1 == 3 and snake.rect.left >= 0:
        snake.x -= snake.speed

    if len(body) > 0:
        for num in range(len(body)):
            body[num].update(snake, body, num + 1)

    snake.type2 = snake.type1
    snake.rect.x = snake.x
    snake.rect.y = snake.y


def display(screen, ai_screen, snake, mouse, body, score):
    screen.fill(ai_screen.bgc)
    snake.draw()
    mouse.draw()
    score.draw()
    for bodies in body:
        bodies.draw()
    pygame.display.flip()


def events(snake, body):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_END:
                sys.exit()

            elif event.key == pygame.K_SPACE:
                if snake.once:
                    snake.pause = not snake.pause
                    snake.once = not snake.once

            elif event.key == pygame.K_UP and snake.type2 != 2:
                snake.type1 = 0
                x = int(snake.rect.x + snake.width / 3)
                y = int(snake.rect.y + snake.height/3)

            elif event.key == pygame.K_RIGHT and snake.type2 != 3:
                snake.type1 = 1
                x = int(snake.rect.x + snake.height / 3)
                y = int(snake.rect.y + snake.height / 3)

            elif event.key == pygame.K_DOWN and snake.type2 != 0:
                snake.type1 = 2
                x = int(snake.rect.x + snake.width / 3)
                y = int(snake.rect.y + snake.height / 3)

            elif event.key == pygame.K_LEFT and snake.type2 != 1:
                snake.type1 = 3
                x = int(snake.rect.x + snake.width / 3)
                y = int(snake.rect.y + snake.height / 3)

            result = snake.change_direction()
            if len(body) > 0 and result:
                body[0].location(snake, x, y)
