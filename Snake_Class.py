import pygame


class Setting:
    def __init__(self):
        self.height = 650
        self.width = 1300
        self.bgc = (255, 255, 255)


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.width = 75
        self.height = 75
        self.speed = 1.5
        self.type1 = 1
        self.type2 = 1
        self.angle = 90
        self.direction = [True, True, True, True]
        self.active = True

        self.image = pygame.image.load('Images\Snake.bmp')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.x = 650
        self.rect.y = 325
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.image = pygame.transform.rotate(self.image, self.angle)

    def change_direction(self):
        if self.direction[self.type1]:
            self.angle = 90 * (self.type2 - self.type1)
            self.angle %= 360
            self.image = pygame.transform.rotate(self.image, self.angle)
            for num in range(4):
                self.direction[num] = True
            self.direction[self.type1] = False
            return True
        else:
            return False

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Mouse:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images\Mouse copy.bmp')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Body:
    def __init__(self, snake):
        self.screen = snake.screen
        self.color = (100, 156, 73)
        self.type_now = snake.type1
        self.type_new = snake.type1
        self.rect = pygame.Rect(0, 0, 25, 25)
        self.rect.x = snake.rect.x
        self.rect.y = snake.rect.y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_change = -5
        self.y_change = -5
        self.num = True

    def update(self, snake, body, num):
        if self.x_change == self.rect.x and self.y_change == self.rect.y:
            self.type_now = self.type_new
            if len(body) > 1 and num < len(body):
                body[num].x_change = self.x_change
                body[num].y_change = self.y_change
                body[num].type_new = self.type_new

        if self.type_now == 0:
            self.y -= snake.speed

        elif self.type_now == 1:
            self.x += snake.speed

        elif self.type_now == 2:
            self.y += snake.speed

        elif self.type_now == 3:
            self.x -= snake.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def location(self, snake, x, y):
        if self.num:
            self.num = False
            if snake.type1 == 0:
                self.x = snake.rect.x + snake.width / 3
                self.y = snake.rect.y + snake.height - 1

            elif snake.type1 == 1:
                self.x = snake.rect.x - snake.width / 4 - 4
                self.y = snake.rect.y + snake.height / 3

            elif snake.type1 == 2:
                self.x = snake.rect.x + snake.width / 3
                self.y = snake.rect.y - snake.height / 4 - 4

            elif snake.type1 == 3:
                self.x = snake.rect.x + snake.width - 1
                self.y = snake.rect.y + snake.height / 3

        self.rect.x = self.x
        self.rect.y = self.y
        self.x_change = x
        self.y_change = y
        self.type_new = snake.type1

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Score:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = 0
        self.text_color = (255, 233, 0)
        self.font = pygame.font.SysFont('DejaVu Sans Mono', 50, True)
        self.prep_score()

    def prep_score(self,end = False):
        self.stats_str = "{:,}".format(int(self.stats))
        self.image = self.font.render(self.stats_str, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.right - 20
        self.rect.top = 10
        if end:
            self.rect.x = 750
            self.rect.y = 300

    def prep_image(self):
        self.msg_image = self.font.render('Your Score : ', True, self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.x = 500
        self.msg_rect.y = 300
        self.screen.blit(self.msg_image, self.msg_rect)

    def draw(self):
        self.screen.blit(self.image, self.rect)
