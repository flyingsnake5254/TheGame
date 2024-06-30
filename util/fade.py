from const import WINDOW_SIZE


class Fade:
  states = {}

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
  def fadeout(args):
    for obj in args['ui_obj']:
      if obj['tag'] == args['obj_tag']:
        alpha = obj['object'].get_alpha()

        # 進行淡出

        if alpha > 0:
          alpha = alpha - args['speed']
          # 完成淡出
          if alpha <= 0:
            obj['object'].set_alpha(0)
            # 移除 fade out 方法
            function_index = -1
            for i in range(len(args['ui_obj'])):
              if args['ui_obj'][i]['tag'] == args['fade_tag']:
                function_index = i
                break
            if function_index != -1:
              args['ui_obj'].pop(function_index)
              break
          else:
            obj['object'].set_alpha(alpha)
