# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import font
import tkinter.font
import getpass, os, os.path, time, webbrowser, pyperclip, configparser, shutil
from tkinter import ttk

### ИМПОРТ ВАЖНЫХ ФАЙЛОВ ПРОГРАММЫ ###
import program_constants
import program_constants as CONST
import frame_createproject
import frame_projectmenu

class Main:
    def __init__(self, root_name=None):
        self.root_name = root_name
        self.Frame = Frame(root_name, bg=CONST.BG)

        Label(self.Frame, text=CONST.WIN_NAME, font="Cambria 30", fg=CONST.FG, bg=CONST.BG).pack(anchor=N)
        Label(self.Frame, text=CONST.AUTHOR_TEXT+"\n", font="Calibi 10", fg=CONST.FG_GREY, bg=CONST.BG).pack(anchor=N)

        CONST.menu_button(self.Frame, "Создать Новый проект...", lambda: frame_createproject.Main().packFrame(self.Frame)).pack(fill=X)
        CONST.intedent(self.Frame).pack(fill=X)


        def openProject(start_path=CONST.FOLDERS["projects"]):
            def nextProjectView(now_path, game, frameForOpenProject):
                LISTBOX_PROJECTS.delete(0, END)
                try:
                    test = entryNowPath.get()+CONST.getGameDirProject(game)
                    try:
                        entryNowPath.insert(END, CONST.getGameDirProject(game))
                    except Exception:
                        entryNowPath.insert(END, game)

                    try:
                        for e in os.listdir(entryNowPath.get()):
                            LISTBOX_PROJECTS.insert(0, e)
                    except Exception:
                        pass
                except Exception:
                    projectName = game
                    path_project = entryNowPath.get()+game
                    forGameName = CONST.GAMES_NAMES_LIST[CONST.PROGRAM_GAMES_NAMES_LIST.index(entryNowPath.get().split("\\")[1]+"\\")]
                    frameForOpenProject.destroy()
                    frame_projectmenu.Main(projectName=projectName,
                                           forGameName=forGameName,
                                           path_project=path_project+"\\").packFrame(self.Frame)

            def backProjectView():
                LISTBOX_PROJECTS.delete(0, END)
                entryNowPath.delete(0, END)
                entryNowPath.insert(0, CONST.FOLDERS["projects"])
                for e in os.listdir(entryNowPath.get()):
                    LISTBOX_PROJECTS.insert(0, CONST.GAMES_NAMES_LIST[CONST.PROGRAM_GAMES_NAMES_LIST.index(e + "\\")])

            now_path = start_path
            # fd.askdirectory(title="Выберите папку с необходимым проектом")
            frameForOpenProject = CONST.contextWindowVar1(textOk="Выбрать",
                bindCommandNext=lambda: nextProjectView(now_path, LISTBOX_PROJECTS.get(LISTBOX_PROJECTS.curselection()), frameForOpenProject),
                commandNext=lambda: nextProjectView(now_path, LISTBOX_PROJECTS.get(LISTBOX_PROJECTS.curselection()), frameForOpenProject),
                title="Выберите проект...", draw=True, win_size="600x500", titleLabel=" ", titleFont="Calibri 0")
            frameForOpenProject.create()

            frameEntryOpenProject = Frame(frameForOpenProject.getFrame(), bg=CONST.BG)
            CONST.menu_button(frameEntryOpenProject, "←", font="Calibri 11", bg=CONST.BG_ENTRY, command=lambda: backProjectView()).pack(fill=X, anchor=N, side=LEFT)
            entryNowPath = CONST.mainEntry(frameEntryOpenProject, insert_text=now_path)
            entryNowPath.pack(fill=X)
            entryNowPath["state"] = NORMAL
            frameEntryOpenProject.pack(fill=X)

            CONST.intedent(frameForOpenProject.getFrame(), size=1).pack()

            LISTBOX_PROJECTS = CONST.mainListbox(frameForOpenProject.getFrame(), font="Calibri 16")
            scrollY = CONST.scrollerY(LISTBOX_PROJECTS, frameForOpenProject.getFrame())
            scrollY.pack()
            LISTBOX_PROJECTS.pack(fill=BOTH, expand=1)
            LISTBOX_PROJECTS.bind_all("<Double-Button-1>", lambda event: nextProjectView(now_path, LISTBOX_PROJECTS.get(LISTBOX_PROJECTS.curselection()), frameForOpenProject))

            for e in os.listdir(now_path):
                LISTBOX_PROJECTS.insert(0, CONST.GAMES_NAMES_LIST[CONST.PROGRAM_GAMES_NAMES_LIST.index(e+"\\")])

        # def aboutProgram():
        #     aboutProgramContextWindow = CONST.contextWindowVar1(title="О программе", textOk="", textBack="Закрыть", titleFont="Calibri 0", draw=True, win_size="700x700")
        #     aboutWindow = aboutProgramContextWindow.create()
        #     textWidgetAboutProgram = CONST.textWidget(aboutProgramContextWindow.getFrame(), insertText=CONST.__doc__+f"НАЗВАНИЕ: {CONST.WIN_NAME}\nВЕРСИЯ: {CONST.VERSION}\nПУТЬ К ПАПКЕ С ПРОЕКТАМИ: {os.getcwd()}\\{CONST.FOLDERS['projects']}").widget
        #     textWidgetAboutProgram.pack(fill=BOTH, expand=1)
        #     textWidgetAboutProgram["state"] = DISABLED

            # scrollerAboutY = CONST.scrollerY(textWidgetAboutProgram, aboutProgramContextWindow.getFrame())
            # scrollerAboutY.pack()

        CONST.menu_button(self.Frame, "Открыть проект...", command=lambda: openProject()).pack(fill=X)
        CONST.intedent(self.Frame).pack(fill=X)

        CONST.menu_button(self.Frame, "Открыть папку "+CONST.FOLDERS["projects"][:-1],
                          lambda: os.system("explorer.exe "+os.getcwd()+"\\"+CONST.FOLDERS["projects"])).pack(fill=X)
        CONST.intedent(self.Frame).pack(fill=X)

        CONST.menu_button(self.Frame, "О программе", command=lambda: CONST.aboutProgram()).pack(fill=X)
        CONST.intedent(self.Frame).pack(fill=X)

        CONST.menu_button(self.Frame, "Настройки").pack(fill=X)
        CONST.intedent(self.Frame).pack(fill=X)

        CONST.menu_button(self.Frame, "Выход",
                          lambda: CONST.mainQuit()).pack(fill=X)
        CONST.intedent(self.Frame).pack(fill=X)

        # bad relief "1": must be flat, groove, raised, ridge, solid, or sunken



    def get_frame(self):
        return self.Frame



    def packFrame(self, oldFrame):
        oldFrame.pack_forget()
        self.Frame.pack(fill=Y)
























