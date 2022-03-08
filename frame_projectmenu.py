# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import font
import tkinter.font
import getpass, os, os.path, time, webbrowser, pyperclip, configparser, shutil, random
from tkinter import ttk
import frame_startmenu as FRAME_STARTMENU

### ИМПОРТ ВАЖНЫХ ФАЙЛОВ ПРОГРАММЫ ###
import program_constants as CONST
import frame_createproject
PROJECT_INFO = dict()
PROJECT_PATH = dict()


TITLE_INFO = ["Название проекта:",
        "Поддерживаемая игра:",
        "Время создания проекта:",
        "Общее количество:",
        "Оружия:",
        "Брони:",
        "Еды:",
        "Медикаментов:"]

# Новый_проект_podst751123
class Main:
    def __init__(self, root_name=None, projectName="Новый_проект_podst751123", forGameName=CONST.GAMES_NAMES_LIST[::-1][0], path_project="Projects\\ShadowOfChernobyl\\tankalxat34\\"):
        self.root_name = root_name
        self.Frame = Frame(root_name, bg=CONST.BG)
        PROJECT_PATH["g"] = path_project

        #########################################
        self.Frame.pack(fill=BOTH, expand=1)
        #########################################

        try:
            config = configparser.ConfigParser()
            config.read(path_project+CONST.CONFIG_FILE_NAME)
        except Exception:
            if mb.askyesno(CONST.WIN_NAME, 'Не обнаружен файл '+path_project+CONST.CONFIG_FILE_NAME+'. Вы хотите удалить этот проект? Действие необратимо!'):
                os.remove(CONST.FOLDERS["projects"]+CONST.PROGRAM_GAMES_NAMES_LIST[CONST.GAMES_NAMES_LIST.index(forGameName)]+PROJECT_PATH["g"])
                mb.showinfo(CONST.WIN_NAME, f'Проект "{PROJECT_PATH["g"]}" удален!')
                quit()



        PROJECT_INFO[0] = PROJECT_PATH["g"].split("\\")[::-1][1]
        PROJECT_INFO[1] = forGameName
        PROJECT_INFO[2] = CONST.PROGRAM_GAMES_NAMES_LIST[CONST.GAMES_NAMES_LIST.index(forGameName)]
        PROJECT_INFO[3] = config["info"]["time_create"]
        PROJECT_INFO[4] = config["info"]["column_elements"]
        PROJECT_INFO[5] = config["info"]["column_weapon"]
        PROJECT_INFO[6] = config["info"]["column_outfit"]
        PROJECT_INFO[7] = config["info"]["column_eat"]
        PROJECT_INFO[8] = config["info"]["column_med"]
        # PROJECT_INFO[9] = config["info"]["description"]
        # bad relief "1": must be flat, groove, raised, ridge, solid, or sunken

        LOCAL_FONT_SIZE_PROJECTINFO = 13


        frameLEFT_Interface = Frame(self.Frame, bg=CONST.BG)
        frameTitle = CONST.mainLabelFrame(frameLEFT_Interface, text="Информация о проекте", bg=CONST.BG)
        LISTBOX_PROJECTINFO = CONST.mainListbox(frameTitle, bd=0,font="Calibri "+str(LOCAL_FONT_SIZE_PROJECTINFO), height=10, width=30, listvariable=list(PROJECT_INFO.values()))
        LISTBOX_PROJECTINFO.delete(0, END)
        LISTBOX_PROJECTINFO.pack(side=RIGHT)
        LISTBOX_PROJECTINFO.bind("<Double-Button-1>", lambda event: isAcceptedValue_NameProject(LISTBOX_PROJECTINFO.get(LISTBOX_PROJECTINFO.curselection())))

        LISTBOX_PROJECTINFO_TITLES = CONST.mainListbox(frameTitle, bd=0, font="Calibri " + str(LOCAL_FONT_SIZE_PROJECTINFO),
                                                       height=10, width=25, listvariable=TITLE_INFO, justify=RIGHT)
        LISTBOX_PROJECTINFO_TITLES.delete(0, END)
        LISTBOX_PROJECTINFO_TITLES.pack(side=LEFT)
        LISTBOX_PROJECTINFO_TITLES.focus_force()
        LISTBOX_PROJECTINFO_TITLES.delete(0, END)

        # for i in range(len(list(PROJECT_INFO.keys()))):
        for e in list(PROJECT_INFO.values())[::-1]:
            if e not in CONST.PROGRAM_GAMES_NAMES_LIST:
                LISTBOX_PROJECTINFO.insert(0, e)

        for e in TITLE_INFO[::-1]:
            LISTBOX_PROJECTINFO_TITLES.insert(0, e+" ")

        LISTBOX_PROJECTINFO.focus_force()
        def copyParam():
            try:
                pyperclip.copy((LISTBOX_PROJECTINFO.get(LISTBOX_PROJECTINFO.curselection())).replace("\n", " "))
            except Exception:
                pass

        def copyParamWithName():
            try:
                pyperclip.copy(TITLE_INFO[LISTBOX_PROJECTINFO.curselection()[0]]+" "+(LISTBOX_PROJECTINFO.get(LISTBOX_PROJECTINFO.curselection())).replace("\n", " "))
            except Exception:
                pass

        def isAcceptedValue_NameProject(value):
            if (value not in CONST.GAMES_NAMES_LIST) and LISTBOX_PROJECTINFO.curselection()[0] not in [2,3,4,5,6,7,8,9]:
                # print(LISTBOX_PROJECTINFO.curselection())
                try:
                    renameWindow = CONST.contextWindow("600x200", titleWindow="Переименование объекта - "+LISTBOX_PROJECTINFO.get(LISTBOX_PROJECTINFO.curselection()), titleLabel=" ")
                    CONST.frameBottomNextBack(renameWindow.child, "Отмена", "ОК",
                                              commandNext=lambda: setNewConfigProjectValue(entryLabelContext.get_entry(), renameWindow, oldPathProject=PROJECT_PATH["g"]),
                                              commandBack=lambda: renameWindow.child.destroy()).pack(fill=X)
                    entryLabelContext = CONST.frameLabelWithEntry(renameWindow.getFrame(), "Введите значение: ", "", set_focus=True)
                    entryLabelContext.get_frame().pack()
                    renameWindow.child.bind_all("<Return>", lambda event: setNewConfigProjectValue(entryLabelContext.get_entry(), renameWindow, oldPathProject=PROJECT_PATH["g"]))
                    renameWindow.child.bind_all("<Escape>", lambda event: renameWindow.child.destroy())
                except Exception:
                    pass
            else:
                mb.showerror(CONST.WIN_NAME, "Это значение невозможно изменить!")

        def setNewConfigProjectValue(newName, winContextDestroy, oldPathProject, config=config):
            if len(newName) >= 4 and (" " not in newName) and (newName not in os.listdir(CONST.FOLDERS["projects"] + CONST.getGameDirProject(forGameName))):
                config["info"]["project_name"] = newName
                with open((PROJECT_PATH["g"]+"\\"+CONST.CONFIG_FILE_NAME).replace("\\\\", "\\"), 'w') as configfile:
                    config.write(configfile)
                PROJECT_PATH["g"] = PROJECT_PATH["g"].replace(PROJECT_INFO[0], newName)
                PROJECT_INFO[0] = PROJECT_PATH["g"].split("\\")[::-1][1]
                LISTBOX_PROJECTINFO.delete(0, END)
                for e in list(PROJECT_INFO.values())[::-1]:
                    if e not in CONST.PROGRAM_GAMES_NAMES_LIST:
                        LISTBOX_PROJECTINFO.insert(0, e)
                os.rename(oldPathProject, PROJECT_PATH["g"])
                winContextDestroy.child.destroy()
            else:
                mb.showerror(CONST.WIN_NAME, "Некорректный ввод! Проверьте, выполнены ли следующие условия:\n- в названии проекта не должно быть пробелов;\n- проект имеет название, состоящее более чем из четырех символов;\n- проект имеет уникальное название;\n- выбрана игра, для которой будет создан проект;")

        MENU_LISTBOX_PROJECTINFO = CONST.menuMouse(LISTBOX_PROJECTINFO)
        MENU_LISTBOX_PROJECTINFO.insert(("Копировать значение", lambda: copyParam()))
        MENU_LISTBOX_PROJECTINFO.insert(("Копировать значение с названием", lambda: copyParamWithName()))
        MENU_LISTBOX_PROJECTINFO.insert(("Изменить значение", lambda: isAcceptedValue_NameProject(LISTBOX_PROJECTINFO.get(LISTBOX_PROJECTINFO.curselection()))))
        LISTBOX_PROJECTINFO.bind("<Control-C>", lambda event: copyParam())

        frameTitle.pack(side=TOP, anchor=N)


        # frame_contextWindow_Description.getFrame()
        # CONST.secondLabel(frame_contextWindow_Description.getFrame(), "Text").pack()

        frameDescription = CONST.mainLabelFrame(frameLEFT_Interface, "Описание проекта")
        textDescriptionWidget = CONST.textWidget(frameDescription, config["info"]["description"], height=13, state=DISABLED).widget
        textDescriptionWidget.pack(fill=X)


        frame_contextWindow_Description = CONST.contextWindowVar1(commandNext=None, titleFont="Carimba 0", draw=True)
        def setNewConfigDescriptionValue(windowContext, widgetFromGetNewDescription):
            config["info"]["description"] = widgetFromGetNewDescription.get(1.0, END)
            # PROJECT_INFO[9] = config["info"]["description"]
            with open((PROJECT_PATH["g"] + "\\" + CONST.CONFIG_FILE_NAME).replace("\\\\", "\\"), 'w') as configfile:
                config.write(configfile)
            textDescriptionWidget["state"] = NORMAL
            textDescriptionWidget.delete(0.0, END)
            textDescriptionWidget.insert(0.0, config["info"]["description"])
            textDescriptionWidget["state"] = DISABLED
            windowContext.destroy()

        def isAcceptedValue_NewProject(frame_contextWindow_Description=frame_contextWindow_Description):
            frame_contextWindow_Description.create()
            frame_contextWindow_Description.getFrame()
            mainTextWidget = CONST.textWidget(frame_contextWindow_Description.getFrame(), insertText="", height=5, state=NORMAL).widget
            mainTextWidget.insert(0.0, config["info"]["description"])
            mainTextWidget.pack(fill=BOTH, expand=1)
            mainTextWidget.focus_force()
            frame_contextWindow_Description.commandNext=lambda: setNewConfigDescriptionValue(windowContext=frame_contextWindow_Description, widgetFromGetNewDescription=mainTextWidget)

        def deleteProject():
            if mb.askyesno(CONST.WIN_NAME, 'Вы действительно хотите удалить этот проект? Действие необратимо! Проект удаляется навсегда!'):
                shutil.rmtree(PROJECT_PATH["g"])
                FRAME_STARTMENU.Main(root_name).packFrame(self.Frame)
                mb.showinfo(CONST.WIN_NAME, "Проект "+projectName+" успешно удален!")


        MENU_TEXTWIDGET_DESCRIPTION = CONST.menuMouse(textDescriptionWidget)
        MENU_TEXTWIDGET_DESCRIPTION.insert(("Копировать значение", lambda: pyperclip.copy(textDescriptionWidget.get(1.0, END))))
        MENU_TEXTWIDGET_DESCRIPTION.insert(("Изменить значение", lambda: isAcceptedValue_NewProject()))

        frameDescription.pack(fill=BOTH)



        frameButtonsMenu = CONST.mainLabelFrame(frameLEFT_Interface, text="Меню")
        CONST.intedent(frameButtonsMenu, size=7).pack()

        frame_MenuType1 = Frame(frameButtonsMenu, bg=CONST.BG)
        CONST.menu_button(frame_MenuType1, "Добавить сущность...", bg=CONST.BG_GREYGREEN, width=40, command=lambda: CONST.setNewFrame(frame_MenuType1, frame_MenuType2)).pack()
        CONST.intedent(frame_MenuType1).pack()
        CONST.menu_button(frame_MenuType1, "Закрыть проект", width=40, bg=CONST.BG_GREYRED, command=lambda: FRAME_STARTMENU.Main(root_name).packFrame(self.Frame)).pack()
        CONST.intedent(frame_MenuType1).pack()
        CONST.menu_button(frame_MenuType1, "Открыть в проводнике", width=40,
                          command=lambda: os.system("explorer.exe "+PROJECT_PATH["g"])).pack()
        CONST.intedent(frame_MenuType1).pack()
        CONST.menu_button(frame_MenuType1, "О программе", width=40, command=lambda: CONST.aboutProgram()).pack()
        CONST.intedent(frame_MenuType1).pack()
        CONST.menu_button(frame_MenuType1, "Удалить проект", width=40, command=lambda: deleteProject()).pack()
        CONST.intedent(frame_MenuType1).pack()
        CONST.menu_button(frame_MenuType1, "Выйти из программы", width=40, command=lambda: CONST.mainQuit()).pack()
        frame_MenuType1.pack(fill=BOTH, expand=1)

        frame_MenuType2 = Frame(frameButtonsMenu, bg=CONST.BG)
        CONST.menu_button(frame_MenuType2, "Оружие...", width=40).pack()
        CONST.intedent(frame_MenuType2).pack()
        CONST.menu_button(frame_MenuType2, "Броня...", width=40, command=lambda: CONST.mbFlocked()).pack()
        CONST.intedent(frame_MenuType2).pack()
        CONST.menu_button(frame_MenuType2, "Еда...", width=40, command=lambda: CONST.mbFlocked()).pack()
        CONST.intedent(frame_MenuType2).pack()
        CONST.menu_button(frame_MenuType2, "Медикаменты...", width=40, command=lambda: CONST.mbFlocked()).pack()
        CONST.intedent(frame_MenuType2).pack()
        CONST.menu_button(frame_MenuType2, "Диалог...", width=40, command=lambda: CONST.mbFlocked()).pack()
        CONST.intedent(frame_MenuType2).pack()
        CONST.menu_button(frame_MenuType2, "NPC...", width=40, command=lambda: CONST.mbFlocked()).pack()
        CONST.intedent(frame_MenuType2).pack()
        CONST.menu_button(frame_MenuType2, "Группировка...", width=40, command=lambda: CONST.mbFlocked()).pack()
        CONST.intedent(frame_MenuType2, size=5).pack()
        CONST.menu_button(frame_MenuType2, "<<< Назад", width=40, command=lambda: CONST.setNewFrame(frame_MenuType2, frame_MenuType1)).pack()
        CONST.intedent(frame_MenuType2).pack()
        # frame_MenuType2.pack(fill=BOTH, expand=1)


        CONST.secondLabel(frameButtonsMenu, text=CONST.AUTHOR_TEXT).pack(side=BOTTOM)
        frameButtonsMenu.pack(fill=BOTH, expand=1)

        frameLEFT_Interface.pack(side=LEFT, fill=Y, anchor=NE)




        frameCENTER_Interface = CONST.mainLabelFrame(self.Frame, "Список сущностей")
        CONST.secondLabel(frameCENTER_Interface, "Ни одной сущности не добавлено").pack(expand=1)

        frameCENTER_Interface.pack(side=LEFT, fill=BOTH, anchor=NE, expand=1)

        frameRIGHT_Interface = CONST.mainLabelFrame(self.Frame, "Внешний вид в игре")
        CONST.secondLabel(frameRIGHT_Interface, "Не выбрана сущность для просмотра").pack(expand=1)

        frameRIGHT_Interface.pack(side=LEFT, fill=BOTH, anchor=NE, expand=1)





    def get_frame(self):
        return self.Frame

    def packFrame(self, oldFrame):
        oldFrame.pack_forget()
        self.Frame.pack(fill=BOTH, expand=1)





















