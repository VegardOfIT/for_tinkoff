import random

class MachineLearning_text():
    #Инициализация класса
	def __init__(self):
		self.dict = {}
		
		
		
	#Метод обучения на выбранных файлах и ограничения списков значений
	def fit(self,files_to_open,number_of_simillar_words):
		#Объявление основного словаря
		dictionary = {}
		
		#Основной цикл 
		for file_to_open in files_to_open:
			
			#Открытие чтение и закрытие
			file = open(file_to_open)
			text = file.read()
			file.close()
			
			#Очистка от мусора
			trash = ("?","!",".",",")
			for object_trash in trash:
				text = text.replace(object_trash, "")
				
			#Приведение к единому размеру
			text = text.lower()
            
			#Преобразование к списку
			text = text.split()
			
			#Создание пар ключ:значение
			for i in range(len(text) - 1):
				
				list_of_word = []
				for j in range(1,number_of_simillar_words+1):
					try:
						list_of_word.append(text[i+j])
					except:
						pass
						
				if dictionary.get(i):	
					dictionary[text[i]] += list_of_word
					
				else:
					dictionary[text[i]] = list_of_word
					
		#Добавление к последнему элементу
		dictionary[text[len(text)-1]] = text[:len(text)-1-number_of_simillar_words]
		
		self.dict = dictionary
	#Метод генерации текста
	
	def generate(self,lenght):
		
		base = random.choice(self.dict.keys())
		
		for i in range(lenght):
			print(base)
			base = random.choice(self.dict[base])
			
