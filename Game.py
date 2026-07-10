import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

while True:

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False

pygame.quit()

screen.fill(BLACK)

pygame.display.update()

player_width = 10
Player_height = 100

player_1 = pygame.Rect(

    20,
    200,
    player_width,
    Player_height
)

player_2 = pygame.Rect(
    670,
    200,
    player_width,
    Player_height
)

pygame.draw.rect(screen,WHITE,player_1)
pygame.draw.rect(screen,WHITE,player_2)

keys = pygame.key.get_pressed()

if keys[pygame.K_z]:
    player_1.y -= 5

if keys[pygame.K_s]:
    player_1.y += 5
    
if keys[pygame.K_UP]:
    player_2.y -= 5

if keys[pygame.K_DOWN]:
    player_2.y += 5

    ball = pygame.Rect(
        345,
        245,
        10,
        10
)

ball_speed_x = 5
ball_speed_y = 5

ball.x += ball_speed_x
ball.y += ball_speed_y

if ball.top <= 0 or ball.bottom >= 500:
    ball_speed_y *= -1

ball.colliderect(player_1)

if ball.colliderect(player_1) or ball.colliderect(player_2):
    ball_speed_x *= -1

pygame.draw.rect(screen,WHITE,ball)

clock = pygame.time.Clock()

clock.tick(60)

