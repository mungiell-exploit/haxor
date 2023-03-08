import requests
import concurrent.futures
from colorama import Fore, Style,init
init()
reset = Style.RESET_ALL
red = Fore.RED
green = Fore.GREEN
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"}

def save_wp(url):
    saver = open('wordpress.txt', 'a')
    if url in open('wordpress.txt').read():
        pass
    else:
        saver.write(url + '\n')
def save_lv(url):
    saver = open('laravel.txt', 'a')
    if url in open('laravel.txt').read():
        pass
    else:
        saver.write(url + '\n')
def filter(url):
    try:
        url = url.strip()
        response = requests.get(url + '/wp-content/', )
        if response.status_code == 200:
            print(f"{url} {green}[wordpress]{reset}")
            save_wp(url)
        else:
            response2 = requests.get(url + '/.env')
            if response2.status_code == 200:
                print(f"{url} {green}[Laravel]{reset}")
                save_lv(url)
            else:
                print(f"{url} {red}[Unkown]{reset}")
    except:
        pass
banner = f'''{green}
 _ _           _                                                      _
( ) |__   ___ | |_ _ __ ___   __ _ _ __     __ _ _ __ _ __ ___  _   _( )
|/| '_ \ / _ \| __| '_ ` _ \ / _` | '_ \   / _` | '__| '_ ` _ \| | | |/
  | |_) | (_) | |_| | | | | | (_| | | | | | (_| | |  | | | | | | |_| |
  |_.__/ \___/ \__|_| |_| |_|\__,_|_| |_|  \__,_|_|  |_| |_| |_|\__, |
                                                                |___/
  {red}FILTER WORDPRESS AND LARAVEL SITES
  TELEGRAM - @botmanarmy{reset}

'''
print(banner)
sites = input(F'{green}enter site: {reset}')
with open(sites) as f:
    urls = f.readlines()
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(filter, url) for url in urls]
    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
        except:
            print('server error')