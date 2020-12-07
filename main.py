import sys, pygame, time, random, math
from threading import Thread
pygame.init()

size = width, height = 300, 600
playerSpeed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
enemyArray = []
waveNumber = 0

pygame.display.set_caption('Avoiding Game!')
font = pygame.font.Font('freesansbold.ttf', 20)
wave = font.render('Wave: ' + str(waveNumber), 0, (255,255,255))
waveSpawner = font.render('Wave enemy count: 0', 0, (255,255,255))
waveSpawnerRect = waveSpawner.get_rect()
waveSpawnerRect=waveSpawnerRect.move(0,22) 
background = pygame.image.load("background.png")
loserMessage = font.render('You lose!', 0, (255,0,0))
loserMessageRect = loserMessage.get_rect()
loserMessageRect  = loserMessageRect.move(65,260)
waveSpawnerRect= waveSpawnerRect.move(0,0) 

class player:
    def __init__(self, size):
        self.entity = pygame.image.load("ship.png")
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(130,470)
        self.speed = [1, 0]
        self.moveRight = 0
        self.moveLeft = 0
        self.lives = 30
    def move(self, dir):
        if(self.rect.left == 0):
            self.rect = self.rect.move(5,0)
        elif(self.rect.right == 300):
            self.rect = self.rect.move(-10,0)
        else:
            self.rect = self.rect.move(dir,0)
    def gotHit(self):
        self.lives-=1
        if(self.lives == 0):
            print ("You lose!")

class enemy: 
    def __init__(self, size):
        self.entity = pygame.image.load("ufo.png")
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(random.randint(0,265), random.randint(-800,0))
        self.speed = [0, random.randint(2,3)]
        self.size = size
    def moveDown(self):
        self.rect = self.rect.move(self.speed)
    def destroy(self):
        if self.rect.bottom == (self.size[1]):
            return 1
    def checkCollision(self, player):
        if(self.rect.bottom <= player.rect.top+15 and self.rect.bottom>= player.rect.top):
            return self.rect.colliderect(player.rect)

class explosion:
    def __init__(self, pos):
        self.entity = pygame.image.load("explosion.png")
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(random.randint(pos-50,pos-30), random.randint(460,500))
        self.counter = 0
    def increaseCount(self):
        self.counter += 1

player = player(size)
currentTime = time.time()
explosionArray = []

while 1:
    time.sleep(0.01)
    if(math.ceil(time.time()) - math.ceil(currentTime) == 5):
        i = 0
        for i in range((waveNumber*2)+1):
            enemyArray.append(enemy(size))
            currentTime = time.time()
        print(time.time())
        waveNumber+=1
        wave = font.render('Wave: ' + str(waveNumber), 0, (255,255,255))
        waveSpawner = font.render('Wave enemy count: ' + str((waveNumber-1)*2+1), 0, (255,255,255))
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
            player.gotHit()
            explosionArray.append(explosion(en.rect.right))
            enemyArray.remove(en)
        if(en.destroy() == 1):
            enemyArray.remove(en)
    '''------------------------------------------------'''
    # TO REMOVE THE OLD IMAGE OF THE MOVED ENEMIES/PLAYER
    screen.blit(background, background.get_rect())
    # REDRAWS ALL THE ENEMIES ON THE SCREEN
    en = 0
    for en in enemyArray:
        screen.blit(en.entity, en.rect)


    if player.lives <= 0:
        break
        font = pygame.font.Font('freesansbold.ttf', 40)
        loserMessage = font.render('You lose!', 0, (255,0,0))
        screen.blit(loserMessage, loserMessageRect)
        font = pygame.font.Font('freesansbold.ttf', 20)
    # GUI STUFF
    screen.blit(wave, wave.get_rect())
    screen.blit(waveSpawner, waveSpawnerRect)
    # DRAWS PLAYER
    screen.blit(player.entity, player.rect)
    # EXPLOSION
    te = 0
    for te in explosionArray:
        if te.counter == 10:
            explosionArray.remove(te)
        screen.blit(te.entity, te.rect)
        te.increaseCount()

    pygame.display.flip()