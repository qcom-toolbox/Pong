import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

player_width = 10
player_height = 100

ball = pygame.Rect(
            345,
            245,
            10,
            10
    )

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

font = pygame.font.Font(None, 50)

clock = pygame.time.Clock()

player_1 = pygame.Rect(

    20,
    200,
    player_width,
    player_height
)

player_2 = pygame.Rect(
    670,
    200,
    player_width,
    player_height
)

ball_speed_x = 5
ball_speed_y = 5

score_1 = 0
score_2 = 0

def reset_ball():
    global ball_speed_x, ball_speed_y

    ball.center = (350, 250)

    ball_speed_x *= -1
    ball_speed_y = 5

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_1.y -= 5

    if keys[pygame.K_s]:
        player_1.y += 5

    if keys[pygame.K_UP]:
        player_2.y -= 5

    if keys[pygame.K_DOWN]:
        player_2.y += 5

    if player_1.top < 0:
            player_1.top = 0

    if player_1.bottom > 500:
            player_1.bottom = 500

    if player_2.top < 0:
            player_2.top = 0

    if player_2.bottom > 500:
            player_2.bottom = 500

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= 500:
        ball_speed_y *= -1
        
    if ball.colliderect(player_1):
        ball.left = player_1.right
        ball_speed_x *= -1

    if ball.colliderect(player_2):
        ball.right = player_2.left
        ball_speed_x *= -1

    if ball.left <=0:
         score_2 += 1
         reset_ball()

    if ball.right >= 700:
         score_1 += 1
         reset_ball()

    screen.fill(BLACK)

    pygame.draw.rect(screen,WHITE,player_1)

    score_text = font.render(
         f"{score_1}     {score_2}",
         True,
         WHITE
    )

    screen.blit(score_text,(300,20))
    


    pygame.draw.rect(screen,WHITE,player_2)

    pygame.draw.rect(screen,WHITE,ball)

    pygame.display.update()

    clock.tick(60)

pygame.quit()