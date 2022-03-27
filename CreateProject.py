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
#import PIL
from PIL import ImageTk
from PIL import Image


'''
RedirectionFunctions - перенаправляющие функции, написанные в файле config.py

, font=(config.font_name, config.font_size)
, font=(config.low_font_name, config.low_font_size)
, justify=LEFT


---------------ПОМОЖЕТ В ПОСЛЕДНЕМ СЛАЙДЕ (показ меню при клике правой кнопкой мыши)---------------
menu=Menu(tearoff=0)
menu.add_command(label="Очистить", command=delete_text)
WIDGET.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))
---------------------------------------------------------------------------------------------------

'''

#========КОНСТАНТЫ=============
win_icon='res'+chr(92)+'yellow.ico'
win_name='LTX-Gen'
win_draw=False
#win_geometry='700x420'   
# win_geometry='900x500' 
win_geometry='825x430'   
author_label='ταŋᶄắḽჯãṫ34 ©2020 - ver1.0'
simple_author_label='tankalxat34 ©2020 - ver1.0'
path_win_logo='res/BG_win_logo.jpg'

# СПИСОК ЭЛЕМЕНТОВ ПРОЕКТА
prj_elements=[]
#==============================


#img2 = ImageTk.PhotoImage(image=PIL.Image.fromarray(image))


#======ПОСТОЯННЫЕ ФУНКЦИИ======

def Otstup(widget):
	FrameOtstup = Frame(widget)
	Label(FrameOtstup, text=6*'  ').pack()
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
	path_logo = 'res/bg_win_logo.jpg'
	image_logo = Image.open(path_logo)
	loaded_image_logo = ImageTk.PhotoImage(image_logo)

	image = ImageTk.PhotoImage(file=path_logo)
	Label(root_name, image=image).pack()
	#Label(root_name, image=loaded_image_logo).pack()
	#Button(root_name, image=loaded_image_logo, bd=0).pack()

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

	text = Text(help_window, bd=0, font=(config.low_font_name, config.low_font_size+1), wrap=WORD)
	text.pack(side=LEFT, fill=BOTH, expand=1)
	#text.focus()

	scrollY = Scrollbar(help_window, command=text.yview)
	scrollY.pack(side=RIGHT, fill=Y)  
	text.config(yscrollcommand=scrollY.set)

	text.insert(END, help_text)
	text.configure(state=DISABLED)

	help_window.mainloop()


class ListSearch():
	def simple(string, lst):
		'''
		Функция ищет строку string в списке lst
		'''
		if string in lst:
			return 'True'
		elif string not in lst:
			return 'False'

	def hard(string, lst):
		'''
		Функция ищет строку string в списке lst, однако ищется только совпадение букв из целого слова
		'''
		k=0

		for element in lst:
			if re.search(re.escape(string), element)==True:
				k+=1
			elif re.search(re.escape(string), element)==False:
				k+=0

		if k==0:
			return False
		elif k!=0:
			return True



#==============================

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





#######################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################




# Eat_description_add.window(root_name=root_name, prj_name=prj_name, sys_eat_name=sys_eat_name)
# AddEatInTraiders.window(root_name=root_name, prj_name=prj_name, sys_outfit_name=sys_eat_name, inv_name_eat=inv_name_eat)
# AddEatParameters.window(root_name=root_name, prj_name=prj_name, sys_eat_name=sys_eat_name, text_coordinate_icons=outfit_icon_info.get(0.0, END), eat_cost=cost_outfit.get(), inv_name_eat=inv_name_eat)


class END_PROJECT_MENU(): # END_PROJECT_MENU.window(root_name, prj_name)
	def window(root_name, prj_name):				
		project_path=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/'
		PATH_project_info_ltx=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/project_info.inf'

		def BTN_PROJECT_INFORMATION():

			def CopyAllInformation():
				pyperclip.copy(insert_text)
				btn_copy_all.configure(text='Скопировано...   ', state=DISABLED)

			def SaveAllInformation():
				try:
					file_name = fd.asksaveasfilename(title=win_name+' ➖ сохранение информации о проекте...', filetypes=(("TXT files", "*.txt"), ("TXT files", "*.txt")))
					if file_name!='':
						f = open(file_name+'.txt', 'w')
						f.write(insert_text+simple_author_label)
						f.close()
						mb.showinfo(win_name, 'Описание успешно сохранено в '+file_name)
					elif file_name=='':
						mb.showerror(win_name, 'Описание не было сохранено!')
				except FileNotFoundError:
					mb.showerror(win_name, 'Описание не было сохранено!')
				



			if os.path.exists(PATH_project_info_ltx)==True:

				open_project_info_ltx = open(PATH_project_info_ltx, 'r') # получаем список строк из файла
				project_info_ltx = open_project_info_ltx.readlines()
				open_project_info_ltx.close()
				#===================НАЧИНАЕТСЯ АНАЛИЗ ФАЙЛА============================

				# СОЗДАЕМ СЧЕТЧИКИ
				global count; # ГЛАВНЫй СЧЕТЧИК
				count=0

				# СЧЕТЧИК КОСТЮМОВ
				outfit_count = 0

				# СЧЕТЧИК ОРУЖИЯ
				weapon_count = 0

				# СЧЕТЧИК ЕДЫ (медикаменты тоже интерпретируются как еда)
				eat_count = 0

				# начинаем считать количество бронекостюмов, оружия и еды в проекте путем нахождения нужных строчек
				for word in project_info_ltx:
					if re.search(re.escape('outfit_'), word):
						outfit_count+=1				
					elif re.search(re.escape('weapon_'), word):
						weapon_count+=1
					elif re.search(re.escape('eat_'), word):
						eat_count+=1

				win_prj_info = Toplevel(root_name)
				win_prj_info.title(win_name+' ➖ информация о '+prj_name)
				win_prj_info.resizable(win_draw, win_draw)
				win_prj_info.iconbitmap(win_icon)
				win_prj_info.geometry('700x500')

				win_prj_info.focus_force()


				# СОЗДАЕМ ТЕКСТОВОЕ ПОЛЕ И СКРОЛЛБАР В ОТДЕЛЬНОМ ВИДЖЕТЕ И РАСТЯГИВАЕМ ПО ВСЕМУ ОКНУ
				FrameTextWinget = Frame(win_prj_info)
				widget_text_information = Text(FrameTextWinget, bd=0, font=(config.low_font_name, config.low_font_size-1), wrap=WORD, width=50, height=19)
				widget_text_information.pack(side=LEFT, expand=1, fill=BOTH)
				#text.focus()

				scrollY = Scrollbar(FrameTextWinget, command=widget_text_information.yview)
				scrollY.pack(side=RIGHT, fill=Y)  
				widget_text_information.config(yscrollcommand=scrollY.set)
				FrameTextWinget.pack(expand=1, fill=BOTH)


				# СОЗДАЕМ ФРЕЙМ ВНИЗУ ОКНА И ДЕЛАЕМ КНОПКИ
				FrameBtn = LabelFrame(win_prj_info, bg='#DCDCDC', text='')
				btn_copy_all = ttk.Button(FrameBtn, text='Скопировать все', command=CopyAllInformation)
				btn_copy_all.pack(side=LEFT, anchor=N, expand=1, fill=X)
				ttk.Button(FrameBtn, text='Сохранить как...', command=SaveAllInformation).pack(side=LEFT, anchor=N, expand=1, fill=X)
				#ttk.Button(FrameBtn, text='Сохранить в проект как description.txt').pack(side=LEFT, anchor=N, expand=1, fill=X)
				FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)


				# СОЗДАЕМ ТЕКСТ С ИНФОЙ
				insert_text='''{data_time}
=========================================================================
		ИНФОРМАЦИЯ О ПРОЕКТЕ "{prj_name}"
=========================================================================

	Имя проекта: {prj_name};
	Дата создания проекта: {data_time};

=========================================================================
====================КОЛИЧЕСТВЕННАЯ ИНФОРМАЦИЯ=============================
=========================================================================

	Бронекостюмов в проекте: {c_outfit};
	Оружия в проекте: {c_weapon};
	Еды в проекте: {c_eat};

   ----------------------------
   |Всего предметов: {count} |
   ----------------------------

=========================================================================
			Спасибо за использование {win_name}!
'''.format(prj_name=prj_name, data_time=time.ctime(), c_outfit=str(outfit_count), c_weapon=str(weapon_count), c_eat=str(eat_count), count=str(outfit_count+weapon_count+eat_count),
	win_name=win_name, author_label=author_label)
				
				widget_text_information.insert(END, insert_text+author_label)
				widget_text_information.configure(state=DISABLED)

				win_prj_info.mainloop()

			else:
				mb.showerror(win_name, 'Проверьте наличие файла project_info.ltx по пути:\n\n'+PATH_project_info_ltx+'\n\nи снова повторите попытку!')





		# ФУНКЦИЯ ВЫЗЫВАЕТСЯ ПРИ НАЖАТИИ НА КОНКРЕТНЫЙ ПРЕДМЕТ В СПИСКЕ
		def GET_INFORMATION_ESSENCE():
			pass





		def ReloadListFromFile():
			#print(prj_name)
			if os.path.exists(PATH_project_info_ltx)==True:
				open_project_info_ltx = open(PATH_project_info_ltx, 'r') # получаем список строк из файла
				project_info_ltx = open_project_info_ltx.readlines()
				open_project_info_ltx.close()
				#===================НАЧИНАЕТСЯ АНАЛИЗ ФАЙЛА============================
				global essence_str;
				# начинаем считать количество бронекостюмов, оружия и еды в проекте путем нахождения нужных строчек
				for word in project_info_ltx:
					#print(word)
					if re.search(re.escape('eat_'), word) or re.search(re.escape('outfit_'), word) or re.search(re.escape('weapon_'), word):
						#print(word)
						#word=word.replase('\n', '')

						LTST_inv_essence_name = word.split('=')
						#print(LTST_inv_essence_name)
						inv_essence_name = LTST_inv_essence_name[1]
						#print(inv_essence_name)
						LIST_sys_essence_name = LTST_inv_essence_name[0].split('_')
						#print(LIST_sys_essence_name)
						if LIST_sys_essence_name[0]=='eat':
							essence_str = 'ТИП: еда | '
						elif LIST_sys_essence_name[0]=='outfit':
							essence_str = 'ТИП: броня | '
						elif LIST_sys_essence_name[0]=='weapon':
							essence_str = 'ТИП: оружие | '

						essence_str+='НАЗВАНИЕ: '+inv_essence_name+' | Системное имя: {}'.format(LIST_sys_essence_name[1])
						
						#print(len(essence_str))
						if essence_str not in prj_elements:
							prj_elements.append(essence_str)
						

				return prj_elements

			else:
				mb.showerror(win_name, 'Проверьте наличие файла project_info.ltx по пути:\n\n'+PATH_project_info_ltx+'\n\nи снова повторите попытку!')


		def RedirectionFunction_CreateProjectFolder_OUTFIT():
			Frame_END_SLIDE.pack_forget()
			Project_Registration_step1.window.RedirectionFunction_CreateProjectFolder_OUTFIT()



		def RedirectionFunction_AddEATSysNameDDSOGF():
			Frame_END_SLIDE.pack_forget()
			Project_Registration_step1.window.RedirectionFunction_AddEATSysNameDDSOGF()

		def RedirectionFunction_CreateProjectFolder_WEAPON():
			mb.showwarning(win_name, 'Раздел находится в разработке, не добавлен механизм многоразового использования цепочки!')

# Project_Registration_step1.window.RedirectionFunction_CreateProjectFolder_OUTFIT()
# Project_Registration_step1.window.RedirectionFunction_AddEATSysNameDDSOGF()
# Project_Registration_step1.window.RedirectionFunction_CreateProjectFolder_WEAPON()

		root_name.geometry('825x430')

		Frame_END_SLIDE = Frame(root_name, bg='#f0f0f0')

		ReloadListFromFile()

		#-----
		Label(Frame_END_SLIDE, text='Добавление новых предметов в проект "'+prj_name+'"', font=(config.font_name, config.font_size)).pack()
		ttk.Button(Frame_END_SLIDE, text='Информация о проекте...', width=30, command=BTN_PROJECT_INFORMATION).pack()


		Frame_All_Widgets = Frame(Frame_END_SLIDE)

		FrameListButtons = Frame(Frame_All_Widgets)
		w=30
		Label(FrameListButtons, text=' ').pack()
		#ttk.Button(FrameListButtons, text='\n➕ Добавить оружие\n', width=w, command=RedirectionFunction_CreateProjectFolder_WEAPON).pack()
		#ttk.Button(FrameListButtons, text='\n➕ Добавить бронекостюм\n', width=w, command=RedirectionFunction_CreateProjectFolder_OUTFIT).pack()
		#ttk.Button(FrameListButtons, text='\n➕ Добавить еду\n', width=w, command=RedirectionFunction_AddEATSysNameDDSOGF).pack()
		#ttk.Button(FrameListButtons, text='Показать больше...', width=w, state=DISABLED).pack()

		FrameListButtons.pack(side=LEFT, anchor=N)


		# ttk.Button(FrameListButtons, text='➕ Добавить оружие', width=w, command=lambda: Project_Registration_step1.RedirectionFunction_CreateProjectFolder_WEAPON(entry_project_name=prj_name, FrameS1=Frame_END_SLIDE, root=root_name, satus_fill=True)).pack()
		# ttk.Button(FrameListButtons, text='➕ Добавить бронекостюм', width=w, command=lambda:  Project_Registration_step1.RedirectionFunction_CreateProjectFolder_OUTFIT(entry_project_name=prj_name, FrameS1=Frame_END_SLIDE, root=root_name, satus_fill=True)).pack()
		# ttk.Button(FrameListButtons, text='➕ Добавить еду/медикамент', width=w, command=lambda:  Project_Registration_step1.RedirectionFunction_AddEATSysNameDDSOGF(entry_project_name=prj_name, FrameS1=Frame_END_SLIDE, root=root_name, satus_fill=True)).pack()
		# ttk.Button(FrameListButtons, text='Показать больше...', width=w).pack()

		ttk.Button(FrameListButtons, text='➕ Добавить оружие', width=w, command=lambda: Project_Registration_step1.RedirectionFunction_CreateProjectFolder_WEAPON(entry_project_name=prj_name, FrameS1=Frame_END_SLIDE, root=root_name, status_fill=True)).pack()
		ttk.Button(FrameListButtons, text='➕ Добавить бронекостюм', width=w, command=lambda:  Project_Registration_step1.RedirectionFunction_CreateProjectFolder_OUTFIT(entry_project_name=prj_name, FrameS1=Frame_END_SLIDE, root=root_name, status_fill=True)).pack()
		ttk.Button(FrameListButtons, text='➕ Добавить еду/медикамент', width=w, command=lambda:  Project_Registration_step1.RedirectionFunction_AddEATSysNameDDSOGF(entry_project_name=prj_name, FrameS1=Frame_END_SLIDE, root=root_name, status_fill=True)).pack()
		ttk.Button(FrameListButtons, text='Показать больше...', width=w).pack()




		###############
		Frame_Otstup = Frame(Frame_All_Widgets)
		Label(Frame_Otstup, text=' ').pack()
		Frame_Otstup.pack(side=LEFT, anchor=N)
		###############

		lb_width=70

		FrameComponentDemonstration = Frame(Frame_All_Widgets)
		Label(FrameComponentDemonstration, text='Содержимое проекта "{}":'.format(prj_name)).pack()
		GlobalListbox = Listbox(FrameComponentDemonstration, bd=0, highlightcolor='#87CEFA', width=lb_width, height=5+5+2)
		GlobalListbox.pack()
		for i in range(0, len(prj_elements)):
			GlobalListbox.insert(END, prj_elements[i])
		FrameComponentDemonstration.pack(side=LEFT, anchor=N)

		Frame_All_Widgets.pack()

		Label(Frame_END_SLIDE, text=desc_END_SLIDE, font=(config.low_font_name, config.low_font_size), justify=LEFT).pack()

		#-----
		FrameBtn = LabelFrame(Frame_END_SLIDE, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='<< ЗАВЕРШИТЬ ПРОЕКТ >>', width=26).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23, state=DISABLED).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		Frame_END_SLIDE.pack(side=BOTTOM, fill=BOTH, expand=1)






#######################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################
########################################ЕДА############################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################



# Eat_description_add.window(root_name=root_name, prj_name=prj_name, sys_eat_name=sys_eat_name)
# AddEatInTraiders.window(root_name=root_name, prj_name=prj_name, sys_outfit_name=sys_eat_name, inv_name_eat=inv_name_eat)
# AddEatParameters.window(root_name=root_name, prj_name=prj_name, sys_eat_name=sys_eat_name, text_coordinate_icons=outfit_icon_info.get(0.0, END), eat_cost=cost_outfit.get(), inv_name_eat=inv_name_eat)




class AddEatParameters():
	def window(root_name, prj_name, sys_eat_name, text_coordinate_icons, eat_cost, inv_name_eat):
		def is_digit(string):
			if string.isdigit():
				return True
			else:
				try:
					float(string)
					return True
				except ValueError:
					return False

		def Analyze():
			if (ENTRY_inv_eat_weight.get()!='' and ENTRY_inv_eat_weight.get()!='0' and '.' in ENTRY_inv_eat_weight.get()) and (ENTRY_eat_portions.get()!='' and ENTRY_eat_portions.get()!='0'):

				if is_digit(ENTRY_inv_eat_weight.get())==True and is_digit(ENTRY_eat_portions.get())==True:
					inv_weight = ENTRY_inv_eat_weight.get() # вес еды

					eat_portions_num = ENTRY_eat_portions.get() # кол-во порций

					eat_health = cb_eat_healt.get()
					eat_satiety = cb_eat_satiety.get()
					eat_power = cb_eat_power.get()
					eat_radiation = cb_eat_rad.get()
					wounds_heal_perc = cb_eat_wounds.get()
					eat_max_power = cb_eat_max_power.get()

					append_text=shablon_eat_text.format(sys_eat_name=sys_eat_name,
					inv_weight=inv_weight,
					text_coordinate_icons=text_coordinate_icons,
					cost=eat_cost,
					# характеристики
					eat_health=eat_health,
					eat_satiety=eat_satiety,
					eat_power=eat_power,
					eat_radiation=eat_radiation,
					wounds_heal_perc=wounds_heal_perc,
					eat_portions_num=eat_portions_num,
					eat_max_power=eat_max_power)

					path=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/items.ltx'
					if os.path.exists(path)==True:	
						f = open(path, 'a')
						f.write(append_text)
						f.close()



					elif os.path.exists(path)==False:						
						shutil.copy('res/default_configs/SoC/items.ltx', config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/')
						f = open(path, 'a')
						f.write(append_text)
						f.close()

					#--------------



					# ЗАПИСЫВАЕМ ИНФОРМАЦИЮ О ПРОЕКТЕ В ФАЙЛ project_info.ini (ПОТОМ БУДЕМ ДЕЛАТЬ В ui_ltx_gen_info.script)
					if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/project_info.inf')==False:
						f_info = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/project_info.inf', 'w')
						f_info.write(desc_file_text+'eat_{0} = {1}\n'.format(sys_eat_name, inv_name_eat))
						f_info.close()

					elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/project_info.inf')==True:
						f_info = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/project_info.inf', 'a')
						f_info.write('eat_{0} = {1}\n'.format(sys_eat_name, inv_name_eat))
						f_info.close()

					#prj_elements.append(inv_name_eat+' ({})'.format(sys_eat_name))
					#mb.showinfo(win_name, 'Запись успешно завершена! Переход на следующий шаг!')
					FrameAddEat_s4.pack_forget()
					END_PROJECT_MENU.window(root_name=root_name, prj_name=prj_name)





				else:
					mb.showerror(win_name, 'Не все данные коректно заполнены! Обратите внимание, для ввода дробных чисел используйте в качестве запятой точку! Так же, если вы вводите целое число, то нуль после точки ОБЯЗАТЕЛЬНО СТАВИТСЯ!')

			else:
				mb.showerror(win_name, 'Не все данные коректно заполнены! Обратите внимание, для ввода дробных чисел используйте в качестве запятой точку! Так же, если вы вводите целое число, то нуль после точки ОБЯЗАТЕЛЬНО СТАВИТСЯ!')




		FrameAddEat_s4 = Frame(root_name, bg='#f0f0f0')

		#-----


		shablon_eat_text='''


[{sys_eat_name}]:identity_immunities
GroupControlSection	= spawn_group
discovery_dependency = 
$spawn 				= "food and drugs\\{sys_eat_name}"
$prefetch 			= 8
class				= II_FOOD
cform				= skeleton
visual				= equipments\\{sys_eat_name}.ogf
description			= enc_equipment_food_{sys_eat_name}

inv_name			= {sys_eat_name}
inv_name_short		= {sys_eat_name}
inv_weight			= {inv_weight}


{text_coordinate_icons}

cost				= {cost}

attach_angle_offset		= 0.440521, 1.378287, -0.644026
attach_position_offset	= 0.104196, -0.010821, 0.076969
attach_bone_name		= bip01_r_hand
auto_attach				= false

// should be deleted after update
bone_name				= bip01_r_hand
position_offset			 = 0.0,0.0,0.0
angle_offset			 = 1.570790,1.570790,3.92699

; eatable item - эффекты после съедения
eat_health = {eat_health} ; пополнение здоровья
eat_satiety = {eat_satiety} ; уменьшение голода
eat_power = {eat_power} ; уменьшаение усталости
eat_radiation = {eat_radiation}	; уменьшение радиации
wounds_heal_perc = {wounds_heal_perc} ; заживление ран (лекарства)
eat_portions_num = {eat_portions_num} ; количество порций в упаковке (-1 по умолчанию - нет порций, сколько раз можно съесть 1 штуку)
eat_max_power		= {eat_max_power} ; мгновенное увеличение максимальной силы (хз что делает)

; food item
slot				= 4
animation_slot		= 4

;hud item
hud = wpn_vodka_hud'''


		FrameAllWidgets4 = Frame(FrameAddEat_s4)

		FrameInAllWidgets = Frame(FrameAllWidgets4)

		Label(FrameInAllWidgets, text='Добавьте характеристики "{}".\n'.format(inv_name_eat), font=(config.font_name, config.font_size)).pack()

		FrameDescEatS4 = Frame(FrameInAllWidgets)
		Label(FrameDescEatS4, text=desc_eat_s4, font=(config.low_font_name, config.low_font_size), justify=LEFT).pack()
		#Button(FrameDescEatS4, text='Для получения дополнительной информации нажмите сюда', fg='blue', bd=0).pack(side=BOTTOM)
		FrameDescEatS4.pack(side=BOTTOM, fill=X)

		# ttk.Separator(FrameInAllWidgets, orient='horizontal').pack(fill=BOTH, expand=1, side=TOP)

		# ttk.Separator(FrameInAllWidgets, orient='vertical').pack(fill=BOTH, expand=1, side=LEFT)



		for i in range(0, 100):
			nums=[]
			for i in range(0, 100):
				if len('0,'+str(i))<=3:
					nums.append('0.0{}'.format(str(i)))
				else:
					nums.append('0.'+str(i))

			for i in range(1, 100):
				if len('0,'+str(i))<=3:
					nums.append('-0.0{}'.format(str(i)))
				else:
					nums.append('-0.'+str(i))

		nums = sorted(nums)

		set_widget='0.00'



		FrameSideLeft = ttk.LabelFrame(FrameInAllWidgets, text='')

		FrameInvWeight = Frame(FrameSideLeft)
		Label(FrameInvWeight, text='Вес: ', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		ENTRY_inv_eat_weight = ttk.Entry(FrameInvWeight, width=3)
		ENTRY_inv_eat_weight.pack(side=LEFT, anchor=N)
		ENTRY_inv_eat_weight.focus()
		Label(FrameInvWeight, text=' кг.\n', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		FrameInvWeight.pack(anchor=W)

		FrameEatHealt = Frame(FrameSideLeft)
		Label(FrameEatHealt, text='Пополнение здоровья на: ', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		#ENTRY_eat_healt = ttk.Entry(FrameEatHealt, width=3)
		#ENTRY_eat_healt.pack(side=LEFT, anchor=N)
		cb_eat_healt =  ttk.Combobox(FrameEatHealt, values = nums, width=5, state="readonly")
		cb_eat_healt.pack(side=LEFT, anchor=N)
		cb_eat_healt.set(set_widget)
		Label(FrameEatHealt, text=' %\n', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		FrameEatHealt.pack(anchor=W)

		FrameEatSatiety = Frame(FrameSideLeft)
		Label(FrameEatSatiety, text='Уменьшение голода на: ', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		# ENTRY_eat_satiety = ttk.Entry(FrameEatSatiety, width=3)
		# ENTRY_eat_satiety.pack(side=LEFT, anchor=N)
		cb_eat_satiety =  ttk.Combobox(FrameEatSatiety, values = nums, width=5, state="readonly")
		cb_eat_satiety.pack(side=LEFT, anchor=N)
		cb_eat_satiety.set(set_widget)
		Label(FrameEatSatiety, text=' %\n', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		FrameEatSatiety.pack(anchor=W)

		FrameEatPower = Frame(FrameSideLeft)
		Label(FrameEatPower, text='Уменьшение усталости на: ', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		# ENTRY_eat_power = ttk.Entry(FrameEatPower, width=3)
		# ENTRY_eat_power.pack(side=LEFT, anchor=N)
		cb_eat_power =  ttk.Combobox(FrameEatPower, values = nums, width=5, state="readonly")
		cb_eat_power.pack(side=LEFT, anchor=N)
		cb_eat_power.set(set_widget)
		Label(FrameEatPower, text=' %\n', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		FrameEatPower.pack(anchor=W)

		FrameSideLeft.pack(side=LEFT, anchor=N)

		# ttk.Separator(FrameInAllWidgets, orient='horizontal').pack(fill=BOTH, expand=1, side=BOTTOM)

		#---------------------

		# ttk.Separator(FrameInAllWidgets, orient='vertical').pack(fill=BOTH, expand=1, side=LEFT)

		FrameSideRight = ttk.LabelFrame(FrameInAllWidgets, text='')


		FrameEatRad = Frame(FrameSideRight)
		Label(FrameEatRad, text='Уменьшение радиации на: ', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		# ENTRY_eat_rad = ttk.Entry(FrameEatRad, width=3)
		# ENTRY_eat_rad.pack(side=LEFT, anchor=N)
		cb_eat_rad =  ttk.Combobox(FrameEatRad, values = nums, width=5, state="readonly")
		cb_eat_rad.pack(side=LEFT, anchor=N)
		cb_eat_rad.set(set_widget)
		Label(FrameEatRad, text=' %\n', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		FrameEatRad.pack(anchor=W)


		FrameEatWounds = Frame(FrameSideRight)
		Label(FrameEatWounds, text='Заживление ран на: ', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		# ENTRY_eat_wounds = ttk.Entry(FrameEatWounds, width=3)
		# ENTRY_eat_wounds.pack(side=LEFT, anchor=N)
		cb_eat_wounds =  ttk.Combobox(FrameEatWounds, values = nums, width=5, state="readonly")
		cb_eat_wounds.pack(side=LEFT, anchor=N)
		cb_eat_wounds.set(set_widget)
		Label(FrameEatWounds, text=' %\n', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		FrameEatWounds.pack(anchor=W)

		FrameEatPortions = Frame(FrameSideRight)
		Label(FrameEatPortions, text='Количество порций: ', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		ENTRY_eat_portions = ttk.Entry(FrameEatPortions, width=3)
		ENTRY_eat_portions.pack(side=LEFT, anchor=N)
		Label(FrameEatPortions, text=' шт.\n', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		FrameEatPortions.pack(anchor=W)

		FrameEatMaxPower = Frame(FrameSideRight)
		Label(FrameEatMaxPower, text='Максимальная энергия: ', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		# ENTRY_eat_max_power = ttk.Entry(FrameEatMaxPower, width=3)
		# ENTRY_eat_max_power.pack(side=LEFT, anchor=N)
		cb_eat_max_power =  ttk.Combobox(FrameEatMaxPower, values = nums, width=5, state="readonly")
		cb_eat_max_power.pack(side=LEFT, anchor=N)
		cb_eat_max_power.set(set_widget)
		Label(FrameEatMaxPower, text=' %\n', font=(config.low_font_name, config.low_font_size), justify=LEFT).pack(side=LEFT, anchor=N)
		FrameEatMaxPower.pack(anchor=W)
		FrameSideRight.pack(side=RIGHT, anchor=N)

		# ttk.Separator(FrameInAllWidgets, orient='horizontal').pack(fill=BOTH, expand=1, side=BOTTOM)

		Label(FrameInAllWidgets, text=' ').pack()

		FrameInAllWidgets.pack(side=LEFT, anchor=N)



		FrameAllWidgets4.pack(expand=1, fill=Y)

		#-----
		FrameBtn = LabelFrame(FrameAddEat_s4, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=Analyze).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameAddEat_s4.pack(side=BOTTOM, fill=BOTH, expand=1)






















class AddEatInTraiders():
	def window(root_name, prj_name, sys_eat_name, inv_name_eat):
		
		def InsertOutfitIcon():
			#print(str(pyperclip.paste()))
			outfit_icon_info.delete(0.0, END)
			outfit_icon_info.insert(END, str(pyperclip.paste()))

		def SELF_InsertOutfitIcon(self):
			InsertWpnIcon()

		def InsertRecommendParams():
			entry_minimum_purchase_price.delete(0, END)
			entry_maximum_purchase_price.delete(0, END)
			entry_number.delete(0, END)
			entry_chance.delete(0, END)
			entry_minimum_sale_price.delete(0, END)
			entry_maximum_sale_price.delete(0, END)


			entry_maximum_purchase_price.insert(END, '0.5')
			entry_minimum_purchase_price.insert(END, '0.7')
			entry_number.insert(END, '4')
			entry_chance.insert(END, '0.5')
			entry_minimum_sale_price.insert(END, '1')
			entry_maximum_sale_price.insert(END, '2')

		def ClickAllTraider():
			def DeletedAllTraiders():
				cvar1.set(0)
				cvar2.set(0)
				cvar3.set(0)
				cvar4.set(0)
				cvar5.set(0)
				btn_click_all.configure(text='Отметить всех', command=ClickAllTraider)



			cvar1.set(1)
			cvar2.set(1)
			cvar3.set(1)
			cvar4.set(1)
			cvar5.set(1)
			btn_click_all.configure(text='Убрать всех', command=DeletedAllTraiders)


		def is_digit(string):
			if string.isdigit():
				return True
			else:
				try:
					float(string)
					return True
				except ValueError:
					return False



		def Analyze():
			sys_name=sys_eat_name

			if cost_outfit.get()!='' and (cost_outfit.get()).isdigit()==True and cost_outfit.get()!='0' and len(outfit_icon_info.get(0.0, END))>=3 and outfit_icon_info.get(0.0, END)!='':
				#print('OK')
				count_errors=0
				######################
				if is_digit(cost_outfit.get())==True:
					if int(cost_outfit.get())>=1:
						outfit_cost=cost_outfit.get()
					else:
						count_errors+=1
					#print(weapon_cost.get())
				else:
					count_errors+=1
				#####################
				if is_digit(entry_minimum_purchase_price.get())==True and is_digit(entry_maximum_purchase_price.get())==True:
					line_trader_generic_buy = '{0} = {1}, {2}\n'.format(sys_name, str(entry_minimum_purchase_price.get()), str(entry_maximum_purchase_price.get()))
				else:
					count_errors+=1
				######################
				if is_digit(entry_number.get())==True and is_digit(entry_chance.get())==True:
					line_supplies_start = '{0} = {1}, {2}\n'.format(sys_name, str(entry_number.get()), str(entry_chance.get()))
				else:
					count_errors+=1
				######################
				if is_digit(entry_minimum_sale_price.get())==True and is_digit(entry_maximum_sale_price.get())==True:
					line_trader_start_sell = '{0} = {1}, {2}\n'.format(sys_name, str(entry_minimum_sale_price.get()), str(entry_maximum_sale_price.get()))
				else:
					count_errors+=1
				######################
				if count_errors>=1:
					mb.showerror(win_name, 'Не все данные корректно заполнены! Проверьте заполнение формы!\n\nОБРАТИТЕ ВНИМАНИЕ!\n- Должен быть выбран хотя бы один торговец и настроены параметры этого оружия!\n- Боеприпасы должны быть в любом случае выбраны!')
				elif count_errors==0:
					#print(weapon_cost.get())

					project_name=prj_name
					
					sidor_status=str(cvar1.get())
					barman_status=str(cvar2.get())
					sakharov_status=str(cvar3.get())
					dolg_status=str(cvar4.get())
					freedom_status=str(cvar5.get())
					'''
					print(sidor_status)
					print(barman_status)
					print(sakharov_status)
					print(dolg_status)
					print(freedom_status)
					'''
					#№№№№№№№№№№№№№№№№№				
					if install_status.get()==True and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script')==False:
						#setup_naxac=install_status.get()
						#print('Добавление спавн-меню в проект...')
						shutil.unpack_archive(filename='res/default_configs/SoC/naxac.zip', extract_dir=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/')

						if add_status.get()==True:
							#dd_wpn_in_naxac
							#print('Выполняется условие 1')

							f_ui_cheat_naxac_script=open('res/default_configs/SoC/ui_cheat_naxac.script', 'r')
							lines=f_ui_cheat_naxac_script.readlines()
							f_ui_cheat_naxac_script.close()

							f_ui_cheat_naxac_script=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script', 'w')
							for word in lines:
								'''
								if re.search(re.escape('--items'), word):
									word = '--items\n	{"*** LTX-Gen eats ***",\n'
									f_ui_cheat_naxac_script.write(word)
								elif re.search(re.escape('"*** Артефакты ***"'), word):
									word = '	"'+sys_eat_name+'",\n	"*** Артефакты ***",\n'
									f_ui_cheat_naxac_script.write(word)
								'''
								if re.search(re.escape('--items'), word):
									new_word='--items\n    {'+'"*** LTX-Gen eats ***",\n    "{}",\n'.format(sys_eat_name)
									f_ui_cheat_naxac_script.write(word.replace(word, new_word))

								elif re.search(re.escape('"*** Артефакты ***"'), word):
									new_word='    "*** Артефакты ***",\n'
									f_ui_cheat_naxac_script.write(word.replace(word, new_word))

								else:
									f_ui_cheat_naxac_script.write(word)

					elif install_status.get()==True and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script')==True:
						if add_status.get()==True:
							#dd_wpn_in_naxac
							
							f_ui_cheat_naxac_script=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script', 'r')
							lines=f_ui_cheat_naxac_script.readlines()
							f_ui_cheat_naxac_script.close()

							f_ui_cheat_naxac_script=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script', 'w')

							'''
							if re.search(re.escape('"*** LTX-Gen eats ***"'), word):

								lines.insert(lines.index(word)+1, '	"'+sys_eat_name+'",\n')
								new_word = lines[lines.index(word)]
								f_ui_cheat_naxac_script.write(new_word)	'''


							title_section = '    {"*** LTX-Gen eats ***",\n'

							result = ListSearch.hard('"*** LTX-Gen eats ***"', lines)

							if result==True:
								for word in lines:
									if re.search(re.escape('"*** LTX-Gen eats ***"'), word):
										lines.insert(lines.index(word)+1, '    "{}",\n'.format(sys_eat_name))
										word = lines[lines.index(word)]
										f_ui_cheat_naxac_script.write(word)
									else:
										f_ui_cheat_naxac_script.write(word)
							elif result==False:
								for word in lines:
									if re.search(re.escape('--items'), word):
										lines.insert(lines.index(word)+1, title_section+'    "{}",\n'.format(sys_eat_name))
										word = lines[lines.index(word)]
										f_ui_cheat_naxac_script.write(word)
									else:
										f_ui_cheat_naxac_script.write(word)


							f_ui_cheat_naxac_script.close()

					elif install_status.get()==False and add_status.get()==False:
						shutil.copy('res/default_configs/SoC/ui_main_menu.script', config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/')
					#№№№№№№№№№№№№№№№№№

					copy_file=''

					k=0

					# line_trader_generic_buy | line_supplies_start | line_trader_start_sell

					#=================СИДОРОВИЧ=========================================
					#ltx_gen_section = '' #';LTX-Gen section\n'
					if sidor_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_trader.ltx')==False:
						copy_file='trade_trader.ltx'

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[trader_generic_buy]'), word):
								word = '[trader_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_fabric]'), word):
								word = '[supplies_after_fabric]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[trader_start_sell]'), word):
								word = '[trader_start_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[trader_after_fabric_sell]'), word):
								word = '[trader_after_fabric_sell]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()


					elif sidor_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_trader.ltx')==True:
						copy_file='trade_trader.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[trader_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_fabric]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[trader_start_sell]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[trader_after_fabric_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()
						
					    
					#===================================================================

					
					#=================БАРМЕН============================================
					# line_trader_generic_buy | line_supplies_start | line_trader_start_sell

					if barman_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_barman.ltx')==False:                
						copy_file='trade_barman.ltx'

						shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[barman_generic_buy]'), word):
								word = '[barman_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_darkvalley]'), word):
								word = '[supplies_after_darkvalley]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_brain]'), word):
								word = '[supplies_after_brain]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[barman_start_sell]'), word):
								word = '[barman_start_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[barman_after_darkvalley_sell]'), word):
								word = '[barman_after_darkvalley_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[barman_after_brain_sell]'), word):
								word = '[barman_after_brain_sell]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()

					elif barman_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_barman.ltx')==True:
						copy_file='trade_barman.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[barman_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_darkvalley]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_brain]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[barman_start_sell]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[barman_after_darkvalley_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[barman_after_brain_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()

					    
					#===================================================================


					#=====================ПЕТРЕНКО======================================
					# line_trader_generic_buy | line_supplies_start | line_trader_start_sell
					if dolg_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_dolg.ltx')==False:                
						copy_file='trade_dolg.ltx'

						shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[dolg_generic_buy]'), word):
								word = '[dolg_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_rg6]'), word):
								word = '[supplies_after_rg6]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[dolg_start_sell]'), word):
								word = '[dolg_start_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[dolg_after_rg6_sell]'), word):
								word = '[dolg_after_rg6_sell]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()

					elif dolg_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_dolg.ltx')==True:
						copy_file='trade_dolg.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[dolg_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_rg6]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[dolg_start_sell]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[dolg_after_rg6_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()
					                    
					#elif barman_status=='False':
						#k+=1                    

					#===================================================================



					#=====================САХАРОВ======================================
					# line_trader_generic_buy | line_supplies_start | line_trader_start_sell
					if sakharov_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_ecolog.ltx')==False:                
						copy_file='trade_ecolog.ltx'

						shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[ecolog_generic_buy]'), word):
								word = '[ecolog_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_brain]'), word):
								word = '[supplies_after_brain]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[ecolog_start_sell]'), word):
								word = '[ecolog_start_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[ecolog_after_brain_sell]'), word):
								word = '[ecolog_after_brain_sell]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()

					elif sakharov_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_ecolog.ltx')==True:
						copy_file='trade_ecolog.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[ecolog_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_brain]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[ecolog_start_sell]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[ecolog_after_brain_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()
						                    
					#elif sakharov_status=='False':
						#k+=1                    

					#===================================================================            


					#=====================СКРЯГА========================================
					if freedom_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_freedom.ltx')==False:                
						copy_file='trade_freedom.ltx'

						shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[freedom_generic_buy]'), word):
								word = '[freedom_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_dolg]'), word):
								word = '[supplies_after_dolg]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_pavlik]'), word):
								word = '[supplies_after_pavlik]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[freedom_sell_start]'), word):
								word = '[freedom_sell_start]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[freedom_sell_after_dolg]'), word):
								word = '[freedom_sell_after_dolg]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[freedom_sell_after_pavlik]'), word):
								word = '[freedom_sell_after_pavlik]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()

					elif freedom_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_freedom.ltx')==True:
						copy_file='trade_freedom.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[freedom_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_dolg]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_pavlik]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[freedom_sell_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[freedom_sell_after_dolg]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell) 
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[freedom_sell_after_pavlik]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()
					                        
					#elif freedom_status=='False':
						#k+=1  
					
					
					#print('Координаты иконки:\n'+outfit_icon_info.get(0.0, END))

					#print('Цена: {} рублей'.format(outfit_cost))

					#print('ВСЕ ГОТОВО\nПЕРЕХОД НА СЛЕДУЮЩИЙ ШАГ!!!')
					FrameAddEat_s3.pack_forget()
					AddEatParameters.window(root_name=root_name, prj_name=prj_name, sys_eat_name=sys_eat_name, text_coordinate_icons=outfit_icon_info.get(0.0, END), eat_cost=cost_outfit.get(), inv_name_eat=inv_name_eat)

			else:
				mb.showerror(win_name, '''Не все поля были заполнены! Проверьте заполнение еще раз!

		Цена не должна быть равна 0 (минимально 1).

		Координаты иконки должны быть внесены в специальном поле в любом случае, даже если иконка не задана.

		Еда может быть добавлена или в спавн-меню или любому торговцу, или в оба места. Можно выбрать всех торговцев.''')













		def AddClassicEatsIcon():


			def ReloadIcon():
				new_icon=(cb_add_text.get()).replace('\n', '')

				#print(new_icon)

				coordinate_icons='*'

				path=(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/ui_icon_equipment.dds') #'res/default_ui/ui_icon_equipment.dds'
		#		image = Image.open(path)
				
				if new_icon=='NO ICON':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((450, 1350, 600, 1450)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 3
inv_grid_height    = 2
inv_grid_x         = 9
inv_grid_y         = 27'''
				
				elif new_icon=='Антирадиационные препараты':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((900, 600, 950, 650)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 1
inv_grid_height    = 1
inv_grid_x         = 18
inv_grid_y         = 12'''

				elif new_icon=='Колбаса':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((950, 600, 1000, 650)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 1
inv_grid_height    = 1
inv_grid_x         = 19
inv_grid_y         = 12'''

				elif new_icon=='Энергетик NonStop':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((950, 350, 1000, 400)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 1
inv_grid_height    = 1
inv_grid_x         = 19
inv_grid_y         = 7'''

				elif new_icon=='Coca Cola':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((400, 1850, 450, 1900)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 1
inv_grid_height    = 1
inv_grid_x         = 8
inv_grid_y         = 37'''
				

				else:
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((450, 1350, 600, 1450)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 3
inv_grid_height    = 2
inv_grid_x         = 9
inv_grid_y         = 27'''
				
				pyperclip.copy(coordinate_icons)

			def SELF_ReloadIcon(self):
				ReloadIcon()

			def CloseInsert():
				#wpn_icon_text=ReloadIcon()
				#pyperclip.copy(wpn_icon_text)
				#ReloadIcon()
				win_shbl.destroy()
				outfit_icon_info.delete(0.0, END)
				outfit_icon_info.insert(END, pyperclip.paste())

			def SELF_CloseInsert(self):
				CloseInsert()

			win_shbl = Toplevel(root_name)
			win_shbl.title(win_name+' - выбор иконки еды')
			win_shbl.resizable(win_draw, win_draw)
			win_shbl.iconbitmap(win_icon)
			win_shbl.geometry('700x400')

			win_shbl.focus_force()

			#win_shbl.protocol('WM_DELETE_WINDOW', CloseInsert)


			#f_string_table_enc_weapons_xml=open('res/default_configs/SoC/string_table_enc_equipment.xml', 'r')
			#string_table_enc_weapons_xml=f_string_table_enc_weapons_xml.readlines()
			#f_string_table_enc_weapons_xml.close()

			name_items=['Антирадиационные препараты',
			'Колбаса',
			'Энергетик NonStop',
			'Coca Cola',
			'NO ICON']	



			#Label(FrameTitle, text='S.T.A.L.K.E.R. LTX-Gen 2.0', font=('AmazS.T.A.L.K.E.R.v.3.0', config.font_size+20), bg='#DCDCDC').pack()



			FrameOutfitIconDemonstration = Frame(win_shbl, bg='#f0f0f0')

			FrameSmallTitle1 = Frame(FrameOutfitIconDemonstration)
			Label(FrameSmallTitle1, text='Демонстрируемая иконка', font=(config.font_name, config.font_size)).pack(side=LEFT, anchor=N)
			#Button(FrameSmallTitle1, text='↺', font=(config.font_name, config.font_size), bd=0, fg='blue', command=ReloadIcon).pack(side=LEFT, anchor=N)
			FrameSmallTitle1.pack(side=TOP)



			#img = ImageTk.PhotoImage(Image.open(config.folder_projects+'/'+prj_name+'/gamedata/textures/ui/ui_icon_equipment.dds'))
			#img = ImageTk.PhotoImage(Image.open('res/default_ui/ui_icon_equipment_jpg.jpg'))
			 
			panel_1=Label(FrameOutfitIconDemonstration, bg='#A0522D', width=120, height=150)
			panel_1.pack()

			Label(FrameOutfitIconDemonstration, text='Выберите еду, иконоку которой хотите использовать', font=(config.font_name, config.font_size)).pack(side=TOP, anchor=N)
			Label(FrameOutfitIconDemonstration, text='Для обновления иконки в окне нажмите клавишу F5\nДля выбора иконки выберите ее и нажмите Enter', font=('Verdana', config.low_font_size)).pack()
			#Label(FrameOutfitIconDemonstration, text='Обратите внимание, иконки пистолетов выбираются через SIE.exe!', font=('Verdana', config.low_font_size), fg='red').pack()
			#reload_btn = Button(FrameWpnIconDemonstration, text='↺', font=(config.font_name, config.font_size), bd=0, fg='blue', command=ReloadIcon)
			#reload_btn.pack(side=TOP, anchor=N)


			cb_add_text=ttk.Combobox(FrameOutfitIconDemonstration, values = name_items, width=30, height=20, state="readonly")
			cb_add_text.pack(side=TOP, anchor=N)
			cb_add_text.set(name_items[len(name_items)-1])

			Label(FrameOutfitIconDemonstration, text=' ').pack()
			# Label(FrameOutfitIconDemonstration, text='Автор программы добавил множество других иконок, но поленился их добавить сюда!', font=('Verdana', config.low_font_size), fg='red').pack()

			ttk.Button(FrameOutfitIconDemonstration, text='Применить и закрыть окно', width=35, command=CloseInsert).pack()
			
			win_shbl.bind_all('<F5>', SELF_ReloadIcon)
			win_shbl.bind_all('<Return>', SELF_CloseInsert)

			FrameOutfitIconDemonstration.pack(fill=BOTH, expand=1, side=TOP, anchor=NW)

			eat_icon_text=ReloadIcon()

			win_shbl.mainloop()










		def OpenSIE():
			project_name=prj_name
			#root_name.destroy()
			root_name.withdraw()
			os.system("sie.exe "+config.folder_projects+"/"+config.folder_projects_soc+'/'+project_name+"/gamedata/textures/ui/ui_icon_equipment.dds")
			root_name.deiconify()




		sys_name=sys_eat_name



		FrameAddEat_s3 = Frame(root_name, bg='#f0f0f0')
		#-----


		Label(FrameAddEat_s3, text='Введите цену новой еды.', font=(config.font_name, config.font_size)).pack()

		cost_outfit = ttk.Entry(FrameAddEat_s3, width=35)
		cost_outfit.pack()
		cost_outfit.focus()

		##########

		FrameAllWidgtsOutfit = Frame(FrameAddEat_s3)

		FrameAddSpawnMenu = Frame(FrameAllWidgtsOutfit)

		Label(FrameAddSpawnMenu, text='Добавление еды в spawn-menu', font=(config.font_name, config.font_size)).pack()
		#Label(FrameAddSpawnMenu, text=' ').pack()

		FrameCheckbuttons_naxac = Frame(FrameAddSpawnMenu)

		install_status = BooleanVar()
		install_status.set(1)
		install_spawn_menu = ttk.Checkbutton(FrameCheckbuttons_naxac, text="Установить spawn-menu by naxaс\nс денежным трейнером tankalxat34.", variable=install_status, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 9), justify=LEFT)
		install_spawn_menu.pack(anchor=W)
		        
		add_status = BooleanVar()
		add_status.set(1)
		add_outfit_in_spawn_menu = ttk.Checkbutton(FrameCheckbuttons_naxac, text="Добавить еду в данное spawn-menu.", variable=add_status, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 9), justify=LEFT)
		add_outfit_in_spawn_menu.pack(anchor=W)

		FrameCheckbuttons_naxac.pack()

		Button(FrameAddSpawnMenu, text='Для получения дополнительной\nинформации нажмите сюда', fg='blue', bd=0, command=step5_help_naxac_eat).pack()
		Label(FrameAddSpawnMenu, text='Некоторые иконки невозможны для быстрой вставки\n(автор ленивый), добавьте их вручную! Если не знаете\nкак это сделать, читайте руководство по кнопке выше!', font=('Verdana', config.low_font_size-3), fg='red').pack()

		######

		Label(FrameAddSpawnMenu, text='Добавление иконки еды', font=(config.font_name, config.font_size)).pack()


		FrameBtns = Frame(FrameAddSpawnMenu)
		w=35
		ttk.Button(FrameBtns, text='Открыть шаблон в SIE.exe', command=OpenSIE, width=w).pack(side=TOP, anchor=N)
		ttk.Button(FrameBtns, text='Выбрать классическую иконку', width=w, command=AddClassicEatsIcon).pack(side=BOTTOM, anchor=N)
		FrameBtns.pack()

		Label(FrameAddSpawnMenu, text='Вставьте сюда координаты иконки', font=('Verdana', config.low_font_size)).pack()

		#insert_text=wpn_icon_text


		outfit_icon_info = Text(FrameAddSpawnMenu, bd=1, font=(config.low_font_name, config.low_font_size-1), wrap=WORD, width=25, height=4)
		outfit_icon_info.pack(side=BOTTOM)

		Button(FrameAddSpawnMenu, text='[Вставить]', bd=0, fg='blue', command=InsertOutfitIcon).pack(side=BOTTOM)

		FrameAddSpawnMenu.pack(side=LEFT, expand=1, anchor=N)
		#Label(FrameAllWidgtsOutfit, text='Вставьте сюда координаты иконки', font=('Verdana', config.low_font_size)).pack()
		##########



		FrameListTraiders = Frame(FrameAllWidgtsOutfit)

		Label(FrameListTraiders, text='\n\nВыберете торговцев, которым\nхотите добавить новую еду.', font=(config.font_name, config.font_size)).pack()


		FrameCheckbuttonsTraider = Frame(FrameListTraiders)

		cvar1 = BooleanVar()
		cvar1.set(0)
		c1 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Сидорович", variable=cvar1, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c1.pack(anchor=W)
				        
		cvar2 = BooleanVar()
		cvar2.set(0)
		c2 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Бармен", variable=cvar2, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c2.pack(anchor=W)
				        
		cvar3 = BooleanVar()
		cvar3.set(0)
		c3 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Сахаров", variable=cvar3, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c3.pack(anchor=W)
				        
		cvar4 = BooleanVar()
		cvar4.set(0)
		c4 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Петренко", variable=cvar4, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c4.pack(anchor=W)
				        
		cvar5 = BooleanVar()
		cvar5.set(0)
		c5 =ttk.Checkbutton(FrameCheckbuttonsTraider, text="Скряга", variable=cvar5, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c5.pack(anchor=W)

		FrameCheckbuttonsTraider.pack()

		btn_click_all=ttk.Button(FrameListTraiders, text='Отметить всех', width=20, command=ClickAllTraider)
		btn_click_all.pack()



		FrameListTraiders.pack(side=LEFT, fill=Y, expand=1, anchor=S)




		FrameParamsInTraiders = Frame(FrameAllWidgtsOutfit)

		Label(FrameParamsInTraiders, text='Настройте параметры продажи', font=(config.font_name, config.font_size)).pack()

		Button(FrameParamsInTraiders, text='Для получения дополнительной\nинформации нажмите сюда', fg='blue', bd=0, command=step5_help).pack()

		Label(FrameParamsInTraiders, text='Секция [trader_generic_buy]\n({0} = {2} {1})'.format(sys_name, 'минимальная цена покупки %', 'максимальная цена покупки %,\n'), font=(config.font_name, config.low_font_size)).pack()

		####--                           trader_generic_buy
		Frame_trader_generic_buy = Frame(FrameParamsInTraiders)
		Label(Frame_trader_generic_buy, text='{}  ='.format(sys_name), font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)#'Минимальная цена покупки (%):', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		Label(Frame_trader_generic_buy, text=' ').pack(side=LEFT, anchor=N)

		entry_minimum_purchase_price=ttk.Entry(Frame_trader_generic_buy, width=10)
		entry_minimum_purchase_price.pack(side=LEFT, anchor=N)

		Label(Frame_trader_generic_buy, text=',', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)

		entry_maximum_purchase_price=ttk.Entry(Frame_trader_generic_buy, width=10)
		entry_maximum_purchase_price.pack(side=LEFT, anchor=N)
		Frame_trader_generic_buy.pack()




		Label(FrameParamsInTraiders, text='Секция [supplies_start]\n({0} = {1}, {2})'.format(sys_name, 'количество', 'вероятность появления'), font=(config.font_name, config.low_font_size)).pack()

		#  supplies_start
		Frame_supplies_start = Frame(FrameParamsInTraiders)
		Label(Frame_supplies_start, text='{}  ='.format(sys_name), font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)#'Минимальная цена покупки (%):', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		Label(Frame_supplies_start, text=' ').pack(side=LEFT, anchor=N)

		entry_number=ttk.Entry(Frame_supplies_start, width=10)
		entry_number.pack(side=LEFT, anchor=N)

		Label(Frame_supplies_start, text=',', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)

		entry_chance=ttk.Entry(Frame_supplies_start, width=10)
		entry_chance.pack(side=LEFT, anchor=N)
		Frame_supplies_start.pack()




		Label(FrameParamsInTraiders, text='Секция [trader_start_sell]\n({0} = {1} {2})'.format(sys_name, 'минимальная цена продажи,\n', 'максимальная цена продажи'), font=(config.font_name, config.low_font_size)).pack()

		#  supplies_start
		Frame_trader_start_sell = Frame(FrameParamsInTraiders)
		Label(Frame_trader_start_sell, text='{}  ='.format(sys_name), font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)#'Минимальная цена покупки (%):', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		Label(Frame_trader_start_sell, text=' ').pack(side=LEFT, anchor=N)

		entry_minimum_sale_price=ttk.Entry(Frame_trader_start_sell, width=10)
		entry_minimum_sale_price.pack(side=LEFT, anchor=N)

		Label(Frame_trader_start_sell, text=',', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)

		entry_maximum_sale_price=ttk.Entry(Frame_trader_start_sell, width=10)
		entry_maximum_sale_price.pack(side=LEFT, anchor=N)

		Label(Frame_trader_start_sell, text='\n').pack(side=LEFT, anchor=N)

		Frame_trader_start_sell.pack()



		ttk.Button(FrameParamsInTraiders, text='Рекомендуемые значения', width=30, command=InsertRecommendParams).pack()

		FrameParamsInTraiders.pack(side=LEFT, fill=Y, expand=1)

		FrameAllWidgtsOutfit.pack(side=TOP, fill=BOTH, expand=1)



		FrameAllWidgtsOutfit.pack()




		#-----
		FrameBtn = LabelFrame(FrameAddEat_s3, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=Analyze).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameAddEat_s3.pack(side=BOTTOM, fill=BOTH, expand=1)



















class Eat_description_add():
	def window(root_name, prj_name, sys_eat_name):
		def LoadFromFile():
			try:
				path_txt_description = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ', filetypes=(("TXT files", "*.txt"), ("All files", "*.*")))
		        
				process1=str(path_txt_description)[:-3]
				path_txt_description=process1[2:]            
		        
				f=open(str(path_txt_description), 'r', encoding='utf-8')
				description_file=f.read()
				f.close()
		        
				text_description_eat.insert(END, description_file)
			except FileNotFoundError:
				#mb.showerror(win_name, 'Файл не был загружен!')
				text_description_eat.insert(END, '')


		def Analyze(root_name, prj_name, sys_eat_name): # sys_outfit_name
			inv_description_eat=''
			n=3
			path='/gamedata/config/text/rus/string_table_enc_equipment.xml'

			if name_eat.get()!='':
				if len(text_description_eat.get(0.0, END))<=n:
					inv_description_eat='Еда имеет системное имя "{0}".{2}{2}Создано в приложении {1} '.format(sys_eat_name, win_name, chr(92)+'n')+author_label

				elif len(text_description_eat.get(0.0, END))>n:
					inv_description_eat=(text_description_eat.get(0.0, END)).replace('\n', chr(92)+'n')

				#print(inv_description_eat)
				inv_name_eat = name_eat.get()
				#if re.search(r'\bзвать\b', 'меня звать Олег, мне 35 лет'):
				#shutil.copy('res/default_configs/SoC/string_table_outfit.xml', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/'))

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+path)==False:
					default_table = open('res/default_configs/SoC/string_table_enc_equipment.xml', 'r')
					table_list_old = default_table.readlines()
					default_table.close()

					table_list = list(table_list_old)

					table_in_project = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+path, 'w')
					
					for word in table_list:
						if re.search('</string_table>', word):
							new_word='''	<string id="enc_equipment_food_{sys_name}">
		<text>{inv_desc_name}</text>
	</string>
	<string id="{sys_name}">
		<text>{inv_name_name}</text>
	</string>
</string_table>'''.format(sys_name=sys_eat_name, inv_desc_name=inv_description_eat, inv_name_name=inv_name_eat)

							table_in_project.write(new_word)

						else:
							table_in_project.write(word)

					table_in_project.close()

				elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+path)==True:


					table_in_project = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+path, 'r')
					table_list = table_in_project.readlines()
					table_in_project.close()

					table_in_project = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+path, 'w')
					
					for word in table_list:
						if re.search('</string_table>', word):
							new_word='''	<string id="enc_equipment_food_{sys_name}">
		<text>{inv_desc_name}</text>
	</string>
	<string id="{sys_name}">
		<text>{inv_name_name}</text>
	</string>
</string_table>'''.format(sys_name=sys_eat_name, inv_desc_name=inv_description_eat, inv_name_name=inv_name_eat)

							table_in_project.write(word.replace(word, new_word))

						else:
							table_in_project.write(word)

					table_in_project.close()

				FrameAddEat_s2.pack_forget()
				AddEatInTraiders.window(root_name=root_name, prj_name=prj_name, sys_eat_name=sys_eat_name, inv_name_eat=inv_name_eat)

			else:
				mb.showerror(win_name, 'Необходимо задать название еды!\n\nЗадавать описание не обязательно, программа сама его сделает следующим:\n'+'"Еда имеет системное имя "{0}".{2}{2}Создано в приложении {1} by tankalxat34 (tnkSoftware)"'.format(sys_outfit_name, win_name, chr(92)+'n'))




		def Red_Fun_Analyze():
			Analyze(root_name=root_name, prj_name=prj_name, sys_eat_name=sys_eat_name)



		FrameAddEat_s2 = Frame(root_name, bg='#f0f0f0')
		#-----


		FrameReturnInvOutfitName = Frame(FrameAddEat_s2, bg='#f0f0f0')
		Label(FrameReturnInvOutfitName, text='Введите название новой еды.', font=(config.font_name, config.font_size)).pack()

		name_eat=ttk.Entry(FrameReturnInvOutfitName, width=55)
		name_eat.pack()
		name_eat.focus()

		#Label(FrameReturnInvOutfitName, text=' ').pack()

		FrameReturnInvOutfitName.pack(side=TOP, fill=X)





		FrameReturnInvOutfitText = Frame(FrameAddEat_s2, bg='#f0f0f0')

		Label(FrameReturnInvOutfitText, text='Введите описание новой еды.', font=(config.font_name, config.font_size)).pack()

		Button(FrameReturnInvOutfitText, text='Для загрузки описания из txt-файла нажмите на эту надпись', fg='blue', bd=0, bg='#f0f0f0', command=LoadFromFile).pack()

		#text_description_weapon = Text(FrameReturnInvOutfitText, bd=1, font=(config.low_font_name, config.low_font_size-1), width=100, height=13)
		text_description_eat = Text(FrameReturnInvOutfitText, bd=1, font=(config.low_font_name, config.low_font_size-1), wrap=WORD, width=110, height=19)
		text_description_eat.pack(side=LEFT)#, expand=1)
		#text.focus()

		scrollY = Scrollbar(FrameReturnInvOutfitText, command=text_description_eat.yview)
		scrollY.pack(side=RIGHT, fill=Y)  
		text_description_eat.config(yscrollcommand=scrollY.set)

		Label(FrameReturnInvOutfitName, text=' ').pack()

		FrameReturnInvOutfitText.pack(side=TOP, fill=X)



		#-----
		FrameBtn = LabelFrame(FrameAddEat_s2, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=Red_Fun_Analyze).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameAddEat_s2.pack(side=BOTTOM, fill=BOTH, expand=1)








class AddEATSysNameDDSOGF():
	def window(root_name, prj_name, status_fill):

		def Add_sys_eat_name():
			system_wpn_name=ENTRY_sys_eat_name.get()
		    
			global memory
		    
			k=0
			alphabet='qwertyuiopasdfghjklzxcvbnm_1234567890'
			if system_wpn_name[0] not in alphabet:                
				mb.showerror(win_name, 'Первый символ в названии не является корректным!')
				k+=1
			else:
				for i in range(len(system_wpn_name)):
					if system_wpn_name[i] in alphabet or i==len(system_wpn_name)-1:
						k+=0
					else:
						k+=1
			#print(k)
			if k>0:
				mb.showerror(win_name, 'В названии есть некорректные символы! Введите название, состоящее из латинских букв, цифр и нижних подчеркиваний. Желательно, что бы название было очень коротким, так как игре будет легче обращатся к файлам с коротким названием.')
			elif k==0:
				#mb.showinfo(win_name, 'Системное имя {} успешно зарегестрировано!'.format(system_wpn_name))
				#btn_load_ogf.configure(state=NORMAL)
				btn_load_dds_eat.configure(state=NORMAL)
				btn_load_dds_eat.focus()
				sys_eat_name = system_wpn_name
				return sys_eat_name

		def Load_DDS_Eat():
			try:
				path_dds = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ', filetypes=(("DDS files", "*.dds"), ("DDS files", "*.dds")))

				dds_folder = config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/item/'
				
				if status_fill==False:
					list_dir=os.listdir(dds_folder)

					for i in range(0, len(list_dir)):
						#print(list_dir[i])
						os.remove(dds_folder+list_dir[i])

					for i in range(0, len(path_dds)):					
						shutil.copy(path_dds[i], dds_folder)

					#path_dds.clear()
				

				if status_fill==True:
					for i in range(0, len(path_dds)):					
						shutil.copy(path_dds[i], dds_folder)
						#print('---------\n'+path_dds[i]+'\n----------')

				btn_load_dds_eat.configure(width=20, text='{0} и др.'.format(os.path.basename(path_dds[0])))
				btn_load_ogf_eat.configure(state=NORMAL)
				btn_load_ogf_eat.focus()

				return path_dds
			except IndexError:
				mb.showerror(win_name, 'Файлы не были загружены!')




		def OGF_on_ground():
			try:
				path_ogf = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ', filetypes=(("OGF files", "*.ogf"), ("OGF files", "*.ogf")))

				ogf_ground_folder = config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/equipments/'


				if status_fill==False:
					list_dir=os.listdir(ogf_ground_folder)

					for i in range(0, len(list_dir)):
						#print(list_dir[i])
						os.remove(ogf_ground_folder+list_dir[i])

					for i in range(0, 1):					
						shutil.copy(path_ogf[i], ogf_ground_folder)


				if status_fill==True:
					for i in range(0, 1):					
						shutil.copy(path_ogf[i], ogf_ground_folder)
						#print('---------\n'+path_dds[i]+'\n----------')

					#mb.showinfo('text', 'Директории оружия сформированы!')

				if len(path_ogf)!=1:
					mb.showerror(win_name, 'Загрузите только один OGF-файл!')
					OGF_on_ground()
				elif len(path_ogf)==1:
					btn_load_ogf_eat.configure(width=20, text='{0}'.format(os.path.basename(path_ogf[0])))
					
				return path_ogf
			except IndexError:
				mb.showerror(win_name, 'Файлы не были загружены!')



		def SELF_Add_sys_eat_name(self):
			Add_sys_eat_name()



		def Analyze():
			sys_eat_name = ENTRY_sys_eat_name.get()

			if sys_eat_name!='':
				dds_folder = config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/item/'
				ogf_ground_folder = config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/equipments/'


				ways_ground_ogf=os.listdir(ogf_ground_folder)
				ways_dds=os.listdir(dds_folder)

				#if len(ways_dds)<=3 and len(ways_ground_ogf)==1:
				try:

					text_continue='''Пожалуйста, подтвердите верность введенных данных в программу! Эти данные верны?

• {0} - Имя проекта.

• {1} - Системное имя бронекостюма.

• {2} - Файлы текстур dds.

• {3} - Файлы ogf когда на земле.

Нажмите "Да" для продолжения, "Нет" для отмены.
'''.format(prj_name, sys_eat_name, ways_dds, ways_ground_ogf)

					answer=mb.askyesno('Подтверждение действия', text_continue) # для еды
					if answer==True:
						#print('Подтверждено!')
						#if len(ways_dds)==1:
						if str(rename_status.get())=='False':
							for i in range(0, len(ways_dds)):
								if i==0:
									os.rename(dds_folder+ways_dds[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/item/item_{0}{1}.dds'.format(sys_eat_name, ''))
								elif i==1:
									os.rename(dds_folder+ways_dds[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/item/item_{0}{1}.dds'.format(sys_eat_name, '_bump'))
								elif i==2:
									os.rename(dds_folder+ways_dds[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/item/item_{0}{1}.dds'.format(sys_eat_name, '_bump#'))
								
						os.rename(ogf_ground_folder+ways_ground_ogf[0], ogf_ground_folder+'{0}{1}'.format(sys_eat_name, '.ogf'))
						

						FrameAddEat_s1.pack_forget()
						Eat_description_add.window(root_name=root_name, prj_name=prj_name, sys_eat_name=sys_eat_name)
				except Exception:
					mb.showerror(win_name, 'Произошла неизвестная ошибка, дальнейшее продолжение не возможно!')
				#else:
					#mb.showerror(win_name, 'Проверьте количество загруженных файлов в программу! DDS-текстуры не больше 3-х файлов, OGF файлов не больше одного файла!')



		FrameAddEat_s1 = Frame(root_name, bg='#f0f0f0')
		#-----

		FrameEatAllWidgets1 = Frame(FrameAddEat_s1)

		FrameStrokaEat1 = Frame(FrameEatAllWidgets1)

		FrameEntrySysEatName = Frame(FrameStrokaEat1)
		Label(FrameEntrySysEatName, text='Введите системное имя еды:', font=(config.font_name, config.font_size)).pack()

		ENTRY_sys_eat_name = ttk.Entry(FrameEntrySysEatName, width=35)
		ENTRY_sys_eat_name.pack()
		ENTRY_sys_eat_name.focus()
		ENTRY_sys_eat_name.bind_all('<Return>', SELF_Add_sys_eat_name)

		ttk.Button(FrameEntrySysEatName, text='Применить', width=20, command=Add_sys_eat_name).pack()
		FrameEntrySysEatName.pack(side=LEFT, anchor=N)

		Otstup(FrameStrokaEat1)

		FrameLoadDdsEat = Frame(FrameStrokaEat1)
		Label(FrameLoadDdsEat, text='Загрузите DDS текстуры еды:', font=(config.font_name, config.font_size)).pack()
		btn_load_dds_eat = ttk.Button(FrameLoadDdsEat, text='Загрузить...', width=20, state=DISABLED, command=Load_DDS_Eat)
		btn_load_dds_eat.pack()

		name_items=['Аптечка', 'Бинт', 'Еда']
		rename_status = BooleanVar()
		rename_status.set(0)
		rename_status_widget = ttk.Checkbutton(FrameLoadDdsEat, text="Отключить переименование текстур", variable=rename_status, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 9), justify=LEFT)
		rename_status_widget.pack(side=TOP)

		FrameLoadDdsEat.pack(side=LEFT, anchor=N)


		Otstup(FrameStrokaEat1)



		FrameLoadOgfEat = Frame(FrameStrokaEat1)
		Label(FrameLoadOgfEat, text='Загрузите OGF файл еды:', font=(config.font_name, config.font_size)).pack()
		btn_load_ogf_eat = ttk.Button(FrameLoadOgfEat, text='Загрузить...', width=20, state=DISABLED, command=OGF_on_ground)
		btn_load_ogf_eat.pack()
		FrameLoadOgfEat.pack(side=LEFT, anchor=N)

		FrameStrokaEat1.pack(side=TOP)



		FrameStrokaEat2 = Frame(FrameEatAllWidgets1)



		Label(FrameStrokaEat2, text=' ', font=(config.font_name, config.font_size)).pack()

		FrameAddClassEat = Frame(FrameStrokaEat2)

		Label(FrameAddClassEat, text='Класс еды (аптечка, бинт или еда):', font=(config.font_name, config.font_size)).pack()
		cb_add_class_eat=ttk.Combobox(FrameAddClassEat, values = name_items, width=8, height=20, state="readonly")
		cb_add_class_eat.set(name_items[len(name_items)-1])
		cb_add_class_eat.pack()

		#FrameAddClassEat.pack(side=TOP)

		FrameStrokaEat2.pack(side=TOP)



		# ОПИСАНИЕ СЛАЙДА

		Label(FrameEatAllWidgets1, text=desc_eat_s1, justify=LEFT, font=(config.low_font_name, config.low_font_size)).pack()



		FrameEatAllWidgets1.pack(expand=1, fill=BOTH)
		#-----
		FrameBtn = LabelFrame(FrameAddEat_s1, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=Analyze).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameAddEat_s1.pack(side=BOTTOM, fill=BOTH, expand=1)






























#######################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################
########################################БРОНЯ##########################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################


class AddOutfitParameters():
	def window(root_name, prj_name, sys_outfit_name, text_coordinate_icons, outf_cost, outfit_inv_name):
		def is_digit(string):
			if string.isdigit():
				return True
			else:
				try:
					float(string)
					return True
				except ValueError:
					return False

		def AddInvActorIcon():

			def ReloadIcon():
				new_icon=(cb_add_text.get()).replace('\n', '')

				#print(new_icon)
				global coordinate_icons;
				coordinate_icons='*'

				#path=(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/ui_icons_npc.dds') #'res/default_ui/ui_icon_equipment.dds'
				path='res/default_ui/SoC/ui_icons_npc.dds'
		#		image = Image.open(path)
				
				if new_icon=='Без костюма':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((384, 384, 512, 704)))
					panel_1.configure(image=img2)
					panel_1.image = img2


					coordinate_icons='npc_icon_without_outfit'

					#btn_actor_icon.configure(text=)

					#pyperclip.copy(coordinate_icons)
					#btn_actor_icon.configure(text=coordinate_icons)

				elif new_icon=='Бандитская куртка':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 384, 128, 704)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_bandit_outfit'

				elif new_icon=='"Страж свободы"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((128, 384, 256, 704)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_svoboda_heavy_outfit'

				elif new_icon=='Берилл-5М':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((256, 384, 384, 704)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_specops_outfit' # npc_icon_specops_outfit

				elif new_icon=='ПСЗ-9Мд «Универсальная защита»':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((512, 704, 640, 1024)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_dolg_outfit'

				elif new_icon=='Комбинезон ССП-99М':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((768, 384, 896, 704)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_protection_outfit'

				elif new_icon=='ССП-99 "Эколог"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((896, 384, 1024, 704)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_ecolog_outfit'

				elif new_icon=='Куртка новичка':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 704, 128, 1024)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_novice_outfit'

				elif new_icon=='Экзоскелет':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((128, 704, 256, 1024)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_exo_outfit'

				elif new_icon=='Комбинезон наемника':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((256, 704, 384, 1024)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_killer_outfit'

				elif new_icon=='Комбинезон монолита':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((384, 704, 512, 1024)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_monolit_outfit'

				elif new_icon=='Комбинезон долга':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((512, 704, 640, 1024)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_dolg_outfit'

				elif new_icon=='"Ветер свободы"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((640, 704, 768, 1024)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_svoboda_light_outfit'

				elif new_icon=='СЕВА':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((768, 704, 896, 1024)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_svoboda_light_outfit'

				elif new_icon=='Комбинезон сталкера':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((896, 704, 1024, 1024)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='npc_icon_svoboda_light_outfit'



			def CloseInsert():
				icon_name=cb_add_text.get()
				btn_actor_icon.configure(text=icon_name)
				win_actor_icon.destroy()
				return coordinate_icons


			def SELF_CloseInsert(self):
				CloseInsert()

			def SELF_ReloadIcon(self):
				ReloadIcon()

			win_actor_icon = Toplevel(root_name)
			win_actor_icon.title(win_name+' - выбор иконки персонажа в инвентаре')
			win_actor_icon.resizable(win_draw, win_draw)
			win_actor_icon.iconbitmap(win_icon)
			win_actor_icon.geometry('700x550')

			win_actor_icon.focus_force()

			FrameOutfitActorIcon = Frame(win_actor_icon, bg='#f0f0f0')

			FrameSmallTitle1 = Frame(FrameOutfitActorIcon)
			Label(FrameSmallTitle1, text='Демонстрируемая иконка', font=(config.font_name, config.font_size)).pack(side=LEFT, anchor=N)
			#Button(FrameSmallTitle1, text='↺', font=(config.font_name, config.font_size), bd=0, fg='blue', command=ReloadIcon).pack(side=LEFT, anchor=N)
			FrameSmallTitle1.pack(side=TOP)
			 
			panel_1=Label(FrameOutfitActorIcon, bg='grey', width=150, height=330)#bg='#A0522D', width=150, height=330)
			panel_1.pack()

			Label(FrameOutfitActorIcon, text='Выберите бронекостюм, иконоку которого хотите использовать', font=(config.font_name, config.font_size)).pack(side=TOP, anchor=N)
			Label(FrameOutfitActorIcon, text='Для обновления иконки в окне нажмите клавишу F5\nДля выбора иконки выберите ее и нажмите Enter', font=('Verdana', config.low_font_size)).pack()

			name_items=['Бандитская куртка',
			'"Страж свободы"',
			'Берилл-5М',
			'ПСЗ-9Мд «Универсальная защита»',
			#'Тяжелый бронекостюм',
			'ССП-99 "Эколог"',
			'Комбинезон ССП-99М',
			'Куртка новичка',
			'Экзоскелет',
			'Комбинезон наемника',
			'Комбинезон монолита',
			'Комбинезон долга',
			'"Ветер свободы"',
			'СЕВА',
			'Комбинезон сталкера',
			'Без костюма']

			cb_add_text=ttk.Combobox(FrameOutfitActorIcon, values = name_items, width=35, height=20, state="readonly")
			cb_add_text.pack(side=TOP, anchor=N)
			cb_add_text.set(name_items[len(name_items)-1])


			win_actor_icon.bind_all('<F5>', SELF_ReloadIcon)
			win_actor_icon.bind_all('<Return>', SELF_CloseInsert)


			Label(FrameOutfitActorIcon, text=' ').pack()

			ttk.Button(FrameOutfitActorIcon, text='Применить и закрыть окно', width=35, command=CloseInsert).pack()

			inv_actor_icon = ReloadIcon()
			
			FrameOutfitActorIcon.pack(fill=BOTH, expand=1, side=TOP, anchor=NW)



			win_actor_icon.mainloop()



		def DeleteOUTFITltx(path):
			os.remove(path)

			btn_load_outfit_ltx.configure(text='Загрузить...', width=20)

			separator_TOP.pack(fill=BOTH)
			separator_BOTTOM.pack(fill=BOTH, side=BOTTOM)

			FrameAllOutfitLTXWidgets.pack(expand=0, fill=BOTH)

			FrameDescription.pack()

			mb.showinfo(win_name, 'Файл outfit.ltx успешно удален из программы!')




		def LoadOUTFITltx():
			def Red_Fun_DeleteOUTFITltx():
				answer=mb.askyesno(win_name, 'Вы действительно хотите удалить файл outfit.ltx из программы?')

				if answer==True:
					FrameNoRedactionWidgets.pack_forget()
					DeleteOUTFITltx(path=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/outfit.ltx')

			try:
				path_outfit_ltx_description = fd.askopenfilenames(title=win_name+' - загрузите файлы... ', filetypes=(("outfit.ltx", "outfit.ltx"), ("LTX files", "*.ltx"), ("All files", "*.*")))

				#print(path_outfit_ltx_description[0])

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/')==True:
					shutil.copy(path_outfit_ltx_description[0], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/')
				else:
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/')
					shutil.copy(path_outfit_ltx_description[0], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/')

				btn_load_outfit_ltx.configure(text=path_outfit_ltx_description[0], width=len(path_outfit_ltx_description[0])+8)#os.path.basename(path_outfit_ltx_description[0]))


				FrameAllOutfitLTXWidgets.pack_forget()

				FrameNoRedactionWidgets = Frame(FrameOutfitS4)

				Label(FrameNoRedactionWidgets, text='\nВы не можете отредактировать новые параметры, так как вы загрузили уже готовый файл outfit.ltx\nУдалить файл из программы можно нажав на соответствующюю кнопку\nОбратите внимание, в данной версии программы не предусмотрена проверка наличия нового бронекостюма в скрипте!\nВы загружаете скрипт, подтверждая тем самым наличие костюма '+sys_outfit_name+' в нем!', font=(config.font_name, config.font_size)).pack()
				
				delete_outfit_ltx = ttk.Button(FrameNoRedactionWidgets, text='Удалить outfit.ltx из программы', width=len('Удалить outfit.ltx из программы')+5, command=Red_Fun_DeleteOUTFITltx)
				delete_outfit_ltx.pack()

				FrameNoRedactionWidgets.pack(expand=0, fill=BOTH)

				separator_TOP.pack_forget()
				separator_BOTTOM.pack_forget()

				FrameDescription.pack_forget()
				FrameDescription.pack(side=BOTTOM, anchor=S)

				#print('ВЫВОД ВСЕХ ПАРАМЕТРОВ КОСТЮМА\n\nПЕРЕХОД НА СЛЕД. СЛАЙД\n\n'+path_outfit_ltx_description[0])
				

				
			except FileNotFoundError:
				mb.showerror(win_name, 'Файл не был загружен!')

			except IndexError:
				mb.showerror(win_name, 'Файл не был загружен!')
				

		def Analyze():
			if (ENTRY_inv_outfit_weight.get()!='' or ENTRY_inv_outfit_weight.get()!='0') and (ENTRY_inv_add_weight.get()!=''):

				# НАЧИНАЕМ ГИГАНТСКИЙ СБОР ДАННЫХ СО СЛАЙДА.
				#	основные данные
				#inv_outft_icon = outfit_inv_name
				text_coord_outfit_in_ui_icons = '\n'+outfit_inv_name # иконка костюма в инвентаре

				try:
					inv_icon_actor = coordinate_icons # текстовое название иконки npc_icon_***_outfit
				except NameError:
					inv_icon_actor = 'npc_icon_without_outfit'

				outfit_cost = outf_cost # цена костюма

				if cb_pnv_type.get()=='хороший':
					pnv_type = 'effector_nightvision_good' # тип пнв
				elif cb_pnv_type.get()=='плохой':
					pnv_type = 'effector_nightvision_bad'

				if cb_sprint_type.get()=='да':
					outfit_sprint = 'true' # может ли игрок бегать в костюме
				elif cb_sprint_type.get()=='нет':
					outfit_sprint = 'false'

				if is_digit(ENTRY_inv_outfit_weight.get())==True and is_digit(ENTRY_inv_add_weight.get()):
					inv_outfit_weight = ENTRY_inv_outfit_weight.get() #вес в инвентаре - число
					add_inv_weight = ENTRY_inv_add_weight.get() # сколько добавлять к переносимому весу - число

				
					# -------------------------------------------------------------------------------------------------
					
					# ЗАЩИТА ИГРОКА ОТ ВОЗДЕЙСТВИЙ
					fire_wound_protection = cb_FIRE_WOUND_Prot.get() # пулестойкость

					burn_protection = cb_BURN_Prot.get() # ожог

					strike_protection = cb_STRIKE_Prot.get() # удар

					shock_protection = cb_SHOK_Prot.get() # электрошок

					wound_protection = cb_WOUND_Prot.get() # разрыв

					radiation_protection = cb_RAD_Prot.get() # радиация

					telepatic_protection = cb_TELE_Prot.get() # пси-устойчивость

					chemical_burn_protection = cb_CHEM_BURN_Prot.get() # химический ожег

					explosion_protection = cb_EXPLOSION_Prot.get() # взрыв

					# -------------------------------------------------------------------------------------------------

					# ИММУНИТЕТ К ВОЗДЕЙСТВИЯМ САМОГО КОСТЮМА (пояснения воздействий выше)
					fire_wound_immunity = cb_FIRE_WOUND_Imm.get()

					burn_immunity = cb_BURN_Imm.get()

					strike_immunity = cb_STRIKE_Imm.get()

					shock_immunity = cb_SHOK_Imm.get()

					wound_immunity = cb_WOUND_Imm.get()

					radiation_immunity = cb_RAD_Imm.get()

					telepatic_immunity = cb_TELE_Imm.get()

					chemical_burn_immunity = cb_CHEM_BURN_Imm.get()

					explosion_immunity = cb_EXPLOSION_Imm.get()

					# -------------------------------------------------------------------------------------------------

					# НАЧИНАЮ ЗАПИСЬ В ФАЙЛ outfit.ltx


					outfit_info=shablon_outfit.format(
						#секция 1
						win_name=win_name,
						outfit_name=outfit_inv_name,
						system_outfit_name=sys_outfit_name,
						inv_outfit_weight=inv_outfit_weight,
						text_coord_outfit_in_ui_icons=text_coordinate_icons,
						#секция 2
						inv_icon_actor=inv_icon_actor,
						outfit_cost=outfit_cost,
						pnv_type=pnv_type,
						outfit_sprint=outfit_sprint,
						add_inv_weight=add_inv_weight,
						#секция 3
						burn_protection=burn_protection,
						strike_protection=strike_protection,
						shock_protection=shock_protection,
						wound_protection=wound_protection,
						radiation_protection=radiation_protection,
						telepatic_protection=telepatic_protection,
						chemical_burn_protection=chemical_burn_protection,
						explosion_protection=explosion_protection,
						fire_wound_protection=fire_wound_protection,
						# секция 4
						burn_immunity=burn_immunity,
						strike_immunity=strike_immunity,
						shock_immunity=shock_immunity,
						wound_immunity=wound_immunity,
						radiation_immunity=radiation_immunity,
						telepatic_immunity=telepatic_immunity,
						chemical_burn_immunity=chemical_burn_immunity,
						explosion_immunity=explosion_immunity,
						fire_wound_immunity=fire_wound_immunity)



					path=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/outfit.ltx'

					if os.path.exists(path)==True:	
						f = open(path, 'a')
						f.write(outfit_info)
						f.close()



					elif os.path.exists(path)==False:						
						shutil.copy('res/default_configs/SoC/outfit.ltx', config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/')
						f = open(path, 'a')
						f.write(outfit_info)
						f.close()


					# ЗАПИСЫВАЕМ ИНФОРМАЦИЮ О ПРОЕКТЕ В ФАЙЛ project_info.ini (ПОТОМ БУДЕМ ДЕЛАТЬ В ui_ltx_gen_info.script)
					if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/project_info.inf')==False:
						f_info = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/project_info.inf', 'w')
						f_info.write(desc_file_text+'outfit_{system_outfit_name} = {outfit_inv_name}\n'.format(system_outfit_name=sys_outfit_name, outfit_inv_name=outfit_inv_name))
						f_info.close()

					elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/project_info.inf')==True:
						f_info = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/project_info.inf', 'a')
						f_info.write('outfit_{system_outfit_name} = {outfit_inv_name}\n'.format(system_outfit_name=sys_outfit_name, outfit_inv_name=outfit_inv_name))
						f_info.close()

					#mb.showinfo(win_name, 'Запись успешно завершена! Переход на следующий шаг!')
					FrameOutfitS4.pack_forget()
					END_PROJECT_MENU.window(root_name=root_name, prj_name=prj_name)


				else:
					mb.showerror(win_name, 'Не все данные введены верно, убедитесь что вы ввели числа там, где они нужны!\n\nОБРАТИТЕ ВНИМАНИЕ\nЕсли вы не задали иконку персонажа, одетого в костюм в инвентаре, то такой иконкой станет персонаж без костюма!')
			else:
				mb.showerror(win_name, 'Не все данные введены верно, убедитесь что вы ввели числа там, где они нужны!\n\nОБРАТИТЕ ВНИМАНИЕ\nЕсли вы не задали иконку персонажа, одетого в костюм в инвентаре, то такой иконкой станет персонаж без костюма!')
					




		FrameOutfitS4 = Frame(root_name, bg='#f0f0f0')
		#-----

		# root_name.geometry('1020x500')
		root_name.geometry('1020x430')

		Label(FrameOutfitS4, text='Настройте параметры бронекостюма "'+outfit_inv_name+'"', font=(config.font_name, config.font_size)).pack()
		Label(FrameOutfitS4, text='Или загрузите готовый скрипт outfit.ltx', font=(config.low_font_name, config.low_font_size-2)).pack()
		btn_load_outfit_ltx = ttk.Button(FrameOutfitS4, text='Загрузить...', width=20, command=LoadOUTFITltx)
		btn_load_outfit_ltx.pack()

		Label(FrameOutfitS4, text=' ').pack()
		separator_TOP=ttk.Separator(FrameOutfitS4, orient='horizontal')
		separator_TOP.pack(fill=BOTH)


		shablon_outfit='''
;---------------------------------------------------------------------------------------------
;   {win_name} - Outfit information.
; Outfit name: {outfit_name}
; System outfit name: {system_outfit_name}
;---------------------------------------------------------------------------------------------
[{system_outfit_name}_outfit]:outfit_base
GroupControlSection	= spawn_group
discovery_dependency = 
$spawn 			= "outfit\\{system_outfit_name}_outfit"
;$prefetch 		= 32
class			= E_STLK
cform           = skeleton
visual          = equipments\\{system_outfit_name}_suit
actor_visual	= actors\\hero\\stalker_{system_outfit_name}.ogf

ef_equipment_type	= 3

inv_name			= {system_outfit_name}_outfit_name
inv_name_short		= {system_outfit_name}_outfit_name
description			= {system_outfit_name}_outfit_description
inv_weight			= {inv_outfit_weight}

{text_coord_outfit_in_ui_icons}

full_icon_name		= {inv_icon_actor}

cost		  = {outfit_cost}
slot		  = 6
full_scale_icon   = 6,6
nightvision_sect  = {pnv_type}
 
sprint_allowed = {outfit_sprint}

bones_koeff_protection = exo_helmet_damage

additional_inventory_weight  = {add_inv_weight}
additional_inventory_weight2 = {add_inv_weight}
immunities_sect   = sect_{system_outfit_name}_outfit_immunities

; NO RESISTANCE
burn_protection          = {burn_protection}
strike_protection        = {strike_protection}
shock_protection         = {shock_protection}
wound_protection         = {wound_protection}
radiation_protection     = {radiation_protection}
telepatic_protection     = {telepatic_protection}
chemical_burn_protection = {chemical_burn_protection}
explosion_protection     = {explosion_protection}
fire_wound_protection    = {fire_wound_protection}



[sect_{system_outfit_name}_outfit_immunities]
burn_immunity				= {burn_immunity}
strike_immunity				= {strike_immunity}
shock_immunity				= {shock_immunity}
wound_immunity				= {wound_immunity}
radiation_immunity			= {radiation_immunity}
telepatic_immunity			= {telepatic_immunity}
chemical_burn_immunity		= {chemical_burn_immunity}
explosion_immunity			= {explosion_immunity}
fire_wound_immunity			= {fire_wound_immunity}

		'''

		#print(shablon_outfit)
		#print(inv_outft_icon)
		#print(outf_cost)


		FrameAllOutfitLTXWidgets = Frame(FrameOutfitS4)


		FrameDecorOtstup = Frame(FrameAllOutfitLTXWidgets)
		Label(FrameDecorOtstup, text='  ').pack()
		FrameDecorOtstup.pack(side=LEFT, anchor=N)



		FrameStolb1 = Frame(FrameAllOutfitLTXWidgets)

		Label(FrameStolb1, text='Основные параметры:', font=(config.font_name, config.font_size)).pack(anchor=N)

		FrameInvOutfitWeight = Frame(FrameStolb1)
		Label(FrameInvOutfitWeight, text='Вес бронекостюма: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		ENTRY_inv_outfit_weight = ttk.Entry(FrameInvOutfitWeight, width=5)
		ENTRY_inv_outfit_weight.pack(side=LEFT, anchor=N)
		Label(FrameInvOutfitWeight, text=' кг.', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		FrameInvOutfitWeight.pack(anchor=W)

		FrameInvIconOutfitActor = Frame(FrameStolb1)
		Label(FrameInvIconOutfitActor, text='Иконка персонажа: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		btn_actor_icon=ttk.Button(FrameInvIconOutfitActor, text='Выбрать...', width=15, command=AddInvActorIcon)
		btn_actor_icon.pack(side=LEFT, anchor=N)
		FrameInvIconOutfitActor.pack(anchor=W)

		FramePNVType = Frame(FrameStolb1)
		Label(FramePNVType, text='Тип ПНВ: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		list_pnv_types=['хороший', 'плохой', 'нет']
		cb_pnv_type=ttk.Combobox(FramePNVType, values = list_pnv_types, width=10, state="readonly")
		cb_pnv_type.pack(side=LEFT, anchor=N)
		cb_pnv_type.set('хороший')
		FramePNVType.pack(anchor=W)

		FrameSprintOutfit = Frame(FrameStolb1)
		Label(FrameSprintOutfit, text='Бег в костюме: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		list_sprint_types=['да', 'нет']
		cb_sprint_type=ttk.Combobox(FrameSprintOutfit, values = list_sprint_types, width=10, state="readonly")
		cb_sprint_type.pack(side=LEFT, anchor=N)
		cb_sprint_type.set('да')
		FrameSprintOutfit.pack(anchor=W)

		FrameSelectAddInvWeight = Frame(FrameStolb1)
		Label(FrameSelectAddInvWeight, text='Добавлять к перенос. весу: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		ENTRY_inv_add_weight = ttk.Entry(FrameSelectAddInvWeight, width=5)
		ENTRY_inv_add_weight.pack(side=LEFT, anchor=N)
		Label(FrameSelectAddInvWeight, text=' кг.', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		FrameSelectAddInvWeight.pack(anchor=W)


		#ttk.Separator(FrameStolb1, orient='vertical').pack(fill=Y, side=RIGHT, expand=1)
		FrameStolb1.pack(side=LEFT, anchor=N)








		#===============================================
		FrameDecorOtstup2 = Frame(FrameAllOutfitLTXWidgets)
		Label(FrameDecorOtstup2, text=' ').pack()
		FrameDecorOtstup2.pack(side=LEFT, anchor=N)
		#===============================================








		FrameStolb2 = Frame(FrameAllOutfitLTXWidgets)

		separator1=ttk.Separator(FrameStolb2, orient='vertical')
		separator1.pack(fill=BOTH, side=LEFT)

		Label(FrameStolb2, text='Защита от воздействий:', font=(config.font_name, config.font_size)).pack(anchor=N)
		Label(FrameStolb2, text='(0.99 - непробиваемый, 0.00 - не защитит вообще)', font=(config.low_font_name, config.low_font_size-2)).pack(anchor=N)


		nums=[]
		for i in range(0, 100):
			if len('0,'+str(i))<=3:
				nums.append('0.0{}'.format(str(i)))
			else:
				nums.append('0.'+str(i))
			#print(nums)

		set_widget='0.99'

		Frame_Sec1 = Frame(FrameStolb2)

		Frame_FIRE_WOUND_Protection = Frame(Frame_Sec1)
		Label(Frame_FIRE_WOUND_Protection, text='Пулестойкость: ', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_FIRE_WOUND_Prot =  ttk.Combobox(Frame_FIRE_WOUND_Protection, values = nums, width=5, state="readonly")
		cb_FIRE_WOUND_Prot.pack(side=LEFT, anchor=N)
		cb_FIRE_WOUND_Prot.set(set_widget)
		Frame_FIRE_WOUND_Protection.pack(side=LEFT, anchor=NW)


		Frame_BURN_Protection = Frame(Frame_Sec1)
		Label(Frame_BURN_Protection, text='Ожог: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_BURN_Prot = ttk.Combobox(Frame_BURN_Protection, values = nums, width=5, state="readonly")
		cb_BURN_Prot.pack(side=LEFT, anchor=N)
		cb_BURN_Prot.set(set_widget)
		Frame_BURN_Protection.pack(side=LEFT, anchor=NW)


		Frame_STRIKE_Protection = Frame(Frame_Sec1)
		Label(Frame_STRIKE_Protection, text='Удар: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_STRIKE_Prot =  ttk.Combobox(Frame_STRIKE_Protection, values = nums, width=5, state="readonly")
		cb_STRIKE_Prot.pack(side=LEFT, anchor=N)
		cb_STRIKE_Prot.set(set_widget)
		Frame_STRIKE_Protection.pack(side=LEFT, anchor=NW)


		Frame_Sec1.pack(anchor=W)


		Frame_Sec2 = Frame(FrameStolb2)

		Frame_SHOK_Protection = Frame(Frame_Sec2)
		Label(Frame_SHOK_Protection, text='Электрошок: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_SHOK_Prot =  ttk.Combobox(Frame_SHOK_Protection, values = nums, width=5, state="readonly")
		cb_SHOK_Prot.pack(side=LEFT, anchor=N)
		cb_SHOK_Prot.set(set_widget)
		Frame_SHOK_Protection.pack(side=LEFT, anchor=NW)

		Frame_WOUND_Protection = Frame(Frame_Sec2)
		Label(Frame_WOUND_Protection, text=' Разрыв: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_WOUND_Prot =  ttk.Combobox(Frame_WOUND_Protection, values = nums, width=5, state="readonly")
		cb_WOUND_Prot.pack(side=LEFT, anchor=N)
		cb_WOUND_Prot.set(set_widget)
		Frame_WOUND_Protection.pack(side=LEFT, anchor=NW)

		Frame_Sec2.pack(anchor=W)


		Frame_Sec3 = Frame(FrameStolb2)

		Frame_RADIATION_Protection = Frame(Frame_Sec3)
		Label(Frame_RADIATION_Protection, text='Радиация: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_RAD_Prot =  ttk.Combobox(Frame_RADIATION_Protection, values = nums, width=5, state="readonly")
		cb_RAD_Prot.pack(side=LEFT, anchor=N)
		cb_RAD_Prot.set(set_widget)
		Frame_RADIATION_Protection.pack(side=LEFT, anchor=NW)

		Frame_TELEPATIC_Protection = Frame(Frame_Sec3)
		Label(Frame_TELEPATIC_Protection, text='Пси-воздействие: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_TELE_Prot =  ttk.Combobox(Frame_TELEPATIC_Protection, values = nums, width=5, state="readonly")
		cb_TELE_Prot.pack(side=LEFT, anchor=N)
		cb_TELE_Prot.set(set_widget)
		Frame_TELEPATIC_Protection.pack(side=LEFT, anchor=NW)

		Frame_Sec3.pack(anchor=W)


		Frame_Sec4 = Frame(FrameStolb2) # chemical_burn

		Frame_CHEMICAL_BURN_Protection = Frame(FrameStolb2)
		Label(Frame_CHEMICAL_BURN_Protection, text='Хим. ожог: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_CHEM_BURN_Prot =  ttk.Combobox(Frame_CHEMICAL_BURN_Protection, values = nums, width=5, state="readonly")
		cb_CHEM_BURN_Prot.pack(side=LEFT, anchor=N)
		cb_CHEM_BURN_Prot.set(set_widget)
		Frame_CHEMICAL_BURN_Protection.pack(side=LEFT, anchor=NW)

		Frame_EXPLOSION_Protection = Frame(FrameStolb2)
		Label(Frame_EXPLOSION_Protection, text='     Взрыв: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_EXPLOSION_Prot =  ttk.Combobox(Frame_EXPLOSION_Protection, values = nums, width=5, state="readonly")
		cb_EXPLOSION_Prot.pack(side=LEFT, anchor=N)
		cb_EXPLOSION_Prot.set(set_widget)
		Frame_EXPLOSION_Protection.pack(side=LEFT, anchor=NW)

		Frame_Sec4.pack(anchor=W)



		FrameStolb2.pack(side=LEFT, anchor=N, fill=Y)







		#==================================
		FrameDecorOtstup2 = Frame(FrameAllOutfitLTXWidgets)
		Label(FrameDecorOtstup2, text=' ').pack()
		FrameDecorOtstup2.pack(side=LEFT, anchor=N)
		#==================================


		nums.append('1')
		set_widget='0.00'   #(nums[len(nums)-1])


		FrameStolb3 = Frame(FrameAllOutfitLTXWidgets)

		separator2=ttk.Separator(FrameStolb3, orient='vertical')
		separator2.pack(fill=Y, side=LEFT)

		Label(FrameStolb3, text='Иммунитет костюма:', font=(config.font_name, config.font_size)).pack(anchor=N)
		Label(FrameStolb3, text='(1 - лучше даже не дышать, 0.00 - абсолютно неуязвимый)', font=(config.low_font_name, config.low_font_size-2)).pack(anchor=N)

		Frame_Sec1 = Frame(FrameStolb3)

		Frame_FIRE_WOUND_Immunitet = Frame(Frame_Sec1)
		Label(Frame_FIRE_WOUND_Immunitet, text='Пулестойкость: ', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_FIRE_WOUND_Imm =  ttk.Combobox(Frame_FIRE_WOUND_Immunitet, values = nums, width=5, state="readonly")
		cb_FIRE_WOUND_Imm.pack(side=LEFT, anchor=N)
		cb_FIRE_WOUND_Imm.set(set_widget)
		Frame_FIRE_WOUND_Immunitet.pack(side=LEFT, anchor=NW)


		Frame_BURN_Immunitet = Frame(Frame_Sec1)
		Label(Frame_BURN_Immunitet, text='Ожог: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_BURN_Imm = ttk.Combobox(Frame_BURN_Immunitet, values = nums, width=5, state="readonly")
		cb_BURN_Imm.pack(side=LEFT, anchor=N)
		cb_BURN_Imm.set(set_widget)
		Frame_BURN_Immunitet.pack(side=LEFT, anchor=NW)


		Frame_STRIKE_Imm = Frame(Frame_Sec1)
		Label(Frame_STRIKE_Imm, text='Удар: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_STRIKE_Imm =  ttk.Combobox(Frame_STRIKE_Imm, values = nums, width=5, state="readonly")
		cb_STRIKE_Imm.pack(side=LEFT, anchor=N)
		cb_STRIKE_Imm.set(set_widget)
		Frame_STRIKE_Imm.pack(side=LEFT, anchor=NW)




		Frame_Sec1.pack(anchor=W)


		Frame_Sec2 = Frame(FrameStolb3)

		Frame_SHOK_Immunitet = Frame(Frame_Sec2)
		Label(Frame_SHOK_Immunitet, text='Электрошок: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_SHOK_Imm =  ttk.Combobox(Frame_SHOK_Immunitet, values = nums, width=5, state="readonly")
		cb_SHOK_Imm.pack(side=LEFT, anchor=N)
		cb_SHOK_Imm.set(set_widget)
		Frame_SHOK_Immunitet.pack(side=LEFT, anchor=NW)

		Frame_WOUND_Immunitet = Frame(Frame_Sec2)
		Label(Frame_WOUND_Immunitet, text=' Разрыв: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_WOUND_Imm =  ttk.Combobox(Frame_WOUND_Immunitet, values = nums, width=5, state="readonly")
		cb_WOUND_Imm.pack(side=LEFT, anchor=N)
		cb_WOUND_Imm.set(set_widget)
		Frame_WOUND_Immunitet.pack(side=LEFT, anchor=NW)

		Frame_Sec2.pack(anchor=W)


		Frame_Sec3 = Frame(FrameStolb3)

		Frame_RADIATION_Immunitet = Frame(Frame_Sec3)
		Label(Frame_RADIATION_Immunitet, text='Радиация: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_RAD_Imm =  ttk.Combobox(Frame_RADIATION_Immunitet, values = nums, width=5, state="readonly")
		cb_RAD_Imm.pack(side=LEFT, anchor=N)
		cb_RAD_Imm.set(set_widget)
		Frame_RADIATION_Immunitet.pack(side=LEFT, anchor=NW)

		Frame_TELEPATIC_Immunitet = Frame(Frame_Sec3)
		Label(Frame_TELEPATIC_Immunitet, text='Пси-воздействие: \n', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_TELE_Imm =  ttk.Combobox(Frame_TELEPATIC_Immunitet, values = nums, width=5, state="readonly")
		cb_TELE_Imm.pack(side=LEFT, anchor=N)
		cb_TELE_Imm.set(set_widget)
		Frame_TELEPATIC_Immunitet.pack(side=LEFT, anchor=NW)

		Frame_Sec3.pack(anchor=W)


		Frame_Sec4 = Frame(FrameStolb3) # chemical_burn

		Frame_CHEMICAL_BURN_Immunitet = Frame(FrameStolb3)
		Label(Frame_CHEMICAL_BURN_Immunitet, text='Хим. ожог: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_CHEM_BURN_Imm =  ttk.Combobox(Frame_CHEMICAL_BURN_Immunitet, values = nums, width=5, state="readonly")
		cb_CHEM_BURN_Imm.pack(side=LEFT, anchor=N)
		cb_CHEM_BURN_Imm.set(set_widget)
		Frame_CHEMICAL_BURN_Immunitet.pack(side=LEFT, anchor=NW)

		Frame_EXPLOSION_Immunitet = Frame(FrameStolb3)
		Label(Frame_EXPLOSION_Immunitet, text='     Взрыв: ', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		cb_EXPLOSION_Imm =  ttk.Combobox(Frame_EXPLOSION_Immunitet, values = nums, width=5, state="readonly")
		cb_EXPLOSION_Imm.pack(side=LEFT, anchor=N)
		cb_EXPLOSION_Imm.set(set_widget)
		Frame_EXPLOSION_Immunitet.pack(side=LEFT, anchor=NW)

		Frame_Sec4.pack(anchor=W)







		FrameStolb3.pack(side=LEFT, anchor=N, fill=Y)

		#==========================
		FrameAllOutfitLTXWidgets.pack(expand=0, fill=BOTH)

		separator_BOTTOM=ttk.Separator(FrameOutfitS4, orient='horizontal')
		separator_BOTTOM.pack(fill=BOTH)

		FrameDescription = Frame(FrameOutfitS4)
		Label(FrameDescription, text=description_outfit_s4, font=(config.low_font_name, config.low_font_size), justify=LEFT).pack()
		FrameDescription.pack()

		#-----
		FrameBtn = LabelFrame(FrameOutfitS4, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=Analyze).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameOutfitS4.pack(side=BOTTOM, fill=BOTH, expand=1)



class AddOutfitInTraiders():

	def window(root_name, prj_name, sys_outfit_name, inv_name_outfit):
		FrameOutfitS3 = Frame(root_name, bg='#f0f0f0')

		#-----

		def OpenSIE():
			project_name=prj_name
			#root_name.destroy()
			root_name.withdraw()
			os.system("sie.exe "+config.folder_projects+"/"+config.folder_projects_soc+'/'+project_name+"/gamedata/textures/ui/ui_icon_equipment.dds")
			root_name.deiconify()


		def AddClassicOutfitIcon():

			def ReloadIcon():
				new_icon=(cb_add_text.get()).replace('\n', '')

				#print(new_icon)

				coordinate_icons='*'

				path=(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/ui_icon_equipment.dds') #'res/default_ui/ui_icon_equipment.dds'
		#		image = Image.open(path)
				
				if new_icon=='NO ICON':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((450, 1350, 600, 1450)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 3
inv_grid_height    = 2
inv_grid_x         = 9
inv_grid_y         = 27'''

					pyperclip.copy(coordinate_icons)

				elif new_icon=='Бандитская куртка':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((600, 0, 700, 100)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 2
inv_grid_x         = 12
inv_grid_y         = 0'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Кольчужная куртка':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((700, 1050, 800, 1150)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 2
inv_grid_x         = 14
inv_grid_y         = 21'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ПСЗ-9д "Броня Долга"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((600, 800, 700, 950)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 12
inv_grid_y         = 16'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Охотничий ПСЗ-9д':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((800, 1050, 900, 1200)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 16
inv_grid_y         = 21'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ПСЗ-9Мд "Универсальная защита"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((800, 800, 900, 950)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 16
inv_grid_y         = 16'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ССП-99 "Эколог"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((900, 650, 1000, 800)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 18
inv_grid_y         = 13'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Экзоскелет':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((700, 650, 800, 800)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 14
inv_grid_y         = 13'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Комбинезон наемника':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((200, 750, 300, 900)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 4
inv_grid_y         = 15'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Укрепленный комбез':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((900, 1050, 1000, 1200)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 18
inv_grid_y         = 21'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Армейский бронекостюм':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((500, 1200, 600, 1300)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 2
inv_grid_x         = 10
inv_grid_y         = 24'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Комбинезон монолита':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((500, 800, 600, 950)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 10
inv_grid_y         = 16'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Аномальная кожанка':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((600, 1050, 700, 1150)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 2
inv_grid_x         = 12
inv_grid_y         = 21'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Кожаная куртка':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 900, 100, 1000)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 18'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Комбинезон ССП-99М':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((700, 800, 800, 950)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 14
inv_grid_y         = 16'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Комбинезон "СЕВА"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((800, 650, 900, 800)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 16
inv_grid_y         = 13'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Лечебный Берилл':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((900, 1200, 1000, 1350)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 18
inv_grid_y         = 24'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Комбинезон сталкера':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((300, 750, 400, 900)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 6
inv_grid_y         = 15'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Комбинезон Призрака':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((800, 1200, 900, 1350)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 16
inv_grid_y         = 24'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Комбинезон туриста':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((800, 1200, 900, 1350)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 16
inv_grid_y         = 24'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Бронекостюм Берилл-5М':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((500, 650, 600, 800)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 10
inv_grid_y         = 13'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Комбинезон "Страж свободы"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((400, 750, 500, 900)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 8
inv_grid_y         = 15'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Комбинезон "Ветер свободы"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((600, 650, 700, 800)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 12
inv_grid_y         = 13'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='Научный комбенизон монолита':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((1200, 450, 1300, 600)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 24
inv_grid_y         = 9'''
					pyperclip.copy(coordinate_icons)

				else:
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((450, 1350, 600, 1450)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 3
inv_grid_height    = 2
inv_grid_x         = 9
inv_grid_y         = 27'''
					pyperclip.copy(coordinate_icons)

				pyperclip.copy(coordinate_icons)
				return coordinate_icons;


			def SELF_ReloadIcon(self):
				ReloadIcon()


			def SELF_CloseInsert(self):
				wpn_icon_text=ReloadIcon()
				pyperclip.copy(wpn_icon_text)
				#ReloadIcon()
				win_shbl.destroy()
				outfit_icon_info.insert(END, pyperclip.paste())

			def CloseInsert():
				wpn_icon_text=ReloadIcon()
				pyperclip.copy(wpn_icon_text)
				#ReloadIcon()
				win_shbl.destroy()
				outfit_icon_info.insert(END, pyperclip.paste())


			win_shbl = Toplevel(root_name)
			win_shbl.title(win_name+' - выбор иконки бронекостюма')
			win_shbl.resizable(win_draw, win_draw)
			win_shbl.iconbitmap(win_icon)
			win_shbl.geometry('700x360')

			win_shbl.focus_force()

			#win_shbl.protocol('WM_DELETE_WINDOW', CloseInsert)


			f_string_table_enc_weapons_xml=open('res/default_configs/SoC/string_table_enc_weapons.xml', 'r')
			string_table_enc_weapons_xml=f_string_table_enc_weapons_xml.readlines()
			f_string_table_enc_weapons_xml.close()

			name_items=['Бандитская куртка',
			'Кольчужная куртка',
			'ПСЗ-9д "Броня Долга"',
			'Охотничий ПСЗ-9д',
			'ПСЗ-9Мд "Универсальная защита"',
			'ССП-99 "Эколог"',
			'Экзоскелет',
			'Комбинезон наемника',
			'Укрепленный комбез',
			'Комбинезон монолита',
			'Аномальная кожанка', 
			'Кожаная куртка',
			'Комбинезон ССП-99М',
			'Комбинезон "СЕВА"',
			'Лечебный Берилл',
			'Бронекостюм Берилл-5М',
			'Комбинезон сталкера',
			'Комбинезон Призрака',
			'Комбинезон туриста',
			'Комбинезон "Страж свободы"',
			'Комбинезон "Ветер свободы"',
			'Армейский бронекостюм',
			'Научный комбенизон монолита',
			'NO ICON']
			

			FrameOutfitIconDemonstration = Frame(win_shbl, bg='#f0f0f0')

			FrameSmallTitle1 = Frame(FrameOutfitIconDemonstration)
			Label(FrameSmallTitle1, text='Демонстрируемая иконка', font=(config.font_name, config.font_size)).pack(side=LEFT, anchor=N)
			#Button(FrameSmallTitle1, text='↺', font=(config.font_name, config.font_size), bd=0, fg='blue', command=ReloadIcon).pack(side=LEFT, anchor=N)
			FrameSmallTitle1.pack(side=TOP)



			#img = ImageTk.PhotoImage(Image.open(config.folder_projects+'/'+prj_name+'/gamedata/textures/ui/ui_icon_equipment.dds'))
			#img = ImageTk.PhotoImage(Image.open('res/default_ui/ui_icon_equipment_jpg.jpg'))
			 
			panel_1=Label(FrameOutfitIconDemonstration, bg='#A0522D', width=120, height=150)
			panel_1.pack()

			Label(FrameOutfitIconDemonstration, text='Выберите бронекостюм, иконоку которого хотите использовать', font=(config.font_name, config.font_size)).pack(side=TOP, anchor=N)
			Label(FrameOutfitIconDemonstration, text='Для обновления иконки в окне нажмите клавишу F5\nДля выбора иконки выберите ее и нажмите Enter', font=('Verdana', config.low_font_size)).pack()
			#Label(FrameOutfitIconDemonstration, text='Обратите внимание, иконки пистолетов выбираются через SIE.exe!', font=('Verdana', config.low_font_size), fg='red').pack()
			#reload_btn = Button(FrameWpnIconDemonstration, text='↺', font=(config.font_name, config.font_size), bd=0, fg='blue', command=ReloadIcon)
			#reload_btn.pack(side=TOP, anchor=N)

			cb_add_text=ttk.Combobox(FrameOutfitIconDemonstration, values = name_items, width=30, height=20, state="readonly")
			cb_add_text.pack(side=TOP, anchor=N)
			cb_add_text.set(name_items[len(name_items)-1])

			Label(FrameOutfitIconDemonstration, text=' ').pack()

			ttk.Button(FrameOutfitIconDemonstration, text='Применить и закрыть окно', width=35, command=CloseInsert).pack()
			
			win_shbl.bind_all('<F5>', SELF_ReloadIcon)
			win_shbl.bind_all('<Return>', SELF_CloseInsert)

			FrameOutfitIconDemonstration.pack(fill=BOTH, expand=1, side=TOP, anchor=NW)

			outfit_icon_text=ReloadIcon()

			win_shbl.mainloop()


		def InsertOutfitIcon():
			#print(str(pyperclip.paste()))
			outfit_icon_info.delete(0.0, END)
			outfit_icon_info.insert(END, str(pyperclip.paste()))

		def SELF_InsertOutfitIcon(self):
			InsertWpnIcon()

		def InsertRecommendParams():
			entry_minimum_purchase_price.delete(0, END)
			entry_maximum_purchase_price.delete(0, END)
			entry_number.delete(0, END)
			entry_chance.delete(0, END)
			entry_minimum_sale_price.delete(0, END)
			entry_maximum_sale_price.delete(0, END)


			entry_maximum_purchase_price.insert(END, '0.5')
			entry_minimum_purchase_price.insert(END, '0.7')
			entry_number.insert(END, '4')
			entry_chance.insert(END, '0.5')
			entry_minimum_sale_price.insert(END, '1')
			entry_maximum_sale_price.insert(END, '2')

		def ClickAllTraider():
			def DeletedAllTraiders():
				cvar1.set(0)
				cvar2.set(0)
				cvar3.set(0)
				cvar4.set(0)
				cvar5.set(0)
				btn_click_all.configure(text='Отметить всех', command=ClickAllTraider)



			cvar1.set(1)
			cvar2.set(1)
			cvar3.set(1)
			cvar4.set(1)
			cvar5.set(1)
			btn_click_all.configure(text='Убрать всех', command=DeletedAllTraiders)


		def is_digit(string):
			if string.isdigit():
				return True
			else:
				try:
					float(string)
					return True
				except ValueError:
					return False



		def Analyze():
			sys_name=sys_outfit_name

			if cost_outfit.get()!='' and (cost_outfit.get()).isdigit()==True and cost_outfit.get()!='0' and len(outfit_icon_info.get(0.0, END))>=3 and outfit_icon_info.get(0.0, END)!='':
				#print('OK')
				count_errors=0
				######################
				if is_digit(cost_outfit.get())==True:
					if int(cost_outfit.get())>=1:
						outfit_cost=cost_outfit.get()
					else:
						count_errors+=1
					#print(weapon_cost.get())
				else:
					count_errors+=1
				#####################
				if is_digit(entry_minimum_purchase_price.get())==True and is_digit(entry_maximum_purchase_price.get())==True:
					line_trader_generic_buy = '{0}_outfit = {1}, {2}\n'.format(sys_name, str(entry_minimum_purchase_price.get()), str(entry_maximum_purchase_price.get()))
				else:
					count_errors+=1
				######################
				if is_digit(entry_number.get())==True and is_digit(entry_chance.get())==True:
					line_supplies_start = '{0}_outfit = {1}, {2}\n'.format(sys_name, str(entry_number.get()), str(entry_chance.get()))
				else:
					count_errors+=1
				######################
				if is_digit(entry_minimum_sale_price.get())==True and is_digit(entry_maximum_sale_price.get())==True:
					line_trader_start_sell = '{0}_outfit = {1}, {2}\n'.format(sys_name, str(entry_minimum_sale_price.get()), str(entry_maximum_sale_price.get()))
				else:
					count_errors+=1
				######################
				if count_errors>=1:
					mb.showerror(win_name, 'Не все данные корректно заполнены! Проверьте заполнение формы!\n\nОБРАТИТЕ ВНИМАНИЕ!\n- Должен быть выбран хотя бы один торговец и настроены параметры этого оружия!\n- Боеприпасы должны быть в любом случае выбраны!')
				elif count_errors==0:
					#print(weapon_cost.get())

					project_name=prj_name
					
					sidor_status=str(cvar1.get())
					barman_status=str(cvar2.get())
					sakharov_status=str(cvar3.get())
					dolg_status=str(cvar4.get())
					freedom_status=str(cvar5.get())
					'''
					print(sidor_status)
					print(barman_status)
					print(sakharov_status)
					print(dolg_status)
					print(freedom_status)
					'''
					#№№№№№№№№№№№№№№№№№				
					if install_status.get()==True and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script')==False:
						#setup_naxac=install_status.get()
						#print('Добавление спавн-меню в проект...')
						shutil.unpack_archive(filename='res/default_configs/SoC/naxac.zip', extract_dir=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/')

						if add_status.get()==True:
							#dd_wpn_in_naxac
							#print('Выполняется условие 1')

							f_ui_cheat_naxac_script=open('res/default_configs/SoC/ui_cheat_naxac.script', 'r')
							lines=f_ui_cheat_naxac_script.readlines()
							f_ui_cheat_naxac_script.close()

							f_ui_cheat_naxac_script=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script', 'w')
							for word in lines:
								if re.search(re.escape('--outfits'), word):
									word = '--outfits\n	{"*** LTX-Gen outfits ***",\n'
									f_ui_cheat_naxac_script.write(word)
								elif re.search(re.escape('"*** Броня ***"'), word):
									word = '	"'+sys_outfit_name+'_outfit",\n	"*** Броня ***",\n'
									f_ui_cheat_naxac_script.write(word)
								else:
									f_ui_cheat_naxac_script.write(word)

					elif install_status.get()==True and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script')==True:
						if add_status.get()==True:
							#dd_wpn_in_naxac
							
							f_ui_cheat_naxac_script=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script', 'r')
							lines=f_ui_cheat_naxac_script.readlines()
							f_ui_cheat_naxac_script.close()

							f_ui_cheat_naxac_script=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script', 'w')

							title_section = '    {"*** LTX-Gen outfits ***",\n'

							result = ListSearch.hard('"*** LTX-Gen outfits ***"', lines)

							if result == True:
								for word in lines:
									if re.search(re.escape('"*** LTX-Gen outfits ***"'), word):									
										lines.insert(lines.index(word)+1, '    "{}_outfit",\n'.format(sys_outfit_name))
										word = lines[lines.index(word)]
										f_ui_cheat_naxac_script.write(word)
									else:
										f_ui_cheat_naxac_script.write(word)

							elif result == False:
								for word in lines:
									if re.search(re.escape('--outfits'), word):									
										lines.insert(lines.index(word)+1, title_section+'    "{}_outfit",\n'.format(sys_outfit_name))
										word = lines[lines.index(word)]
										f_ui_cheat_naxac_script.write(word)
									else:
										f_ui_cheat_naxac_script.write(word)

							f_ui_cheat_naxac_script.close()

					elif install_status.get()==False and add_status.get()==False:
						shutil.copy('res/default_configs/SoC/ui_main_menu.script', config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/')
					#№№№№№№№№№№№№№№№№№

					copy_file=''

					k=0

					# line_trader_generic_buy | line_supplies_start | line_trader_start_sell

					#=================СИДОРОВИЧ=========================================
					#ltx_gen_section = '' #';LTX-Gen section\n'
					if sidor_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_trader.ltx')==False:
						copy_file='trade_trader.ltx'

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[trader_generic_buy]'), word):
								word = '[trader_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_fabric]'), word):
								word = '[supplies_after_fabric]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[trader_start_sell]'), word):
								word = '[trader_start_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[trader_after_fabric_sell]'), word):
								word = '[trader_after_fabric_sell]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()


					elif sidor_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_trader.ltx')==True:
						copy_file='trade_trader.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[trader_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_fabric]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[trader_start_sell]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[trader_after_fabric_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()
						
					    
					#===================================================================

					
					#=================БАРМЕН============================================
					# line_trader_generic_buy | line_supplies_start | line_trader_start_sell

					if barman_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_barman.ltx')==False:                
						copy_file='trade_barman.ltx'

						shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[barman_generic_buy]'), word):
								word = '[barman_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_darkvalley]'), word):
								word = '[supplies_after_darkvalley]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_brain]'), word):
								word = '[supplies_after_brain]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[barman_start_sell]'), word):
								word = '[barman_start_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[barman_after_darkvalley_sell]'), word):
								word = '[barman_after_darkvalley_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[barman_after_brain_sell]'), word):
								word = '[barman_after_brain_sell]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()

					elif barman_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_barman.ltx')==True:
						copy_file='trade_barman.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[barman_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_darkvalley]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_brain]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[barman_start_sell]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[barman_after_darkvalley_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[barman_after_brain_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()

					    
					#===================================================================


					#=====================ПЕТРЕНКО======================================
					# line_trader_generic_buy | line_supplies_start | line_trader_start_sell
					if dolg_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_dolg.ltx')==False:                
						copy_file='trade_dolg.ltx'

						shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[dolg_generic_buy]'), word):
								word = '[dolg_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_rg6]'), word):
								word = '[supplies_after_rg6]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[dolg_start_sell]'), word):
								word = '[dolg_start_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[dolg_after_rg6_sell]'), word):
								word = '[dolg_after_rg6_sell]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()

					elif dolg_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_dolg.ltx')==True:
						copy_file='trade_dolg.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[dolg_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_rg6]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[dolg_start_sell]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[dolg_after_rg6_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()
					                    
					#elif barman_status=='False':
						#k+=1                    

					#===================================================================



					#=====================САХАРОВ======================================
					# line_trader_generic_buy | line_supplies_start | line_trader_start_sell
					if sakharov_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_ecolog.ltx')==False:                
						copy_file='trade_ecolog.ltx'

						shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[ecolog_generic_buy]'), word):
								word = '[ecolog_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_brain]'), word):
								word = '[supplies_after_brain]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[ecolog_start_sell]'), word):
								word = '[ecolog_start_sell]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[ecolog_after_brain_sell]'), word):
								word = '[ecolog_after_brain_sell]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()

					elif sakharov_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_ecolog.ltx')==True:
						copy_file='trade_ecolog.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[ecolog_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_brain]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[ecolog_start_sell]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[ecolog_after_brain_sell]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()
						                    
					#elif sakharov_status=='False':
						#k+=1                    

					#===================================================================            


					#=====================СКРЯГА========================================
					if freedom_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_freedom.ltx')==False:                
						copy_file='trade_freedom.ltx'

						shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

						f=open('res/default_configs/SoC/'+copy_file, 'r')
						lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for word in lines:
							if re.search(re.escape('[freedom_generic_buy]'), word):
								word = '[freedom_generic_buy]\n'+line_trader_generic_buy
								f_write.write(word)
							elif re.search(re.escape('[supplies_start]'), word):
								word = '[supplies_start]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_dolg]'), word):
								word = '[supplies_after_dolg]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[supplies_after_pavlik]'), word):
								word = '[supplies_after_pavlik]\n'+line_supplies_start
								f_write.write(word)
							elif re.search(re.escape('[freedom_sell_start]'), word):
								word = '[freedom_sell_start]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[freedom_sell_after_dolg]'), word):
								word = '[freedom_sell_after_dolg]\n'+line_trader_start_sell
								f_write.write(word)
							elif re.search(re.escape('[freedom_sell_after_pavlik]'), word):
								word = '[freedom_sell_after_pavlik]\n'+line_trader_start_sell
								f_write.write(word)
							else:
								f_write.write(word)

						f_write.close()

					elif freedom_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_freedom.ltx')==True:
						copy_file='trade_freedom.ltx'

						f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
						trader_lines=f.readlines()
						f.close()

						f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

						for trader_word in trader_lines:
							if re.search(re.escape('[freedom_generic_buy]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_dolg]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[supplies_after_pavlik]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[freedom_sell_start]'), trader_word):

								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[freedom_sell_after_dolg]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell) 
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							elif re.search(re.escape('[freedom_sell_after_pavlik]'), trader_word):
								
								trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
								trader_new_word = trader_lines[trader_lines.index(trader_word)]
								f_write.write(trader_new_word)

							else:
								f_write.write(trader_word)

						f_write.close()
					                        
					#elif freedom_status=='False':
						#k+=1  
					
					
					#print('Координаты иконки:\n'+outfit_icon_info.get(0.0, END))

					#print('Цена: {} рублей'.format(outfit_cost))

					#print('ВСЕ ГОТОВО\nПЕРЕХОД НА СЛЕДУЮЩИЙ ШАГ!!!')
					FrameOutfitS3.pack_forget()
					AddOutfitParameters.window(root_name=root_name, prj_name=prj_name, sys_outfit_name=sys_outfit_name, text_coordinate_icons=outfit_icon_info.get(0.0, END), outf_cost=cost_outfit.get(), outfit_inv_name=inv_name_outfit)

			else:
				mb.showerror(win_name, '''Не все поля были заполнены! Проверьте заполнение еще раз!

		Цена не должна быть равна 0 (минимально 1).

		Координаты иконки должны быть внесены в специальном поле в любом случае, даже если иконка не задана.

		Броня может быть добавлена или в спавн-меню или любому торговцу. Можно выбрать всех торговцев.''')


		sys_name=sys_outfit_name

		FrameOutfitS3 = Frame(root_name, bg='#f0f0f0')
		#-----

		Label(FrameOutfitS3, text='Введите цену нового бронекостюма.', font=(config.font_name, config.font_size)).pack()

		cost_outfit = ttk.Entry(FrameOutfitS3, width=35)
		cost_outfit.pack()
		cost_outfit.focus()

		##########

		FrameAllWidgtsOutfit = Frame(FrameOutfitS3)

		FrameAddSpawnMenu = Frame(FrameAllWidgtsOutfit)

		Label(FrameAddSpawnMenu, text='Добавление брони в spawn-menu', font=(config.font_name, config.font_size)).pack()
		#Label(FrameAddSpawnMenu, text=' ').pack()

		FrameCheckbuttons_naxac = Frame(FrameAddSpawnMenu)

		install_status = BooleanVar()
		install_status.set(1)
		install_spawn_menu = ttk.Checkbutton(FrameCheckbuttons_naxac, text="Установить spawn-menu by naxaс\nс денежным трейнером tankalxat34.", variable=install_status, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 9), justify=LEFT)
		install_spawn_menu.pack(anchor=W)
		        
		add_status = BooleanVar()
		add_status.set(1)
		add_outfit_in_spawn_menu = ttk.Checkbutton(FrameCheckbuttons_naxac, text="Добавить броню в данное spawn-menu.", variable=add_status, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 9), justify=LEFT)
		add_outfit_in_spawn_menu.pack(anchor=W)

		FrameCheckbuttons_naxac.pack()

		Button(FrameAddSpawnMenu, text='Для получения дополнительной\nинформации нажмите сюда', fg='blue', bd=0, command=step5_help_naxac_outfit).pack()

		######

		Label(FrameAddSpawnMenu, text='\nДобавление иконки брони', font=(config.font_name, config.font_size)).pack()


		FrameBtns = Frame(FrameAddSpawnMenu)
		w=35
		ttk.Button(FrameBtns, text='Открыть шаблон в SIE.exe', command=OpenSIE, width=w).pack(side=TOP, anchor=N)
		ttk.Button(FrameBtns, text='Выбрать классическую иконку', width=w, command=AddClassicOutfitIcon).pack(side=BOTTOM, anchor=N)
		FrameBtns.pack()

		Label(FrameAddSpawnMenu, text='Вставьте сюда координаты иконки', font=('Verdana', config.low_font_size)).pack()

		#insert_text=wpn_icon_text


		outfit_icon_info = Text(FrameAddSpawnMenu, bd=1, font=(config.low_font_name, config.low_font_size-1), wrap=WORD, width=25, height=4)
		outfit_icon_info.pack(side=BOTTOM)

		Button(FrameAddSpawnMenu, text='[Вставить]', bd=0, fg='blue', command=InsertOutfitIcon).pack(side=BOTTOM)

		FrameAddSpawnMenu.pack(side=LEFT, expand=1, anchor=N)

		##########



		FrameListTraiders = Frame(FrameAllWidgtsOutfit)

		Label(FrameListTraiders, text='\n\nВыберете торговцев, которым\nхотите добавить новую броню.', font=(config.font_name, config.font_size)).pack()


		FrameCheckbuttonsTraider = Frame(FrameListTraiders)

		cvar1 = BooleanVar()
		cvar1.set(0)
		c1 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Сидорович", variable=cvar1, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c1.pack(anchor=W)
				        
		cvar2 = BooleanVar()
		cvar2.set(0)
		c2 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Бармен", variable=cvar2, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c2.pack(anchor=W)
				        
		cvar3 = BooleanVar()
		cvar3.set(0)
		c3 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Сахаров", variable=cvar3, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c3.pack(anchor=W)
				        
		cvar4 = BooleanVar()
		cvar4.set(0)
		c4 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Петренко", variable=cvar4, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c4.pack(anchor=W)
				        
		cvar5 = BooleanVar()
		cvar5.set(0)
		c5 =ttk.Checkbutton(FrameCheckbuttonsTraider, text="Скряга", variable=cvar5, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c5.pack(anchor=W)

		FrameCheckbuttonsTraider.pack()

		btn_click_all=ttk.Button(FrameListTraiders, text='Отметить всех', width=20, command=ClickAllTraider)
		btn_click_all.pack()



		FrameListTraiders.pack(side=LEFT, fill=Y, expand=1, anchor=S)




		FrameParamsInTraiders = Frame(FrameAllWidgtsOutfit)

		Label(FrameParamsInTraiders, text='Настройте параметры продажи', font=(config.font_name, config.font_size)).pack()

		Button(FrameParamsInTraiders, text='Для получения дополнительной\nинформации нажмите сюда', fg='blue', bd=0, command=step5_help).pack()

		Label(FrameParamsInTraiders, text='Секция [trader_generic_buy]\n({0}_outfit = {2} {1})'.format(sys_name, 'минимальная цена покупки %', 'максимальная цена покупки %,\n'), font=(config.font_name, config.low_font_size)).pack()

		####--                           trader_generic_buy
		Frame_trader_generic_buy = Frame(FrameParamsInTraiders)
		Label(Frame_trader_generic_buy, text='{}_outfit  ='.format(sys_name), font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)#'Минимальная цена покупки (%):', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		Label(Frame_trader_generic_buy, text=' ').pack(side=LEFT, anchor=N)

		entry_minimum_purchase_price=ttk.Entry(Frame_trader_generic_buy, width=10)
		entry_minimum_purchase_price.pack(side=LEFT, anchor=N)

		Label(Frame_trader_generic_buy, text=',', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)

		entry_maximum_purchase_price=ttk.Entry(Frame_trader_generic_buy, width=10)
		entry_maximum_purchase_price.pack(side=LEFT, anchor=N)
		Frame_trader_generic_buy.pack()




		Label(FrameParamsInTraiders, text='Секция [supplies_start]\n({0}_outfit = {1}, {2})'.format(sys_name, 'количество', 'вероятность появления'), font=(config.font_name, config.low_font_size)).pack()

		#  supplies_start
		Frame_supplies_start = Frame(FrameParamsInTraiders)
		Label(Frame_supplies_start, text='{}_outfit  ='.format(sys_name), font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)#'Минимальная цена покупки (%):', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		Label(Frame_supplies_start, text=' ').pack(side=LEFT, anchor=N)

		entry_number=ttk.Entry(Frame_supplies_start, width=10)
		entry_number.pack(side=LEFT, anchor=N)

		Label(Frame_supplies_start, text=',', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)

		entry_chance=ttk.Entry(Frame_supplies_start, width=10)
		entry_chance.pack(side=LEFT, anchor=N)
		Frame_supplies_start.pack()




		Label(FrameParamsInTraiders, text='Секция [trader_start_sell]\n({0}_outfit = {1} {2})'.format(sys_name, 'минимальная цена продажи,\n', 'максимальная цена продажи'), font=(config.font_name, config.low_font_size)).pack()

		#  supplies_start
		Frame_trader_start_sell = Frame(FrameParamsInTraiders)
		Label(Frame_trader_start_sell, text='{}_outfit  ='.format(sys_name), font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)#'Минимальная цена покупки (%):', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		Label(Frame_trader_start_sell, text=' ').pack(side=LEFT, anchor=N)

		entry_minimum_sale_price=ttk.Entry(Frame_trader_start_sell, width=10)
		entry_minimum_sale_price.pack(side=LEFT, anchor=N)

		Label(Frame_trader_start_sell, text=',', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)

		entry_maximum_sale_price=ttk.Entry(Frame_trader_start_sell, width=10)
		entry_maximum_sale_price.pack(side=LEFT, anchor=N)

		Label(Frame_trader_start_sell, text='\n').pack(side=LEFT, anchor=N)

		Frame_trader_start_sell.pack()



		ttk.Button(FrameParamsInTraiders, text='Рекомендуемые значения', width=30, command=InsertRecommendParams).pack()

		FrameParamsInTraiders.pack(side=LEFT, fill=Y, expand=1)

		FrameAllWidgtsOutfit.pack(side=TOP, fill=BOTH, expand=1)



		FrameAllWidgtsOutfit.pack()




		#-----
		FrameBtn = LabelFrame(FrameOutfitS3, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=Analyze).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameOutfitS3.pack(side=BOTTOM, fill=BOTH, expand=1)






class Outfit_description_add():

	def window(root_name, prj_name, sys_outfit_name):
		def LoadFromFile():
			try:
				path_txt_description = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ', filetypes=(("TXT files", "*.txt"), ("All files", "*.*")))
		        
				process1=str(path_txt_description)[:-3]
				path_txt_description=process1[2:]            
		        
				f=open(str(path_txt_description), 'r', encoding='utf-8')
				description_file=f.read()
				f.close()
		        
				text_description_outfit.insert(END, description_file)
			except FileNotFoundError:
				#mb.showerror(win_name, 'Файл не был загружен!')
				text_description_outfit.insert(END, '')


		def Analyze(root_name, prj_name, sys_outfit_name):
			inv_description_outfit=''
			n=3

			if name_outfit.get()!='':
				if len(text_description_outfit.get(0.0, END))<=n:
					inv_description_outfit='Бронекостюм имеет системное имя "{0}".{2}{2}Создано в приложении {1} '.format(sys_outfit_name, win_name, chr(92)+'n')+author_label

				elif len(text_description_outfit.get(0.0, END))>n:
					inv_description_outfit=(text_description_outfit.get(0.0, END)).replace('\n', chr(92)+'n')

				#print(inv_description_outfit)
				inv_name_outfit = name_outfit.get()
				#if re.search(r'\bзвать\b', 'меня звать Олег, мне 35 лет'):
				#shutil.copy('res/default_configs/SoC/string_table_outfit.xml', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/'))

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_outfit.xml')==False:
					default_table = open('res/default_configs/SoC/string_table_outfit.xml', 'r')
					table_list_old = default_table.readlines()
					default_table.close()

					table_list = list(table_list_old)

					table_in_project = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_outfit.xml', 'w')
					
					for word in table_list:
						if re.search('</string_table>', word):
							new_word='''	<string id="{sys_name}_outfit_description">
		<text>{inv_desc_name}</text>
	</string>
	<string id="{sys_name}_outfit_name">
		<text>{inv_name_name}</text>
	</string>
</string_table>'''.format(sys_name=sys_outfit_name, inv_desc_name=inv_description_outfit, inv_name_name=inv_name_outfit)

							table_in_project.write(new_word)

						else:
							table_in_project.write(word)

					table_in_project.close()

				elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_outfit.xml')==True:


					table_in_project = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_outfit.xml', 'r')
					table_list = table_in_project.readlines()
					table_in_project.close()

					table_in_project = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_outfit.xml', 'w')
					
					for word in table_list:
						if re.search('</string_table>', word):
							new_word='''	<string id="{sys_name}_outfit_description">
		<text>{inv_desc_name}</text>
	</string>
	<string id="{sys_name}_outfit_name">
		<text>{inv_name_name}</text>
	</string>
</string_table>'''.format(sys_name=sys_outfit_name, inv_desc_name=inv_description_outfit, inv_name_name=inv_name_outfit)

							table_in_project.write(word.replace(word, new_word))

						else:
							table_in_project.write(word)

					table_in_project.close()

				FrameOutfitS2.pack_forget()
				AddOutfitInTraiders.window(root_name=root_name, prj_name=prj_name, sys_outfit_name=sys_outfit_name, inv_name_outfit=inv_name_outfit)

			else:
				mb.showerror(win_name, 'Необходимо задать имя бронекостюма!\n\nЗадавать описание не обязательно, программа сама его сделает следующим:\n'+'"Бронекостюм имеет системное имя "{0}".{2}{2}Создано в приложении {1} by tankalxat34 (tnkSoftware)"'.format(sys_outfit_name, win_name, chr(92)+'n'))


		def Rediction_Function_Analyze():
			Analyze(root_name=root_name, prj_name=prj_name, sys_outfit_name=sys_outfit_name)




		FrameOutfitS2 = Frame(root_name, bg='#f0f0f0')
		#-----



		FrameReturnInvOutfitName = Frame(FrameOutfitS2, bg='#f0f0f0')
		Label(FrameReturnInvOutfitName, text='Введите название нового бронекостюма.', font=(config.font_name, config.font_size)).pack()

		name_outfit=ttk.Entry(FrameReturnInvOutfitName, width=55)
		name_outfit.pack()
		name_outfit.focus()

		#Label(FrameReturnInvOutfitName, text=' ').pack()

		FrameReturnInvOutfitName.pack(side=TOP, fill=X)





		FrameReturnInvOutfitText = Frame(FrameOutfitS2, bg='#f0f0f0')

		Label(FrameReturnInvOutfitText, text='Введите описание нового бронекостюма.', font=(config.font_name, config.font_size)).pack()

		Button(FrameReturnInvOutfitText, text='Для загрузки описания из txt-файла нажмите на эту надпись', fg='blue', bd=0, bg='#f0f0f0', command=LoadFromFile).pack()

		#text_description_weapon = Text(FrameReturnInvOutfitText, bd=1, font=(config.low_font_name, config.low_font_size-1), width=100, height=13)
		text_description_outfit = Text(FrameReturnInvOutfitText, bd=1, font=(config.low_font_name, config.low_font_size-1), wrap=WORD, width=110, height=19)
		text_description_outfit.pack(side=LEFT)#, expand=1)
		#text.focus()

		scrollY = Scrollbar(FrameReturnInvOutfitText, command=text_description_outfit.yview)
		scrollY.pack(side=RIGHT, fill=Y)  
		text_description_outfit.config(yscrollcommand=scrollY.set)

		Label(FrameReturnInvOutfitName, text=' ').pack()

		FrameReturnInvOutfitText.pack(side=TOP, fill=X)

		#-----
		FrameBtn = LabelFrame(FrameOutfitS2, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=Rediction_Function_Analyze).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameOutfitS2.pack(side=BOTTOM, fill=BOTH, expand=1)



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

			sys_outfit_name = entry_system_outfit_name.get()

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

			sys_outfit_name = entry_system_outfit_name.get()

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

			sys_outfit_name = entry_system_outfit_name.get()

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
					Outfit_description_add.window(root_name=root_name, prj_name=prj_name, sys_outfit_name=entry_system_outfit_name.get())

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












##########################################################################################################################################################################################
##########################################################################################################################################################################################
###################################ОРУЖИЕ#################################################################################################################################################
##########################################################################################################################################################################################
##########################################################################################################################################################################################
class AddWeaponInTraders():

	def window(root_name, prj_name, sys_name, game_wnp_name):
		def AddIconFromShablon():
			global panel_1;


			def ReloadIcon():
				new_icon=(cb_add_text.get()).replace('\n', '')

				#print(new_icon)

				coordinate_icons='*'

				path=(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/ui_icon_equipment.dds') #'res/default_ui/ui_icon_equipment.dds'
		#		image = Image.open(path)
				
				if new_icon=='NO ICON':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((450, 1350, 600, 1450)))
					panel_1.configure(image=img2)
					panel_1.image = img2


				elif new_icon=='СВДм 2':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 0, 300, 100)))			
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 6
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 0'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='СВУмк2':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 100, 250, 200)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 2'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Винтарь ВС':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 200, 250, 300)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 4'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ТРс 301':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 300, 250, 400)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 6'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Бульдог-6':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 400, 200, 500)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 4
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 8'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ГП37':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 500, 250, 600)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 10'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ИЛ86':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 600, 250, 700)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 12'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Гром С14':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 700, 200, 800)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 4
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 14'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Акм 74/2У':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 800, 200, 900)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 4
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 16'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Обокан снайперский':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 1000, 250, 1100)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 20'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='СИП снайперский':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 1100, 250, 1200)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 22'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Облегченная ИЛ 86':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 1200, 250, 1300)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 24'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ТРс 301 снайперская':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 1300, 250, 1400)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 26'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Обокан штурмовой':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 1400, 250, 1500)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 28'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Скоростр. Акм 74/2':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 1500, 250, 1600)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 30'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='СГИ 5,45':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 1600, 250, 1700)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 0
inv_grid_y         = 32'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='СПСА-14 нарезной':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 1700, 250, 1750)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 1
inv_grid_x         = 0
inv_grid_y         = 34'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Чейзер "Свобода"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((0, 1750, 250, 1800)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 1
inv_grid_x         = 0
inv_grid_y         = 35'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='РПГ-7у':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((300, 0, 550, 50)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 1
inv_grid_x         = 6
inv_grid_y         = 0'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Обрез двустволки':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((300, 50, 450, 100)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 3
inv_grid_height    = 1
inv_grid_x         = 6
inv_grid_y         = 1'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Обокан':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((300, 100, 550, 200)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 6
inv_grid_y         = 2'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Акм 74/2':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 250, 500, 350)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 5
inv_grid_y         = 5'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='СГИ 5к':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 350, 500, 450)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 5
inv_grid_y         = 7'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ФТ 200М':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 450, 450, 550)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 4
inv_grid_height    = 2
inv_grid_x         = 5
inv_grid_y         = 9'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Гадюка 5':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 550, 400, 600)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 3
inv_grid_height    = 1
inv_grid_x         = 5
inv_grid_y         = 11'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Акм 74/2У спецназ':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 1000, 450, 1100)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 5
inv_grid_y         = 20'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Бесшумная Гадюка 5':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 1100, 450, 1150)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 4
inv_grid_height    = 1
inv_grid_x         = 5
inv_grid_y         = 22'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='СВДм 2 "Дальнобойщик"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 1150, 550, 1250)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 6
inv_grid_height    = 2
inv_grid_x         = 5
inv_grid_y         = 23'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ИЛ 86 Баланс':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 1250, 500, 1350)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 5
inv_grid_y         = 25'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Бульдог-6 м209':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 1350, 450, 1450)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 4
inv_grid_height    = 2
inv_grid_x         = 5
inv_grid_y         = 27'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='"Гром" 5.45':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 1450, 450, 1550)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 4
inv_grid_height    = 2
inv_grid_x         = 5
inv_grid_y         = 29'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Снайперский ВЛА':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 1550, 450, 1650)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 4
inv_grid_height    = 2
inv_grid_x         = 5
inv_grid_y         = 31'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Гадюка 5 9х18':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 1650, 400, 1700)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 3
inv_grid_height    = 1
inv_grid_x         = 5
inv_grid_y         = 33'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='ТОС-34':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((600, 100, 900, 150)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 6
inv_grid_height    = 1
inv_grid_x         = 12
inv_grid_y         = 2'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='СПСА14':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((600, 150, 850, 200)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 1
inv_grid_x         = 12
inv_grid_y         = 3'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Чейзер 13':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((500, 250, 750, 300)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 1
inv_grid_x         = 10
inv_grid_y         = 5'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Гаусс-пушка':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((500, 300, 750, 400)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 10
inv_grid_y         = 6'''
					pyperclip.copy(coordinate_icons)


				elif new_icon=='ВСС Винторез m1':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((750, 1350, 1000, 1450)))
					panel_1.configure(image=img2)
					panel_1.image = img2

					coordinate_icons='''inv_grid_width     = 5
inv_grid_height    = 2
inv_grid_x         = 15
inv_grid_y         = 27'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='СВД Егерь m1':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((700, 1450, 1000, 1550)))
					panel_1.configure(image=img2)
					panel_1.image = img2 

					coordinate_icons='''inv_grid_width     = 6
inv_grid_height    = 2
inv_grid_x         = 14
inv_grid_y         = 29'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='Спецавтомат "ВЛА"':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((750, 200, 950, 300)))
					panel_1.configure(image=img2)
					panel_1.image = img2 

					coordinate_icons='''inv_grid_width     = 4
inv_grid_height    = 2
inv_grid_x         = 15
inv_grid_y         = 4'''
					pyperclip.copy(coordinate_icons)

				elif new_icon=='NO ICON (rus)':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((700, 1550, 1000, 1650)))
					panel_1.configure(image=img2)
					panel_1.image = img2 

					coordinate_icons='''inv_grid_width     = 6
inv_grid_height    = 2
inv_grid_x         = 14
inv_grid_y         = 31'''
					pyperclip.copy(coordinate_icons)

				else:
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((700, 1550, 1000, 1650)))
					panel_1.configure(image=img2)
					panel_1.image = img2 

					coordinate_icons='''inv_grid_width     = 6
inv_grid_height    = 2
inv_grid_x         = 14
inv_grid_y         = 31'''
					pyperclip.copy(coordinate_icons)

				pyperclip.copy(coordinate_icons)
				return coordinate_icons;





			def SELF_ReloadIcon(self):
				ReloadIcon()


			def SELF_CloseInsert(self):
				wpn_icon_text=ReloadIcon()
				pyperclip.copy(wpn_icon_text)
				#ReloadIcon()
				win_shbl.destroy()
				wpn_icon_info.insert(END, pyperclip.paste())

			def CloseInsert():
				wpn_icon_text=ReloadIcon()
				pyperclip.copy(wpn_icon_text)
				#ReloadIcon()
				win_shbl.destroy()
				wpn_icon_info.insert(END, pyperclip.paste())





			win_shbl = Toplevel(root_name)
			win_shbl.title(win_name+' - выбор иконки оружия')
			win_shbl.resizable(win_draw, win_draw)
			win_shbl.iconbitmap(win_icon)
			win_shbl.geometry('700x400')

			win_shbl.focus_force()

			f_string_table_enc_weapons_xml=open('res/default_configs/SoC/string_table_enc_weapons.xml', 'r')
			string_table_enc_weapons_xml=f_string_table_enc_weapons_xml.readlines()
			f_string_table_enc_weapons_xml.close()

			name_items=[]
			a='0'
			a_process='0'
			i=0            
			for i in range(0, len(string_table_enc_weapons_xml)):
				if i!=0 and i%3==0 and i!=3 and i>=445: 
					#print(i)                                                    #i!=0 and i%3==0 and i!=3 - если показать все содержимое
					id_items_process1=string_table_enc_weapons_xml[i]           #i!=0 and i%3==0 and i<=149 and i!=3 - если показать только патроны
			                            
					a_process=id_items_process1.replace('</text>', '')          #---
					a=a_process.replace('		<text>', '') #		<text>
					name_items.append(a)


			name_items.append('Обокан')
			name_items.append('Обокан снайперский')
			name_items.append('Обокан штурмовой')
			name_items.append('СГИ 5,45')
			name_items.append('Чейзер "Свобода"')
			name_items.append('СВД Егерь m1')
			name_items.append('ВСС Винторез m1')
			name_items.append('NO ICON (rus)')
			name_items.append('NO ICON')


			FrameWpnIconDemonstration = Frame(win_shbl, bg='#f0f0f0')

			FrameSmallTitle1 = Frame(FrameWpnIconDemonstration)
			Label(FrameSmallTitle1, text='Демонстрируемая иконка', font=(config.font_name, config.font_size)).pack(side=LEFT, anchor=N)
			#Button(FrameSmallTitle1, text='↺', font=(config.font_name, config.font_size), bd=0, fg='blue', command=ReloadIcon).pack(side=LEFT, anchor=N)
			FrameSmallTitle1.pack(side=TOP)



			#img = ImageTk.PhotoImage(Image.open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/ui_icon_equipment.dds'))
			#img = ImageTk.PhotoImage(Image.open('res/default_ui/ui_icon_equipment_jpg.jpg'))
			 
			panel_1=Label(FrameWpnIconDemonstration, bg='#A0522D', width=320, height=120)
			panel_1.pack()

			Label(FrameWpnIconDemonstration, text='\nВыберите оружие, иконоку которого хотите использовать', font=(config.font_name, config.font_size)).pack(side=TOP, anchor=N)
			Label(FrameWpnIconDemonstration, text='Для обновления иконки в окне нажмите клавишу F5', font=('Verdana', config.low_font_size)).pack()
			Label(FrameWpnIconDemonstration, text='Обратите внимание, иконки пистолетов выбираются через SIE.exe!', font=('Verdana', config.low_font_size), fg='red').pack()
			#reload_btn = Button(FrameWpnIconDemonstration, text='↺', font=(config.font_name, config.font_size), bd=0, fg='blue', command=ReloadIcon)
			#reload_btn.pack(side=TOP, anchor=N)

			cb_add_text=ttk.Combobox(FrameWpnIconDemonstration, values = name_items, width=25, height=20, state="readonly")
			cb_add_text.pack(side=TOP, anchor=N)
			cb_add_text.set(name_items[len(name_items)-1])

			Label(FrameWpnIconDemonstration, text=' ').pack()

			ttk.Button(FrameWpnIconDemonstration, text='Применить и закрыть окно', width=35, command=CloseInsert).pack()
			
			win_shbl.bind_all('<F5>', SELF_ReloadIcon)
			win_shbl.bind_all('<Return>', SELF_CloseInsert)

			FrameWpnIconDemonstration.pack(fill=BOTH, expand=1, side=TOP, anchor=NW)

			wpn_icon_text=ReloadIcon()

			win_shbl.mainloop()



		def AddAmmoIconFromShablon():

			def ReloadAmmoIcon():
				ammo_name=(ammo_list_widget.get()).replace('\n', '')

				coordinate__icons='*'

				path=(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/ui_icon_equipment.dds') #'res/default_ui/ui_icon_equipment.dds'

				if ammo_name=='NO ICON' or ammo_name=='-не выбрано-': # биноколь в данном случае
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((800, 400, 900, 450)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2 

					#coordinate_icons=''''''
					#pyperclip.copy(coordinate_icons)
				elif ammo_name=='Патроны .45ACP' or ammo_name=='.45ACP':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((450, 600, 550, 650)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2 

				elif ammo_name=='.45ACP Гидрошок' or ammo_name=='.45Гидро':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((350, 600, 450, 650)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2 

				elif ammo_name=='Патроны 12х70 дробь' or ammo_name=='12х70 др.':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((650, 450, 750, 500)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2 

				elif ammo_name=='Патроны 12x76 дротик' or ammo_name=='12x76 дт.':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((650, 500, 750, 550)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2 

				elif ammo_name=='Патроны 12x76 жекан' or ammo_name=='12x76 жк.':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((550, 500, 650, 550)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2 

				elif ammo_name=='Патроны 5,45x39 мм БП' or ammo_name=='5,45 БП':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((600, 550, 700, 600)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2 

				elif ammo_name=='Патроны 5,45x39 мм' or ammo_name=='5.45x39':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((800, 550, 900, 600)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2 

				elif ammo_name=='Патроны 5,56x45 мм AP' or ammo_name=='5,56 AP':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((500, 550, 600, 600)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='5,56х45 мм SS109' or ammo_name=='5,56 SS':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((700, 550, 800, 600)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Патроны 7,62x54 мм 7H1' or ammo_name=='7,62 7H1':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((750, 450, 850, 500)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Патроны 7,62х54R 7Н14' or ammo_name=='7,62 7Н14':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((850, 450, 950, 500)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Патроны 7,62x54 мм БП' or ammo_name=='7,62 БП':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((750, 500, 850, 550)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Патроны 9х18 мм' or ammo_name=='9х18':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((550, 600, 600, 650)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Патроны 9х18 мм +P+' or ammo_name=='9х18 +P+':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((600, 600, 650, 650)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='9х19mm ЦМО' or ammo_name=='9х19 ЦМО':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((750, 600, 800, 650)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Патроны 9x19mm PBP' or ammo_name=='9x19 PBP':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((700, 600, 750, 650)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Патроны 9x39 мм СП-6' or ammo_name=='9x39 СП-6':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 600, 350, 650)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Патроны 9х39 мм ПАБ-9' or ammo_name=='9х39 ПАБ9':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((850, 500, 950, 550)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Патроны 9х39 мм СП-5' or ammo_name=='9х39 СП-5':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((900, 550, 1000, 600)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Гаусс-патроны' or ammo_name=='Гаусс':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((200, 700, 250, 750)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Заряд M209' or ammo_name=='M209':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((250, 650, 300, 700)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Заряд ОГ-7B' or ammo_name=='ОГ-7B':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((750, 950, 900, 1000)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Заряд ВОГ-25' or ammo_name=='ВОГ-25':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((950, 450, 1000, 500)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				elif ammo_name=='Заряд ВОГ-25P' or ammo_name=='ВОГ-25P':
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((950, 500, 1000, 550)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2

				else:
					image = Image.open(path)
					img2 = ImageTk.PhotoImage(image.crop((800, 400, 900, 450)))
					ammo_panel.configure(image=img2)
					ammo_panel.image = img2 



			def SELF_ReloadAmmoIcon(self):
				ReloadAmmoIcon()



			def AddNewAmmo(self):
				if added_ammo_list.size()<=4 and ammo_list_widget.get()!='-не выбрано-' and ammo_list_widget.get() not in added_ammo_list.get(0, added_ammo_list.size()-1):
					ReloadAmmoIcon()
					ammo_add_name = ammo_list_widget.get()
					added_ammo_list.insert(END, ammo_add_name)

				elif added_ammo_list.size()>4:
					mb.showerror(win_name, 'Нельзя добавить больше 5 боеприпасов!')

				elif ammo_list_widget.get()=='-не выбрано-':
					mb.showerror(win_name, 'Этот боеприпас невозможно добавить к этому оружию! Попробуйте добавить другой!')

				elif ammo_list_widget.get() in added_ammo_list.get(0, added_ammo_list.size()-1):
					mb.showerror(win_name, 'Боеприпас {} уже был добавлен ранее!'.format((ammo_list_widget.get()).replace('\n', '')))



			def DeleteAmmoInListbox(self):
				selection = added_ammo_list.curselection()
				added_ammo_list.delete(selection[0])

			def ReloadIconAddedAmmo(self):
				selection = added_ammo_list.curselection()
				tuple_ammo = added_ammo_list.get(0, added_ammo_list.size()-1)
				g = len(ammo_items)-int(selection[0])
				ammo_list_widget.set((tuple_ammo[len(ammo_items)-g]).replace('\n', ''))
				ReloadAmmoIcon()


			def SaveAmmoWpn():
				if len(added_ammo_list.get(0, added_ammo_list.size()-1))>=1:
					ammo = added_ammo_list.get(0, added_ammo_list.size()-1)

					#pyperclip.copy(ammo)
					added_ammo_list_win.delete(0, added_ammo_list_win.size()-1)

					for i in range(0, len(ammo)):
						added_ammo_list_win.insert(END, ammo[i])

					win_ammo_shbl.destroy()

				else:
					win_ammo_shbl.destroy()

			def SELF_SaveAmmoWpn(self):
				SaveAmmoWpn()



			win_ammo_shbl = Toplevel(root_name)
			win_ammo_shbl.title(win_name+' - выбор боеприпасов оружия')
			win_ammo_shbl.resizable(win_draw, win_draw)
			win_ammo_shbl.iconbitmap(win_icon)
			win_ammo_shbl.geometry('700x400')

			win_ammo_shbl.focus_force()

			win_ammo_shbl.protocol('WM_DELETE_WINDOW', SaveAmmoWpn)

			win_ammo_shbl.bind_all('<F5>', SELF_ReloadAmmoIcon)

			f_string_table_enc_weapons_xml=open('res/default_configs/SoC/string_table_enc_weapons.xml', 'r')
			string_table_enc_weapons_xml=f_string_table_enc_weapons_xml.readlines()
			f_string_table_enc_weapons_xml.close()

			ammo_items=[]
			a='0'
			a_process='0'
			i=0            
			for i in range(0, len(string_table_enc_weapons_xml)):
				if i!=0 and i%3==0 and i!=3 and i>=4 and i<=149: 
					#print(i)                                                    #i!=0 and i%3==0 and i!=3 - если показать все содержимое
					id_items_process1=string_table_enc_weapons_xml[i]           #i!=0 and i%3==0 and i<=149 and i!=3 - если показать только патроны
			                            
					a_process=id_items_process1.replace('</text>', '')          #---
					a=a_process.replace('		<text>', '') #		<text>
					if len(a)<=10:
						ammo_items.append(a)


			#ammo_items.append('NO ICON')
			ammo_items.append('-не выбрано-')


			#Label(FrameTitle, text='S.T.A.L.K.E.R. LTX-Gen 2.0', font=('AmazS.T.A.L.K.E.R.v.3.0', config.font_size+20), bg='#DCDCDC').pack()


			FrameAmmoIconDemonstration = Frame(win_ammo_shbl, bg='#f0f0f0')

			Label(FrameAmmoIconDemonstration, text='Иконка выбранных боеприпасов', font=(config.font_name, config.font_size)).pack()

			ammo_panel=Label(FrameAmmoIconDemonstration, bg='#A0522D', width=200, height=50)
			ammo_panel.pack()

			Label(FrameAmmoIconDemonstration, text='\nВыберите боеприпасы и нажмите клавишу Enter', font=(config.font_name, config.font_size)).pack()
			Label(FrameAmmoIconDemonstration, text='Для обновления иконки в окне нажмите клавишу F5', font=('Verdana', config.low_font_size)).pack()

			ammo_list_widget=ttk.Combobox(FrameAmmoIconDemonstration, values = ammo_items, width=15, height=20, state="readonly")
			ammo_list_widget.pack()
			ammo_list_widget.set(ammo_items[len(ammo_items)-1])

			Label(FrameAmmoIconDemonstration, text='Для добавления боеприпаса в список выберите его и нажмите Enter\nДля удаления боеприпаса выделите его и нажмите Delete', font=('Verdana', config.low_font_size)).pack()





			FrameAddedAmmoList = LabelFrame(FrameAmmoIconDemonstration, text='Выбранные боеприпасы')

			#added_ammo_list=Label(FrameAddedAmmoList, text='Ничего не добавлено', font=('Verdana', config.low_font_size), fg='grey', width=20, height=20)
			#added_ammo_list.pack()

			added_ammo_list = Listbox(FrameAddedAmmoList, width=20, height=10, bd=0, highlightcolor='#87CEFA') #87CEFA / #cce4f7
			added_ammo_list.pack()

			win_ammo_shbl.bind_all('<Return>', AddNewAmmo)
			win_ammo_shbl.bind_all('<Delete>', DeleteAmmoInListbox)
			added_ammo_list.bind('<F5>', ReloadIconAddedAmmo)


			FrameAddedAmmoList.pack()


			ttk.Button(FrameAmmoIconDemonstration, text='Применить и закрыть окно', command=SELF_SaveAmmoWpn).pack()




			FrameAmmoIconDemonstration.pack(fill=BOTH, expand=1, side=TOP, anchor=E)

			ReloadAmmoIcon()


			win_ammo_shbl.mainloop()


		def is_digit(string):
		    if string.isdigit():
		       return True
		    else:
		        try:
		            float(string)
		            return True
		        except ValueError:
		            return False

		def Analyze():
			count_errors=0
			######################
			if is_digit(weapon_cost.get())==True:
				if int(weapon_cost.get())>=1:
					wpn_cost=weapon_cost.get()
				else:
					count_errors+=1
				#print(weapon_cost.get())
			else:
				count_errors+=1
			#####################
			if is_digit(entry_minimum_purchase_price.get())==True and is_digit(entry_maximum_purchase_price.get())==True:
				line_trader_generic_buy = 'wpn_{0} = {1}, {2}\n'.format(sys_name, str(entry_minimum_purchase_price.get()), str(entry_maximum_purchase_price.get()))
			else:
				count_errors+=1
			######################
			if is_digit(entry_number.get())==True and is_digit(entry_chance.get())==True:
				line_supplies_start = 'wpn_{0} = {1}, {2}\n'.format(sys_name, str(entry_number.get()), str(entry_chance.get()))
			else:
				count_errors+=1
			######################
			if is_digit(entry_minimum_sale_price.get())==True and is_digit(entry_maximum_sale_price.get())==True:
				line_trader_start_sell = 'wpn_{0} = {1}, {2}\n'.format(sys_name, str(entry_minimum_sale_price.get()), str(entry_maximum_sale_price.get()))
			else:
				count_errors+=1
			######################
			if added_ammo_list_win.size()==0:
				count_errors+=1
			######################

			if count_errors>=1:
				mb.showerror(win_name, 'Не все данные корректно заполнены! Проверьте заполнение формы!\n\nОБРАТИТЕ ВНИМАНИЕ!\n- Должен быть выбран хотя бы один торговец и настроены параметры этого оружия!\n- Боеприпасы должны быть в любом случае выбраны!')
			elif count_errors==0:
				#print(weapon_cost.get())

				project_name=prj_name
				
				sidor_status=str(cvar1.get())
				barman_status=str(cvar2.get())
				sakharov_status=str(cvar3.get())
				dolg_status=str(cvar4.get())
				freedom_status=str(cvar5.get())
				'''
				print(sidor_status)
				print(barman_status)
				print(sakharov_status)
				print(dolg_status)
				print(freedom_status)
				'''
				#№№№№№№№№№№№№№№№№№				
				if install_status.get()==True and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script')==False:
					#setup_naxac=install_status.get()
					#print('Добавление спавн-меню в проект...')
					shutil.unpack_archive(filename='res/default_configs/SoC/naxac.zip', extract_dir=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/')

					if add_status.get()==True:
						#dd_wpn_in_naxac
						#print('Выполняется условие 1')

						f_ui_cheat_naxac_script=open('res/default_configs/SoC/ui_cheat_naxac.script', 'r')
						lines=f_ui_cheat_naxac_script.readlines()
						f_ui_cheat_naxac_script.close()

						f_ui_cheat_naxac_script=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script', 'w')
						for word in lines:
							if re.search(re.escape('-- weapons and ammo'), word):
								word = '-- weapons and ammo\n	{"*** LTX-Gen weapons ***",\n'
								f_ui_cheat_naxac_script.write(word)
							elif re.search(re.escape('"*** Оружие ***"'), word):
								word = '	"wpn_'+sys_name+'",\n	"*** Оружие ***",\n'
								f_ui_cheat_naxac_script.write(word)
							else:
								f_ui_cheat_naxac_script.write(word)

				elif install_status.get()==True and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script')==True:
					if add_status.get()==True:
						#dd_wpn_in_naxac
						
						f_ui_cheat_naxac_script=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script', 'r')
						lines=f_ui_cheat_naxac_script.readlines()
						f_ui_cheat_naxac_script.close()

						f_ui_cheat_naxac_script=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/scripts/ui_cheat_naxac.script', 'w')
						for word in lines:
							if re.search(re.escape('"*** LTX-Gen weapons ***"'), word):

								lines.insert(lines.index(word)+1, '	"wpn_'+sys_name+'",\n')
								new_word = lines[lines.index(word)]
								f_ui_cheat_naxac_script.write(new_word)
							else:
								f_ui_cheat_naxac_script.write(word)

						f_ui_cheat_naxac_script.close()
				#№№№№№№№№№№№№№№№№№

				copy_file=''

				k=0

				# line_trader_generic_buy | line_supplies_start | line_trader_start_sell

				#=================СИДОРОВИЧ=========================================
				#ltx_gen_section = '' #';LTX-Gen section\n'
				if sidor_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_trader.ltx')==False:
					copy_file='trade_trader.ltx'

					f=open('res/default_configs/SoC/'+copy_file, 'r')
					lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for word in lines:
						if re.search(re.escape('[trader_generic_buy]'), word):
							word = '[trader_generic_buy]\n'+line_trader_generic_buy
							f_write.write(word)
						elif re.search(re.escape('[supplies_start]'), word):
							word = '[supplies_start]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[supplies_after_fabric]'), word):
							word = '[supplies_after_fabric]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[trader_start_sell]'), word):
							word = '[trader_start_sell]\n'+line_trader_start_sell
							f_write.write(word)
						elif re.search(re.escape('[trader_after_fabric_sell]'), word):
							word = '[trader_after_fabric_sell]\n'+line_trader_start_sell
							f_write.write(word)
						else:
							f_write.write(word)

					f_write.close()


				elif sidor_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_trader.ltx')==True:
					copy_file='trade_trader.ltx'

					f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
					trader_lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for trader_word in trader_lines:
						if re.search(re.escape('[trader_generic_buy]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_start]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_after_fabric]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[trader_start_sell]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[trader_after_fabric_sell]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						else:
							f_write.write(trader_word)

					f_write.close()
					
				    
				#===================================================================

				
				#=================БАРМЕН============================================
				# line_trader_generic_buy | line_supplies_start | line_trader_start_sell

				if barman_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_barman.ltx')==False:                
					copy_file='trade_barman.ltx'

					shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

					f=open('res/default_configs/SoC/'+copy_file, 'r')
					lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for word in lines:
						if re.search(re.escape('[barman_generic_buy]'), word):
							word = '[barman_generic_buy]\n'+line_trader_generic_buy
							f_write.write(word)
						elif re.search(re.escape('[supplies_start]'), word):
							word = '[supplies_start]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[supplies_after_darkvalley]'), word):
							word = '[supplies_after_darkvalley]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[supplies_after_brain]'), word):
							word = '[supplies_after_brain]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[barman_start_sell]'), word):
							word = '[barman_start_sell]\n'+line_trader_start_sell
							f_write.write(word)
						elif re.search(re.escape('[barman_after_darkvalley_sell]'), word):
							word = '[barman_after_darkvalley_sell]\n'+line_trader_start_sell
							f_write.write(word)
						elif re.search(re.escape('[barman_after_brain_sell]'), word):
							word = '[barman_after_brain_sell]\n'+line_trader_start_sell
							f_write.write(word)
						else:
							f_write.write(word)

					f_write.close()

				elif barman_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_barman.ltx')==True:
					copy_file='trade_barman.ltx'

					f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
					trader_lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for trader_word in trader_lines:
						if re.search(re.escape('[barman_generic_buy]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_start]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_after_darkvalley]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_after_brain]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[barman_start_sell]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[barman_after_darkvalley_sell]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[barman_after_brain_sell]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						else:
							f_write.write(trader_word)

					f_write.close()

				    
				#===================================================================


				#=====================ПЕТРЕНКО======================================
				# line_trader_generic_buy | line_supplies_start | line_trader_start_sell
				if dolg_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_dolg.ltx')==False:                
					copy_file='trade_dolg.ltx'

					shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

					f=open('res/default_configs/SoC/'+copy_file, 'r')
					lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for word in lines:
						if re.search(re.escape('[dolg_generic_buy]'), word):
							word = '[dolg_generic_buy]\n'+line_trader_generic_buy
							f_write.write(word)
						elif re.search(re.escape('[supplies_start]'), word):
							word = '[supplies_start]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[supplies_after_rg6]'), word):
							word = '[supplies_after_rg6]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[dolg_start_sell]'), word):
							word = '[dolg_start_sell]\n'+line_trader_start_sell
							f_write.write(word)
						elif re.search(re.escape('[dolg_after_rg6_sell]'), word):
							word = '[dolg_after_rg6_sell]\n'+line_trader_start_sell
							f_write.write(word)
						else:
							f_write.write(word)

					f_write.close()

				elif dolg_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_dolg.ltx')==True:
					copy_file='trade_dolg.ltx'

					f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
					trader_lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for trader_word in trader_lines:
						if re.search(re.escape('[dolg_generic_buy]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_start]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_after_rg6]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[dolg_start_sell]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[dolg_after_rg6_sell]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						else:
							f_write.write(trader_word)

					f_write.close()
				                    
				#elif barman_status=='False':
					#k+=1                    

				#===================================================================



				#=====================САХАРОВ======================================
				# line_trader_generic_buy | line_supplies_start | line_trader_start_sell
				if sakharov_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_ecolog.ltx')==False:                
					copy_file='trade_ecolog.ltx'

					shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

					f=open('res/default_configs/SoC/'+copy_file, 'r')
					lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for word in lines:
						if re.search(re.escape('[ecolog_generic_buy]'), word):
							word = '[ecolog_generic_buy]\n'+line_trader_generic_buy
							f_write.write(word)
						elif re.search(re.escape('[supplies_start]'), word):
							word = '[supplies_start]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[supplies_after_brain]'), word):
							word = '[supplies_after_brain]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[ecolog_start_sell]'), word):
							word = '[ecolog_start_sell]\n'+line_trader_start_sell
							f_write.write(word)
						elif re.search(re.escape('[ecolog_after_brain_sell]'), word):
							word = '[ecolog_after_brain_sell]\n'+line_trader_start_sell
							f_write.write(word)
						else:
							f_write.write(word)

					f_write.close()

				elif sakharov_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_ecolog.ltx')==True:
					copy_file='trade_ecolog.ltx'

					f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
					trader_lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for trader_word in trader_lines:
						if re.search(re.escape('[ecolog_generic_buy]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_start]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_after_brain]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[ecolog_start_sell]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[ecolog_after_brain_sell]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						else:
							f_write.write(trader_word)

					f_write.close()
					                    
				#elif sakharov_status=='False':
					#k+=1                    

				#===================================================================            


				#=====================СКРЯГА========================================
				if freedom_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_freedom.ltx')==False:                
					copy_file='trade_freedom.ltx'

					shutil.copy('res/default_configs/SoC/'+copy_file, config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/')

					f=open('res/default_configs/SoC/'+copy_file, 'r')
					lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for word in lines:
						if re.search(re.escape('[freedom_generic_buy]'), word):
							word = '[freedom_generic_buy]\n'+line_trader_generic_buy
							f_write.write(word)
						elif re.search(re.escape('[supplies_start]'), word):
							word = '[supplies_start]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[supplies_after_dolg]'), word):
							word = '[supplies_after_dolg]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[supplies_after_pavlik]'), word):
							word = '[supplies_after_pavlik]\n'+line_supplies_start
							f_write.write(word)
						elif re.search(re.escape('[freedom_sell_start]'), word):
							word = '[freedom_sell_start]\n'+line_trader_start_sell
							f_write.write(word)
						elif re.search(re.escape('[freedom_sell_after_dolg]'), word):
							word = '[freedom_sell_after_dolg]\n'+line_trader_start_sell
							f_write.write(word)
						elif re.search(re.escape('[freedom_sell_after_pavlik]'), word):
							word = '[freedom_sell_after_pavlik]\n'+line_trader_start_sell
							f_write.write(word)
						else:
							f_write.write(word)

					f_write.close()

				elif freedom_status=='True' and os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+'trade_freedom.ltx')==True:
					copy_file='trade_freedom.ltx'

					f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'r')
					trader_lines=f.readlines()
					f.close()

					f_write=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc/'+copy_file, 'w')

					for trader_word in trader_lines:
						if re.search(re.escape('[freedom_generic_buy]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_generic_buy)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_start]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_after_dolg]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[supplies_after_pavlik]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_supplies_start)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[freedom_sell_start]'), trader_word):

							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[freedom_sell_after_dolg]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell) 
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						elif re.search(re.escape('[freedom_sell_after_pavlik]'), trader_word):
							
							trader_lines.insert(trader_lines.index(trader_word)+1, line_trader_start_sell)
							trader_new_word = trader_lines[trader_lines.index(trader_word)]
							f_write.write(trader_new_word)

						else:
							f_write.write(trader_word)

					f_write.close()


				print('ВСЕ ГОТОВО\nПЕРЕХОД НА СЛЕДУЮЩИЙ ШАГ!!!')


				#===================================================================



			#print('wpn_{0} = {1}, {2}'.format(sys_name, str(entry_minimum_purchase_price.get()), str(entry_maximum_purchase_price.get())))
			#print('wpn_{0} = {1}, {2}'.format(sys_name, str(entry_number.get()), str(entry_chance.get())))
			#print('wpn_{0} = {1}, {2}'.format(sys_name, str(entry_minimum_sale_price.get()), str(entry_maximum_sale_price.get())))



		def RedirectionFunctions_step5_help_naxac():
			step5_help_naxac(game_wnp_name, sys_name)


		def InsertRecommendParams():

			entry_minimum_purchase_price.delete(0, END)
			entry_maximum_purchase_price.delete(0, END)
			entry_number.delete(0, END)
			entry_chance.delete(0, END)
			entry_minimum_sale_price.delete(0, END)
			entry_maximum_sale_price.delete(0, END)


			entry_maximum_purchase_price.insert(END, '0.5')
			entry_minimum_purchase_price.insert(END, '0.7')
			entry_number.insert(END, '4')
			entry_chance.insert(END, '0.5')
			entry_minimum_sale_price.insert(END, '1')
			entry_maximum_sale_price.insert(END, '2')



		def SELF_Analyze(self):
			Analyze()


		def OpenSIE():
			project_name=prj_name
			#root_name.destroy()
			root_name.withdraw()
			os.system("sie.exe "+config.folder_projects+"/"+config.folder_projects_soc+'/'+project_name+"/gamedata/textures/ui/ui_icon_equipment.dds")
			root_name.deiconify()


		def InsertWpnIcon():
			#print(str(pyperclip.paste()))
			wpn_icon_info.delete(0.0, END)
			wpn_icon_info.insert(END, str(pyperclip.paste()))

		def SELF_InsertWpn_Icon(self):
			InsertWpnIcon()

		def WIN_DeleteAmmo(self):
			selection_n = added_ammo_list_win.curselection()
			added_ammo_list_win.delete(selection_n[0])

		def ClickAllTraider():
			def DeletedAllTraiders():
				cvar1.set(0)
				cvar2.set(0)
				cvar3.set(0)
				cvar4.set(0)
				cvar5.set(0)
				btn_click_all.configure(text='Отметить всех', command=ClickAllTraider)



			cvar1.set(1)
			cvar2.set(1)
			cvar3.set(1)
			cvar4.set(1)
			cvar5.set(1)
			btn_click_all.configure(text='Убрать всех', command=DeletedAllTraiders)


		FrameS6 = Frame(root_name, bg='#f0f0f0')

		#==========================
			

		FrameBorderline = Frame(FrameS6, bg='#f0f0f0')


		#--------------

		FrameCost = Frame(FrameBorderline)

		Label(FrameCost, text='Введите цену оружия строго больше 0', font=(config.font_name, config.font_size)).pack()
		#Label(FrameCost, text=' ').pack()

		weapon_cost=ttk.Entry(FrameCost, width=25)
		weapon_cost.pack()
		weapon_cost.focus()

		FrameCost.pack(side=TOP, anchor=N, expand=1)

		#--------------

		FrameAddSpawnMenu = Frame(FrameBorderline)

		Label(FrameAddSpawnMenu, text='Добавление оружия в spawn-menu', font=(config.font_name, config.font_size)).pack()
		#Label(FrameAddSpawnMenu, text=' ').pack()

		FrameCheckbuttons_naxac = Frame(FrameAddSpawnMenu)

		install_status = BooleanVar()
		install_status.set(1)
		install_spawn_menu = ttk.Checkbutton(FrameCheckbuttons_naxac, text="Установить spawn-menu by naxaс\nс денежным трейнером tankalxat34.", variable=install_status, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 9), justify=LEFT)
		install_spawn_menu.pack(anchor=W)
		        
		add_status = BooleanVar()
		add_status.set(1)
		add_wpn_in_spawn_menu = ttk.Checkbutton(FrameCheckbuttons_naxac, text="Добавить оружие в данное spawn-menu.", variable=add_status, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 9), justify=LEFT)
		add_wpn_in_spawn_menu.pack(anchor=W)

		FrameCheckbuttons_naxac.pack()

		Button(FrameAddSpawnMenu, text='Для получения дополнительной\nинформации нажмите сюда', fg='blue', bd=0, command=RedirectionFunctions_step5_help_naxac).pack()

		######

		Label(FrameAddSpawnMenu, text='\nДобавление иконки оружия', font=(config.font_name, config.font_size)).pack()


		FrameBtns = Frame(FrameAddSpawnMenu)
		w=35
		ttk.Button(FrameBtns, text='Открыть шаблон в SIE.exe', command=OpenSIE, width=w).pack(side=TOP, anchor=N)
		ttk.Button(FrameBtns, text='Выбрать классическую иконку', command=AddIconFromShablon, width=w).pack(side=BOTTOM, anchor=N)
		FrameBtns.pack()

		Label(FrameAddSpawnMenu, text='Вставьте сюда координаты иконки', font=('Verdana', config.low_font_size)).pack()

		#insert_text=wpn_icon_text

		icon_default='''inv_grid_width     = 3
		inv_grid_height    = 2
		inv_grid_x         = 9
		inv_grid_y         = 27'''

		wpn_icon_info = Text(FrameAddSpawnMenu, bd=1, font=(config.low_font_name, config.low_font_size-1), wrap=WORD, width=25, height=4)
		wpn_icon_info.pack(side=BOTTOM)

		wpn_icon_info.bind('<Control-v>', SELF_InsertWpn_Icon)

		Button(FrameAddSpawnMenu, text='[Вставить]', bd=0, command=InsertWpnIcon, fg='blue').pack(side=BOTTOM)

		#wpn_icon_info.insert(END, insert_text)

		FrameAddSpawnMenu.pack(side=LEFT, expand=1, anchor=N)

		#--------------


		FrameListTraiders = Frame(FrameBorderline)

		Label(FrameListTraiders, text='Выберете торговцев, которым\nхотите добавить новое оружие.', font=(config.font_name, config.font_size)).pack()


		FrameCheckbuttonsTraider = Frame(FrameListTraiders)

		cvar1 = BooleanVar()
		cvar1.set(0)
		c1 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Сидорович", variable=cvar1, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c1.pack(anchor=W)
				        
		cvar2 = BooleanVar()
		cvar2.set(0)
		c2 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Бармен", variable=cvar2, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c2.pack(anchor=W)
				        
		cvar3 = BooleanVar()
		cvar3.set(0)
		c3 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Сахаров", variable=cvar3, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c3.pack(anchor=W)
				        
		cvar4 = BooleanVar()
		cvar4.set(0)
		c4 = ttk.Checkbutton(FrameCheckbuttonsTraider, text="Петренко", variable=cvar4, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c4.pack(anchor=W)
				        
		cvar5 = BooleanVar()
		cvar5.set(0)
		c5 =ttk.Checkbutton(FrameCheckbuttonsTraider, text="Скряга", variable=cvar5, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', config.low_font_size+2), justify=LEFT)
		c5.pack(anchor=W)

		FrameCheckbuttonsTraider.pack()

		btn_click_all=ttk.Button(FrameListTraiders, text='Отметить всех', width=20, command=ClickAllTraider)
		btn_click_all.pack()


		#############################################
		Label(FrameListTraiders, text='\nДобавление боеприпасов оружия', font=(config.font_name, config.font_size)).pack()
		ttk.Button(FrameListTraiders, text='Добавить боеприпасы', width=35, command=AddAmmoIconFromShablon).pack()

		added_ammo_list_win = Listbox(FrameListTraiders, width=20, height=5, bd=0, highlightcolor='#87CEFA') #87CEFA / #cce4f7
		added_ammo_list_win.pack()

		added_ammo_list_win.bind('<Delete>', WIN_DeleteAmmo)

		#added_ammo_list_win.insert(END, pyperclip.paste())
		############################################

		FrameListTraiders.pack(side=LEFT, fill=Y, expand=1, anchor=S)




		FrameParamsInTraiders = Frame(FrameBorderline)

		Label(FrameParamsInTraiders, text='Настройте параметры продажи', font=(config.font_name, config.font_size)).pack()

		Button(FrameParamsInTraiders, text='Для получения дополнительной\nинформации нажмите сюда', fg='blue', bd=0, command=step5_help).pack()

		Label(FrameParamsInTraiders, text='Секция [trader_generic_buy]\n(wpn_{0} = {2} {1})'.format(sys_name, 'минимальная цена покупки %', 'максимальная цена покупки %,\n'), font=(config.font_name, config.low_font_size)).pack()

		####--                           trader_generic_buy
		Frame_trader_generic_buy = Frame(FrameParamsInTraiders)
		Label(Frame_trader_generic_buy, text='wpn_{}  ='.format(sys_name), font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)#'Минимальная цена покупки (%):', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		Label(Frame_trader_generic_buy, text=' ').pack(side=LEFT, anchor=N)

		entry_minimum_purchase_price=ttk.Entry(Frame_trader_generic_buy, width=10)
		entry_minimum_purchase_price.pack(side=LEFT, anchor=N)

		Label(Frame_trader_generic_buy, text=',', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)

		entry_maximum_purchase_price=ttk.Entry(Frame_trader_generic_buy, width=10)
		entry_maximum_purchase_price.pack(side=LEFT, anchor=N)
		Frame_trader_generic_buy.pack()




		Label(FrameParamsInTraiders, text='Секция [supplies_start]\n(wpn_{0} = {1}, {2})'.format(sys_name, 'количество', 'вероятность появления'), font=(config.font_name, config.low_font_size)).pack()

		#  supplies_start
		Frame_supplies_start = Frame(FrameParamsInTraiders)
		Label(Frame_supplies_start, text='wpn_{}  ='.format(sys_name), font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)#'Минимальная цена покупки (%):', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		Label(Frame_supplies_start, text=' ').pack(side=LEFT, anchor=N)

		entry_number=ttk.Entry(Frame_supplies_start, width=10)
		entry_number.pack(side=LEFT, anchor=N)

		Label(Frame_supplies_start, text=',', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)

		entry_chance=ttk.Entry(Frame_supplies_start, width=10)
		entry_chance.pack(side=LEFT, anchor=N)
		Frame_supplies_start.pack()




		Label(FrameParamsInTraiders, text='Секция [trader_start_sell]\n(wpn_{0} = {1} {2})'.format(sys_name, 'минимальная цена продажи,\n', 'максимальная цена продажи'), font=(config.font_name, config.low_font_size)).pack()

		#  supplies_start
		Frame_trader_start_sell = Frame(FrameParamsInTraiders)
		Label(Frame_trader_start_sell, text='wpn_{}  ='.format(sys_name), font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)#'Минимальная цена покупки (%):', font=(config.low_font_name, config.low_font_size)).pack(side=LEFT, anchor=N)
		Label(Frame_trader_start_sell, text=' ').pack(side=LEFT, anchor=N)

		entry_minimum_sale_price=ttk.Entry(Frame_trader_start_sell, width=10)
		entry_minimum_sale_price.pack(side=LEFT, anchor=N)

		Label(Frame_trader_start_sell, text=',', font=(config.font_name, config.low_font_size)).pack(side=LEFT, anchor=N)

		entry_maximum_sale_price=ttk.Entry(Frame_trader_start_sell, width=10)
		entry_maximum_sale_price.pack(side=LEFT, anchor=N)

		Label(Frame_trader_start_sell, text='\n').pack(side=LEFT, anchor=N)

		Frame_trader_start_sell.pack()



		ttk.Button(FrameParamsInTraiders, text='Рекомендуемые значения', width=30, command=InsertRecommendParams).pack()


		#entry_maximum_sale_price.bind('<Return>', SELF_Analyze)




		FrameParamsInTraiders.pack(side=LEFT, fill=Y, expand=1)




		FrameBorderline.pack(side=TOP, fill=BOTH, expand=1)





		#==========================
		FrameBtn = LabelFrame(FrameS6, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=Analyze).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отменить [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=S, fill=X, expand=1)
		FrameS6.pack(side=BOTTOM, fill=BOTH, expand=1)






class ReturnDescritptionWeapon(): #step5

	def window(root_name, prj_name, sys_name):

		def LoadFromFile():
			try:
				path_txt_description = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ', filetypes=(("TXT files", "*.txt"), ("All files", "*.*")))
		        
				process1=str(path_txt_description)[:-3]
				path_txt_description=process1[2:]            
		        
				f=open(str(path_txt_description), 'r', encoding='utf-8')
				description_file=f.read()
				f.close()
		        
				text_description_weapon.insert(END, description_file)
			except FileNotFoundError:
				#mb.showerror(win_name, 'Файл не был загружен!')
				text_description_weapon.insert(END, '')


		def Analyze(root_name, prj_name, sys_wpn_name):
			inv_description_outfit=''
			n=3

			if name_wpn.get()!='':
				if len(text_description_weapon.get(0.0, END))<=n:
					inv_description_wpn='Оружие имеет системное имя "{0}".{2}{2}Создано в приложении {1} '.format(sys_wpn_name, win_name, chr(92)+'n')+author_label

				elif len(text_description_weapon.get(0.0, END))>n:
					inv_description_wpn=(text_description_weapon.get(0.0, END)).replace('\n', chr(92)+'n')

				#print(inv_description_outfit)
				inv_name_wpn = name_wpn.get()
				#if re.search(r'\bзвать\b', 'меня звать Олег, мне 35 лет'):
				#shutil.copy('res/default_configs/SoC/string_table_enc_weapons.xml', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/'))
				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_enc_weapons.xml')==False:
					default_table = open('res/default_configs/SoC/string_table_enc_weapons.xml', 'r')
					table_list_old = default_table.readlines()
					default_table.close()

					table_list = list(table_list_old)

					table_in_project = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_enc_weapons.xml', 'w')
					
					for word in table_list:
						if re.search('</string_table>', word):
							new_word='''	<string id="enc_weapons1_wpn-{sys_name}">
		<text>{inv_desc_name}</text>
	</string>
	<string id="wpn_{sys_name}">
		<text>{inv_name_name}</text>
	</string>
</string_table>'''.format(sys_name=sys_wpn_name, inv_desc_name=inv_description_wpn, inv_name_name=inv_name_wpn)
							table_in_project.write(new_word)

						else:
							table_in_project.write(word)

					table_in_project.close()

				elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_enc_weapons.xml')==True:


					table_in_project = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_enc_weapons.xml', 'r')
					table_list = table_in_project.readlines()
					table_in_project.close()

					table_in_project = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/text/rus/string_table_enc_weapons.xml', 'w')
					
					for word in table_list:
						if re.search('</string_table>', word):
							new_word='''	<string id="enc_weapons1_wpn-{sys_name}">
		<text>{inv_desc_name}</text>
	</string>
	<string id="wpn_{sys_name}">
		<text>{inv_name_name}</text>
	</string>
</string_table>'''.format(sys_name=sys_wpn_name, inv_desc_name=inv_description_wpn, inv_name_name=inv_name_wpn)

							table_in_project.write(word.replace(word, new_word))

						else:
							table_in_project.write(word)

					table_in_project.close()

				FrameS5.pack_forget()
				AddWeaponInTraders.window(root_name=root_name, prj_name=prj_name, sys_name=sys_name, game_wnp_name=inv_name_wpn)

			else:
				mb.showerror(win_name, 'Необходимо задать имя бронекостюма!\n\nЗадавать описание не обязательно, программа сама его сделает следующим:\n'+'"Бронекостюм имеет системное имя "{0}".{2}{2}Создано в приложении {1} by tankalxat34 (tnkSoftware)"'.format(sys_outfit_name, win_name, chr(92)+'n'))


		def Rediction_Function_Analyze():
			Analyze(root_name=root_name, prj_name=prj_name, sys_wpn_name=sys_name)




		FrameS5 = Frame(root_name, bg='#f0f0f0')

		#-----



		FrameReturnInvWpnName = Frame(FrameS5, bg='#f0f0f0')
		Label(FrameReturnInvWpnName, text='Введите название нового оружия.', font=(config.font_name, config.font_size)).pack()

		name_wpn=ttk.Entry(FrameReturnInvWpnName, width=55)
		name_wpn.pack()
		name_wpn.focus()

		#Label(FrameReturnInvWpnName, text=' ').pack()

		FrameReturnInvWpnName.pack(side=TOP, fill=X)


		FrameReturnInvWpnText = Frame(FrameS5, bg='#f0f0f0')

		Label(FrameReturnInvWpnText, text='Введите описание нового оружия.', font=(config.font_name, config.font_size)).pack()

		Button(FrameReturnInvWpnText, text='Для загрузки описания из txt-файла нажмите на эту надпись', fg='blue', bd=0, bg='#f0f0f0', command=LoadFromFile).pack()

		#text_description_weapon = Text(FrameReturnInvWpnText, bd=1, font=(config.low_font_name, config.low_font_size-1), width=100, height=13)
		text_description_weapon = Text(FrameReturnInvWpnText, bd=1, font=(config.low_font_name, config.low_font_size-1), wrap=WORD, width=110, height=19)
		text_description_weapon.pack(side=LEFT)#, expand=1)
		#text.focus()

		scrollY = Scrollbar(FrameReturnInvWpnText, command=text_description_weapon.yview)
		scrollY.pack(side=RIGHT, fill=Y)  
		text_description_weapon.config(yscrollcommand=scrollY.set)

		Label(FrameReturnInvWpnName, text=' ').pack()

		FrameReturnInvWpnText.pack(side=TOP, fill=X)

		#-----
		FrameBtn = LabelFrame(FrameS5, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=Rediction_Function_Analyze).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameS5.pack(side=BOTTOM, fill=BOTH, expand=1)





class InitializationInConfigs(): # step4

	def window(root_name, prj_name, sys_name):
		
		#=========ВНОСИМ ИЗМЕНЕНИЯ В КОНФИГИ (ИНИЦИАЛИЗИРУЕМ ОРУЖИЕ В ИГРЕ)========
		project_name=prj_name
		system_wpn_name=sys_name
		##============weapons.ltx=========
		f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/weapons/weapons.ltx', 'w')
		f.write('#include "delayed_action_fuse.ltx"\n#include "w_'+system_wpn_name+'.ltx"\n')
                
		f_weapons_ltx = open('res/default_configs/SoC/weapons.ltx', 'r')
		weapons_ltx=f_weapons_ltx.readlines()
		f_weapons_ltx.close() 
		for i in range(1, len(weapons_ltx)):
			f.write(weapons_ltx[i])
                    
		f.close()                
		##===============================

		##============prefetch_globals.ltx=========
		f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/prefetch/prefetch_globals.ltx', 'w')
		f.write('[prefetch_visuals_weapons]\n;weapons\nweapons'+chr(92)+system_wpn_name+chr(92)+'wpn_'+system_wpn_name+'\nweapons'+chr(92)+system_wpn_name+chr(92)+'wpn_'+system_wpn_name+'_hud\n')
                
		f_prefetch_globals_ltx = open('res/default_configs/SoC/prefetch_globals.ltx', 'r')
		prefetch_globals_ltx=f_prefetch_globals_ltx.readlines()
		f_prefetch_globals_ltx.close() 
		for i in range(2, len(prefetch_globals_ltx)):
			f.write(prefetch_globals_ltx[i])
                    
		f.close()                
		##=================================================  

		##============mp_ranks.ltx=========
		f=open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/mp/mp_ranks.ltx', 'w')
                
		f_mp_ranks_ltx = open('res/default_configs/SoC/mp_ranks.ltx', 'r')
		mp_ranks_ltx=f_mp_ranks_ltx.readlines()
		f_mp_ranks_ltx.close() 
                
		for i in range(100):
			f.write(mp_ranks_ltx[i])
		f.write('available_items					= mp_wpn_fn2000,mp_wpn_gauss,mp_wpn_rg-6,mp_ammo_gauss, wpn_svd_m1, wpn_svu_m1, wpn_vintorez_coll, wpn_g36_m1, wpn_mp5_m1, wpn_gauss_m1, wpn_pm_arena, wpn_mp5_arena, wpn_mp5_m2, wpn_toz34_arena, wpn_spas12_arena, wpn_ak74_arena, wpn_bm16_arena, wpn_ak74u_arena, wpn_val_arena, wpn_groza_arena, wpn_fn2000_arena, wpn_g36_arena, wpn_sig_m1, wpn_sig_m2, wpn_rg6_m1, wpn_'+system_wpn_name+'\n')
                
		for i in range(101, len(mp_ranks_ltx)):
			f.write(mp_ranks_ltx[i])
                    
		f.close()                
		##=================================================                

		#==========================================================================
                
                
		f = open(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/weapons/w_'+system_wpn_name+'.ltx', 'w')
		f.close()

		os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/', access_rights)    
		shutil.copy('res/default_ui/SoC/ui_icon_equipment.dds', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/'))


		#=========================
		'''
		pb.pack()		
		Label(FrameS4, text='100%').pack()
		FrameBtn = LabelFrame(FrameS4, bg='#DCDCDC', text='')
		#ttk.Button(FrameBtn, text='Продолжить >>>', width=23).pack(side=RIGHT)
		#ttk.Button(FrameBtn, text='<<< Отменить [резерв]', width=23).pack(side=LEFT)
		Label(FrameBtn, text=author_label, bg='#DCDCDC').pack(anchor=S)

		FrameBtn.pack(side=BOTTOM, anchor=S, fill=X, expand=1)
		FrameS4.pack(side=BOTTOM, fill=BOTH, expand=1)

		pb.step(399)		
		mb.showinfo(win_name, 'Инициализация оружия в игре успешно завершена!')
		FrameS4.pack_forget()
		'''
		ReturnDescritptionWeapon.window(root_name=root_name, prj_name=prj_name, sys_name=sys_name)












class Load_DDS_OGF_SystemWeaphonName_step3():

	def window(root_name, prj_name, status_fill):



		def Continue(sys_name, root_name, prj_name):

			#ways_dds='({0} ; {1} ; {2})'.format(os.path.basename(ways_dds[0]), os.path.basename(ways_dds[1]), os.path.basename(ways_dds[2]))
			#ways_ogf='({0} ; {1})'.format(os.path.basename(ways_ogf[0]), os.path.basename(ways_ogf[1]))

			ways_ogf=os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+sys_name+'/')
			ways_dds=os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/')

			text_continue='''Пожалуйста, подтвердите верность введенных данных в программу! Эти данные верны?

• {0} - Имя проекта.

• {1} - системное имя оружия.

• {2} - Файлы текстур dds.

• {3} - Файлы формата ogf.

Нажмите "Да" для продолжения, "Нет" для отмены.
'''.format(prj_name, sys_name, ways_dds, ways_ogf)
			answer=mb.askyesno('Подтверждение действия', text_continue)
			if answer==True:
				if str(rename_status.get())=='False':
					for word in ways_dds:
						if re.search('_bump.dds', word):
							os.rename(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/'+word, config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/wpn_{0}{1}.dds'.format(sys_name, '_bump'))
						elif re.search('_bump#.dds', word):
							os.rename(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/'+word, config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/wpn_{0}{1}.dds'.format(sys_name, '_bump#'))
						elif re.search('.dds', word):
							os.rename(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/'+word, config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/wpn_{0}{1}.dds'.format(sys_name, ''))

				for word in ways_ogf:
					if re.search('_hud.ogf', word):
						os.rename(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+sys_name+'/'+word, config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+sys_name+'/'+'wpn_{0}{1}.ogf'.format(sys_name, '_hud'))
					elif re.search('.ogf', word):
						os.rename(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+sys_name+'/'+word, config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+sys_name+'/'+'wpn_{0}{1}.ogf'.format(sys_name, ''))


				FrameS3.pack_forget()
				InitializationInConfigs.window(root_name=root_name, prj_name=prj_name, sys_name=sys_name)

		def RedirectionFunction_Continue():
			Continue(sys_name=entry_system_wpn_name.get(), root_name=root_name, prj_name=prj_name)

		def ReturnSystemWpnName():
			system_wpn_name=entry_system_wpn_name.get()
		    
			global memory
		    
			k=0
			alphabet='qwertyuiopasdfghjklzxcvbnm_1234567890'
			if system_wpn_name[0] not in alphabet:                
				mb.showerror(win_name, 'Первый символ в названии не является корректным!')
				k+=1
			else:
				for i in range(len(system_wpn_name)):
					if system_wpn_name[i] in alphabet or i==len(system_wpn_name)-1:
						k+=0
					else:
						k+=1
			#print(k)
			if k>0:
				mb.showerror(win_name, 'В названии есть некорректные символы! Введите название, состоящее из латинских букв, цифр и нижних подчеркиваний. Желательно, что бы название было очень коротким, так как игре будет легче обращатся к файлам с коротким названием.')
			elif k==0:
				#mb.showinfo(win_name, 'Системное имя {} успешно зарегестрировано!'.format(system_wpn_name))
				#btn_load_ogf.configure(state=NORMAL)
				btn_load_wpn_dds.configure(state=NORMAL)
				btn_load_wpn_dds.focus()
				return system_wpn_name


		def RETURN_ReturnSystemWpnName(self):
			ReturnSystemWpnName()


		def LoadDDS():
			try:
				path_dds = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ', filetypes=(("DDS files", "*.dds"), ("DDS files", "*.dds")))

				if status_fill==False:
					for i in range(0, len(list_dir)):
						#print(list_dir[i])
						list_dir=os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/')
						os.remove(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/'+list_dir[i])

					for i in range(0, len(path_dds)):					
						shutil.copy(path_dds[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/')

					#path_dds.clear()


				if status_fill==True:# and len(path_dds)==3:
					for i in range(0, len(path_dds)):					
						shutil.copy(path_dds[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/wpn/')
						#print('---------\n'+path_dds[i]+'\n----------')

					#mb.showinfo('text', 'Директории оружия сформированы!')

				#elif len(path_dds)!=3:
					#mb.showerror(win_name, 'Не обнаружено три текстуры! Загрузите текстуры еще раз!')

				#btn_load_dds.configure(width=75, text='Загружены: {0} ; {1} ; {2}'.format(os.path.basename(path_dds[0]), os.path.basename(path_dds[1]), os.path.basename(path_dds[2])))
				btn_load_wpn_dds.configure(width=30, text='Загружены: {0} и др.'.format(os.path.basename(path_dds[0])))#, os.path.basename(path_dds[1]), os.path.basename(path_dds[2])))
				btn_load_wpn_ogf.configure(state=NORMAL)
				btn_load_wpn_ogf.focus()

				return path_dds
			except IndexError:
				mb.showerror(win_name, 'Файлы не были загружены!')
				LoadDDS()

		def SELF_LoadDDS(self):
			LoadDDS()


		def LoadOGF():
			path_ogf = fd.askopenfilenames(title=win_name + ' - загрузите файлы... ',filetypes=(("OGF files", "*.ogf"), ("OGF files", "*.ogf")))

			weapon_name=entry_system_wpn_name.get()
			try:
				os.mkdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name)

				if len(os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/'))!=0:
					list_dir=os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/')

					for i in range(0, len(list_dir)):
						#print(list_dir[i])
						os.remove(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/'+list_dir[i])



				if len(os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/'))==0: #and len(path_ogf)==2:
					for i in range(0, len(path_ogf)):					
						shutil.copy(path_ogf[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/')
						#print('---------\n'+path_dds[i]+'\n----------')

					#mb.showinfo('text', 'Директории оружия сформированы!')

				#elif len(path_ogf)!=2:
					#mb.showerror(win_name, 'Не обнаружено два ogf-файла! Загрузите их еще раз!')


				#btn_load_ogf.configure(width=75, text='Загружены: {0} ; {1}'.format(os.path.basename(path_ogf[0]), os.path.basename(path_ogf[1])))
				btn_load_wpn_ogf.configure(width=30, text='Загружены: {0} и др.'.format(os.path.basename(path_ogf[0])))#, os.path.basename(path_ogf[1])))

				return path_ogf

			except FileExistsError:
				try:
					if len(os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/'))!=0:
						list_dir=os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/')

						for i in range(0, len(list_dir)):
							#print(list_dir[i])
							os.remove(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/'+list_dir[i])



					if len(os.listdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/'))==0: #and len(path_ogf)==2:
						for i in range(0, len(path_ogf)):					
							shutil.copy(path_ogf[i], config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/meshes/weapons/'+weapon_name+'/')
							#print('---------\n'+path_dds[i]+'\n----------')

						#mb.showinfo('text', 'Директории оружия сформированы!')

					#elif len(path_ogf)!=2:
						#mb.showerror(win_name, 'Не обнаружено два ogf-файла! Загрузите их еще раз!')


					#btn_load_ogf.configure(width=55, text='Загружены: {0} ; {1}'.format(os.path.basename(path_ogf[0]), os.path.basename(path_ogf[1])))
					btn_load_wpn_ogf.configure(width=30, text='Загружены: {0} и др.'.format(os.path.basename(path_ogf[0])))#, os.path.basename(path_ogf[1])))

					return path_ogf
				except IndexError:
					mb.showerror(win_name, 'Файлы не были загружены!')
					LoadOGF()


		def SELF_LoadOGF(self):
			LoadOGF()




		FrameS3 = Frame(root_name, bg='#f0f0f0')

		w=20

		Label(FrameS3, text=' ').pack()

		FrameColumns = Frame(FrameS3)

		FrameEntrySysWpnName = Frame(FrameColumns)
		#Frame_dds_load_wpn.bind_all('<Return>', SELF_GetSysNameOutfit)

		Label(FrameEntrySysWpnName, text='Введите системное имя оружия   ', font=(config.font_name, config.font_size)).pack()

		entry_system_wpn_name=ttk.Entry(FrameEntrySysWpnName, width=w+15)
		entry_system_wpn_name.pack()
		entry_system_wpn_name.focus()
		entry_system_wpn_name.bind_all('<Return>', RETURN_ReturnSystemWpnName)

		ttk.Button(FrameEntrySysWpnName, text='Применить', width=20, command=ReturnSystemWpnName).pack()

		FrameEntrySysWpnName.pack(side=LEFT, anchor=N)


		Frame_sys_name_wpn = Frame(FrameColumns)

		Label(Frame_sys_name_wpn, text='DDS-текстуры оружия   ', font=(config.font_name, config.font_size)).pack()

		btn_load_wpn_dds=ttk.Button(Frame_sys_name_wpn, text='Загрузить...', width=w, state=DISABLED, command=LoadDDS)
		btn_load_wpn_dds.pack()
		#btn_load_wpn_dds.bind_all('<Return>', SELF_LoadDDS)
		#btn_load_wpn_dds.bind_all('<Return>', SELF_btn_load_outfit_dds)

		Frame_sys_name_wpn.pack(side=LEFT, anchor=N)

		FrameOGF_load = Frame(FrameColumns)
		Label(FrameOGF_load, text='    OGF-текстуры оружия', font=(config.font_name, config.font_size)).pack()

		btn_load_wpn_ogf = ttk.Button(FrameOGF_load, text='Загрузить...', width=w, state=DISABLED, command=LoadOGF)
		btn_load_wpn_ogf.pack()
		#btn_load_wpn_ogf.bind_all('<Return>', SELF_LoadOGF)

		FrameOGF_load.pack(side=LEFT, anchor=N)


		FrameColumns.pack()



		#root_name.bind('F1', step3_help)


		Label(FrameS3, text=' ').pack()

		rename_status = BooleanVar()
		rename_status.set(0)
		rename_status_widget = ttk.Checkbutton(FrameS3, text="Отключить переименование текстур", variable=rename_status, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 9), justify=LEFT)
		rename_status_widget.pack(side=TOP)

		Label(FrameS3, text=desc_wpn_step3, font=(config.low_font_name, config.low_font_size), justify=LEFT).pack()
		Button(FrameS3, text='Для получения дополнительной информации нажмите сюда', bd=0, fg='blue', command=help_step3).pack(side=TOP)



		#=========================


		FrameBtn = LabelFrame(FrameS3, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Продолжить >>>', width=23, command=RedirectionFunction_Continue).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отменить [резерв]', width=23).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=S, fill=X, expand=1)
		FrameS3.pack(side=BOTTOM, fill=BOTH, expand=1)







# Project_Registration_step1.window.RedirectionFunction_CreateProjectFolder_OUTFIT()
# Project_Registration_step1.window.RedirectionFunction_AddEATSysNameDDSOGF()
# Project_Registration_step1.window.RedirectionFunction_CreateProjectFolder_WEAPON()

class Project_Registration_step1(): 



	def RedirectionFunction_CreateProjectFolder_WEAPON(entry_project_name, FrameS1, root, status_fill):
		try:
			project_name=(entry_project_name).replace(' ', '_')
		except AttributeError:
			project_name=(entry_project_name.get()).replace(' ', '_')

		if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name) == False:
			os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name, config.access_rights)
			#print(os.path.expandvars('%windir%'))

			if os.path.isdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/'+'gamedata') == False and project_name!='':

				os.makedirs(config.folder_projects+chr(92)+config.folder_projects_soc+'/'+project_name+'/'+'gamedata', config.access_rights)

				prj_name=project_name

				#column=0

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/wpn')==False:
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/wpn', config.access_rights)
                    
				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/weapons')==False:    
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/weapons', config.access_rights)
                        
				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/weapons')==False:    
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/weapons', config.access_rights)
                        
				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/mp')==False:
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/mp', config.access_rights)
                        
				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/prefetch')==False:
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/prefetch', config.access_rights)
                        
				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc')==False:
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc', config.access_rights)
                        
				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus')==False:
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus', config.access_rights)

				FrameS1.pack_forget()
				Load_DDS_OGF_SystemWeaphonName_step3.window(root_name=root, prj_name=project_name, status_fill=status_fill)
				root.title(win_name+' — '+prj_name)

		elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name) == True and status_fill==False:
			mb.showerror(win_name, 'Проект с таким именем уже существует! Введите другое название!')	

		elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name) == True and status_fill==True:
			#mb.showerror(win_name, 'Проект с таким именем уже существует! Введите другое название!')
			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/wpn')==False:
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/wpn', config.access_rights)
                
			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/weapons')==False:    
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/weapons', config.access_rights)
                    
			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/weapons')==False:    
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/weapons', config.access_rights)
                    
			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/mp')==False:
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/mp', config.access_rights)
                    
			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/prefetch')==False:
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/prefetch', config.access_rights)
                    
			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc')==False:
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc', config.access_rights)
                    
			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus')==False:
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus', config.access_rights)	

			FrameS1.pack_forget()
			Load_DDS_OGF_SystemWeaphonName_step3.window(root_name=root, prj_name=project_name, status_fill=status_fill)
			#root.title(win_name+' — '+prj_name)

		else:
			mb.showerror(win_name, 'Произошла неизвестная ошибка в создании проекта!')	




	def RedirectionFunction_CreateProjectFolder_OUTFIT(entry_project_name, FrameS1, root, status_fill):
		try:
			project_name=(entry_project_name).replace(' ', '_')
		except AttributeError:
			project_name=(entry_project_name.get()).replace(' ', '_')

		if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name) == False:
			os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name, config.access_rights)
			#print(os.path.expandvars('%windir%'))
			if os.path.isdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/'+'gamedata') == False and project_name!='':

				os.makedirs(config.folder_projects+chr(92)+config.folder_projects_soc+'/'+project_name+'/'+'gamedata', config.access_rights)

				prj_name=project_name

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc')==False: # тут будут характеристики костюма
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc', config.access_rights)

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus')==False: # тут будет описание
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus', config.access_rights)

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/equipments')==False: # модель костюма, лежащего на земле
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/equipments', config.access_rights)   
                        
				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/actors/hero')==False: # модель костюма, надетого на игрока
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/actors/hero', config.access_rights)

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/act')==False: # текстуры костюма
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/act', config.access_rights)

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/ui')==False: # текстуры инвентаря
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/ui', config.access_rights)
					shutil.copy('res/default_ui/SoC/ui_icon_equipment.dds', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/'))
					shutil.copy('res/default_ui/SoC/ui_icons_npc.dds', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/'))


				FrameS1.pack_forget()
				Outfit_loadDDSOGF.window(root_name=root, prj_name=project_name, status_fill=status_fill)
				root.title(win_name+' — '+prj_name)

		elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name) == True and status_fill==False:
			mb.showerror(win_name, 'Проект с таким именем уже существует! Введите другое название!')	

		elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name) == True and status_fill==True:
			#mb.showerror(win_name, 'Проект с таким именем уже существует! Введите другое название!')
			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc')==False: # тут будут характеристики костюма
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc', config.access_rights)

			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus')==False: # тут будет описание
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus', config.access_rights)

			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/equipments')==False: # модель костюма, лежащего на земле
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/equipments', config.access_rights)   
                    
			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/actors/hero')==False: # модель костюма, надетого на игрока
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/actors/hero', config.access_rights)

			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/act')==False: # текстуры костюма
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/act', config.access_rights)

			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/ui')==False: # текстуры инвентаря
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/ui', config.access_rights)
				shutil.copy('res/default_ui/SoC/ui_icon_equipment.dds', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/'))
				shutil.copy('res/default_ui/SoC/ui_icons_npc.dds', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/'))


			FrameS1.pack_forget()
			Outfit_loadDDSOGF.window(root_name=root, prj_name=project_name, status_fill=status_fill)
			#root.title(win_name+' — '+prj_name)

		else:
			mb.showerror(win_name, 'Произошла неизвестная ошибка в создании проекта!')	


	def RedirectionFunction_AddEATSysNameDDSOGF(entry_project_name, FrameS1, root, status_fill):
		#project_name=(entry_project_name.get()).replace(' ', '_')
		try:
			project_name=(entry_project_name).replace(' ', '_')
		except AttributeError:
			project_name=(entry_project_name.get()).replace(' ', '_')

		if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name) == False:
			os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name, config.access_rights)

			if os.path.isdir(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/'+'gamedata') == False and project_name!='':

				os.makedirs(config.folder_projects+chr(92)+config.folder_projects_soc+'/'+project_name+'/'+'gamedata', config.access_rights)

				prj_name=project_name

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc')==False: # тут будут характеристики еды
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc', config.access_rights)

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/equipments')==False: # модель еды
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/equipments', config.access_rights)

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/item')==False: # текстуры еды
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/item', config.access_rights)

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus')==False: # тут будет описание
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus', config.access_rights)

				if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/ui')==False: # текстуры инвентаря
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/ui', config.access_rights)
					shutil.copy('res/default_ui/SoC/ui_icon_equipment.dds', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/'))
				
				FrameS1.pack_forget()
				AddEATSysNameDDSOGF.window(root_name=root, prj_name=project_name, status_fill=status_fill)
				root.title(win_name+' — '+prj_name)

		elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name) == True and status_fill==False:
			mb.showerror(win_name, 'Проект с таким именем уже существует! Введите другое название!')	

		elif os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name) == True and status_fill==True:

			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc')==False: # тут будут характеристики еды
					os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/misc', config.access_rights)

			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/equipments')==False: # модель еды
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/meshes/equipments', config.access_rights)

			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/item')==False: # текстуры еды
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/item', config.access_rights)

			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus')==False: # тут будет описание
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/config/text/rus', config.access_rights)

			if os.path.exists(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/ui')==False: # текстуры инвентаря
				os.makedirs(config.folder_projects+'/'+config.folder_projects_soc+'/'+project_name+'/gamedata/textures/ui', config.access_rights)
				shutil.copy('res/default_ui/SoC/ui_icon_equipment.dds', (config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/textures/ui/'))

			FrameS1.pack_forget()
			AddEATSysNameDDSOGF.window(root_name=root, prj_name=project_name, status_fill=status_fill)
			#root.title(win_name+' — '+prj_name)

		else:
			mb.showerror(win_name, 'Произошла неизвестная ошибка в создании проекта!')	




	def window():
		def RedirectionFunction_CheckCloseRoot():
			CheckCloseRoot(root_name=root)

		def back_in_START():
			root.destroy()
			START()

		root = Tk()
		root.title(win_name)#+' — Создание проекта')

		x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3.2
		y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3.2
		root.wm_geometry("+%d+%d" % (x, y))  

		root.geometry(win_geometry)
		root.resizable(win_draw, win_draw)
		root.iconbitmap(win_icon)
		root.configure(background=config.bg_color)
		root.protocol('WM_DELETE_WINDOW', RedirectionFunction_CheckCloseRoot)

		root.focus_force()
		root.grab_release()

		#==============ОСНОВА======================

		FrameS1 = Frame(root, bg='#f0f0f0')

		Label(FrameS1, text='Введите название вашего проекта:', font=(config.font_name, config.font_size)).pack()


		entry_project_name = ttk.Entry(FrameS1, width=55)
		entry_project_name.pack()
		entry_project_name.focus()

		text='''
Создается папка с введенным названием, в которой будут создаваться 
и храниться каталоги gamedata. Введенное название должно быть уникальным
'''

		Label(FrameS1, text=text, font=(config.low_font_name, config.low_font_size), justify=LEFT).pack()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

		
		Label(FrameS1, text='Выберите, что Вы собираетесь первым добавить в проект:', font=(config.font_name, config.font_size)).pack()
		Label(FrameS1, text=' ').pack()

		w=30


		FrameSelectionFirstStep = Frame(FrameS1)

		FrameButtonsAddNewType = Frame(FrameSelectionFirstStep)

		ttk.Button(FrameButtonsAddNewType, text='➕ Добавить оружие', width=w, command=lambda: Project_Registration_step1.RedirectionFunction_CreateProjectFolder_WEAPON(entry_project_name=entry_project_name, FrameS1=FrameS1, root=root, status_fill=False)).pack()
		ttk.Button(FrameButtonsAddNewType, text='➕ Добавить бронекостюм', width=w, command=lambda:  Project_Registration_step1.RedirectionFunction_CreateProjectFolder_OUTFIT(entry_project_name=entry_project_name, FrameS1=FrameS1, root=root, status_fill=False)).pack()
		ttk.Button(FrameButtonsAddNewType, text='➕ Добавить еду/медикамент', width=w, command=lambda:  Project_Registration_step1.RedirectionFunction_AddEATSysNameDDSOGF(entry_project_name=entry_project_name, FrameS1=FrameS1, root=root, status_fill=False)).pack()
		ttk.Button(FrameButtonsAddNewType, text='Показать больше...', width=w).pack()

		FrameButtonsAddNewType.pack(side=LEFT, fill=Y, expand=1)

		#print(len('➕ Добавить еду/медикамент'))

		#ProjectListboxWidget = Listbox(FrameSelectionFirstStep, width=20+10, height=5+5, bd=0, highlightcolor='#87CEFA') #87CEFA / #cce4f7
		#ProjectListboxWidget.pack(side=RIGHT)

		Label(FrameSelectionFirstStep, text=' ').pack()

		FrameSelectionFirstStep.pack()

		text2='''
Нажмите на одну из кнопок выше что бы добавить что-то в проект.
'''

		Label(FrameS1, text=text2, font=(config.low_font_name, config.low_font_size), justify=LEFT).pack()


		'''
		Label(FrameS1, text='\nОтметте галочками те пункты, которые будут в вашем проекте:\n', font=(config.font_name, config.font_size)).pack()

		FrameTypeProject = Frame(FrameS1)

		cvar1 = BooleanVar()
		cvar1.set(0)
		c1 = ttk.Checkbutton(FrameS1, text="Оружие", variable=cvar1, onvalue=1, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 10+1), justify=LEFT)
		c1.pack()

		cvar2 = BooleanVar()
		cvar2.set(0)
		c2 = ttk.Checkbutton(FrameS1,text="Броня", variable=cvar2, onvalue=2, offvalue=0)#, bg='#f0f0f0', fg=config.fg_color, font=('Verdana', 10+1), justify=LEFT)
		c2.pack()

		#c1.bind('<Return>', SELF_AnalyzeCheckbuttons)
		FrameTypeProject.pack()

		text2='''
		#Поставив галочки на определенных пунктах, программа автоматически создаст под них 
		#директории, точно повторяющие ветвление в оригинальной игре. После того, как вы
		#выберете все подходящие варианты и введете название проекта, нажмите внизу кнопку,
		#нажмите [Продолжить].
		'''

		Label(FrameS1, text=text2, font=(config.low_font_name, config.low_font_size), justify=LEFT).pack()

		#FrameS1.bind_all('<Return>', RedirectionFunction_RETURN_CreateProjectFolder)
		'''
		#==============================

		FrameBtn = LabelFrame(FrameS1, bg='#DCDCDC', text='')
		ttk.Button(FrameBtn, text='Вернутся в лаунчер', width=23, state=DISABLED).pack(side=RIGHT)
		ttk.Button(FrameBtn, text='<<< Отмена', width=23, state=NORMAL, command=back_in_START).pack(side=LEFT)
		AuthorLabel(FrameBtn)

		FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
		FrameS1.pack(side=BOTTOM, fill=BOTH, expand=1)
		
		#==========================================

		root.mainloop()


def Close_List_Games(root_name):
	answer=mb.askyesno('Закрыть программу?', 'Вы действительно хотите закрыть программу?')
	if answer==True:
		root_name.quit()

def ErrorGame():
	mb.showinfo(win_name, 'Адаптация для этой игры находится в разработке! На данный момент работает адаптация только для S.T.A.L.K.E.R. Тень Чернобыля.')


def START():
	def Rediction_Function_CLOSE_LIST_GAMES():
		Close_List_Games(root_start)
	#Project_Registration_step1.window()
	def Rediction_Function_SoC_Project_reg():
		root_start.destroy()
		Project_Registration_step1.window()

	root_start = Tk()
	root_start.title(win_name)#+' — Создание проекта')

	x = (root_start.winfo_screenwidth() - root_start.winfo_reqwidth()) / 3
	y = (root_start.winfo_screenheight() - root_start.winfo_reqheight()) / 5
	root_start.wm_geometry("+%d+%d" % (x, y))  

	root_start.geometry('900x550')#win_geometry)
	root_start.resizable(win_draw, win_draw)
	root_start.iconbitmap(win_icon)
	root_start.configure(background=config.bg_color)
	root_start.protocol('WM_DELETE_WINDOW', lambda: Close_List_Games(root_start))
	root_start.focus_force()
	root_start.grab_set()
	#==============ОСНОВА======================

	FrameS0 = Frame(root_start, bg='#f0f0f0')

	FrameTitle = LabelFrame(FrameS0, bg='#DCDCDC', text='')
	image = Image.open(path_win_logo)
	img2 = ImageTk.PhotoImage(image)
	Label(FrameTitle, image=img2, bg='#DCDCDC').pack()
	FrameTitle.pack(side=TOP, fill=X)

	Label(FrameS0, text='Выберите игру, с которой будем работать:', font=(config.font_name, config.font_size)).pack()

	FrameGameSelection = Frame(FrameS0)

	path_soc = 'res/SoC.jpg'
	image_soc = Image.open(path_soc)
	loaded_image_soc = ImageTk.PhotoImage(image_soc)
	ttk.Button(FrameGameSelection, image=loaded_image_soc, command=Rediction_Function_SoC_Project_reg).pack(side=LEFT, anchor=N)

	path_cs='res/CS.jpg'
	image_cs = Image.open(path_cs)
	loaded_image_cs = ImageTk.PhotoImage(image_cs)
	ttk.Button(FrameGameSelection, image=loaded_image_cs, state=NORMAL, command=ErrorGame).pack(side=LEFT, anchor=N)

	path_cop='res/CoP.jpg'
	image_cop = Image.open(path_cop)
	loaded_image_cop = ImageTk.PhotoImage(image_cop)
	ttk.Button(FrameGameSelection, image=loaded_image_cop, state=NORMAL, command=ErrorGame).pack(side=LEFT, anchor=N)

	FrameGameSelection.pack()

	Label(FrameS0, text='Адаптации для S.T.A.L.K.E.R. Чистое Небо и Зов Припяти находятся еще в разработке!', font=(config.low_font_name, config.low_font_size), fg='red').pack()


	FrameBtn = LabelFrame(FrameS0, bg='#DCDCDC', text='')
	ttk.Button(FrameBtn, text='Вернутся в лаунчер', width=23, state=DISABLED).pack(side=RIGHT)
	ttk.Button(FrameBtn, text='❌ Выход ❌', width=23, command=lambda: Close_List_Games(root_start)).pack(side=LEFT)
	#Label(FrameBtn, text=author_label, bg='#DCDCDC').pack(anchor=S)
	AuthorLabel(FrameBtn)

	FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
	FrameS0.pack(side=BOTTOM, fill=BOTH, expand=1)

	root_start.mainloop()

if __name__=='__main__':
	START()