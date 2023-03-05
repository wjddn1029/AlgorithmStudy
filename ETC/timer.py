import pygame
import time

# 게임화면 설정
pygame.init()
screen_width = 800
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Digital Clock")

# 색상
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 폰트 설정
font = pygame.font.Font(None, 100)

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면에 그리기
    screen.fill(black)

    # 현재 시간
    current_time = time.strftime("%H:%M:%S", time.localtime())
    text = font.render(current_time, True, red)
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(text, text_rect)

    pygame.display.update()

# 게임 종료
pygame.quit()
