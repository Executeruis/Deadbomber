from json import load, dump

CONFIG_NAME = 'config.json'



def check_config():

    while True:
        with open(CONFIG_NAME) as f:
            return load(f)



def change_config(key, value, int_=False):

    config = check_config()
    if int_:
        config[key] = value
    else:
        config[key] = f'{value}'
    with open(CONFIG_NAME, 'w') as f:
        dump(config, f)


