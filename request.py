import requests
import time

ip_address = '104.21.1.218'  
domain = 'seaqua.io'  

while True:
    try:
        headers = {'Host': domain}
        response = requests.get(f'http://{ip_address}', headers=headers)
        print(response.text)
        time.sleep(1)  # Adjust this delay according to your needs
    except Exception as e:
        print(f"An error occurred: {e}")
