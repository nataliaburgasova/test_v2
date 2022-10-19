from tkinter import *

class TestQuestion: # класс Тестовый вопрос
	def __init__(self,text,correct_variant,variant_of_ansver):
		self.text = text # содержание вопроса
		self.correct_variant = correct_variant # правильный вариант
		self.variant_of_answer= variant_of_ansver # варианты ответа

class Test: # класс Тест
	def __init__(self,title='test',test_question_list = []):
		self.title = title # название теста
		self.test_question_list = test_question_list # список тестовых вопросов
		self.total_questions = len(test_question_list) # количество вопросов в тесте
	
class TestInterface: # интерфейс для теста
	def __init__(self,test):
		self.root = Tk() # основное окно
		self.root.title(test.title) # надпись вверху окна
		self.root.geometry("600x300")# геометрия окна
		self.font = "Arial 12 bold"# шрифт виджетов
		self.lbl_text = StringVar()# переменная lbl
		self.lbl_text.set("для начала теста нажмите кнопку 'начать'")
		self.lbl = Label(textvariable=self.lbl_text,font = self.font,wraplength =300)
		self.lbl.pack(side=TOP)#расположение вверху окна
		self.checkbtn_list =[] #список галочек
		self.score = 0 #счет
		self.variant = StringVar() # вариант ответа выбранный пользователем
		self.variant.set(0) # вариант не выбран
		self.n = 0 # счетчик шагов
		self.lbl_checked = Label(font = "Arial 12 bold") # lbl который пишет Правильно\ неправильно
		self.lbl_checked.pack(side=BOTTOM) # внизу окна
		self.btn = Button(text="начать",font = "Arial 12 bold", command=self.change_lbl_text) # кнопка
		self.btn.pack(side=BOTTOM) #
		self.root.mainloop() #обновление окна

	def change_lbl_text(self): #изменение текста верхнего lbl
		if self.n< test.total_questions:# если число шагов меньше количества вопросов в тесте:
			self.btn.config(text="следующий>>", state=DISABLED,command = self.next_quest) #кнопка меняет текст и тд...
			self.lbl_text.set("Вопрос № {}\n{}".format(self.n+1,test.test_question_list[self.n].text)) # меняется текст лейбла
			self.set_check_btn()# метод установки галочек
			self.lbl_checked.config(text="\nНабрано баллов: {}".format(self.score)) # изменяется текст другог лейбла
		else:
			print("тестирование окончено") # чтобы понять что вопросы кончились
			self.end() # метод конец

	def set_check_btn(self): #метод установки галочек
		for key,value in test.test_question_list[self.n].variant_of_answer.items(): # для ключ,значение присвоить ключ,значение из каждого варианта ответа тестового вопроса
			ch =Checkbutton(text ="{}) {}".format(key,value),font = "Arial 12 bold",onvalue =key,variable =self.variant,command = self.checked)# создает галочку
			ch.pack(expand=1, fill=Y)
			self.checkbtn_list.append(ch) # добавляет в список галочек

	def remove_check_btn(self): # метод удаляет галочки с окна
		if self.checkbtn_list: # если список не пустой
			for ch in self.checkbtn_list: # каждую галочку
				ch.destroy() # убирает с окна
			self.checkbtn_list.clear() # очищает список

	def change_check_btn(self):# метод изменяет свойства галочек
		for ch in self.checkbtn_list:
			ch.config(state=DISABLED)#отключает
			if ch["onvalue"] == test.test_question_list[self.n].correct_variant: # если правильный вариант
				ch.config( disabledforeground="#000", bg="#0f0") # зеленый
			elif ch["onvalue"]== self.variant.get():# иначе
				ch.config(disabledforeground="#fff", bg="#f00") # красный

	def checked(self): # проверка варианта с вариантом ответа
		if self.variant.get() == test.test_question_list[self.n].correct_variant: # если сходится
			self.score+=1 # прибавляет балл
			self.btn.config(state = NORMAL)#делает кнопку активной
			self.lbl_checked.config(text="Правильно\nНабрано баллов: {}".format(self.score))#изменяет лейбл
		else:
			self.lbl_checked.config(text="Вы ошиблись\nНабрано баллов: {}".format(self.score))#изменяет лейбл
			self.btn.config(state = NORMAL)
		self.change_check_btn() # изменяет цвет галочки

        
	def reset(self): # обнуляет переменные в начальное положение
		self.n = 0
		self.score = 0
		self.variant.set(0)
		self.remove_check_btn()
		self.lbl_text.set("для начала теста нажмите кнопку 'начать'")
		self.lbl_checked.config(text='')
		self.btn.config(text="начать", command=self.change_lbl_text)

	def next_quest(self): # следующий шаг
		self.n+=1
		self.variant.set(0)# обнуляет вариант ответа
		self.remove_check_btn()# удаляет старые галки
		self.change_lbl_text() # изменяет лейбл на следующий вопрос

	def end(self): 
		self.lbl_checked.config(text="Тест пройден. Вы свободны\nНабрано баллов: {}".format(self.score))
		self.lbl_text.set("Вопросы закончились")
		
	               
test_question_list=[]
test_question_list.append(TestQuestion("Создатель языка программирования Python",'a',
                                       {'a': 'Гвидо Ван Россум', 'b': 'Дэвид Паттерсон ', 'c': 'Эрвин Дональд Кнут', 'd': 'Джеймс Артур Гослинг'}))
test_question_list.append(TestQuestion("Python является", 'b',
                                       {'a': 'компилируемым языком', 'b': 'интерпретируемым языком'}))
test_question_list.append(TestQuestion("Команда print() используется для", 'a',
                                       {'a': 'вывода данных на экран', 'b': 'считывания данных с клавиатуры'}))
test_question_list.append(TestQuestion("Значения для вывода, указываемые через запятую в команде print(), называются", 'a',
                                       {'a': 'аргументами', 'b': 'символами', 'e':'строками'}))
test_question_list.append(TestQuestion("Какие из имён допустимы для названия переменных в Python?", 'a',
                                       {'a': 'teacher_2', 'b': '2teacher', 'c': '!2_teacher'}))
test_question_list.append(TestQuestion("Вычислите результат целочисленного деления 23//7", 'b',
                                       {'a': '4', 'b': '3', 'e': '5'}))
test_question_list.append(TestQuestion("Вычислите остаток от деления 23%7", 'b',
                                       {'a': '3', 'b': '2', 'e':'1'}))
test_question_list.append(TestQuestion("Что будет выведено на экран в результате выполнения следующей программы? print (82 // 3 ** 2 % 7)", 'a',
                                       {'a': '2', 'b': '41', 'e':'9'}))
test_question_list.append(TestQuestion("Для чего нужен оператор break?", 'a',
                                       {'a': 'Для выхода из цикла', 'b': 'Для завершения программы', 'e':'Для удаления программы'}))
test_question_list.append(TestQuestion("Что делает функция len()", 'b',
                                       {'a': 'Возвращает случайное число ', 'b': 'Возвращает длину строки', 'r':'Возвращает номер символа', 't':'Возвращает модуль числа'}))

test = Test("Что Вы знаете про Python?",test_question_list) # принимает на вход список из тестовыйх вопросов

TestInterface(test) # интерфейс принимает тест

