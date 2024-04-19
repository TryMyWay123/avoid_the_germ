import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Green color for the player
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Start position of the player

    def update(self, keys):
        # Move the player based on key presses
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Keep the player inside the screen boundaries
        self.rect.x = max(0, min(self.rect.x, 750))
        self.rect.y = max(0, min(self.rect.y, 550))

class Virus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))  # Red color for the virus
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Position the virus

    def update(self):
        # Move the virus horizontally
        self.rect.x += 2
        if self.rect.left > 800:
            self.rect.right = 0  # Wrap around if the virus moves off the screen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Avoid the Virus")
        self.clock = pygame.time.Clock()

        # Create player sprite
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        # Create virus sprites
        self.viruses = pygame.sprite.Group()
        self.create_viruses()

    def create_viruses(self):
        # Create viruses and add them to the sprite group
        for i in range(5):
            virus = Virus(i * 150 + 100, 100)
            self.viruses.add(virus)
            self.all_sprites.add(virus)

    def run(self):
        while True:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

        # Update viruses
        self.viruses.update()

        # Check for collisions between player and viruses
        if pygame.sprite.spritecollideany(self.player, self.viruses):
            print("You got infected!")
            pygame.quit()
            sys.exit()

    def render(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

