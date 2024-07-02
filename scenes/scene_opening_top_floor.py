import pygame
import sys
from colors import BLACK, TEXT_BG, WHITE
from const import WINDOW, WINDOW_SIZE
from util.fade import Fade
from util.text_with_background import TextWithBackground

class SceneOpeningTopFloor():
  def __init__(self):
    self.manager = None
    print('SceneOpeningTopFloor')

    # 字體
    self.font = pygame.font.Font('fonts/content.ttf', 36)

    # 對話內容
    self.contents = [
      '今天是消失的日子。',
      '終於等到了這一天，終於要消失在這世界上了。',
      '有多少人會為此而感到開心呢?',
      '嗯…',
      '可能根本不會有人在意吧! ',
      '那些似為朋友的人類，對不起，麻煩你們不少。',
      '願，快樂。',
    ]

    # 背景圖片
    self.contents_background = [
      pygame.image.load('assets/jump_off_building1.jpg'),
      pygame.image.load('assets/jump_off_building2.jpg'),
      pygame.image.load('assets/jump_off_building3.jpg'),
      pygame.image.load('assets/jump_off_building4.jpg'),
      pygame.image.load('assets/jump_off_building5.jpg'),
      pygame.image.load('assets/jump_off_building6.jpg'),
      pygame.image.load('assets/jump_off_building7.jpg')
    ]

    # 調整圖片大小
    for i in range(len(self.contents_background)):
      self.contents_background[i] = pygame.transform.scale(self.contents_background[i], (WINDOW_SIZE[0], WINDOW_SIZE[1]))

    self.current_contents = 0

    # 動態物件
    self.dynamic_objects = {
      'text': TextWithBackground(self.contents[self.current_contents], WHITE, TEXT_BG, self.font).surface,
      'text_rect': TextWithBackground(self.contents[self.current_contents], WHITE, TEXT_BG, self.font).surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 100)),
      'image': self.contents_background[self.current_contents],
      'image_rect': self.contents_background[self.current_contents].get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
    }

    # 顯示的儲列
    self.show_function = [
      ['', lambda: WINDOW.blit(self.dynamic_objects['image'], self.dynamic_objects['image_rect'])],
      ['', lambda: WINDOW.blit(self.dynamic_objects['text'], self.dynamic_objects['text_rect'])],
    ]

    self.show_function.append(
      [
        'window_fadein',
        lambda: Fade.window_fadein(self.show_function, 'window_fadein')
      ]
    )

  def run(self):
    self.running = True
    while self.running:
      # print(len(self.show_function))
      for event in pygame.event.get():
        # 退出遊戲
        if event.type == pygame.QUIT:
          self.running = False
          # 退出 Pygame
          pygame.quit()
          sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
          isFading = False
          for func in self.show_function:
            if 'fade' in func[0]:
              isFading = True
              break
          if not isFading:
            self.current_contents += 1
            if( self.current_contents == 4) or (self.current_contents == 5):
              self.dynamic_objects['text'] = TextWithBackground(self.contents[self.current_contents], WHITE, TEXT_BG, self.font).surface
              self.dynamic_objects['text_rect'] = TextWithBackground(self.contents[self.current_contents], WHITE, TEXT_BG, self.font).surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 100))
              self.dynamic_objects['image'] = self.contents_background[self.current_contents]
              self.dynamic_objects['image_rect'] = self.dynamic_objects['image'].get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
            else:
              self.show_function.append(
                [
                  'click_window_fadeout_then_fadein',
                  lambda: Fade.window_fadeout_then_fadein(
                    self.show_function,
                    self.dynamic_objects,
                    {
                      'text': TextWithBackground(self.contents[self.current_contents], WHITE, TEXT_BG, self.font).surface,
                      'text_rect': TextWithBackground(self.contents[self.current_contents], WHITE, TEXT_BG, self.font).surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 100)),
                      'image': self.contents_background[self.current_contents],
                      'image_rect': self.dynamic_objects['image'].get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
                    },
                    'click_window_fadeout_then_fadein',
                    5
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
    