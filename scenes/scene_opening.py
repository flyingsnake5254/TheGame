import pygame
import sys
from colors import BLACK, WHITE

from const import WINDOW_SIZE
from util.fade import Fade

class SceneOpening():
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode(WINDOW_SIZE)

    # font
    self.font = pygame.font.Font('fonts/content.ttf', 36)

    # 開場文字
    self.contents = [
      '「雖然你很想死，但卻感覺比很多人都活得要認真呢!」',
      '記得好像很久以前有人對我說過這句話。',
      '不過也到此為止了吧。'
    ]
    self.current_contents = 0
    self.text = self.font.render(self.contents[self.current_contents], True, WHITE)
    self.text_rect = self.text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

    # 動態物件
    self.dynamic_objects = {
      'opening_text': self.text,
      'opening_text_rect': self.text_rect
    }

    # 顯示的儲列
    self.show_function = [
      ['', lambda: self.screen.fill(BLACK)],
      ['show_text', lambda: self.screen.blit(self.dynamic_objects['opening_text'], self.dynamic_objects['opening_text_rect'])]
    ]

    # 淡入畫面
    self.text.set_alpha(0)
    self.show_function.append(
      [
        'opening_fadein', 
        Fade.fadein, 
        (self.show_function, self.dynamic_objects, 'opening_text', 'opening_fadein')
      ]
    )


    self.running = True
    while self.running:
      for event in pygame.event.get():
        # 退出遊戲
        if event.type == pygame.QUIT:
          self.running = False
        #點擊滑鼠右鍵
        if event.type == pygame.MOUSEBUTTONDOWN:
          self.current_contents += 1
          self.show_function.append(
            [
              'click_contents',
              Fade.fadeout_then_fadein,
              (
                self.show_function,
                self.dynamic_objects,
                self.font.render(self.contents[self.current_contents], True, WHITE),
                'opening_text',
                'opening_text_rect',
                'click_contents'
              )
            ]
          )
      
      # 顯示物件
      for func in self.show_function:
        if len(func) == 2:
          func[1]()
        elif len(func) == 3:
          func[1](*func[2])

      # 更新畫面
      pygame.display.flip()
    
    # 退出 Pygame
    pygame.quit()
    sys.exit()



