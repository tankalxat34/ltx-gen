# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import font
import tkinter.font
import getpass, os, os.path, time, webbrowser, pyperclip, configparser, shutil
from tkinter import ttk

### ИМПОРТ ВАЖНЫХ ФАЙЛОВ ПРОГРАММЫ ###
import program_constants as CONST
import frame_startmenu as FRAME_STARTMENU
import frame_projectmenu

###################################

if __name__ == '__main__':
    try:
        os.mkdir(CONST.FOLDERS["projects"])
        os.mkdir(CONST.FOLDERS["projects"]+"ShadowOfChernobyl")
        os.mkdir(CONST.FOLDERS["projects"]+"ClearSky")
        os.mkdir(CONST.FOLDERS["projects"]+"CallOfPripyat")
        LIST_PROJECTS = []
    except Exception:
        LIST_PROJECTS = []
        LIST_PROJECTS.append(os.listdir(CONST.FOLDERS["projects"]+"ShadowOfChernobyl"))
        LIST_PROJECTS.append(os.listdir(CONST.FOLDERS["projects"]+"ClearSky"))
        LIST_PROJECTS.append(os.listdir(CONST.FOLDERS["projects"]+"CallOfPripyat"))
    root_name = Tk()
    root_name.title(CONST.WIN_NAME)

    if CONST.PROGRAM_START_IN_FULLSCREEN:
        root_name.overrideredirect(0)
        root_name.state('zoomed')

    ##### СПИСОК ШРИФТОВ НА ПК ЮЗЕРА ####
    LIST_FONTS = list(tkinter.font.families())

    CONST.setWindowOnCenterScreen(root_name)

    root_name.geometry(CONST.WIN_GEOMETRY)
    root_name.resizable(CONST.WIN_DRAW, CONST.WIN_DRAW)
    root_name.iconbitmap(CONST.WIN_ICON)
    root_name.configure()
    root_name.minsize(1300, 910)

    root_name.protocol("WM_DELETE_WINDOW", lambda: CONST.mainQuit())

    root_name["bg"] = CONST.BG

    # FRAME_STARTMENU.Main(root_name).Frame.pack()
    frame_projectmenu.Main(root_name).Frame.pack()

    root_name.mainloop()
