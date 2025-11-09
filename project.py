import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
pygame.display.set_caption("Tusi Couple(Mini project)")
running = True

# parameters
N = 6
R = 150
A = R
spacing =  math.pi / N          
omega = 0.02               
phase = 0.0                      
theta0 = 1.5 * math.pi       

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for line in range(0, (N)):
        x1 = 320 + R * math.cos(math.pi/2 + line * spacing)
        y1 = 180 + R * math.sin(math.pi/2 + line * spacing)
        x2 = 320 + R * math.cos(3 * math.pi/2 + line * spacing)
        y2 = 180 + R * math.sin(3 * math.pi/2 + line * spacing)
        pygame.draw.line(screen, (255,255,255), (int(x1), int(y1)), (int(x2), int(y2)), 1)

    phase += omega

    pygame.draw.circle(screen, (255,0,255), (320,180), R, 1)

    for i in range(N):
        radius_i = A * math.sin(phase - i * spacing)
        theta_i = theta0 + i * spacing
        x = 320 + radius_i * math.cos(theta_i)
        y = 180 + radius_i * math.sin(theta_i)
        pygame.draw.circle(screen, (0,0,255), (int(x), int(y)), 6)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
