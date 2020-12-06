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
        self.entity = pygame.image.load("ship.png")
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(130,500)
        self.speed = [1, 0]
        self.moveRight = 0
        self.moveLeft = 0
    def move(self, dir):
        if(self.rect.left == 0):
            self.rect = self.rect.move(5,0)
        elif(self.rect.right == 300):
            self.rect = self.rect.move(-10,0)
        else:
            self.rect = self.rect.move(dir,0)

class enemy: 
    def __init__(self, size):
        self.entity = pygame.image.load("ufo.png")
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(random.randint(0,265), random.randint(-800,0))
        self.speed = [0, 1]
        self.size = size
    def moveDown(self):
        self.rect = self.rect.move(self.speed)
    def destroy(self):
        if self.rect.bottom == (self.size[1]):
            return 1
    def checkCollision(self, player):
            return self.rect.colliderect(player.rect)

player = player(size)

while 1:
    time.sleep(0.01)
    enemyArray.append(enemy(size))
    # IF QUIT AND MOVEMENT
    '''------------------------------------------------'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moveRight = 1
                player.moveLeft = 0
            if event.key == pygame.K_LEFT:
                player.moveLeft = 1
                player.moveRight = 0
        if event.type == pygame.KEYUP:
            player.moveLeft = 0
            player.moveRight = 0

    if(player.moveRight == 1):
        player.move(5)
    if(player.moveLeft == 1):
        player.move(-5)
    '''------------------------------------------------'''
    # MOVE ALL ENEMIES/DESTROY ENEMIES
    en = 0
    for en in enemyArray:
        en.moveDown()

        if(en.checkCollision(player) == 1):
            enemyArray.remove(en)
        if(en.destroy() == 1):
            enemyArray.remove(en)

    # TO REMOVE THE OLD IMAGE OF THE MOVED ENEMIES/PLAYER
    screen.fill(black)
    # REDRAWS ALL THE ENEMIES ON THE SCREEN
    en = 0
    for en in enemyArray:
        screen.blit(en.entity, en.rect)

    # DRAWS PLAYER
    screen.blit(player.entity, player.rect)
    pygame.display.flip()