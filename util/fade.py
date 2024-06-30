from colors import OVERLAY_BLACK
from const import WINDOW, WINDOW_SIZE
import pygame

class Fade:
  states = {}
  overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
  overlay.fill(OVERLAY_BLACK)

  def __init__(self):
    pass

  @staticmethod
  def fadein_then_fadeout():
    pass

  @staticmethod
  def fadeout_then_fadein(show_function, dynamic_objects, new_object, new_object_rect, obj_tag, obj_rect_tag, function_tag, speed=1):
    if function_tag in Fade.states.keys():
      if Fade.states[function_tag] == 'fadeout':
        alpha = dynamic_objects[obj_tag].get_alpha() - speed
        if alpha > 0:
          dynamic_objects[obj_tag].set_alpha(alpha)
        else:
          new_object.set_alpha(0)
          dynamic_objects[obj_tag] = new_object
          dynamic_objects[obj_rect_tag] = new_object_rect
          Fade.states[function_tag] = 'fadein'
      elif Fade.states[function_tag] == 'fadein':
        alpha = dynamic_objects[obj_tag].get_alpha() + speed
        if alpha < 255:
          dynamic_objects[obj_tag].set_alpha(alpha)
        else:
          dynamic_objects[obj_tag].set_alpha(255)
          del Fade.states[function_tag]
          # 移除 show function 裡面的 function
          for func in show_function:
            if func[0] == function_tag:
              show_function.remove(func)
              break
    else:
      Fade.states[function_tag] = 'fadeout'

  @staticmethod
  def fadein(show_function, dynamic_objects, object_tag, function_tag, speed=1):
    alpha = dynamic_objects[object_tag].get_alpha() + speed
    if alpha < 255:
      dynamic_objects[object_tag].set_alpha(alpha)

    # 完成淡入
    else:
      dynamic_objects[object_tag].set_alpha(255)
      # 移除 show function 裡面的 fadein function
      for func in show_function:
        if func[0] == function_tag:
          show_function.remove(func)
          break

  @staticmethod
  def fadeout(show_function, dynamic_objects, object_tag, function_tag, speed=1):
    alpha = dynamic_objects[object_tag].get_alpha() - speed
    if alpha > 0:
      dynamic_objects[object_tag].set_alpha(alpha)

    # 完成淡入
    else:
      dynamic_objects[object_tag].set_alpha(0)
      # 移除 show function 裡面的 fadein function
      for func in show_function:
        if func[0] == function_tag:
          show_function.remove(func)
          break

  @staticmethod
  def window_fadein(show_function, function_tag, speed=1):
    start_fadein = False
    for func in show_function:
      if func[0] == function_tag:
        start_fadein = True
        break
    
    if start_fadein:
      alpha = Fade.overlay.get_alpha() - speed
      if alpha > 0:
        Fade.overlay.set_alpha(alpha)
        WINDOW.blit(Fade.overlay, (0, 0))
      else:
        Fade.overlay.set_alpha(0)
        WINDOW.blit(Fade.overlay, (0, 0))
        for func in show_function:
          if func[0] == function_tag:
            show_function.remove(func)
    else:
      Fade.overlay.set_alpha(255)

  @staticmethod
  def window_fadeout(show_function, function_tag, speed=1):
    start_fadeout = False
    for func in show_function:
      if func[0] == function_tag:
        start_fadeout = True
        break
    
    if start_fadeout:
      alpha = Fade.overlay.get_alpha() + speed
      if alpha < 255:
        Fade.overlay.set_alpha(alpha)
        WINDOW.blit(Fade.overlay, (0, 0))
      else:
        Fade.overlay.set_alpha(255)
        WINDOW.blit(Fade.overlay, (0, 0))
        for func in show_function:
          if func[0] == function_tag:
            show_function.remove(func)
    else:
      Fade.overlay.set_alpha(255)

  @staticmethod
  def window_fadeout_then_fadein(show_function, dynamic_objects, change_object, function_tag, speed=1):
    if function_tag in Fade.states.keys():
      if Fade.states[function_tag] == 'window_fadeout':
        alpha = Fade.overlay.get_alpha() + speed
        if alpha < 255:
          Fade.overlay.set_alpha(alpha)
          WINDOW.blit(Fade.overlay, (0, 0))
        else:
          Fade.overlay.set_alpha(255)
          WINDOW.blit(Fade.overlay, (0, 0))
          # 更新物件
          for key in change_object.keys():
            dynamic_objects[key] = change_object[key]
          # 更新 state
          Fade.states[function_tag] = 'window_fadein'
      elif Fade.states[function_tag] == 'window_fadein':
        alpha = Fade.overlay.get_alpha() - speed
        if alpha > 0:
          Fade.overlay.set_alpha(alpha)
          WINDOW.blit(Fade.overlay, (0, 0))
        else:
          Fade.overlay.set_alpha(0)
          WINDOW.blit(Fade.overlay, (0, 0))
          # 移除 show function 
          for func in show_function:
            if func[0] == function_tag:
              show_function.remove(func)
          # 移除 state
          del Fade.states[function_tag]
    else:
      Fade.states[function_tag] = 'window_fadeout'
      Fade.overlay.set_alpha(0)
