import re
from enum import Enum
from mouse import Mouse
from selenium import webdriver
from selenium.webdriver.common.by import By
from elementfinder import elefinder
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException, WebDriverException
import time
from stage import checker
from util import util


class summon:
    brief_element_xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[11]/div[2]/div'
    summon_okbt_dialog_xpath = '//*[@id="wrapper"]/div[3]/div[14]'

    def __init__(self, index: int, chm: webdriver.Chrome, mouse: Mouse):

        self.index = index
        self.chm = chm
        self.mouse = mouse
        self.element = self.get_brief_element()
        self.state = self.get_state()
        self.name = self.get_summon_name()
        self.cold_down = self.get_cd()
        print('summon ',  self.index,  ' init...  ',
              self.state, '  cd: ', self.cold_down,
              self.name)

    def get_cd(self):
        e = None
        if self.element:
            try:
                e = self.element.get_attribute('summon-recast')
            except StaleElementReferenceException:
                pass
            except WebDriverException:
                pass
        return e

    def get_summon_name(self):
        e = None
        if self.element:
            try:
                e = self.element.ger_attribute('summon-name')
            except StaleElementReferenceException:
                pass
            except AttributeError:
                pass
        return e

    def get_brief_element(self):
        summons_xpath = self.brief_element_xpath
        summon_xpath = './div[' + str(self.index + 1) + ']'
        ee = None
        elf = elefinder(By.XPATH, summons_xpath, 5, self.chm)
        if elf.is_element_presence():
            try:
                e = self.chm.find_element_by_xpath(summons_xpath)
                ee = e.find_element_by_xpath(summon_xpath)
            except WebDriverException:
                pass
        return ee

    def use(self):
        if self.state == summon_state.available:
            try:
                self.element.click()
            except ElementNotInteractableException:
                self.chm.execute_script(
                    '$(arguments[0]).click()', self.element)
            except ElementClickInterceptedException:
                pass
            time.sleep(1)
            elf = elefinder(
                By.XPATH, self.summon_okbt_dialog_xpath, 3, self.chm)
            if elf.is_element_presence():
                dialog_ele = self.chm.find_element_by_xpath(
                    self.summon_okbt_dialog_xpath)
                try:
                    ok_ele = dialog_ele.find_element_by_xpath(
                        './div[3]/div[2]')
                    ok_ele.click()
                except ElementNotInteractableException:
                    self.chm.execute_script("$(arguments[0]).click()", ok_ele)
                except NoSuchElementException:
                    print('NoSuchElementException')
                    pass
                except ElementClickInterceptedException:
                    pass

            try:
                print('summon ' + str(self.index) + self.name + ' used')
            except TypeError:
                pass

    def get_state(self):
        try:
            if self.element:
                class_name = self.element.get_attribute('class')
                if not re.search('unavailable', class_name):
                    s = summon_state.available
                else:
                    s = summon_state.unavailable
            else:
                s = None
        except StaleElementReferenceException:
            s = None
        except WebDriverException:
            s = None
        return s


class summon_state(Enum):
    available = 1
    unavailable = 0


class battle_summons:

    extend_summon_panel_xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[11]/div[2]/div/div[1]'
    close_summon_panel_xpath = '//*[@id="cnt-raid-information"]/div[1]'
    brief_summons_xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[11]/div[2]/div'
    full_bt_classname = util.screen_label_battle_full['element']
    full_bt_by = util.screen_label_battle_full['by']

    def set_use_all_summons_flag(self, flag: bool):
        if type(flag) == bool:
            self.use_all_summons_flag = flag

    def use_all_summon(self):
        try:
            if self.use_all_summons_flag:
                flag = False
                for s in self.summon_group:
                    if s.state == summon_state.available:
                        self.open_summon_panel()
                        s.use()
                        flag = True
                        break
                if not flag:
                    print('summons are not available')
        except AttributeError:
            pass

    def use_summon(self, index):
        if checker(self.chm, 10).is_battle_page(10) and index > 0 and index < 7:
            self.open_summon_panel()
            self.summon_group[index].use()
        pass

    def close_summon_panel(self):
        selector = {
            'by': By.XPATH,
            'element': self.close_summon_panel
        }
        elf = elefinder(selector['by'], selector['element'], 3, self.chm)
        if elf.is_element_clickable():
            self.mouse.click_by_element(selector, 3)
            print('summon panel closed')

    def open_summon_panel(self):
        selector = {
            'by': By.XPATH,
            'element': self.extend_summon_panel_xpath
        }
        elf = elefinder(selector['by'], selector['element'], 3, self.chm)
        if elf.is_element_clickable():
            self.mouse.click_by_element(selector, 3)
            time.sleep(0.5)
            print('summon panel opened')

    def __init__(self, chm: webdriver.Chrome, mouse: Mouse):
        self.chm = chm
        self.mouse = mouse
        self.summon_group = list()
        self.use_all_summon_flag = False
        pass

    def update(self):
        xpath = self.brief_summons_xpath
        #  elf = elefinder(By.XPATH, xpath, 3, self.chm)
        #  if elf.is_element_presence():
        # 使用full_bt判断页面，然后获取数据
        elf = elefinder(self.full_bt_by, self.full_bt_classname, 10, self.chm)
        if elf.is_element_clickable():
            try:
                self.brief_summons_element = self.chm.find_element_by_xpath(
                    xpath)
                self.summon_group = list()
                for i in range(1, 6):
                    s = summon(i, self.chm, self.mouse)
                    self.summon_group.append(s)
                print('summons updated ')
            except NoSuchElementException:
                self.summon_group = list()
                print('cannot find summons')
        pass
