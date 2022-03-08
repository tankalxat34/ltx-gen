""" -=ОПИСАНИЕ ПРОГРАММЫ=-

Программа STALKER ITEM CREATOR предназначена для создания и добавления в трилогию S.T.A.L.K.E.R. новых предметов: оружия, брони, медикаментов, еды, диалогов, NPC, группировок и др.
Автором программы является один человек: Александр tankalxat34 Подстречный.

Идея создания программы появилась в тот момент, когда GSC Game World анонсировала S.T.A.L.K.E.R 2 вместе с интерфейсом для создания собственных модицикаций. Мне показалось, что подобный инструментарий можно сделать и для предыдущих частей легендарной игры. Разработкой STALKER ITEM CREATOR я занялся в начале лета 2021 года.

Программа работает с внутренностями игры, умеет их редактировать, удалять, изменять и добавлять в них новые элементы. Программа распространяется БЕСПЛАТНО, разрабатывает ее один человек. У каждого пользователя есть возможность материально поддержать ее разработчика.
Все права на программу принадлежат ее создателю.

 -=ИНФОРМАЦИЯ О ДАННОЙ ВЕРСИИ ПРОГРАММЫ=-
"""
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import font
import tkinter.font
import getpass, os, os.path, time, webbrowser, pyperclip, configparser, shutil, random, ctypes
from tkinter import ttk


VERSION = '0.1.2'
WIN_NAME = 'STALKER ITEM CREATOR'
WIN_DRAW = True
WIN_ICON = 'icon.ico'
# WIN_GEOMETRY = '700x500'
WIN_GEOMETRY = '1300x780'
GAMES_NAMES_LIST = ["S.T.A.L.K.E.R. Зов Припяти",
                    "S.T.A.L.K.E.R. Чистое Небо",
                    "S.T.A.L.K.E.R. Тень Чернобыля"]
PROGRAM_GAMES_NAMES_LIST = ["CallOfPripyat\\", "ClearSky\\", "ShadowOfChernobyl\\"]
CONFIG_FILE_NAME = "project_SIC.ini"

PROGRAM_START_IN_FULLSCREEN = True


AUTHOR_TEXT = f"©2021 tankalxat34 v{VERSION}"

# шрифты
DEFAULT_FONT = "Calibri 12"
LOW_DEFAULT_FONT = ('Calibri', 9)

FG = 'white'
FG_GREY = "#A0A0A0"
# BG = 'black'
BG = '#303030'
BG_GREY = "#565656"
BG_GREYBLACK = "#3F3F3F"
# BG_ENTRY = "#3C3F41"
# BG_ENTRY = "#50575B"
BG_ENTRY = "#3C4144"
BG_GREYRED = "#630000"
BG_GREYGREEN = "#217000"


FOLDERS = {
    "data": "data\\",
    "projects": "Projects\\",
    "callofpripyat": "CallOfPripyat\\",
    "clearsky": "ClearSky\\",
    "shadowofchernobyl": "ShadowOfChernobyl\\",
}


def aboutProgram():
    aboutProgramContextWindow =contextWindowVar1(title="О программе", textOk="", textBack="Закрыть",
                                                        titleFont="Calibri 0", draw=True, win_size="700x700")
    aboutWindow = aboutProgramContextWindow.create()
    textWidgetAboutProgram = textWidget(aboutProgramContextWindow.getFrame(),
                                              insertText=__doc__ + f"НАЗВАНИЕ: {WIN_NAME}\nВЕРСИЯ: {VERSION}\nПУТЬ К ПАПКЕ С ПРОЕКТАМИ: {os.getcwd()}\\{FOLDERS['projects']}").widget
    textWidgetAboutProgram.pack(fill=BOTH, expand=1)
    textWidgetAboutProgram["state"] = DISABLED

def setWindowOnCenterScreen(root_name):
    """Устанавливает окно центральном положении на экране юзера"""
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    x = screensize[0]//8
    y = screensize[1]//8
    root_name.wm_geometry(f'+{x}+{y}')


class menuMouse:
    def __init__(self, frame, tupleArgs=None):
        self.menu = Menu(frame, tearoff=0)
        try:
            self.menu.add_command(label=tupleArgs[0], command=lambda: (tupleArgs[1])())
        except Exception:
            pass
        frame.bind("<Button-3>", lambda event: self.menu.post(event.x_root, event.y_root))

    def insert(self, *args):
        self.menu.add_command(label=args[0][0], command=lambda: (args[0][1])())

def menuMouse_old(frame, tupleTextCommand):
    # menu = Menu(frame, tearoff=0)
    menu = Menu(frame, tearoff=0)
    list_added_element = []
    for e in tupleTextCommand:
        menu.add_command(label=e[0], command=lambda: (e[1])())
    frame.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))


def getGameDirProject(forGameName):
    return PROGRAM_GAMES_NAMES_LIST[GAMES_NAMES_LIST.index(forGameName)]

def getGameNameProject(programGameName):
    return GAMES_NAMES_LIST[PROGRAM_GAMES_NAMES_LIST.index(programGameName)]


def menu_button(frame, text, command=lambda: mb.showinfo(WIN_NAME, WIN_NAME), font="Calibri 12", width=None, bg=BG_GREY):
    return Button(frame, text=text, command=lambda: command(), bg=bg, fg=FG, activebackground=BG_GREY,
                  activeforeground=FG, font=font, bd=0, width=width)


def titleLabel(frame, text, font="Calibri 30"):
    return Label(frame, text=text, font=font, fg=FG, bg=BG)


def secondLabel(frame, text, font="Calibi 10", bg=BG, justify=None):
    return Label(frame, text=text, font=font, fg=FG_GREY, bg=bg, justify=justify)


def firstLabel(frame, text, font="Cambria 30", bg=BG_GREYBLACK):
    return Label(frame, text=text, font=font, fg=FG, bg=bg)


def mainLabelFrame(frame, text, bg=BG):
    return LabelFrame(frame, text=text, bg=bg, fg=FG, relief=RIDGE)


# def mainEntry(frame, width=45, font="Calibri 14", bg="#2B2B2B", insert_text="Новый проект"):
def mainEntry(frame, width=45, font="Calibri 14", bg=BG_ENTRY, insert_text="Новый проект", state=NORMAL, justify=None):
    if state == NORMAL:
        localMainEntry = Entry(frame, width=width, font=font, bg=bg, fg=FG, bd=0, state=state, justify=justify)
    else:
        localMainEntry = Entry(frame, width=width, font=font, bg=bg, bd=0, justify=justify)
    localMainEntry.insert(0, insert_text)
    localMainEntry["state"] = state

    return localMainEntry


def mainListbox(frame, font="Calibri 13", listvariable=[], bg=BG_ENTRY, fg=FG, bd=1, width=15, height=5, selectmode=SINGLE, justify=None):
    return Listbox(frame, bg=bg, fg=fg, font=font, bd=bd, listvariable=listvariable, width=width, height=height, selectmode=selectmode, justify=justify, highlightthickness=0)


def intedent(frame, size=1, orient="horizontal", bg=BG):
    if orient == "horizontal" or orient[0] == "h":
        return Label(frame, text="\n", font="Calibri " + str(size), fg=FG, bg=bg)
    elif orient == "vertical" or orient[0] == "v":
        return Label(frame, text=" ", font="Calibri " + str(size), fg=FG, bg=bg)


def frameBottomNextBack(frame, buttonBackText="Назад", buttonNextText="Далее", buttonWidth=20, frameHeight=None, commandNext=lambda: mb.showinfo(WIN_NAME, "NEXT BUTTON PRESSED"), commandBack=lambda: mb.showinfo(WIN_NAME, "BACK BUTTON PRESSED")):
    frameWidgets = Frame(frame, bg=BG_GREYBLACK, height=frameHeight)
    intedent(frameWidgets, orient="v", bg=BG_GREYBLACK).pack()
    intedent(frameWidgets, orient="h", size=13, bg=BG_GREYBLACK).pack(side=RIGHT, anchor=N)
    if len(buttonNextText) != 0:
        menu_button(frameWidgets, buttonNextText, width=buttonWidth, command=lambda: commandNext()).pack(side=RIGHT, anchor=N)
    intedent(frameWidgets, orient="h", size=13, bg=BG_GREYBLACK).pack(side=RIGHT, anchor=N)
    if commandBack != False or len(buttonBackText) != 0:
        menu_button(frameWidgets, buttonBackText, width=buttonWidth, command=lambda: commandBack()).pack(side=RIGHT, anchor=N)
    intedent(frameWidgets, orient="v", bg=BG_GREYBLACK).pack()
    return frameWidgets


class frameLabelWithEntry():
    def __init__(self, frame, labelText="TextText", entryInsertText="TextText", set_focus=False, state=NORMAL, justify=None, width_entry=40):
        self.frame = frame
        self.labelText = labelText
        self.entryInsertText = entryInsertText
        self.state = state

        self.frameEntryName = Frame(frame, bg=BG)
        secondLabel(self.frameEntryName, labelText, justify=justify).pack(side=LEFT, anchor=N)
        self.ENTRY_LOCAL = mainEntry(self.frameEntryName, width=width_entry, insert_text=entryInsertText, state=state, justify=justify)
        self.ENTRY_LOCAL.pack(side=LEFT, anchor=N)
        if set_focus:
            self.ENTRY_LOCAL.focus()
        intedent(self.frameEntryName, orient="h", size=13).pack(side=LEFT, anchor=N)

    def get_frame(self):
        return self.frameEntryName

    def get_entry(self):
        return self.ENTRY_LOCAL.get()

    def set_text(self, newText):
        self.ENTRY_LOCAL["state"] = NORMAL
        self.ENTRY_LOCAL.delete(0, END)
        self.ENTRY_LOCAL.insert(0, newText)
        self.ENTRY_LOCAL["state"] = self.state

class contextWindow:
    def __init__(self, win_size="600x260", titleWindow="Изменение объекта", titleLabel="Переименование объекта", titleFont="Calibri 14", draw=False, title="Изменение объекта"):
        self.child = Toplevel()
        setWindowOnCenterScreen(self.child)
        self.child.iconbitmap(WIN_ICON)
        self.child.grab_set()

        self.title = title
        self.child.title(title)
        self.child.resizable(draw, draw)
        self.child.geometry(win_size)
        self.child.tkraise()
        self.child.focus_force()
        self.child.minsize(400, self.child.winfo_height())

        self.Frame = Frame(self.child, bg=BG)
        if int(titleFont.split()[1]) != 0:
            firstLabel(self.Frame, titleLabel, bg=BG, font=titleFont).pack()
        self.Frame.pack(fill=BOTH, expand=1)

    def getFrame(self):
        return self.Frame

    def getChild(self):
        return self.child


class contextWindowVar1:
    def __init__(self, titleLabel=" ", titleFont="Carimba 14",
                 textBack="Отмена",
                 textOk="OK",
                 commandNext=lambda: print("Next pressed"),
                 bindCommandNext=None,
                 draw=False,
                 title=WIN_NAME,
                 win_size="600x200"):
        self.textBack = textBack
        self.textOk = textOk
        self.commandNext = commandNext
        self.bindCommandNext = bindCommandNext
        self.titleLabel = titleLabel
        self.titleFont = titleFont
        self.draw = draw
        self.title = title
        self.win_size = win_size

    def create(self):
        self.renameWindow = contextWindow(self.win_size, titleLabel=self.titleLabel, titleFont=self.titleFont, draw=self.draw, title=self.title)
        frameBottomNextBack(self.renameWindow.child, self.textBack, self.textOk,
                            commandNext=lambda: self.commandNext(),
                            commandBack=lambda: self.renameWindow.child.destroy()).pack(fill=X)

        try:
            if self.bindCommandNext != None:
                self.renameWindow.getChild().bind_all("<Return>", lambda event: self.bindCommandNext())
        except Exception:
            pass
        self.renameWindow.getChild().bind_all("<Escape>", lambda event: self.renameWindow.child.destroy())

    def getFrame(self):
        return self.renameWindow.getFrame()

    def destroy(self):
        return self.renameWindow.getChild().destroy()


class textWidget:
    def __init__(self, frame, insertText, font="Calibri 14", width=30, height=15, state=NORMAL, minFontSize=10, maxFontSize=20, canFontSizeSelect=False):
        self.widget = Text(frame, bg=BG_ENTRY, font=font, fg=FG, width=width, height=height, wrap=WORD)

        scrollY = Scrollbar(frame, command=self.widget.yview, orient=VERTICAL, bg=BG, bd=0)
        scrollY.pack(side=RIGHT, fill=Y)
        self.widget.config(yscrollcommand=scrollY.set)

        self.widget.insert(1.0, insertText)
        self.widget["state"] = state

        self.widget.bind_all("<Control-minus>", lambda event: self.selectFontSize("minus"))
        self.widget.bind_all("<Control-equal>", lambda event: self.selectFontSize("plus"))

        #self.mainMouseContext

        self.minFontSize = minFontSize
        self.maxFontSize = maxFontSize
        self.canFontSizeSelect = canFontSizeSelect

    def selectFontSize(self, operation="plus"):
        if self.canFontSizeSelect:
            if operation == "plus":
                if int(self.widget["font"].split()[1]) <= self.maxFontSize:
                    self.widget["font"] = self.widget["font"].split()[0]+" "+str(int(self.widget["font"].split()[1])+2)
            elif operation == "minus":
                if int(self.widget["font"].split()[1]) >= self.minFontSize:
                    self.widget["font"] = self.widget["font"].split()[0]+" "+str(int(self.widget["font"].split()[1])-2)


def mainQuit():
    if mb.askyesno("Подтверждение выхода", "Вы уверены, что хотите закрыть программу?"):
        quit()

def setNewFrame(oldFrame, newFrame):
    oldFrame.pack_forget()
    newFrame.pack()

def mbFlocked():
    mb.showerror(WIN_NAME, "Функция не доступна в этой версии программы")


class scrollerY:
    def __init__(self, widget, frame):
        self.widget = widget
        self.frame = frame

    def pack(self):
        self.scrollY = Scrollbar(self.frame, command=self.widget.yview, orient=VERTICAL, bg=BG, bd=0)
        self.scrollY.pack(side=RIGHT, fill=Y)
        self.widget.config(yscrollcommand=self.scrollY.set)





















