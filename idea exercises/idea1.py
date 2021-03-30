import pyautogui, time
import random

time.sleep(5)

f=open("instagram_comments.txt",'r')
for word in f:
    ccc = random.randrange(1,5,2)
    cc = random.randrange(1,8, 3)
    c = random.randrange(20,30, cc)

    print('2.SLeeping time: ')
    print(c)
    pyautogui.typewrite(word)
    time.sleep(ccc)
    print('1.Sleeping time: ')
    print(ccc)
    pyautogui.press("enter")
    time.sleep(c)
    pyautogui.dragTo(1650, 860, button='left')