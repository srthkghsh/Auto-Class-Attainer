# Coded in Visual Studio Code by Sarthak Ghosh.


import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb
lst=[
    ['https://teams.microsoft.com/l/meetup-join/19%3atEnD3oM-UZ3KkGI_RR_tJOHrsYx73YpaWJC4r_hCxz01%40thread.tacv2/1642698995718?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%22b4b335bc-1d88-4397-8284-e44c164b6c3b%22%7d','11:48','13:10']
    
#inKput lecture stats in form of list ......
# ["Link","start_time","end_time"]
# give time in 24 hrs format...
]


keyboard= Controller()

is_class_started =False
for lecture  in lst:
    while True :
        if is_class_started==False:
            if (datetime.now().hour == int(lecture[1].split(':')[0])and 
                datetime.now().minute == int(lecture[1].split(':')[1])):
                wb.open(lecture[0])
                is_class_started=True
                time.sleep(5)
                pyautogui.press('right')
                time.sleep(1)
                pyautogui.press('enter')
                for i in range(1,15,1):
                    time.sleep(1)
                    pyautogui.hotkey('tab');
                time.sleep(1)
                pyautogui.press('enter')
                #time.sleep(5)
                #pyautogui.hotkey('ctrl','shift','m')
                time.sleep(10)
        elif   (datetime.now().hour == int(lecture[2].split(':')[0]) and
                datetime.now().minute == int(lecture[2].split(':')[1])):
                is_class_started=False
                pyautogui.hotkey('ctrl','shift','b')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                #time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                break
