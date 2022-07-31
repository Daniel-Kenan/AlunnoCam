import datetime
from email.mime import image
from glob import glob
import PIL
import numpy as np
import cv2
import pyautogui
import time
import pystray
import getpass
import os
import asyncio
import sys




class AlunnaCam:
    def __init__(self) -> None:
        __username = getpass.getuser()
        self.screenWidth,self.screenHeight = pyautogui.size()
        self.bitmap = PIL.Image.open('favicon.ico')
        self.DirScreenshots = f'c:\\users\\{__username}\\Pictures\\'
        self.fps = 8.2
        self.isrecording = False
    
    def screenshot(self):
        time.sleep(0.5) 
        bitmap = pyautogui.screenshot()
        bitmap.save(f'{self.DirScreenshots}{self.filename}.png')
    
    def closeApp(self):os._exit(0)
    
    @property
    def filename(self):return time.time()

    def main(self):
        while not self.isrecording:     
            self.tray.run()
            time.sleep(3)
            self.isrecording == False
       
    @property
    def tray(self):
        recordORstop = pystray.MenuItem('Record The Screen',self.screenrecord) if not self.isrecording  else pystray.MenuItem(f'Stop Recording',self.screenrecord) 
        return pystray.Icon("Neu" , self.bitmap,menu = pystray.Menu(
            pystray.MenuItem('Take a Screenshot',self.screenshot),
            recordORstop,
    pystray.MenuItem('Remove App Tray',self.closeApp))) 
    
    @staticmethod
    def duration(seconds=None):
        if seconds :return time.time() + seconds
    
    def screenrecord(self):
        self.isrecording =True
        bitmaps = []
        duration = AlunnaCam.duration(5)
        while time.time() < duration:
            pillowImage = pyautogui.screenshot()
            openCVImage = np.array(pillowImage.convert('RGB'))
            openCVImage = openCVImage[:,:,::-1].copy()
            bitmaps.append(openCVImage)

        out = cv2.VideoWriter(f'{self.filename}.avi',cv2.VideoWriter_fourcc(*'DIVX'),self.fps,pyautogui.size())
    
        for bitmap in bitmaps:
            out.write(bitmap)
        out.release()


    
# asyncio.run(main())
