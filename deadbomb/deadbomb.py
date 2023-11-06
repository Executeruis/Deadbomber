from time import sleep
from Deadbomb.console import slow_print, get_input, input_menu, print_menu
import subprocess
from Deadbomb.Config import check_config, change_config
from info import *
from Deadbomb.text import banner, main_menu, setting_menu, information
from Deadbomb.Run import start_async_attacks
from Deadbomb.Attack.Services import urls
def main():
    choice = input_menu()
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
    else:
        slow_print("Неверный выбор.", error=True)

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
        limit = input_menu()
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
            inp_ = input_menu()
            if inp_ == 1:
                return
            elif inp_ == 0:
                subprocess.Popen("clear")
                sleep(0.5)
                slow_print("Запуск)")
                start_async_attacks(number, limit, services)
            else:
                slow_print("Неверный выбор.", error=True)
          
        
    else:
        slow_print("Сначала настройте бомбер.", error=True)

def bomb_setting():
    while True:
        cfg = check_config()
        print_menu(setting_menu.format(cfg['SMS'], cfg['CALL'], cfg['FEEDBACK'], cfg['TG_MSG']))
        slow_print("Напишите номер способа атаки, чтобы включить его", clue=True)
        choice = input_menu()
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
        else:
            slow_print("Неверный выбор.", error=True)
            continue
        if cfg[upd] == "True":
            change_config(upd, "False")
        else:
            change_config(upd, "True")
    

def graph_setting():
    slow_print("Пока что эта опция недоступна\n\n\n", error=True)
    
    
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
        if input_menu() == 0:
            return
        else:
            slow_print("Неверный ввод", error=True)
    


if __name__ == '__main__':
    subprocess.Popen("clear")
    sleep(1)
    slow_print(banner, banner=True)
    slow_print(f"Version: {version}\nAuthor: {author}\n\n\n", clue=True)
    
    while True:
        print_menu(main_menu)
        main()