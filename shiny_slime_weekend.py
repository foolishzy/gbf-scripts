from stage import checker
from game import game
from util import util

class slime_select:
    
    def exit():
        pass

    def __init__(self):
        string_hint = '''
       请选择：
       0. exit
       1. shiny_slime_weekend
       '''
        index_max = 1 
        index_min = 0
        index = -1
        while not (index >= index_min and index <= index_max):
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                index = 0
                break
        if index == 0:
            self.exit()
        elif index == 1:
            shiny_slime_weekend().play()       


class shiny_slime_weekend(game):

    def __init__(self):
        game_data = util.shiny_slime_weekend
        self.url = game_data['url']
        time_limit = game_data['time_limit']
        super().__init__(time_limit)

    def play(self):
        repeat_times = int(input("pls input repeat times :"))
        while repeat_times > 0:
            repeat_times = repeat_times - 1
            print('left times : ', repeat_times)
            self.stage.goto(self.url, util.screen_label_friend_summmon_page)
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
            self.ck.is_goal_page(180)
