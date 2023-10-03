import pyperclip
import requests
import os
import time

text = """
https://s.mj.run/IGTt0ogvlqo AsianFemaleElderly
https://s.mj.run/9XgWBcYepjM AsianFemaleMiddleAged
https://s.mj.run/lqx_nxkHnko AsianFemaleYoungAdult
https://s.mj.run/AOZX6bEYKao AsianMaleElderly
https://s.mj.run/oIP5f4lBQfw AsianMaleMiddleAged
https://s.mj.run/vOPGkpwwe-Q AsianMaleYoungAdult
https://s.mj.run/Ltl-tOEyWZk BlackFemaleElderly
https://s.mj.run/9pyHtiFzqSE BlackFemaleMiddleAged
https://s.mj.run/r3erl-oZ26o BlackFemaleYoungAdult
https://s.mj.run/WEVaslImcrE BlackMaleElderly
https://s.mj.run/ukaxvE02wFU BlackMaleMiddleAged
https://s.mj.run/LRC8T_iupgU BlackMaleYoungAdult
https://s.mj.run/I9gH07xXp4M WhiteFemaleElderly
https://s.mj.run/ks6n8Aza4L4 WhiteFemaleMiddleAged
https://s.mj.run/3guil5kkw0M WhiteFemaleYoungAdult
https://s.mj.run/bqFEbK4QnPo WhiteMaleElderly
https://s.mj.run/h2WPi75vtxQ WhiteMaleMiddleAged
https://s.mj.run/LI8UD2pBKlc WhiteMaleYoungAdult
"""
url_dict = {line.split()[0]: line.split()[1] for line in text.strip().split('\n')}

clipboard_content = pyperclip.paste()
clipboard_lines = clipboard_content.strip().split('\n')

for line in clipboard_lines:
    parts = line.split(' ')
    folder, filename, url = parts[0], url_dict[parts[1]], parts[2]
    
    path = os.path.join(folder)
    if not os.path.exists(path):
        os.makedirs(path)
    
    url = url.strip('\r')
    MAX_RETRIES = 5
    for _ in range(MAX_RETRIES):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError or requests.exceptions.SSLError:
            print(f"Failed to download {url}, status code={response.status_code}")
            time.sleep(5)
            pass
    if response.status_code == 200:
        with open(os.path.join(path, filename + '.png'), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {line}")
    else:
        # print(f"Failed to download {url}")
        print(f"Failed to download {url}, status code={response.status_code}")
    time.sleep(5)