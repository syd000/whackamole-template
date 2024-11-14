import pygame
import random


# testing again

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        new_pos_x = 0
        new_pos_y = 0
        while running:

            screen.fill("light green")

            screen.blit(mole_image, mole_image.get_rect(topleft=(new_pos_x, new_pos_y)))

            for i in range(0, 640, 32):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 512))
            for i in range(0, 512, 32):
                pygame.draw.line(screen, (0, 0, 0), (0, i), (640, i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if (mouse_x >= new_pos_x and mouse_x <= (new_pos_x + 32)) and (mouse_y >= new_pos_y and mouse_y <= (new_pos_y + 32)):
                        new_pos_x = random.randrange(0, 640, 32)
                        new_pos_y = random.randrange(0, 512, 32)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
