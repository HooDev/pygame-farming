import pygame
import sys
import os

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 720
FPS = 60
BG_COLOR = (30, 30, 30)
PLAYER_SPRITESHEET = ".\\assets\Sprout Lands - Sprites - premium pack\Characters\Basic Charakter Spritesheet.png" 

FRAME_WIDTH, FRAME_HEIGHT = 48, 48
FRAME_DURATION = 100 # miliseconds

PLAYER_SPEED = 150

class Player:
    def __init__(self, spritesheet):
        self.spritesheet = pygame.image.load(spritesheet).convert_alpha()
        self.moving = False
        self.direction = "down"
        self.directions = {
                "down": 0,
                "up": 1,
                "left": 2,
                "right": 3
                }
        self.frame = 0
        self.animation_timer = 0
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def handle_events(self, delta_time):
        self.moving = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.direction = "up"
            self.moving = True
            self.position.y -= PLAYER_SPEED * (delta_time / 1000)
        if pressed[pygame.K_s]:
            self.direction = "down"
            self.moving = True
            self.position.y += PLAYER_SPEED * (delta_time / 1000)
        if pressed[pygame.K_a]:
            self.direction = "left"
            self.moving = True
            self.position.x -= PLAYER_SPEED * (delta_time / 1000)
        if pressed[pygame.K_d]:
            self.direction = "right"
            self.moving = True
            self.position.x += PLAYER_SPEED * (delta_time / 1000)

    def update(self, delta_time):
        if self.moving:
            self.animation_timer += delta_time
            if self.animation_timer >= FRAME_DURATION:
                self.animation_timer = 0
                self.frame = (self.frame + 1) % 4
        else:
            self.frame = 0

        self.rect = pygame.Rect(
                self.frame * FRAME_WIDTH, # left 
                self.directions[self.direction] * FRAME_HEIGHT, # top
                FRAME_WIDTH, # width 
                FRAME_HEIGHT # height
                )

    def draw(self, screen):
        screen.blit(self.spritesheet, self.position, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PyGame Farming")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(PLAYER_SPRITESHEET)


    def handle_events(self, delta_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.player.handle_events(delta_time)

    def update(self, delta_time):
        self.player.update(delta_time)

    def draw(self):
        self.screen.fill(BG_COLOR)
        
        self.player.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            delta_time = self.clock.tick(FPS)
            
            self.handle_events(delta_time)
            self.update(delta_time)
            self.draw()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

