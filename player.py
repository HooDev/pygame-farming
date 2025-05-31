import pygame
import config

class Player(pygame.sprite.Sprite):
    def __init__(self, spritesheet):
        super().__init__()

        # Handle Spritesheet Animation
        # Slice up the frames into dirctional lists
        self.spritesheet = pygame.image.load(spritesheet).convert_alpha()
        self.frames = {}
        self.directions = ["down", "up", "left", "right"]
        for idx, direction in enumerate(self.directions):
            row_frames = []
            for i in range(config.FRAMES_PER_DIRECTION):
                rect = pygame.Rect(
                           i  * config.FRAME_WIDTH,
                           idx * config.FRAME_HEIGHT,
                           config.FRAME_WIDTH,
                           config.FRAME_HEIGHT
                        )
                row_frames.append(self.spritesheet.subsurface(rect))
            self.frames[direction] = row_frames   

        # Handle initial animation state
        self.moving = False
        self.direction = "down"
        self.frame_index = 0
        self.animation_timer = 0
        self.position = pygame.Vector2(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2)

        # Set initial player image and rect
        self.image = self.frames[self.direction][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def handle_events(self, delta_time):
        self.moving = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.direction = "up"
            self.moving = True
            self.position.y -= config.PLAYER_SPEED * (delta_time / 1000)
        if pressed[pygame.K_s]:
            self.direction = "down"
            self.moving = True
            self.position.y += config.PLAYER_SPEED * (delta_time / 1000)
        if pressed[pygame.K_a]:
            self.direction = "left"
            self.moving = True
            self.position.x -= config.PLAYER_SPEED * (delta_time / 1000)
        if pressed[pygame.K_d]:
            self.direction = "right"
            self.moving = True
            self.position.x += config.PLAYER_SPEED * (delta_time / 1000)

    def update(self, delta_time):
        if self.moving:
            self.animation_timer += delta_time
            if self.animation_timer >= config.FRAME_DURATION:
                self.animation_timer = 0
                self.frame_index = (self.frame_index + 1) % 4
        else:
            self.frame = 0

        # Update the image
        self.image = self.frames[self.direction][self.frame_index]

        # Update the rect (based on position)
        self.rect.center = self.position

