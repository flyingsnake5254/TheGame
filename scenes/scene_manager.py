import time

class SceneManager:
  def __init__(self):
    self.scenes = []
    self.current_scene = None

  def add_scene(self, scene):
    self.scenes.append(scene)

  def set_scene(self, index):
    if 0 <= index < len(self.scenes):
      self.current_scene = self.scenes[index]
      self.current_scene.manager = self
      self.current_scene.run()

  def next_scene(self, delay=0):
    if self.current_scene:
      current_index = self.scenes.index(self.current_scene)
      next_index = (current_index + 1) % len(self.scenes)
      if delay > 0:
        time.sleep(delay)
      self.set_scene(next_index)