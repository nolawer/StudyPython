from PIL import ImageGrab
from functools import partial
import pyautogui as pg

# ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

#a = pg.confirm(text="내용", title="제목", buttons=["OK","Cancel"])

#a = pg.prompt(text='내용', title='제목', default='입력하세요')

#print(a)

print(pg.size())

button5location = pg.locateOnScreen('8.png')
# print(button5location)
point = pg.center(button5location)
# pg.moveTo(button5location)
print(point)

pg.click(point)

