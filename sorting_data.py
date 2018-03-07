#import nutritional_data.csv as data 
import pandas as pd 
import numpy as np 
import sys

def specifications():
	dict_of_specifications = {'calories': 2000, 'proteins': 150, 'carbs': 150, 'fats': 50, 'meals': 3}
	for key in dict_of_specifications:
		if input('The default number of {} is {}. Would you like to specify a different amount? y/n '\
			.format(key, dict_of_specifications[key])) == 'y'.lower():
	 		dict_of_specifications[key] = int(input('Input the number of {} you eat per day: '.format(key)))
	keys = [i + 1 for i in range(dict_of_specifications['meals'])]
	num_of_meals = {key: None for key in keys}
	if input('Would you like to specify the percentage of calories being divided amoungst each meal? y/n ') == 'y'.lower():
		for i in range(len(keys)):
			num_of_meals[i + 1] = input('What percentage of calories would you like meal {} to be? '.format(i + 1))
	else:
		num_of_meals = {key: 1/dict_of_specifications['meals'] for key in keys}

	user = Sort_Nutr(dict_of_specifications['calories'], dict_of_specifications['proteins'],\
		dict_of_specifications['carbs'], dict_of_specifications['fats'], num_of_meals)

	return user


class Sort_Nutr:
	'''This class will take in different parameters such as ones macros, calories to help identify
	which foods will fit into each different meal and/or day'''

	pass
	def __init__(self, calories = 2000, protein = 150, carbs = 150, fats = 50, num_of_meals = {1: 0.33, 2: 0.33, 3: 0.33}):
		self.calories = calories
		self.num_of_meals = num_of_meals
		self.protein = protein
		self.carbs = carbs
		self.fats = fats

	def calc_cals_per_meal(self):
		'''Calculates the number of calories per meal unless percentage of
		calories per meal specified'''
		macros_per_meal = {key: [] for key in self.num_of_meals}
		for key in self.num_of_meals:
			macros_per_meal[key].append(round(self.num_of_meals[key] * self.calories, 3))
			macros_per_meal[key].append(round(self.num_of_meals[key] * self.protein, 3))
			macros_per_meal[key].append(round(self.num_of_meals[key] * self.carbs, 3))
			macros_per_meal[key].append(round(self.num_of_meals[key] * self.fats, 3))
		for key in macros_per_meal:
			print('Meal {} calls for {} calories, {}g of protein, {}g of carbs, and {}g of fat.'\
				.format(key, macros_per_meal[key][0], macros_per_meal[key][1],macros_per_meal[key][2],\
					macros_per_meal[key][3]))


	def find_meals():
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
	'''