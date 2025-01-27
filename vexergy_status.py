import os
import time
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

print('\nVexergy Down Detector & Website Monitor:')
print('----------------------------------------')

url = 'https://vexergy.com'

response = requests.get(url)
initial_content = response.text

def monitor_website(iterations, interval):
    global initial_content
    for i in range(iterations):
        try:
            response = requests.get(url)
            current_content = response.text
            print("")
            
            if current_content != initial_content:
                print("Change Detected!")
                initial_content = current_content
        
        except requests.exceptions.RequestException as e:
            print(style.RED + f"Error while monitoring {url}: {e}" + style.RESET)

        print(style.YELLOW + f"Monitoring {url}... Iteration {i+1}/{iterations}" + style.RESET)
        
        time.sleep(interval)
    
    print("\nMonitoring complete after", iterations, "iterations.\n")

print("\nChecking 'vexergy.com' Status...")
print('--------------------------------')

vexergy_website_status('vexergy.com')

iterations = 3 # Frequency of website monitoring checks
interval = 10 # Time interval between checks (seconds)

print('Monitoring Website Changes:')
print('--------------------------------')
monitor_website(iterations, interval)
