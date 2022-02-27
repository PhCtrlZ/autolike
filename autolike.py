import requests
from lxml import html
import time
import random
from tkinter import *
from tkinter import messagebox
import webbrowser
import subprocess,json,time
import requests
import os
import ctypes	
import winshell
from colorama import Fore, Back, Style
import socket
import sys
os.system("cls")
print(Fore.GREEN+"đang checking kết nối mạng")
try:
    requests.get('https://www.google.com/').status_code
    print(Fore.GREEN+"Connected to internet is successfully7")
    pass
except:
	print(Fore.RED+"Connected to internet is not successfully please check your internet connection again ")
	print(Style.RESET_ALL)
	time.sleep(5)
	exit()

class ProgressBar(object):
    DEFAULT_BAR_LENGTH = 75
    DEFAULT_CHAR_ON  = '='
    DEFAULT_CHAR_OFF = ' '

    def __init__(self, end, start=0):
        self.end    = end
        self.start  = start
        self._barLength = self.__class__.DEFAULT_BAR_LENGTH

        self.setLevel(self.start)
        self._plotted = False

    def setLevel(self, level):
        self._level = level
        if level < self.start:  self._level = self.start
        if level > self.end:    self._level = self.end

        self._ratio = float(self._level - self.start) / float(self.end - self.start)
        self._levelChars = int(self._ratio * self._barLength)

    def plotProgress(self):
        sys.stdout.write("\r  %3i%% [%s%s]" %(
            int(self._ratio * 100.0),
            self.__class__.DEFAULT_CHAR_ON  * int(self._levelChars),
            self.__class__.DEFAULT_CHAR_OFF * int(self._barLength - self._levelChars),
        ))
        sys.stdout.flush()
        self._plotted = True

    def setAndPlot(self, level):
        oldChars = self._levelChars
        self.setLevel(level)
        if (not self._plotted) or (oldChars != self._levelChars):
            self.plotProgress()

    def __add__(self, other):
        assert type(other) in [float, int], "can only add a number"
        self.setAndPlot(self._level + other)
        return self
    def __sub__(self, other):
        return self.__add__(-other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __isub__(self, other):
        return self.__add__(-other)
    def __del__(self):
        sys.stdout.write("\n")

if __name__ == "__main__":
    count = 150
    print ("Loadding tool...")
    pb = ProgressBar(count)
    for i in range(0, count):
        pb += 1
        time.sleep(0.01)
    del pb

    print ("done")
b ="sever1"
r = requests.get('https://api.npoint.io/365dfdd4fe77a000f2d2')
r = json.loads(r.text)
start = "\033[1m"
end = "\033[0;0m"

try:
	key = r[b]
	if key == True:
		mess=r['message']
		print(Fore.GREEN+start+mess+end)
		print(Fore.GREEN+start+"Connected to sever is successfully"+end)
		time.sleep(1)
		print("Sever sẽ đóng vào 12h->7h30 sáng để bảo trì")
		time.sleep(1)
		print(Fore.GREEN+start+"sever is open"+end)
		time.sleep(1)
		print(Fore.GREEN+start+"Loading...!"+end)
		time.sleep(1)
		print(Style.RESET_ALL)
		print(Style.RESET_ALL)
		print(Style.RESET_ALL)
		print(Style.RESET_ALL)
		print("""
_________    __           .__   __________
\_   ___ \ _/  |_ _______ |  |  \____    /
/    \  \/ \   __\\_  __ \|  |    /     / 
\     \____ |  |   |  | \/|  |__ /     /_ 
 \_______/ |__|   |__|   |____//_________\
                                       

""")
		print(Fore.CYAN+"""
                                                                 ÛÛ
                                                                ÛÛ  
                                                              ÛÛ 
                                                                            
                        ±Û          ÛÛÛÛÛÛÛÛÛ  ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛÛÛÛÛÛÛÛ         
                          Û         ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛ            
                           ²Û       ÛÛÛÛÛÛÛÛÛ  ÛÛÛÛÛÛÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛ             
                          Û         ÛÛÛ        ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛ           
                        ±Û   ²²²²²  ÛÛÛ        ÛÛÛ   ÛÛÛ  ÛÛÛÛÛÛÛÛÛ   ÛÛÛÛÛÛÛÛÛ   
                                          Tool change mode:on   

                                           """)
		print(Style.RESET_ALL)
		user=input("Nhập cookie fb của bạn vô đây:")
		cookie = (user)
		#main.py
		def auto_like(link):
		    try:
		    	#headers để giả lập là người dùng
		        headers = {
		            'authority': 'mbasic.facebook.com',
		            'upgrade-insecure-requests': '1',
		            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
		            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		            'sec-fetch-site': 'same-origin',
		            'sec-fetch-mode': 'navigate',
		            'accept-language': 'en-US,en;q=0.9',
		            'cookie': cookie
		        }
		        #truy cập đến newsfeed của bạn
		        page = requests.get(
		            'https://mbasic.facebook.com' + link,
		            headers=headers
		        )
		        tree = html.fromstring(page.content)
		        # lấy nút like ra
		        like_posts = tree.xpath("//span[contains(@id,'like_')]/a[contains(@href,'a/like.php')]/@href")
		        see_more = tree.xpath("//a[contains(@href,'stories.php?aftercursorr')]/@href")
		        print(see_more[0])
		        # Sau đó thực hiện bấm nút like
		        for link in like_posts:
		            res = requests.get('https://mbasic.facebook.com' + link, headers=headers)
		            print('Đã like bài viêt')
		            time.sleep(random.choice(range(4)))
			        # Chuyển đến trang tiếp theo
		        auto_like(see_more[0])

		    except Exception:
		        auto_like('/')
		auto_like('/')
	elif key == False:
		os.system("cls")
		error=r['error']
		error2=r['error2']
		error3=r['error3']
		print(Fore.RED+error)
		print(Fore.RED+error2)
		print(Fore.RED+error3)
		print(Style.RESET_ALL)
		time.sleep(10)
		exit()

except:
	os.system("cls")
	error=r['error']
	error2=r['error2']
	error3=r['error3']
	print(Fore.RED+error)
	print(Fore.RED+error2)
	print(Fore.RED+error3)
	print(Style.RESET_ALL)
	time.sleep(10)
	exit()