import pygame
import sys
from colors import BLACK, WHITE

from const import SCALE_FACTOR, WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH

# 初始化 Pygame
pygame.init()


# 設置視窗大小
window_size = (WINDOW_WIDTH * SCALE_FACTOR, WINDOW_HEIGHT * SCALE_FACTOR)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(WINDOW_TITLE)

# 主迴圈
running = True
while running:
  for event in pygame.event.get():
    # 退出遊戲
    if event.type == pygame.QUIT:
      running = False

  # 填滿整個視窗為黑色
  screen.fill(BLACK)

  # 在視窗中央顯示文字
  font = pygame.font.Font(None, 36)
  text = font.render('「雖然你很想死，但卻感覺比很多人都活得要認真呢!」', True, WHITE)
  text_rect = text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
  screen.blit(text, text_rect)

  # 更新畫面
  pygame.display.flip()

# 退出 Pygame
pygame.quit()
sys.exit()
