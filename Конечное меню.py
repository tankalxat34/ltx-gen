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

'''

#========КОНСТАНТЫ=============
win_icon='res'+chr(92)+'yellow.ico'
win_name='LTX-Gen'
win_draw=False
#win_geometry='700x420'   
win_geometry='900x500'              #'291x355' # ταŋᶄắḽჯãṫ34
#author_label='tankalxat34 ©2020 - ver1.0' 
author_label='ταŋᶄắḽჯãṫ34 ©2020 - ver1.0' 
simple_author_label='tankalxat34 ©2020 - ver1.0'
#==============================
sys_outfit_name='prorok'
#sys_outfit_name='rose_m132'
outfit_inv_name='Комбинезон «Пророк»'
#sys_wpn_name='laska'
prj_name='броня_для_теста'
#prj_name='оружие_для_теста'
inv_outft_icon='''inv_grid_width     = 2
inv_grid_height    = 3
inv_grid_x         = 18
inv_grid_y         = 33'''
outf_cost='12300'

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
- создать конечное меню для выбора "что еще добавить в проект?"
- начать делать диалог добавления оружия
!!!ВАЖНО!!! ПОЛНОСТЬЮ ПЕРЕСМОТРЕТЬ ДИАЛОГ ДОБАВЛЕНИЯ ОРУЖИЯ ДЛЯ ЕГО МНОГОРАЗОВОГО ИСПОЛЬЗОВАНИЯ. ОСОБЕННО ШАГ ИНИЦИАЛИЗАЦИИ В ИГРЕ!
----------------------------------------------------------------------
- попробовать сделать запись новых текстур в ogf файл.
+ https://www.amk-team.ru/forum/faq/7-spravochnik-vyletov-line-201-line-400/ исправить вылет по этой инструкции. (зайти в геймдату игры и из менить wpn_laska на wpn_las)
+ сделать механизм "в зависимости от наличия спавн меню показывать в главном меню соответствующую надпись".
+ доделать выбор иконки костюма
+ создать механизм создания строчки для записи костюма в outfit.ltx
+ доделать диалог создания бронекостюма
'''


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
	Label(root_name, text='S.T.A.L.K.E.R. {}'.format(win_name), font=('AmazS.T.A.L.K.E.R.v.3.0', config.font_size+20), bg='#DCDCDC').pack()
	#logo = ImageTk.PhotoImage(file="win_logo.png")
	#Label(root_name, image=logo).pack()
	#ttk.Button(root_name, image=image).pack()

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

x = (root_name.winfo_screenwidth() - root_name.winfo_reqwidth()) / 3
y = (root_name.winfo_screenheight() - root_name.winfo_reqheight()) / 6
root_name.wm_geometry("+%d+%d" % (x, y))  

root_name.geometry('900x500')
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


root_name.title(win_name+' ➖ '+prj_name)

########################################################################################################################################################################

desc_END_SLIDE='''
Здесь вы можете осмотреть свой проект прежде чем завершить его наполнение.
Используйте кнопки, что бы добавить что то новое в проект. Если вы хотите
завершить проект, то нажмите на кнопку "ЗАВЕРШИТЬ ПРОЕКТ".

Подробнее о последних изменениях вы можете прочитать в группе ВКонтакте,
перейти в нее можно нажав на одну из кнопок внизу окна.'''



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
		

	project_path=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/'
	PATH_project_info_ltx=config.folder_projects+'/'+config.folder_projects_soc+'/'+prj_name+'/gamedata/config/misc/project_info.ltx'


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
			if re.search(re.escape('[outfit_info'), word):
				outfit_count+=1				
			elif re.search(re.escape('[weapon_info'), word):
				weapon_count+=1
			elif re.search(re.escape('[eat_info'), word):
				eat_count+=1
			elif re.search(re.escape('['), word):
				count+=1

		win_prj_info = Toplevel(root_name)
		win_prj_info.title(win_name+' ➖ информация о '+prj_name)
		win_prj_info.resizable(win_draw, win_draw)
		win_prj_info.iconbitmap(win_icon)
		win_prj_info.geometry('700x500')

		win_prj_info.focus_force()

		FrameTitle = LabelFrame(win_prj_info, bg='#DCDCDC', text='')
		FrameTitle.pack(side=TOP, fill=BOTH)

		WinTitle(FrameTitle)

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
====================ИНФОРМАЦИЯ О ПРОЕКТЕ "{prj_name}"====================
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



def ReloadListEssences():
	if os.path.exists(PATH_project_info_ltx)==True:
		open_project_info_ltx = open(PATH_project_info_ltx, 'r') # получаем список строк из файла
		project_info_ltx = open_project_info_ltx.readlines()
		open_project_info_ltx.close()


		essence_information='''
Имя предмета: {essence_name};
Системное имя предмета: {sys_essence_name};
Вес: {essence_weight};
'''


		# ЗАПУСКАЕМ ЦИКЛ, В КОТОРОМ БУДЕТ РАБОТАТЬ ПАРСЕР LTX ФАЙЛА
		for word in project_info_ltx: 
			if re.search(re.escape('[outfit_info'), word):
				pass

















		win_prj_info = Toplevel(root_name)
		win_prj_info.title(win_name+' ➖ информация о сущности')
		win_prj_info.resizable(win_draw, win_draw)
		win_prj_info.iconbitmap(win_icon)
		win_prj_info.geometry('700x500')

		win_prj_info.focus_force()

		FrameTitle = LabelFrame(win_prj_info, bg='#DCDCDC', text='')
		FrameTitle.pack(side=TOP, fill=BOTH)

		WinTitle(FrameTitle)

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




		win_prj_info.mainloop()


	else:
		mb.showerror(win_name, 'Проверьте наличие файла project_info.ltx по пути:\n\n'+PATH_project_info_ltx+'\n\nи снова повторите попытку!')










Frame_END_SLIDE = Frame(root_name, bg='#f0f0f0')

FrameTitle = LabelFrame(Frame_END_SLIDE, bg='#DCDCDC', text='')
FrameTitle.pack(side=TOP, fill=X)

#Label(FrameTitle, text='S.T.A.L.K.E.R. LTX-Gen 2.0', font=('AmazS.T.A.L.K.E.R.v.3.0', config.font_size+20), bg='#DCDCDC').pack()
WinTitle(FrameTitle)
#-----
Label(Frame_END_SLIDE, text='Добавление новых предметов в проект "'+prj_name+'"', font=(config.font_name, config.font_size)).pack()
ttk.Button(Frame_END_SLIDE, text='Информация о проекте...', width=30, command=BTN_PROJECT_INFORMATION).pack()


Frame_All_Widgets = Frame(Frame_END_SLIDE)

FrameListButtons = Frame(Frame_All_Widgets)
w=30
Label(FrameListButtons, text=' ').pack()
ttk.Button(FrameListButtons, text='\n➕ Добавить оружие\n', width=w).pack()
ttk.Button(FrameListButtons, text='\n➕ Добавить бронекостюм\n', width=w).pack()
ttk.Button(FrameListButtons, text='\n➕ Добавить еду\n', width=w).pack()
ttk.Button(FrameListButtons, text='Показать больше...', width=w, state=DISABLED).pack()

FrameListButtons.pack(side=LEFT, anchor=N)

###############
Frame_Otstup = Frame(Frame_All_Widgets)
Label(Frame_Otstup, text=' ').pack()
Frame_Otstup.pack(side=LEFT, anchor=N)
###############

FrameComponentDemonstration = Frame(Frame_All_Widgets)
Label(FrameComponentDemonstration, text='Содержимое проекта "{}":'.format(prj_name)).pack()
GlobalListbox = Listbox(FrameComponentDemonstration, bd=0, highlightcolor='#87CEFA', width=20+20, height=5+5+2)
GlobalListbox.pack()
FrameComponentDemonstration.pack(side=LEFT, anchor=N)

Frame_All_Widgets.pack()

Label(Frame_END_SLIDE, text=desc_END_SLIDE, font=(config.low_font_name, config.low_font_size), justify=LEFT).pack()

#-----
FrameBtn = LabelFrame(Frame_END_SLIDE, bg='#DCDCDC', text='')
ttk.Button(FrameBtn, text='<< ЗАВЕРШИТЬ ПРОЕКТ >>', width=26).pack(side=RIGHT)
ttk.Button(FrameBtn, text='<<< Отмена [резерв]', width=23).pack(side=LEFT)
AuthorLabel(FrameBtn)

FrameBtn.pack(side=BOTTOM, anchor=W, fill=X)
Frame_END_SLIDE.pack(side=BOTTOM, fill=BOTH, expand=1)

root_name.mainloop()