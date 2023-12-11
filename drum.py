import pygame
import math

pygame.mixer.init()
pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the name for the game window
pygame.display.set_caption("Viljami's Mega Cool Drum Machine v 1.337")

# Load the sounds
kick = pygame.mixer.Sound('kick.wav')
snare = pygame.mixer.Sound('snare.wav')
hihat = pygame.mixer.Sound('hihat.wav')

# Load the images
snare_image = pygame.image.load('snare.png')
hihat_image = pygame.image.load('hihat.png')
kick_image = pygame.image.load('kick.png')

# Scale the images
image_size = (150, 150)
snare_image = pygame.transform.scale(snare_image, image_size)
hihat_image = pygame.transform.scale(hihat_image, image_size)
kick_image = pygame.transform.scale(kick_image, image_size)

# Drum pos
snare_pos = (WIDTH // 4 - image_size[0], HEIGHT // 2 - image_size[1] // 2)
hihat_pos = (WIDTH // 2 - image_size[0] // 2, HEIGHT // 2 - image_size[1] // 2)
kick_pos = (WIDTH // 4 * 3, HEIGHT // 2 - image_size[1] // 2)


# Display the drums
def draw():
    screen.fill((255, 255, 255))
    screen.blit(snare_image, snare_pos)
    screen.blit(hihat_image, hihat_pos)
    screen.blit(kick_image, kick_pos)
    pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h or event.key == pygame.K_u or event.key == pygame.K_i:
                hihat.play()
            elif event.key == pygame.K_k or event.key == pygame.K_o or event.key == pygame.K_m:
                kick.play()
            elif event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                snare.play()
    
    draw()

# Default key binds:
# Default kick = K,O,M
# Default hihat = H,U,I
# Default snare = S,A,D

pygame.quit()
