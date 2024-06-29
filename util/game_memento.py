'''
紀錄遊戲進度
'''
class GameRecords:

  def __init__(self, controller):
    # 進度紀錄
    records = {}
  
  def add_record(self, key, value):
    self.records[key] = value

  def get_record(self, key):
    return self.records[key]
  
  def pop_last(self):
    return self.records.popitem()
  
  def pop_record(self, key):
    return self.records.pop(key)
  

'''
遊戲狀態
'''
class GameState:
  def __init__(self, state):
    self.state = state
  
  def get_state(self):
    return self.state



'''
控制遊戲進度
'''
class GameController:
  def __init__(self, game_records, game_state):
    self.game_records = game_records
    self.game_state = game_state

  def set_state(self, state):
    self.game_state = state

  def get_state(self):
    return self.game_state
  
  def save_to_records(self, key, state):
    self.game_records.add_record(key, state)

  def get_from_records(self, key):
    return self.game_records.get_record(key)
  

  
