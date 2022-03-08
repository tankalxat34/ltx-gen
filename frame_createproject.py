# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import font
import tkinter.font
import getpass, os, os.path, time, webbrowser, pyperclip, configparser, shutil, random
from tkinter import ttk

### ИМПОРТ ВАЖНЫХ ФАЙЛОВ ПРОГРАММЫ ###
import program_constants as CONST
import frame_startmenu
import frame_projectmenu

config_shablon = """[info]
column_elements = 0
project_name = %s
game = %s
time_create = %s
column_weapon = 0
column_outfit = 0
column_eat = 0
column_med = 0
description = This project created in program Stalker Items Creator by %s
"""

class Main:
    def __init__(self, root_name=None):
        self.root_name = root_name
        self.Frame = Frame(root_name, bg=CONST.BG)
        # bad relief "1": must be flat, groove, raised, ridge, solid, or sunken

        # frameTitle = CONST.mainLabelFrame(self.Frame, text="", bg=CONST.BG)
        frameTitle = Frame(self.Frame, bg=CONST.BG)
        CONST.titleLabel(frameTitle, "Новый проект...").pack()
        frameTitle.pack(fill=X)
        CONST.intedent(self.Frame).pack()

        frameAllEntryes = Frame(self.Frame, bg=CONST.BG)
        self.frameEntryProjectName = CONST.frameLabelWithEntry(frameAllEntryes, "Название проекта:",
                                                               f"Новый_проект_{getpass.getuser()}{random.randint(99999, 999999)}",
                                                               set_focus=True, justify=LEFT)
        self.frameEntryProjectName.get_frame().pack()



        CONST.secondLabel(frameAllEntryes, "Проект предназначен для игры (двойной клик): ").pack()
        self.LISTBOX_GAMES = CONST.mainListbox(frameAllEntryes, width=40, bd=0, font="Calibri 15", listvariable=CONST.GAMES_NAMES_LIST)
        self.LISTBOX_GAMES.delete(0, 3)
        self.LISTBOX_GAMES.pack()
        for e in CONST.GAMES_NAMES_LIST:
            self.LISTBOX_GAMES.insert(0, e)
        # self.LISTBOX_GAMES.activate(0)
        frameAllEntryes.pack()

        CONST.intedent(self.Frame, size=140).pack()

        CONST.frameBottomNextBack(self.Frame, commandBack=lambda: frame_startmenu.Main().packFrame(self.Frame),
                                  commandNext=lambda: self.getAllEntryes()).pack(fill=X, expand=1, side=BOTTOM, anchor=S)
        self.LISTBOX_GAMES.bind("<Double-Button-1>", lambda event: self.getAllEntryes())

    def get_frame(self):
        return self.Frame

    def packFrame(self, oldFrame):
        oldFrame.pack_forget()
        self.Frame.pack(fill=BOTH, expand=1)

    def getAllEntryes(self):
        try:
            projectName, forGameName = self.frameEntryProjectName.get_entry(), str(self.LISTBOX_GAMES.get(self.LISTBOX_GAMES.curselection()))
            # mb.showinfo(projectName, forGameName)
            if len(projectName) >= 4 and (" " not in projectName) and (projectName not in os.listdir(CONST.FOLDERS["projects"]+CONST.getGameDirProject(forGameName))):
                if mb.askyesno(CONST.WIN_NAME, f'Вы действительно хотите создать проект с именем \n"{projectName}" для игры "{forGameName}"?'):
                    path_project = CONST.FOLDERS["projects"]+CONST.getGameDirProject(forGameName)+projectName+"\\"

                    os.makedirs(path_project+"\\gamedata\\")
                    with open(path_project+"\\"+CONST.CONFIG_FILE_NAME, "w") as file:
                        file.write(config_shablon % (projectName, forGameName, time.ctime(), getpass.getuser()))

                    frame_projectmenu.Main(projectName=projectName, forGameName=forGameName, path_project=path_project).packFrame(self.Frame)

                else:
                    self.frameEntryProjectName.set_text(f"Новый_проект_{getpass.getuser()}{random.randint(99999, 999999)}")
            else:
                raise ValueError
        except Exception:
            mb.showerror(CONST.WIN_NAME, "Некорректный ввод! Проверьте, выполнены ли следующие условия:\n- в названии проекта не должно быть пробелов;\n- проект имеет название, состоящее более чем из четырех символов;\n- проект имеет уникальное название;\n- выбрана игра, для которой будет создан проект;")


