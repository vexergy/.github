import os
import requests

os.system("")

class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(style.GREEN + f'{url} is up!' + style.RESET)
            return True
        else:
            print(style.RED + f'{url} is down! (Status code: {response.status_code})' + style.RESET)
            return False
    except requests.exceptions.RequestException as e:
        print(style.RED + f'{url} is down! (Error: {e})' + style.RESET)
        return False

def vexergy_website_status(base_url):
    variants = [
        f"http://{base_url}",
        f"https://{base_url}",
        f"http://www.{base_url}",
        f"https://www.{base_url}"
    ]
    
    all_online = True
    for variant in variants:
        if not check_url(variant):
            all_online = False
    
    if all_online:
        print('--------------------------------')
        print(style.GREEN + 'All Systems Operational!\n' + style.RESET)

print("\nChecking 'vexergy.com' Status...")
print('--------------------------------')

vexergy_website_status('vexergy.com')
