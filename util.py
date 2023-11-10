from selenium.webdriver.common.by import By


class util:

    # 场景切换页面的loading元素
    loading_page_element = {
            'element': "img-load",
            'by': By.CLASS_NAME
            }

    # 四象降临
    btb_event_main_url = "https://game.granbluefantasy.jp/#event/advent"
    btb_extreme_plus = {
            'by' : By.CLASS_NAME,
            'element' : "prt-raid-image",
            'time_limit' : 10
             }
    btb_impossible = {
            'url': "https://game.granbluefantasy.jp/#quest/supporter/743451/1",
            'by': By.CLASS_NAME,
            'element': "prt-hl-count",          
            'time_limit' : 10
            }
    btb_extreme_xuanwu ={
            'url' : "https://game.granbluefantasy.jp/#quest/supporter/711041/1",
            'time_limit' : 5
            }
    btb_extreme_zhuque ={
            'url' : "https://game.granbluefantasy.jp/#quest/supporter/711191/1",
            'time_limit' : 5
            }
    btb_extreme_qinglong ={
            'url' : "https://game.granbluefantasy.jp/#quest/supporter/711091/1",
            'time_limit' : 5
            }
    btb_extreme_baihu ={
            'url' : "https://game.granbluefantasy.jp/#quest/supporter/711141/1",
            'time_limit' : 5
            }
    


    # 踢馆
    shiny_slime_weekend = {'url' : "https://game.granbluefantasy.jp/#quest/supporter/400151/4", 'time_limit' : 2 }
    chrome_remote_host = "127.0.0.1:9222"

    # 选择队伍界面的ok确认键
    mouse_position_party_ok = {'x': 250, 'y': 570}
    mouse_position_party_ok_dert = {'x' : 100 , 'y' : 10}
    # 选择第一个好友的召唤石
    mouse_position_friend_summon = {'x' : 100, 'y' : 500}
    mouse_position_friend_summon_dert = {'x' : 5, 'y' : 5}
    screen_label_friend_summmon_page = {'text' : 'Choose a Summon', 'by' : By.CLASS_NAME, 'element' : 'prt-supporter-title'}
    # arcum选择队伍界面的ok确认键
    mouse_position_arcum_party_ok = {'x' : 300, 'y' : 600}
    mouse_position_arcum_party_ok_dert = {'x' : 50, 'y' : 10}
    # 战斗界面的attack键坐标和偏移量
    mouse_position_battle_attack = {'x' : 280, 'y' : 380}
    mouse_position_battle_attack_dert = {'x' : 70, 'y' : 30}
    # 战斗界面的full键坐标和偏移量
    mouse_position_battle_full = {'x' : 85, 'y' : 410}
    mouse_position_battle_full_dert = {'x' : 10, 'y' : 10}
    # 多人列表最上面一场战斗
    mouse_position_rapid_filter_frist = {'x' : 200, 'y' : 400}
    mouse_position_rapid_filter_frist_dert = {'x' : 50, 'y' : 50}
    
    # 战斗界面显示last turn processing
    screen_label_battle_lastturn_processing = {'element' : "prt-popup-header", 'by': By.CLASS_NAME, 'text' : 'Processing'}
    screen_label_battle_full = {'element' : 'btn-auto', 'by' : By.CLASS_NAME}
    screen_label_party_ok = {'element' :  '//div[@class="prt-btn-deck"]', 'by' : By.XPATH}
    screen_label_arcum_part_ok = {'by' : By.XPATH, 'element' : '//div[@class="prt-btn-deck"]'}
    screen_label_battle_attack = {'element' : '//div[@class="btn-attack-start display-on"]', 'by' : By.XPATH}
    screen_label_home = {'by' :  By.ID, 'element': "btm-campaign-toggle"}    
    screen_label_battle_alldead = {'text' : "Use Auto Select" , 'element' : "txt-title", 'by' : By.CLASS_NAME} 
    screen_label_battle_goal_exp = {'by' : By.CLASS_NAME, 'element' : "cnt-get-experience"}
    screen_label_auto_refresh = {'by' : By.XPATH, 'element' : '//div[@class="btn-attack-start display-off"]'}
    screen_label_battle_page = {'element' : "prt-gauge-area", 'by' : By.CLASS_NAME}
    screen_label_arcum_gauge = {'element' : "txt-chest-name", 'by' : By.CLASS_NAME}
    screen_label_arcum_gauge_goto_url = {'element' : 'prt-aap-num', "by" : By.CLASS_NAME}
    screen_label_arcum_gauge_mimic = {'text' : "Mimic", 'by' : By.CLASS_NAME, 'element' : "txt-quest-name"}
    screen_label_arcum_gauge_ok = {'element' : 'btn-usual-ok', 'by' : By.CLASS_NAME}
    #url
    url_home = "https://game.granbluefantasy.jp/#mypage"

    #arcum
    #stage 9
    liber_boss_wind_garuda_militis = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/9/9/16/818091/25/0/25078"
            }

    # stage 2
    zoneeletio_fire_de_cleansing_wyrmgod = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/3/811101/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_fire_5_slithering_seductress = {
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10,
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/3/811011/25"
            }
    zoneeletio_light_3_living_lighting_rod = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/5/811021/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_fire_5_eletion_drake = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/6/811031/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_fire_de_usurper_of_the_throne = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/8/811111/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_fire_5_paradoxical_gate = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/8/811041/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_fire_3_blazing_everwing = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/11/811061/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_light_5_death_seer = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/13/811051/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_light_de_violetflash_sovereign = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/13/811121/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_light_3_hundred_armed_hulk = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/15/811081/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_fire_3_rageborn_one = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/17/811091/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_fire_5_terror_trifecta = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/2/2/19/811071/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }
    zoneeletio_fire_boss_eletion_glider = {
            'url' : "",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/2",
            "time_limit" : 10
            }

    # stage 7
    joculator_dark_3_Dreadful_scourge = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/7/7/14/816061/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/7",
            "time_limit" : 10
            
            }
    joculator_dark_ve_jurassic_dino = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/7/7/14/816081/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/7",
            "time_limit" : 10
            }


    #stage 10
    mundus_wind_v2de_morrigna_militis = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/15/819171/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_light_3_goddess_of_the_wild_hunt = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/15/819121/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_dark_3_proud_war_princess_of_dragons = { 
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/11/819091/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_wind_3_dragon_glittering_green = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/14/819111/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_water_3_tide_caller = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/10/819081/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_wind_5_winged_demon_cat = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/13/819101/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_water_5_parasite_steve = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/9/819071/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_fire_v2de_prometheus_militis = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/2/819141/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_fire_5_hotheaded_pincers = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/2/819011/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_earth_v2de_gilgamesh_militis = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/6/819161/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_earth_5_princess_of_the_horde ={
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/6/819041/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_fire_3_earthshattering_fire_demon ={
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/3/819021/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_earth_3_elephant_stormping_ground = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/10/10/7/819051/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit': 3
            }
    mundus_light_5_high_voltage_rock ={
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/10/10/4/819031/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    mundus_dark_5_love_meeee = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/10/10/8/819061/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/10",
            'time_limit' : 3
            }
    arcum_jurassic_dino = {
            'url' : 'https://game.granbluefantasy.jp/#replicard/supporter/7/7/14/816081/25',
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/7",
            'time_limit' :3
            }
    arcum_vestige_of_truth = {
            'url' : "https://game.granbluefantasy.jp/#replicard/supporter/4/4/3/813011/25",
            'gauge_url' : "https://game.granbluefantasy.jp/#replicard/stage/4",
            'time_limit' : 3
            }
    

    # event
    hope_from_a_snow_drop_impossible = {
            'url' : 'https://game.granbluefantasy.jp/#quest/supporter/912341/1/0/10504',
            'time_limit' : 10
            }
    hope_from_a_snow_drop_extreme = {
            'url' : 'https://game.granbluefantasy.jp/#quest/supporter/912331/1/0/10504',
            'time_limit' : 3 
            }
    hope_from_a_snow_drop_veryhard = {
            'url' : "https://game.granbluefantasy.jp/#quest/supporter/912321/1",
            'time_limit' : 3
            }

    def __init__(self):
        pass
