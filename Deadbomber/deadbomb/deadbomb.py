from time import sleep
from Deadbomb.console import slow_print, get_input, input_menu, print_menu, all_color
import subprocess
from Deadbomb.Config import check_config, change_config
from info import *
from Deadbomb.text import banner, main_menu, setting_menu, information, graph_menu
from Deadbomb.Run import start_async_attacks
from Deadbomb.Attack.Services import urls
def main():
    choice = input_menu(4)
    if choice == 0:
        start_attack()
    elif choice == 1:
        bomb_setting()
    elif choice == 2:
        graph_setting()
    elif choice == 3:
        info()
    elif choice == 4:
        exit()

def start_attack():

    def checker(v, l):
        for i in l:
            if i == v:
                return True
        return False
    cfg = check_config()
    inf = [cfg['SMS'], cfg['CALL'], cfg['FEEDBACK'], cfg['TG_MSG']]
    if checker("True", inf):
        slow_print("Введите номер в формате 79xxxxxxxxx:")
        while True:
            number = get_input()
            if number.isdigit():
                if number[0:2] == '79':
                    if len(number) == 11:
                        break
            slow_print("Неверный номер.", error=True)
        
        slow_print("Введите количество кругов:")
        limit = int(get_input())
        services = []
        sms, call, fb, tg = info(True)
        cfg = check_config()
        __sms = 0
        __call = 0
        __fb = 0
        __tg = 0
        if cfg['SMS'] == "True":
            services.append('SMS')
            __sms = sms * limit
        if cfg['CALL'] == "True":
            services.append('CALL')
            __call = call * limit
        if cfg['FEEDBACK'] == "True":
            services.append('FEEDBACK')
            __fb = fb * limit
        if cfg['TG_MSG'] == "True":
            __tg = tg * limit
            services.append('TG_MSG')
       
                      
        slow_print("Подтвердите атаку:\n\nНомер: {}\nКол-во кругов: {}\nСервисы: {}\nКол-во:\nSMS - {}\nCALL - {}\nFEEDBACK - {}\nTELEGRAM - {}\n\n".format(number, limit, ', '.join(services), __sms, __call, __fb, __tg), error=True)
        print_menu("Подтвердить\nВыход")
        while True:
            inp_ = input_menu(1)
            if inp_ == 1:
                return
            elif inp_ == 0:
                subprocess.Popen("clear")
                sleep(0.5)
                slow_print("Запуск)")
                start_async_attacks(number, limit, services)
          
        
    else:
        slow_print("Сначала настройте бомбер.", error=True)

def bomb_setting():
    while True:
        cfg = check_config()
        print_menu(setting_menu.format(cfg['SMS'], cfg['CALL'], cfg['FEEDBACK'], cfg['TG_MSG']))
        slow_print("Напишите номер способа атаки, чтобы включить его", clue=True)
        choice = input_menu(4)
        if choice == 0:
            upd = 'SMS'
        elif choice == 1:
            upd = 'CALL'
        elif choice == 2:
            upd = 'FEEDBACK'
        elif choice == 3:
            upd = 'TG_MSG'
        elif choice == 4:
            return
        if cfg[upd] == "True":
            change_config(upd, "False")
        else:
            change_config(upd, "True")
    

def graph_setting():
    def change_color(name, v):
        print_menu('\n'.join(all_color) + '\nВыйти')
        while True:
            choice = input_menu(len(all_color))
            if choice == len(all_color):
                return
            elif all_color[choice] == v:
                slow_print("Так нельзя.", error=True)
                continue
            else:
                change_config(name, all_color[choice])
                break

    def change_delay(name, v, limit=0.5):
        while True:
            slow_print('Введите новую задежку в диапазоне от 0.0 до {}: '.format(limit))
            try:
                inp = float(get_input())
            except:
                slow_print("Неверный формат данных.", error=True)
                continue
            if inp > limit or inp < 0 or inp == v:
                slow_print("Введите допустимое число.", error=True)
                continue
            else:
                change_config(name, float(inp))
                break
    while True:
        cfg = check_config()
        banner_color = cfg['banner_color']
        banner_delay = cfg['banner_delay']
        text_color = cfg['text_color']
        text_delay = cfg['text_delay']
        input_color = cfg['input_color']
        input_delay = cfg['input_delay']
        clue_color = cfg['clue_color']
        error_color = cfg['error_color']
        print_menu(graph_menu.format(banner_color, banner_delay, text_color, text_delay, input_color, input_delay, clue_color, error_color))
        choice = input_menu(8)
        if choice == 8:
            return
        elif choice == 0:
            change_color('banner_color', banner_color)
        elif choice == 1:
            change_delay('banner_delay', banner_delay)
        elif choice == 2:
            change_color('text_color', text_color)
        elif choice == 3:
            change_delay('text_delay', text_delay)
        elif choice == 4:
            change_color('input_color', input_color)
        elif choice == 5:
            change_delay('input_delay', input_delay)
        elif choice == 6:
            change_color('clue_color', clue_color)
        elif choice == 7:
            change_color('error_color', error_color)

    
    
def info(ret=False):
    all_services = urls('79999999999')
    sms_services = 0
    call_services = 0
    feedback_services = 0
    tgmsg_services = 0
    for i in all_services:
        inf = i['info']['attack']
        if inf == 'SMS':
            sms_services += 1
        elif inf == 'CALL':
            call_services += 1
        elif inf == 'FEEDBACK': feedback_services += 1
        elif inf == 'TG_MSG': tgmsg_services += 1
    if ret:
        return sms_services, call_services, feedback_services, tgmsg_services
    slow_print(information.format(len(all_services), sms_services, call_services, feedback_services, tgmsg_services), clue=True)
    print_menu("Выйти")
    while True:
        if input_menu(0) == 0:
            return
    


if __name__ == '__main__':
    subprocess.Popen("clear")
    sleep(1)
    slow_print(banner, banner=True)
    slow_print(f"Version: {version}\nAuthor: {author}\n\n\n", clue=True)
    
    while True:
        print_menu(main_menu)
        main()
