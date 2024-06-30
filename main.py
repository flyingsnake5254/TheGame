import pygame

from scenes.scene_manager import SceneManager
from scenes.scene_opening import SceneOpening
from scenes.scene_opening_top_floor import SceneOpeningTopFloor

pygame.init()

manager = SceneManager()
manager.add_scene(SceneOpening())
manager.add_scene(SceneOpeningTopFloor())

manager.set_scene(0)  # 啟動第一個場景
