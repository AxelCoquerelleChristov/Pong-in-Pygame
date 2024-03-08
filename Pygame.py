import sys, pygame, random

pygame.init()


def Ball_restart():
    global Ball_x_speed, Ball_y_speed
    ball.center = (screen_width / 2, screen_height / 2)
    Ball_y_speed *= random.choice((1, -1))
    Ball_x_speed *= random.choice((1, -1))


def ball_animation():
    global Ball_x_speed, Ball_y_speed, score_Opp, score_P1
    ball.x += Ball_x_speed
    ball.y += Ball_y_speed

    if ball.top <= 0 or ball.bottom >= screen_height:
        Ball_y_speed *= -1
    if ball.left <= 0:
        Ball_restart()
        score_P1 += 1
    if ball.right >= screen_width:
        Ball_restart()
        score_Opp += 1

    if ball.colliderect(player1) or ball.colliderect(opponent):
        Ball_x_speed *= -1


def player1animation():
    player1.y += player_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height


def opponentAnimation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


Clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player1 = pygame.Rect(screen_width - 15, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(5, screen_height / 2 - 70, 10, 140)

White = (255, 255, 255)
Black = (0, 0, 0)

Ball_x_speed = 7
Ball_y_speed = 7
player_speed = 0
opponent_speed = 0

score_Opp = 0
score_P1 = 0

game_font = pygame.font.Font("freesansbold.ttf", 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # p1 mov
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
        # opp mov
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opponent_speed += 7
            if event.key == pygame.K_w:
                opponent_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                opponent_speed -= 7
            if event.key == pygame.K_w:
                opponent_speed += 7

    ball_animation()
    player1animation()
    opponentAnimation()

    screen.fill(Black)
    Player1_score = game_font.render(f"{score_P1}", False, White)
    screen.blit(Player1_score, (660, 470))

    Opponent_score = game_font.render(f"{score_Opp}", False, White)
    screen.blit(Opponent_score, (600, 470))

    pygame.draw.rect(screen, White, player1)
    pygame.draw.rect(screen, White, opponent)
    pygame.draw.aaline(screen, White, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.draw.ellipse(screen, White, ball)

    pygame.display.flip()
    Clock.tick(60)
