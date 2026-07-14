import sys
import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)


window_height = 600
window_width = 800

screen = pygame.display.set_mode((window_width, window_height))


bg = pygame.image.load("Textures/Background.png").convert()
bg = pygame.transform.scale(bg, (window_width, window_height))

ts = pygame.image.load("Textures/Title_Screen.jar").convert()
ts = pygame.transform.scale(ts, (window_width, window_height))

ball_texture = pygame.image.load("Textures/Ball.png").convert_alpha()
ball_texture = pygame.transform.scale(ball_texture, (16, 16))

player_1_pad_position = 200
player_2_pad_position = 200

ai_mode = 0

player_1_pad = 20
player_2_pad = window_width - 30

player_width = 10
player_height = 100

ball = pygame.Rect(
            window_width // 2 - 8,
            window_height // 2 - 8,
            16,
            16
    )

size = (window_width,window_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Champions With RTX")

font = pygame.font.Font('Font/Font.ttf', 50)

clock = pygame.time.Clock()

# Player Variables

player_1 = pygame.Rect(

    player_1_pad,
    player_1_pad_position,
    player_width,
    player_height
)

player_2 = pygame.Rect(
    player_2_pad,
    player_2_pad_position,
    player_width,
    player_height
)

# Ball speed variables

ball_speed_x = 5
ball_speed_y = 5

score_1 = 0
score_2 = 0

# Reset the ball to the center of the screen and reverse its direction

def reset_score():
    global score_1, score_2
    score_1 = 0
    score_2 = 0

def reset_ball():
    global ball_speed_x, ball_speed_y

    ball.center = (window_width // 2, window_height // 2)

    ball_speed_x *= -1
    ball_speed_y = 5

running = True

def game():
    global running, ball_speed_x, ball_speed_y, score_1, score_2
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

        if player_1.bottom > window_height:
                player_1.bottom = window_height

        if player_2.top < 0:
                player_2.top = 0

        if player_2.bottom > window_height:
                player_2.bottom = window_height

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= window_height:
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

        if ball.right >= window_width:
             score_1 += 1
             reset_ball()

        screen.blit(bg, (0, 0))

        pygame.draw.rect(screen,WHITE,player_1)

        score_text = font.render(
             f"{score_1}     {score_2}",
             True,
             WHITE
        )

        title_text = font.render(str(int(clock.get_fps())), True, WHITE)
        screen.blit(title_text, (20, 20))

        score_rect = score_text.get_rect(center=(window_width // 2, 30))
        screen.blit(score_text, score_rect)

        if score_1 == 10 or score_2 == 10:
            winner_text = font.render(
                "Player 1 Wins!" if score_1 == 10 else "Player 2 Wins!",
                True,
                WHITE
            )
            winner_rect = winner_text.get_rect(center=(window_width // 2, window_height // 2))
            screen.blit(winner_text, winner_rect)
            pygame.display.update()
            pygame.time.delay(3000)
            reset_score()
            reset_ball()
            start_menu()


        pygame.draw.rect(screen,WHITE,player_2)

        screen.blit(ball_texture, ball)

        pygame.display.update()

        clock.tick(60)

def start_menu():

    while True:

        screen.blit(ts, (0, 0))
        mouse = pygame.mouse.get_pos()

#        title_text = font.render("PONG CHAMPIONS", True, WHITE)
#        title_rect = title_text.get_rect(center=(window_width // 2, 100))
#        screen.blit(title_text, title_rect)

        play_button = pygame.Rect(window_width // 2 - 70, window_height // 2 - 25, 140, 50)
#        solo_button = pygame.Rect(window_width // 2 - 70, window_height // 2 + 5, 140, 50)
        quit_button = pygame.Rect(window_width // 2 - 70, window_height // 2 + 55, 140, 50)

        pygame.draw.rect(screen, WHITE if play_button.collidepoint(mouse) else BLACK, play_button)
#        pygame.draw.rect(screen, WHITE if solo_button.collidepoint(mouse) else BLACK, solo_button)
        pygame.draw.rect(screen, WHITE if quit_button.collidepoint(mouse) else BLACK, quit_button)

        play_text = font.render("Play", True, WHITE)
        play_rect = play_text.get_rect(center=play_button.center)
        screen.blit(play_text, play_rect)

        # solo_text = font.render("Solo", True, WHITE)
        # solo_rect = solo_text.get_rect(center=solo_button.center)
        # screen.blit(solo_text, solo_rect)

        quit_text = font.render("Quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(quit_text, quit_rect)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.collidepoint(mouse):
                    game()

#                if solo_button.collidepoint(mouse):
#                    global ai_mode
#                    ai_mode = 1
#                    game()

                if quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

start_menu()

pygame.quit()