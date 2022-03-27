# -*- coding: utf-8 -*-
from tkinter import ttk
from tkinter import *
import sys
import os
from os import system
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import time, threading
import webbrowser
import os.path
import shutil
import time
from config import *
import config
import pyperclip
import re
from PIL import ImageTk
from PIL import Image


'''
RedirectionFunctions - перенаправляющие функции, написанные в файле config.py

, font=(config.font_name, config.font_size)
, font=(config.low_font_name, config.low_font_size)
, justify=LEFT
'''
#'291x355' # ταŋᶄắḽჯãṫ34
#========КОНСТАНТЫ=============
win_icon='res'+chr(92)+'yellow.ico'
win_name='LTX-Gen'
win_draw=False
#win_geometry='700x420'   
#win_geometry='900x500'         
win_geometry='825x430'       
#author_label='tankalxat34 ©2020 - ver1.0' 
author_label='ταŋᶄắḽჯãṫ34 ©2020 - ver1.0' 
simple_author_label='tankalxat34 ©2020 - ver1.0'
path_win_logo='res/BG_win_logo.jpg'
#==============================
sys_outfit_name='prorok'
#sys_outfit_name='rose_m132'
#outfit_inv_name='Комбинезон «Пророк»'
#sys_wpn_name='laska'
# prj_name='броня_для_теста'
prj_name='броня_для_теста'
#prj_name='оружие_для_теста'
text_coordinate_icons='''inv_grid_width     = 1
inv_grid_height    = 1
inv_grid_x         = 8
inv_grid_y         = 37'''
outf_cost='12300'
#sys_eat_name='cola'
#inv_name_eat='Банка Coca Cola'
#eat_cost='30'
#
#root_name, prj_name, sys_eat_name, text_coordinate_icons, eat_cost, inv_name_eat
#======ПОСТОЯННЫЕ ФУНКЦИИ======
'''
---------------ПОМОЖЕТ В ПОСЛЕДНЕМ СЛАЙДЕ (показ меню при клике правой кнопкой мыши)---------------
menu=Menu(tearoff=0)
menu.add_command(label="Очистить", command=delete_text)
WIDGET.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))
---------------------------------------------------------------------------------------------------

'''

'''
ЧТО СДЕЛАТЬ В БЛИЖАЙШЕЕ ВРЕМЯ?
----------------------------------------------------------------------
- ДОДЕЛАТЬ НАКОНЕЦ ДОБАВЛЕНИЕ ДВУХ И БОЛЕЕ КОСТЮМОВ В СПАВНЕР НОРМАЛЬНО!!!
- сделать аналогично бронекостюмам загрузку текстур и ogf файлов для еды и потом для оружия.
- пересмотреть функцию Analyze после загрузки dds и ogf в бронекостюмах и еде.

- начать делать диалог добавления оружия
!!!ВАЖНО!!! ПОЛНОСТЬЮ ПЕРЕСМОТРЕТЬ ДИАЛОГ ДОБАВЛЕНИЯ ОРУЖИЯ ДЛЯ ЕГО МНОГОРАЗОВОГО ИСПОЛЬЗОВАНИЯ. ОСОБЕННО ШАГ ИНИЦИАЛИЗАЦИИ В ИГРЕ!
----------------------------------------------------------------------
+ попробовать сделать запись новых текстур в ogf файл.
+ https://www.amk-team.ru/forum/faq/7-spravochnik-vyletov-line-201-line-400/ исправить вылет по этой инструкции. (зайти в геймдату игры и из менить wpn_laska на wpn_las)
+ сделать механизм "в зависимости от наличия спавн меню показывать в главном меню соответствующую надпись".
+ доделать выбор иконки костюма
+ создать механизм создания строчки для записи костюма в outfit.ltx
+ доделать диалог создания бронекостюма
+ создать колу в сталкере как новый предмет, что бы протестить механизм.
+ доделать слайд с добавлением характеристик еды
+ создать конечное меню для выбора "что еще добавить в проект?"
+ вернуть возможность перименовки текстур костюмов
+ исправить баг удаления предыдущих файлов в создании еды
+ найти и устранить проблему не добавления еды в спавн меню если еда добавляется второй раз (ПРОГРАММА ИЩЕТ СТРОЧКУ, КОТОРАЯ НЕ БЫЛА ДОБАВЛЕНА В ПЕРВЫЙ РАЗ, 
Т.Е. ЕСЛИ МЫ ПЕРВЫМ ШАГОМ СДЕЛАЛИ ЕДУ, ТО ОНА БУДЕТ ДОБАВЛЯТСЯ ВСЕГДА, А ЕСЛИ СНАЧАЛА СДЕЛАЛИ  КОСТЮМ, ТО ЕДА УЖЕ НИКОГДА НЕ ДОБАВИТЬСЯ, ТАК КАК ФАЙЛ-СПИСОК ЕСТЬ, А НУЖНОЙ СТРОЧКИ НЕТ
МОЖНО СДЕЛАТЬ ПРИВЯЗКУ К СТРОЧКЕ --items, --outfits И ПОДОБНЫМ, И СДЕЛАТЬ ЗАПИСЬ ЧЕРЕЗ replace('--items', 'строка с заглавием и новым предметом'))
+ СДЕЛАТЬ ПЕРЕИМЕНОВКУ ЗАГРУЖАЕМЫХ ФАЙЛОВ С УЧЕТОМ ВВЕДЕННОГО СИСТЕМНОГО ИМЕНИ СРАЗУ ПОСЛЕ ИХ ЗАГРУЖАНИЯ, И ЗАПОМИНАТЬ ИХ НОВОЕ НАЗВАНИЕ НА СЛУЧАЙ ВОЗМОЖНОГО УДАЛЕНИЯ,
И УБРАТЬ ФУНКЦИЮ ПЕРЕИМЕНОВКИ ФАЙЛОВ ЧЕРЕЗ КНОПКУ "ПРОДОЛЖИТЬ"
'''

desc_file_text='''
;-----------------------------------------------------------------
;		ОПИСАНИЕ
;-----------------------------------------------------------------
;тут содержится информация о сущностях в проекте. 
;Файл используется ТОЛЬКО для демонстрации информации.
;Во избежании дизориентации крайне НЕ РЕКОМЕНДУЕТСЯ изменять данный файл, так как что-то изменив  здесь,
;вы НЕ ИЗМЕНИТЕ их в самой игре! Это важно понимать! Внося изменения в данный файл вручную вы автоматически берете
;на себя всю ответственность за работоспособность проекта.
;-----------------------------------------------------------------

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; 		LTX-Gen section
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

'''


desc_END_SLIDE='''
Здесь вы можете осмотреть свой проект прежде чем завершить его наполнение.
Используйте кнопки, что бы добавить что то новое в проект. Если вы хотите
завершить проект, то нажмите на кнопку "ЗАВЕРШИТЬ ПРОЕКТ".

Подробнее о последних изменениях вы можете прочитать в группе ВКонтакте,
перейти в нее можно нажав на одну из кнопок внизу окна.'''

def step3_help():
	help_text='''Шаг 3.
Здесь требуется загрузить в программу определенные файлы визуальной состовляющей нашего оружия.

У любого оружия в S.T.A.L.K.E.R. Тень Чернобыля имеется несколько файлов, определяющих его визуальную составляющую.
Это файлы с следующими расширениями:

- *.dds - это файлы, в которых содержится текстура оружия. В игре она бывает трех видов, стандартная, текстура для
падающих на оружие теней и рельефная текстура. Они имеют названия соответственно wpn_ak47.dds ; wpn_ak47_bump.dds ;
wpn_ak47_bump#.dds .

- *.ogf - это файлы, в которых содержится модель оружия, ее визуал. На ней отрисованы все подвижные элементы и все
выпуклости. 

Что подрузамевается под фразой "Системное имя оружия"?
В данной программе фраза "Системное имя оружия" означает файловое название оружия, которое игра будет использовать
для обращения к конкретно этому оружию. Системное имя оружия не может иметь в названии кириллицу, а так же пробелы
и другие символы - то есть, подрузамевается только английская раскладка. Имейте это ввиду при вводе системного
имени!

Если у вас нет нужных файлов, то можете заглянуть в специальный топик, нажав по кнопке "Шаблоны визуалов"!
Время от времени там публикуются нужные файлы!
'''
	WinHelp(help_text=help_text)


def step5_help_naxac_eat():
	help_naxac='''Какие правки/дополнения в спавн-меню от naxac внес автор данной программы tankalxat34?
- по нажатию клавиши [V] в главном меню игры игроку добавится 100`000 рублей;
- в главном меню игры в левом нижнем углу теперь отображено следующее название: "ver. 1.0003 + spawn-menu by naxac + LTX-Gen by tankalxat34";
- в  меню самого спавн-меню добавлено оружие. Открыть само меню можно нажав клавишу F1, находясь в главном меню игры;
---------------------------------
Как добавить свою иконку?
- Нажать на кнопку [Открыть SIE.exe];
- Откроется программа, в которой вам нужно выделить ту иконку, которая будет использоваться игрой для отображения вашего предмета в инвентаре;
- Кликните правой кнопкой мыши по выделенной области и нажмите "Информация о выделении";
- Скопируйте всю информацию, которая находится в открывшемся окне;
- Закройте STALKER Icon Editor и в открывшемся окне LTX-Gen в поле ввода координаты иконок вставьте то, что скопировали ранее;
- Готово!

Иконку можно не выбирать, однако если она не будет выбрана, то по умолчанию иконкой оружия станет надпись NO ICON
---------------------------------
Программа STALKER Icon Editor выложена бесплатно на множестве известных сайтах и форумах без лицензионного соглашения на ее использование. Это означает, что автор LTX-Gen смог включить ее в свою программу без каких-либо последствий для себя.
Согласно лицензионному соглашению на использование LTX-Gen, автор не несет ответственности за вред/поломки и другие неисправности в работе как LTX-Gen, так и STALKER Icon Editor, но рекомендует её в качестве удобной и бесплатной программы для работы с иконками из игры S.T.A.L.K.E.R. Тень Чернобыля ver1.0003
'''.format()
	WinHelp(help_text=help_naxac)


def step5_help():
	help_text='''-----------------------------------------------------------------------------------------------
АВТОР СТАТЬИ Neptun. ИСТОЧНИК: http://st-md.ru/viewtopic.php?id=415
ДЛЯ LTX-Gen СТАТЬЮ ОТРЕДАКТИРОВАЛ tankalxat34.
-----------------------------------------------------------------------------------------------

Секция [trader_generic_buy]
Эта секция описывает какие товары торговец будет покупать.
Название предмета = минимальная цена покупки, максимальная цена покупки
Например:
wpn_vintorez = 0.7, 0.5 Это значит что торговец купит оружие от 50% полной его стоимости до 70%, т.е. если Винторез стоит 1000, то торговец купит его в диапазоне от 500 до
700 рублей. Диапазон зависит от отношения торговца к Меченому - чем лучше, тем дороже купит

Секция [supplies_start]
Эта секция описывает какие товары у торговца будут вначале.
Название предмета = количество, вероятность появления
Например:
bandage = 5, 1 Это значит что у торговеца всегда будут 5 бинтов, с 100 процентной вероятностью появления в магазине.
bandage = 5, 0.6 А тут уже вероятность появления 60%. Т.е. бинты не всегда будут.

Секция [trader_start_sell]
Эта секция описывает за какую цену торговец будет продавать.
Название предмета = минимальная цена продажи, максимальная цена продажи
Например:
wpn_vintorez = 1, 2 Это значит что торговец продаст оружие от 100% полной его стоимости до 200%, т.е. если Винторез стоит 1000, то торговец продаст его в диапазоне от
1000 до 2000 рублей. Диапазон зависит от отношения торговца к Меченому - чем лучше, тем дешевле продаст.
'''
	WinHelp(help_text=help_text)

#      config.folder_projects+'/'+prj_name+

def step5_help_naxac(game_wnp_name, sys_name):
	help_naxac='''Какие правки/дополнения в спавн-меню от naxac внес автор данной программы tankalxat34?
- по нажатию клавиши [V] в главном меню игры игроку добавится 100`000 рублей;
- в главном меню игры в левом нижнем углу теперь отображено следующее название: "ver. 1.0003 + spawn-menu by naxac + LTX-Gen by tankalxat34";
- в  меню самого спавн-меню добавлено оружие {}. Открыть само меню можно нажав клавишу F1, находясь в главном меню игры;
---------------------------------
Как добавить оружию свою иконку?
- Нажать на кнопку [Открыть SIE.exe];
- Откроется программа, в которой вам нужно выделить ту иконку, которая будет использоваться игрой для отображения вашего оружия в инвентаре;
- Кликните правой кнопкой мыши по выделенной области и нажмите "Информация о выделении";
- Скопируйте всю информацию, которая находится в открывшемся окне;
- Закройте STALKER Icon Editor и в открывшемся окне LTX-Gen в поле ввода координаты иконок вставьте то, что скопировали ранее;
- Готово!

Иконку оружия можно не выбирать, однако если она не будет выбрана, то по умолчанию иконкой оружия станет надпись NO ICON
---------------------------------
Программа STALKER Icon Editor выложена бесплатно на множестве известных сайтах и форумах без лицензионного соглашения на ее использование. Это означает, что автор LTX-Gen смог включить ее в свою программу без каких-либо последствий для себя.
Согласно лицензионному соглашению на использование LTX-Gen, автор не несет ответственности за вред/поломки и другие неисправности в работе как LTX-Gen, так и STALKER Icon Editor, но рекомендует её в качестве удобной и бесплатной программы для работы с иконками из игры S.T.A.L.K.E.R. Тень Чернобыля ver1.0003
'''.format(game_wnp_name+' ('+sys_name+')')
	WinHelp(help_text=help_naxac)

desc_outfit_step2='''Поставьте галочку "Отключить переименование текстур", если 
загружаемые текстуры уже имеют название, которое привязано к загружаемым ogf 
моделям.

Текстуры:
Их должно быть или один или три файла. Если файл только один, то обычно он имеет
название например act_specnaz.dds . Его и следует загружать в программу.

Если файлов несколько, то требуется загрузить их все в программу. Они имеют названия:
act_specnaz.dds
act_specnaz_bump.dds
act_specnaz_bump#.dds'''



desc_wpn_step3='''Поставьте галочку "Отключить переименование текстур", если 
загружаемые текстуры уже имеют название, которое привязано к загружаемым ogf 
моделям.


ОБРАТИТЕ ВНИМАНИЕ!!!
Если в ogf фале не прописаны текстуры, то их нужно прописать там вручную, что бы они отображались
в игре. О том, как это сделать, читайте в интернете, или найдите искодники в моей группе вконтакте!
Программа пока не может приписывать загружаемым ogf моделям их новые текстуры!
'''

desc_eat_s4='''

Здесь требуется ввести параметры нашей еды. Там, где требуется 
ввести процент, входными данными могут быть только числа от 0.00 
до 0.99! Дробное число вводится через ".". Количество порций может
быть равен -1, если порций нет. Если порции есть, введите их коли-
чество, больше чем 0.
После ввода всех значений нажмите "Продолжить".
'''


description_outfit_s4='''Здесь вам нужно ввести параметры вашего бронекостюма, загрузить иконку персонажа в инвентаре. 
Если у вас есть готовый скрипт outfit.ltx с новым бронекостюмом, вы можете загрузить его в программу.
Высший уровень защиты от внешних воздействий равен 0.99, высший иммунитет равен 0.00 .'''


def help_step3():
	help_text='''Здесь требуется загрузить текстуры оружия, его ogf-модель и системное имя оружия.

Системное имя оружия - уникальное слово, написанное английскими буквами для определения конкретного предмета игрой. Каждый предмет, оружие, артефакт или другая существующая в игре сущность обладает определенным системным именем.

Текстуры dds - обычные текстуры, то, что видит игрок, когда смотрит оружие. Редактируются фотошопом со специальным плагином, либо в программе paint.net.

Модели ogf - файлы, имеющие расширение *.ogf, на которые игра "накладывает" загруженную текстуру.

Если у вас нет нужных файлов, то можете заглянуть в специальный топик, нажав по кнопке "Шаблоны визуалов"!
Время от времени там публикуются нужные файлы!
'''
	WinHelp(help_text)

def step5_help_naxac_outfit():
	help_naxac='''Какие правки/дополнения в спавн-меню от naxac внес автор данной программы tankalxat34?
- по нажатию клавиши [V] в главном меню игры игроку добавится 100`000 рублей;
- в главном меню игры в левом нижнем углу теперь отображено следующее название: "ver. 1.0003 + spawn-menu by naxac + LTX-Gen by tankalxat34";
- в  меню самого спавн-меню добавлено оружие. Открыть само меню можно нажав клавишу F1, находясь в главном меню игры;
---------------------------------
Как добавить бронекостюму свою иконку?
- Нажать на кнопку [Открыть SIE.exe];
- Откроется программа, в которой вам нужно выделить ту иконку, которая будет использоваться игрой для отображения вашего бронекостюма в инвентаре;
- Кликните правой кнопкой мыши по выделенной области и нажмите "Информация о выделении";
- Скопируйте всю информацию, которая находится в открывшемся окне;
- Закройте STALKER Icon Editor и в открывшемся окне LTX-Gen в поле ввода координаты иконок вставьте то, что скопировали ранее;
- Готово!

Иконку оружия можно не выбирать, однако если она не будет выбрана, то по умолчанию иконкой оружия станет надпись NO ICON
---------------------------------
Программа STALKER Icon Editor выложена бесплатно на множестве известных сайтах и форумах без лицензионного соглашения на ее использование. Это означает, что автор LTX-Gen смог включить ее в свою программу без каких-либо последствий для себя.
Согласно лицензионному соглашению на использование LTX-Gen, автор не несет ответственности за вред/поломки и другие неисправности в работе как LTX-Gen, так и STALKER Icon Editor, но рекомендует её в качестве удобной и бесплатной программы для работы с иконками из игры S.T.A.L.K.E.R. Тень Чернобыля ver1.0003
'''.format()
	WinHelp(help_text=help_naxac)


desc_eat_s1='''
Поставьте галочку "Отключить переименование текстур", если 
загружаемые текстуры уже имеют название, которое привязано к загружаемым ogf 
моделям.

Здесь требуется загрузить в программы текстуры еды и ее ogf модель, а так же ввести
системное имя еды, используемое игрой.Класс еды можете не трогать и оставить по 
умолчанию (еда).
'''






def Otstup(widget):
	FrameOtstup = Frame(widget)
	Label(FrameOtstup, text=10*'  ').pack()
	FrameOtstup.pack(side=LEFT, anchor=N)

def OpenVK():
	url = 'https://vk.com/ltx_gen'
	if mb.askyesno(win_name, "Вы будете перенаправлены на внешний ресурс "+url):
		webbrowser.open_new(url)

def OpenVisualsTopik():
	url='https://vk.com/topic-187626702_40862849'
	if mb.askyesno(win_name, "Вы будете перенаправлены на внешний ресурс "+url):
		webbrowser.open_new(url)

def AuthorLabel(widget):

	Frame_Author = Frame(widget, bg='#DCDCDC')
	Label(Frame_Author, text=author_label, bg='#DCDCDC', fg='grey').pack(side=LEFT, anchor=N)

	Label(Frame_Author, text='|', bg='#DCDCDC', fg='grey').pack(side=LEFT, anchor=N)
	Button(Frame_Author, text='Группа VK', command=OpenVK, bd=0, bg='#DCDCDC', fg='grey', activebackground='#DCDCDC').pack(side=LEFT, anchor=N)
	Label(Frame_Author, text='|', bg='#DCDCDC', fg='grey').pack(side=LEFT, anchor=N)
	Button(Frame_Author, text='Шаблоны визуалов', command=OpenVisualsTopik,  bd=0, bg='#DCDCDC', fg='grey', activebackground='#DCDCDC').pack(side=LEFT, anchor=N)

	Frame_Author.pack(anchor=S)

def WinTitle(root_name):
	#Label(root_name, text='S.T.A.L.K.E.R. {}'.format(win_name), font=('AmazS.T.A.L.K.E.R.v.3.0', config.font_size+20), bg='#DCDCDC').pack()

	FrameTitle = LabelFrame(root_name, bg='#DCDCDC', text='')
	path_win_logo='res/BG_win_logo.jpg'
	image = Image.open(path_win_logo)
	img2 = ImageTk.PhotoImage(image)
	Label(FrameTitle, image=img2, bg='#DCDCDC').pack()
	FrameTitle.pack(side=TOP, fill=X)

def CheckCloseRoot(root_name):
	answer=mb.askyesno('Закрыть программу?', 'Вы действительно хотите закрыть программу? Не сохраненные действия возможно будут отменены в случае выхода!')
	if answer==True:
		root_name.destroy()


def WinHelp(help_text):
	help_window = Tk()
	help_window.title(win_name)#+' — Создание проекта')


	x = (help_window.winfo_screenwidth() - help_window.winfo_reqwidth()) / 3
	y = (help_window.winfo_screenheight() - help_window.winfo_reqheight()) / 6
	help_window.wm_geometry("+%d+%d" % (x, y))  

	help_window.geometry('900x700')
	help_window.resizable(True, True)
	help_window.iconbitmap(win_icon)
	help_window.configure(background=config.bg_color)
	help_window.focus_force()

	text = Text(help_window, bd=0, font=(config.low_font_name, config.low_font_size+2), wrap=WORD)
	text.pack(side=LEFT, fill=BOTH, expand=1)
	#text.focus()

	scrollY = Scrollbar(help_window, command=text.yview)
	scrollY.pack(side=RIGHT, fill=Y)  
	text.config(yscrollcommand=scrollY.set)

	text.insert(END, help_text)
	text.configure(state=DISABLED)

	help_window.mainloop()



root_name = Tk()
root_name.title(win_name)#+' — Создание проекта')

x = (root_name.winfo_screenwidth() - root_name.winfo_reqwidth()) / 3.2 # 3
y = (root_name.winfo_screenheight() - root_name.winfo_reqheight()) / 3.2 # 6
root_name.wm_geometry("+%d+%d" % (x, y))  

root_name.geometry(win_geometry)
root_name.resizable(win_draw, win_draw)
root_name.iconbitmap(win_icon)
root_name.configure(background=config.bg_color)

''' ШАБЛОН РЕДАКТОРА LTX ФАЙЛОВ

win_prj_info = Toplevel(root_name)
win_prj_info.title(win_name+' ➖ '+prj_name)
win_prj_info.resizable(win_draw, win_draw)
win_prj_info.iconbitmap(win_icon)
win_prj_info.geometry('700x500')

win_prj_info.focus_force()

FrameTitle = LabelFrame(win_prj_info, bg='#DCDCDC', text='')
FrameTitle.pack(side=TOP, fill=BOTH)

#Label(FrameTitle, text='S.T.A.L.K.E.R. LTX-Gen 2.0', font=('AmazS.T.A.L.K.E.R.v.3.0', config.font_size+20), bg='#DCDCDC').pack()
WinTitle(FrameTitle)

text_information = Text(win_prj_info, bd=1, font=(config.low_font_name, config.low_font_size-1), wrap=WORD, width=50, height=19)
text_information.pack(side=LEFT, expand=1, fill=BOTH)
#text.focus()

scrollY = Scrollbar(win_prj_info, command=text_information.yview)
scrollY.pack(side=RIGHT, fill=Y)  
text_information.config(yscrollcommand=scrollY.set)




win_prj_info.mainloop()'''

desc_file_text=''';тут содержится вся информация о проекте. 
;Файл используется ТОЛЬКО для демонстрации информации.
;Во избежании дизориентации крайне НЕ РЕКОМЕНДУЕТСЯ изменять данный файл, так как изменив характеристики здесь,
;вы НЕ ИЗМЕНИТЕ их в самой игре! Это важно понимать! Внося изменения в данный файл вручную вы автоматически берете
;на себя всю ответственность за работоспособность проекта.'''


root_name.title(win_name+' — '+prj_name) #(win_name+' ➖ '+prj_name)

#root_name, prj_name, sys_eat_name, text_coordinate_icons, eat_cost, inv_name_eat

########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################


class Outfit_loadDDSOGF(): # Outfit_loadDDSOGF.window(root_name, prj_name, status_fill) --------------

	def window(root_name, prj_name, status_fill):

		def GetSysNameOutfit():
			system_outfit_name=entry_system_outfit_name.get()
		    
			global memory
		    
			k=0
			alphabet='qwertyuiopasdfghjklzxcvbnm_1234567890'
			if system_outfit_name[0] not in alphabet:                
				mb.showerror(win_name, 'Первый символ в названии не является корректным!')
				k+=1
			else:
				for i in range(len(system_outfit_name)):
					if system_outfit_name[i] in alphabet or i==len(system_outfit_name)-1:
						k+=0
					else:
						k+=1
			#print(k)
			if k>0:
				mb.showerror(win_name, 'В названии есть некорректные символы! Введите название, состоящее из латинских букв, цифр и нижних подчеркиваний. Желательно, что бы название было очень коротким, так как игре будет легче обращатся к файлам с коротким названием.')
			elif k==0:
				#mb.showinfo(win_name, 'Системное имя {} успешно зарегестрировано!'.format(system_outfit_name))
				#btn_load_ogf.configure(state=NORMAL)
				btn_load_outfit_dds.configure(state=NORMAL)
				btn_load_outfit_dds.focus()
				return system_outfit_name


		def SELF_GetSysNameOutfit(self):
			GetSysNameOutfit()


		def Load_DDS_Outfit():

			def DELETE_FILES_Load_DDS_Outfit(file_list, rename_status):

				answer = mb.askyesno(win_name, 'Вы действительно хотите загрузить новые файлы?\n\nОбратите внимание, что уже загруженные файлы будут удалены!')

				if answer==True:
					if rename_status=='True':
						for i in range(0, len(file_list)):
							os.remove(dds_folder+file_list[i])

					elif rename_status=='False':
						for i in range(0, len(file_list)):
							os.remove(dds_folder+'act_{}.dds'.format(sys_outfit_name))

					btn_load_outfit_dds.configure(text='Загрузить...', width=w, command=Load_DDS_Outfit)
					Load_DDS_Outfit()


			try:
				path_dds = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ', filetypes=(("DDS files", "*.dds"), ("DDS files", "*.dds")))

				dds_folder = config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/act/'

				#print(os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/'))

				#print(len(os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/')))

				file_list=[]
				#if str(rename_status.get())=='False':

				# СОЗДАЕМ СПИСОК НАЗВАНИЙ ФАЙЛОВ, КОТОРЫЕ БУДЕМ КОПИРОВАТЬ В ПРОЕКТ, В БУДУЩЕМ ПО ЭТОМУ СПИКУ ЮЗЕР СМОЖЕТ ПЕРЕЗАГРУЗИТЬ ФАЙЛЫ В ЛЮБОМ СЛУЧАЕ
				for i in range(0, len(path_dds)):
					file_list.append(os.path.basename(path_dds[i]))

				#print(file_list)

				# ЕСЛИ ГАЛОЧКА СТОИТ, ТО ПРОСТО КОПИРУЕМ ТЕКСТУРЫ В ПРОЕКТ
				if str(rename_status.get())=='True':
					for i in range(0, len(path_dds)):					
						shutil.copy(path_dds[i], dds_folder)


				# ДЕЛАЕМ ПЕРЕИМЕНОВКУ, ЕСЛИ НЕ СТОИТ ГАЛОЧКА НА ОТКЛЮЧЕНИЕ ПЕРЕИМЕНОВКИ
				elif str(rename_status.get())=='False':
					for i in range(0, len(path_dds)):					
						shutil.copy(path_dds[i], dds_folder)
						#print('file_list[i] = '+file_list[i])
						#print('dds_folder+file_list[i] == '+dds_folder+file_list[i])

						if re.search(re.escape('_bump#'), file_list[i]): # переименовываем в зависимости от условий
							os.rename(dds_folder+file_list[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/act/act_{0}{1}.dds'.format(sys_outfit_name, '_bump#'))

						elif re.search(re.escape('_bump'), file_list[i]):
							os.rename(dds_folder+file_list[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/act/act_{0}{1}.dds'.format(sys_outfit_name, '_bump'))
						
						elif re.search(re.escape(''), file_list[i]):
							os.rename(dds_folder+file_list[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/act/act_{0}{1}.dds'.format(sys_outfit_name, ''))





				btn_load_outfit_dds.configure(width=20, text='{0} и др.'.format(os.path.basename(path_dds[0])), command=lambda: DELETE_FILES_Load_DDS_Outfit(file_list=file_list, rename_status=str(rename_status.get())))
				btn_load_ground_ogf.configure(state=NORMAL)
				btn_load_ground_ogf.focus()

				return path_dds
			except IndexError:
				mb.showerror(win_name, 'Файлы не были загружены!')

		def SELF_btn_load_outfit_dds(self):
			btn_load_outfit_dds()

		# СПИСОК, ИЗ КОТОРОГО ДОЛЖНЫ ПРОВОДИТСЯ ИСКЛЮЧЕНИЯ: ЕСЛИ ЗАГРУЖЕННЫЙ ФАЙЛ НЕ В СПИСКЕ ТО ПЕРЕИМЕНОВЫВАТЬ
		# ['act_himerr.dds', 'act_izlo1.dds', 'act_izlom.dds', 'act_izlom_bump#.dds', 'act_izlom_bump.dds', 'act_zombie_1.dds', 'act_zombie_1_bump#.dds', 'act_zombie_1_bump.dds', 'act_zombie_2.dds', 'act_zombie_2_bump#.dds', 'act_zombie_2_bump.dds', 'act_zombie_3.dds', 'act_zombie_4.dds', 'act_zombie_4_bump#.dds', 'act_zombie_4_bump.dds']

		def OGF_on_ground():

			def DELETE_FILES_OGF_on_ground(file_list):
				answer = mb.askyesno(win_name, 'Вы действительно хотите загрузить новые файлы?\n\nОбратите внимание, что уже загруженные файлы будут удалены!')

				if answer==True:
					for i in range(0, len(file_list)):
						os.remove(ogf_ground_folder+sys_outfit_name+'_suit.ogf')
					btn_load_ground_ogf.configure(width=w, text='Загрузить...', command=OGF_on_ground)
					OGF_on_ground()


			try:
				path_ogf = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ', filetypes=(("OGF files", "*.ogf"), ("OGF files", "*.ogf")))

				ogf_ground_folder = config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/equipments/'

				# ФОРМИРОВАНИЕ СПИСКА ФАЙЛОВ
				file_list=[]
				for i in range(0, len(path_ogf)):
					file_list.append(os.path.basename(path_ogf[i]))

				# КОПИРОВАНИЕ ФАЙЛОВ И ПЕРЕИМЕНОВКА ЕСЛИ ЗАГРУЖАЕТСЯ 1 ФАЙЛ
				if len(file_list)==1:
					for i in range(0, len(path_ogf)):					
						shutil.copy(path_ogf[i], ogf_ground_folder)
						os.rename(ogf_ground_folder+file_list[i], ogf_ground_folder+'{0}{1}'.format(sys_outfit_name, '_suit.ogf'))


					btn_load_ground_ogf.configure(width=20, text='{0}'.format(os.path.basename(path_ogf[0])), command=lambda: DELETE_FILES_OGF_on_ground(file_list))
					btn_load_player_ogf.configure(state=NORMAL)
					btn_load_player_ogf.focus()

				elif len(file_list)==1:
					mb.showerror(win_name, 'Нельзя загрузить файлы модели костюма, лежащего на земле в количестве '+str(len(file_list)))

				return path_ogf
			except IndexError:
				mb.showerror(win_name, 'Файлы не были загружены!')


		def OGF_on_player():

			def DELETE_FILES_OGF_on_player(file_list):				
				if answer==True:
					for i in range(0, len(file_list)):
						os.remove(ogf_ground_folder+file_list[i])
					btn_load_player_ogf.configure(width=w, text='Загрузить...', command=OGF_on_player)
					OGF_on_player()


			try:
				path_player_ogf = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ', filetypes=(("OGF files", "*.ogf"), ("OGF files", "*.ogf")))

				ogf_player_folder = config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/actors/hero/'

				# ФОРМИРОВАНИЕ СПИСКА ФАЙЛОВ
				file_list=[]
				for i in range(0, len(path_player_ogf)):
					file_list.append(os.path.basename(path_player_ogf[i]))

				# КОПИРОВАНИЕ ФАЙЛОВ И ПЕРЕИМЕНОВКА ЕСЛИ ЗАГРУЖАЕТСЯ 1 ФАЙЛ
				if len(file_list)==1:
					for i in range(0, len(path_player_ogf)):					
						shutil.copy(path_player_ogf[i], ogf_player_folder)
						os.rename(ogf_player_folder+file_list[i], ogf_player_folder+'stalker_{0}.ogf'.format(sys_outfit_name).format(sys_outfit_name))



					btn_load_player_ogf.configure(width=20, text='{0}'.format(os.path.basename(path_player_ogf[0])), command=lambda: DELETE_FILES_OGF_on_player(file_list))
				elif len(file_list)==1:
					mb.showerror(win_name, 'Нельзя загрузить файлы модели костюма, одетого на игроке в количестве '+str(len(file_list)))



				return path_player_ogf
			except IndexError:
				mb.showerror(win_name, 'Файлы не были загружены!')


		def Analyze(root_name, prj_name):
				try:
					FrameOutfitS1.pack_forget()
					Outfit_description_add.window(root_name=root_name, prj_name=prj_name, sys_outfit_name=sys_outfit_name)

				except Exception:
					mb.showerror(win_name, 'Произошла неизвестная ошибка!')
				#else:
					#mb.showerror(win_name, 'Проверьте количество загруженных файлов в программу! DDS-текстуры не больше 3-х файлов, OGF на земле и OGF на игроке не больше одного файла!')


		def Rediction_Function_Analyze():
			Analyze(root_name=root_name, prj_name=prj_name)



		FrameOutfitS1 = Frame(root_name, bg='#f0f0f0')

		#=========ОСНОВА==========
		w=20
		#-------------------------

		FrameLoadDDS = Frame(FrameOutfitS1)

		Frame_dds_load_outfit = Frame(FrameLoadDDS)
		Frame_dds_load_outfit.bind_all('<Return>', SELF_GetSysNameOutfit)

		Label(Frame_dds_load_outfit, text='Введите системное имя костюма   ', font=(config.font_name, config.font_size)).pack()
		#-----------
		entry_system_outfit_name=ttk.Entry(Frame_dds_load_outfit, width=w+15)
		entry_system_outfit_name.pack()
		entry_system_outfit_name.focus()

		ttk.Button(Frame_dds_load_outfit, text='Применить', width=20, command=GetSysNameOutfit).pack()

		Frame_dds_load_outfit.pack(side=LEFT, anchor=N)

		Frame_sys_name_outfit = Frame(FrameLoadDDS)

		Label(Frame_sys_name_outfit, text='   DDS-текстуры костюма', font=(config.font_name, config.font_size)).pack()
		#-----------
		btn_load_outfit_dds=ttk.Button(Frame_sys_name_outfit, text='Загрузить...', width=w, state=DISABLED, command=Load_DDS_Outfit)
		btn_load_outfit_dds.pack()
		#btn_load_outfit_dds.bind_all('<Return>', SELF_btn_load_outfit_dds)

		Frame_sys_name_outfit.pack(side=LEFT, anchor=N)


		#-----------
		FrameLoadDDS.pack()
		#-------------------------

		#-------------------------


		#-------------------------
		FrameLoadOGF = Frame(FrameOutfitS1)

		FrameOGF_suit_on_the_ground = Frame(FrameLoadOGF)
		Label(FrameOGF_suit_on_the_ground, text='\nOGF-файл лежащего на земле костюма   ', font=(config.font_name, config.font_size)).pack()

		btn_load_ground_ogf = ttk.Button(FrameOGF_suit_on_the_ground, text='Загрузить...', width=w, state=DISABLED, command=OGF_on_ground)
		btn_load_ground_ogf.pack()

		FrameOGF_suit_on_the_ground.pack(side=LEFT, anchor=N)




		FrameOGF_suit_on_the_player = Frame(FrameLoadOGF)

		Label(FrameOGF_suit_on_the_player, text='\n    OGF-файл надетого на игрока костюма', font=(config.font_name, config.font_size)).pack()

		btn_load_player_ogf = ttk.Button(FrameOGF_suit_on_the_player, text='Загрузить...', width=w, state=DISABLED, command=OGF_on_player)
		btn_load_player_ogf.pack()


		FrameOGF_suit_on_the_player.pack(side=LEFT, anchor=N)

		FrameLoadOGF.pack()
		#-------------------------

		#root_name.bind('F1', step3_help)

		Label(FrameOutfitS1, text=' ').pack()

		#Button(FrameOutfitS1, text='Для получения дополнительной информации нажмите сюда', bd=0, fg='blue').pack(side=TOP)

		rename_status = BooleanVar()
		rename_status.set(1)
		rename_status_widget = ttk.Checkbutton(FrameOutfitS1, text="Отключить переименование текстур", variable=rename_status, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 9), justify=LEFT)
		rename_status_widget.pack(side=TOP)

		Label(FrameOutfitS1, text=desc_outfit_step2, font=(config.low_font_name, config.low_font_size), justify=LEFT).pack()


		#=========================






		FrameBtn = LabelFrame(FrameOutfitS1, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=lambda: Analyze(root_name, prj_name), state=NORMAL).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameOutfitS1.pack(side=BOTTOM, fill=BOTH, expand=1)


Outfit_loadDDSOGF.window(root_name=root_name, prj_name=prj_name, status_fill=False)


root_name.mainloop()