import nutritional_data.csv as data 
import pandas as pd 
import numpy as np 

def specifications():
	dict_of_specifications = {'calories': 2000, 'proteins': 150, 'carbs': 150, 'fat': 50, 'meals': 3}
	for key in dict_of_specifications:
		if raw_input('The default number of {} is {}. Would you like to specify a different amount? y/n '\
			.format(key, dict_of_specifications[key])) == 'y'.lower():
	 		dict_of_specifications[key] = raw_input('Input the number of {} you eat per day: '.format(key))
	keys = [i + 1 for i in range(dict_of_specifications['meals'])]
	num_of_meals = {key: None for key in keys}
	if raw_input('Would you like to specify the percentage of calories being divided amoungst each meal? y/n ') == 'y'.lower():
		for i in range(len(keys)):
			num_of_meals[i] = raw_input('What percentage of calories would you like meal {} to be? '.format(i))
	else:
		num_of_meals = {key: 0.333 for key in keys}





class Sort_Nutr:
	'''This class will take in different parameters such as ones macros, calories to help identify
	which foods will fit into each different meal and/or day'''

	def __init__(self, calories = 2000, num_of_meals = {'breakfast': [], 'lunch':[], 'dinner':[]}, protein = 150, carbs = 150, fats = 50):
		self.calories = calories
		self.num_of_meals = num_of_meals
		self.protein = protein
		self.carbs = carbs
		self.fats = fats

	def calc_cals_per_meal(self,lst = []):
		'''Calculates the number of calories per meal unless percentage of
		calories per meal specified'''
		if len(lst) > 0:
			return cals_per_meal = calories / num_of_meals
		elif len(lst) == 5:
			pass


	'''if we want to ask them what they would like to do, we need to call an input function
		when we are initializing the self objects

		we can ask how many calories they want per day

		we can ask if they just want breakfast lunch and dinner 
			if they say 'n'
			we can ask them what they would like their meals to be 
				as well as the percentages of calories they would
				like to go with that meal - save in a list orderded by meal
					OR save in a dictionary thats keys are numbers and values are percentages
					**** note cannot save by name because dictionaries keys are sorted
					can initate the dictionary when they give us the number of meals 
			if they say 'y' we will automatically set the meals to 
				breakfast lunch and dinner

		we can ask if they would like their macros set to a standard 2000 calorie day
			if they say 'n'
				they will specify they macros they would like and we will divide 
				the macros accoring to the percentages that were provided earlier 

		question: in an init method, can you run an imput function? 
			for example, could you say:
				self.calories = input(....)