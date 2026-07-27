import pygame
from constants import LINE_WIDTH


class Explosion(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()


        self.position = pygame.Vector2(x, y)
        self.radius = 10
        self.timer = 0.3

    def draw(self, screen: pygame.Surface) -> None:
            pygame.draw.circle(screen, 'orange', self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.radius += 100 * dt

        self.timer -= dt
        if self.timer <= 0:
            self.kill()