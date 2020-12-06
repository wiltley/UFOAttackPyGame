import sys, pygame, time, random
pygame.init()

size = width, height = 300, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
enemyArray = []
waveNumber = 0

class enemy: 
    def __init__(self, size):
        self.ball = pygame.image.load("ufo.png")
        self.ballrect = self.ball.get_rect()
        self.ballrect = self.ballrect.move(random.randint(0,265), 0)
        self.speed = [0, 1]
        self.size = size
    def moveDown(self):
        self.ballrect = self.ballrect.move(self.speed)
    def destroy(self):
        if self.ballrect.bottom == (self.size[1]-200):
            return 1

while 1:
    time.sleep(0.01)
    enemyArray.append((enemy(size)))

    # IF QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    # MOVE ALL ENEMIES/DESTROY ENEMIES
    en = 0
    for en in enemyArray:
        en.moveDown()
        if(en.destroy() == 1):
            enemyArray.remove(en)

    # TO REMOVE THE OLD IMAGE OF THE MOVED ENEMIES/PLAYER
    screen.fill(black)

    # REDRAWS ALL THE ENEMIES ON THE SCREEN
    en = 0
    for en in enemyArray:
        screen.blit(en.ball, en.ballrect)
    pygame.display.flip()