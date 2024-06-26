from alert import alert
from threading import Event
from elementfinder import elefinder
from util import util
from mouse import Mouse
import re
import time
from selenium import webdriver
from threading import Thread
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


class lpl:

    ele = util.loading_page_element['element']
    by = util.loading_page_element['by']

    def __init__(self, chm: webdriver.Chrome, refreshtime=10):
        self.chm = chm
        self.time = refreshtime
      # 超过五秒刷新
        pass

    def is_loading_page(self):
        flag = False
        try:
            WebDriverWait(self.chm, 0.5).until(
                EC.visibility_of_element_located(
                    (self.by, self.ele)
                )
            )
            flag = True
        except StaleElementReferenceException:
            pass
        except TimeoutException:
            pass
        except WebDriverException:
            pass
        return flag

    def start(self):
        while True:
            start_time = 0
            end_time = 0
            if self.is_loading_page():
                start_time = time.time()
                while self.is_loading_page():
                    end_time = time.time()
            if end_time - start_time > self.time:
                self.chm.refresh()


class last_turn_locator:

    ele_lt = util.screen_label_battle_lastturn_processing['element']
    by_lt = util.screen_label_battle_lastturn_processing['by']

    def __init__(self, chm: webdriver.Chrome, event: Event, mouse: Mouse):
        self.eve = event
        self.chm = chm
        self.mouse = mouse
        pass

    def start(self):
        string_lt = util.screen_label_battle_lastturn_processing['text']
        elf = elefinder(self.by_lt, self.ele_lt, 2, self.chm)
        while self.eve.is_set():
            if elf.is_element_visibility():
                text = elf.get_element_text()
                if re.search(text, string_lt) and re.search(text, string_lt).span()[1] > 0:
                    self.chm.refresh()
                    self.mouse.click_full()
            time.sleep(0.1)


class goal_page_locator:
    by = util.screen_label_battle_goal_exp['by']
    ele = util.screen_label_battle_goal_exp['element']

    def __init__(self, chm: webdriver.Chrome, event: Event, ctrl_event: Event):
        self.eve = event
        self.chm = chm
        self.ctrl_event = ctrl_event
        pass

    def start(self):
        flag = False
        elf = elefinder(self.by, self.ele, 2, self.chm)
        while self.eve.is_set():
            if elf.is_element_visibility():
                flag = True
            else:
                current_url = self.chm.current_url
                if (re.search(current_url, 'result') and re.search(current_url, 'result').span()[1] > 0) or (re.search(current_url, 'quest') and re.search(current_url, 'quest').span()[1] > 0):
                    flag = True
            if flag:
                self.ctrl_event.clear()
            #  print('ctrl_event: ',self.ctrl_event.is_set())
            time.sleep(0.1)


class battle_final_next_bt_locator:

    def __init__(self, mouse: Mouse, chm: webdriver.Chrome, ctrl_event: Event):
        self.chm = chm
        self.mouse = mouse
        self.ctrl_eve = ctrl_event
        pass

    def start(self):

        pass


class verification_locator:

    data = util.verification_data

    def __init__(self, mouse: Mouse, chm: webdriver.Chrome, ctrl_event: Event):
        self.chm = chm
        self.mouse = mouse
        self.ctrl_event = ctrl_event
        self.alert = alert()

    def start(self):
        flag = False
        elf = elefinder(
            self.data['by'], self.data['element'], 2, self.chm)
        if elf.is_element_visibility():
            flag = True
            self.ctrl_eve.set()
            self.alert.run(msg='验证码窗口', title='请检查')
            self.ctrl_eve.clear()


class rapid_end_locator:
    # 河道还没进入战斗 战斗就已经结束了

    data = {
        'element':
            '/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[4]/div/div[2]/div',
            'by': By.XPATH
    }

    def __init__(self, mouse: Mouse, chm: webdriver.Chrome, ctrl_event:
                 Event, eve: Event):
        self.chm = chm
        self.eve = eve
        self.mouse = mouse
        self.ctrl_event = ctrl_event
        self.alert = alert()

    def start(self):
        if self.eve.is_set():
            flag = False
            elf = elefinder(
                self.data['by'], self.data['element'], 2, self.chm)
            if elf.is_element_visibility():
                flag = True
                self.ctrl_eve.set()
                print("the battle has already ended...")
                time.sleep(1)
        else:
            self.ctrl_event.clear()


class request_dialog_locator:

    dialog_locator = util.screen_lable_battle_request_backup_dialog_backup
    dialog_ok_locator = util.screen_lable_battle_request_backup_dialog_ok

    def __init__(self, mouse: Mouse, chm: webdriver.Chrome, ctrl_event: Event):
        self.chm = chm
        self.mouse = mouse
        self.ctrl_eve = ctrl_event
        pass

    def start(self):
        flag = False
        elf = elefinder(
            self.dialog_locator['by'], self.dialog_locator['element'], 2, self.chm)
        if elf.is_element_visibility():
            flag = True
            self.ctrl_eve.set()
            self.mouse.click_by_element(self.dialog_locator)
            time.sleep(1)
            self.mouse.click_by_element(self.dialog_ok_locator)
            time.sleep(0.1)
            self.ctrl_eve.clear()
