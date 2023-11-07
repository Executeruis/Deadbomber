from time import sleep
from Deadbomb.Config import check_config
from colorama import Fore
all_color = ['RED', 'BLUE', 'YELLOW', 'GREEN']
def convert_color(color_name):
    if color_name == 'RED': return Fore.RED
    elif color_name == 'BLUE': return Fore.BLUE
    elif color_name == 'YELLOW': return Fore.YELLOW
    elif color_name == 'GREEN': return Fore.GREEN

def slow_print(text, banner=False, input=False, endn=True, error=False, clue=False):
    split_text = text.split('\n')
    cfg = check_config()
    if banner:
        color = convert_color(cfg['banner_color'])
        delay = cfg['banner_delay']
    elif input:
        delay = cfg['input_delay']
        color = convert_color(cfg['input_color'])
    elif error:
        color = convert_color(cfg['error_color'])
        delay = cfg['text_delay']
    elif clue:
        color = convert_color(cfg['clue_color'])
        delay = cfg['text_delay']
    else:
        delay = cfg['text_delay']
        color = convert_color(cfg['text_color'])
    for line in split_text:
        symv = ''
        for sym in line:
            symv += sym
            print('\r' + color + symv, end='')
            sleep(float(delay))
        if endn:
            print()

def print_menu(menu):
    split_text = menu.split('\n')
    choices = 0
    for i in split_text:
       if i == '':
           continue
       slow_print(f" [{str(choices)}] {i}")
       choices += 1
    print('\n')



def input_menu(max_value):
    while True:
        input_ = get_input()
        if input_.isdigit():
            if int(input_) > max_value:
                slow_print("Неверный выбор.", error=True)
                continue
            return int(input_)
        else:             
            slow_print("Неверный тип данных.", error=True)
            continue

def get_input():
    slow_print('root@deadbomb >>> ', input=True, endn=False)
    return input()
    

  