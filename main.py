import sys, pygame, time, random
pygame.init()

size = width, height = 300, 600
playerSpeed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
enemyArray = []
waveNumber = 0

class player:
    def __init__(self, size):
        self.ball = pygame.image.load("ship.png")
        self.ballrect = self.ball.get_rect()
        self.ballrect = self.ballrect.move(130,500)
        self.speed = [1, 0]
    def movePlayer(self):
         self.ballrect = self.ballrect.move(self.speed)
    
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
        if self.ballrect.bottom == (self.size[1]-300):
            return 1

player = player(size)

while 1:

    time.sleep(0.01)
    # IF QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.movePlayer()
            if event.key == pygame.K_LEFT:
                print("ok")
    # MOVE ALL ENEMIES/DESTROY ENEMIES
    en = 0
    for en in enemyArray:
        en.moveDown()
        if(en.destroy() == 1):
            enemyArray.remove(en)

    # TO REMOVE THE OLD IMAGE OF THE MOVED ENEMIES/PLAYER
    screen.fill(black)
    # DRAWS PLAYER
    screen.blit(player.ball, player.ballrect)
    # REDRAWS ALL THE ENEMIES ON THE SCREEN
    en = 0
    for en in enemyArray:
        screen.blit(en.ball, en.ballrect)
    pygame.display.flip()