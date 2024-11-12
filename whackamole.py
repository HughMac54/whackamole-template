import pygame
import random

def main():
    try:
        pygame.init()

        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 512
        GRID_SIZE = 32
        GRID_COLUMNS = 20
        GRID_ROWS = 16
        BACKGROUND_COLOR = "light green"
        GRID_COLOR = (0, 0, 0)

        mole_image = pygame.image.load("mole.png")
        mole_pos = (0, 0)

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()
        running = True

        def draw_grid():
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

        def draw_mole():
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))

        def move_mole():
            nonlocal mole_pos
            mole_x = random.randrange(0, GRID_COLUMNS) * GRID_SIZE
            mole_y = random.randrange(0, GRID_ROWS) * GRID_SIZE
            mole_pos = (mole_x, mole_y)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(mole_pos, (GRID_SIZE, GRID_SIZE)).collidepoint(event.pos):
                        move_mole()

            screen.fill(BACKGROUND_COLOR)
            draw_grid()
            draw_mole()
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
