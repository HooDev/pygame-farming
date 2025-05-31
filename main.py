import pygame
import sys
from pytmx.util_pygame import load_pygame
from player import Player
import config

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("PyGame Farming")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(config.PLAYER_SPRITESHEET)
        self.map = load_pygame("assets/Tiled/island.tmx")

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def handle_events(self, delta_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.player.handle_events(delta_time)

    def update(self, delta_time):
        self.player.update(delta_time)

    def draw(self):
        self.screen.fill(config.BG_COLOR)
        
        water = self.map.get_layer_by_name("Water")
        for x, y, tile_surface in water.tiles():
            self.screen.blit(tile_surface, (x*config.TILE_WIDTH, y*config.TILE_HEIGHT))

        ground = self.map.get_layer_by_name("Ground")
        for x, y, tile_surface in ground.tiles():
            self.screen.blit(tile_surface, (x*config.TILE_WIDTH, y*config.TILE_HEIGHT))


    def run(self):
        while self.running:
            delta_time = self.clock.tick(config.FPS)
            
            self.handle_events(delta_time)
            self.update(delta_time)
            self.draw()
           
            self.all_sprites.draw(self.screen) 

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

