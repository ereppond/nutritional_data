# import nutritional_data.csv as data 
import pandas as pd 
import numpy as np 
import sys


'''need to ask if they want to specify their calories OR their macros  '''
def specifications():
	dict_of_specifications = {'calories': 2000, 'proteins': 150, 'carbs': 150, 'fats': 50, 'meals': 3}
	#calories or macros 
	if input('Would you like to specify calories or macronutrient daily count? Enter cal or macros: ') == 'cal'.lower():
		dict_of_specifications = calories_to_macros(dict_of_specifications)
	else: 
		dict_of_specifications = macros_to_calories(dict_of_specifications)
	
	dict_of_specifications['meals'] = int(input('Input the number of meals you eat per day: '))
	#user can choose to set the percentages of calories per meal 
	keys = [i + 1 for i in range(dict_of_specifications['meals'])]

	#this will initiate the percentages of macros the user would like for each meal they have
	num_of_meals = {key: None for key in keys}
	if input('Would you like to specify the percentage of calories being divided amoungst each meal? y/n ') == 'y'.lower():
		for i in range(len(keys)):
			num_of_meals[i + 1] = input('What percentage (in decimal form) of calories would you like meal {} to be? '.format(i + 1))
	#if they choose not to specify the percentages, it will automatically set equally 
	else:
		num_of_meals = {key: 1/dict_of_specifications['meals'] for key in keys}

	user = Sort_Nutr(dict_of_specifications['calories'], dict_of_specifications['proteins'],\
		dict_of_specifications['carbs'], dict_of_specifications['fats'], num_of_meals)

	return user



def calories_to_macros(dict_of_specifications):
	'''This method will clarify how many calories the user would like, as well as calculating the macros
	based off of what percentages of each they would like'''
	dict_of_specifications['calories'] = int(input('Input the number of calories you would like to eat per day: '))
	for key in dict_of_specifications:
		if key != 'calories' and key != 'meals':
			perc = float(input('Input the percentage(in decimal form) of calories you would like to be {}: '.format(key)))
			dict_of_specifications[key] = dict_of_specifications['calories'] * perc
	return dict_of_specifications



def macros_to_calories(dict_of_specifications):
	'''This method will take in the specifications of macros and return the updated dictionary with the proper number
	of calories'''
	calories = 0
	dict_of_specifications['proteins'] = float(input('Input the number of proteins(in grams) you would like to eat per day: ')) * 4
	dict_of_specifications['carbs'] = float(input('Input the number of carbs you(in grams) you would like to eat per day: ')) * 4
	dict_of_specifications['fats'] = float(input('Input the number of fats you(in grams) you would like to eat per day: ')) * 9
	return dict_of_specifications



class Sort_Nutr:
	'''This class will take in different parameters such as ones macros, calories to help identify
	which foods will fit into each different meal and/or day'''

	
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
			print('Meal {} calls for {} calories, {}g of protein, {}g of carbs, and {}g of fat'\
				.format(key, macros_per_meal[key][0], macros_per_meal[key][1],macros_per_meal[keys][2],\
					macros_per_meal[key][3]))


	def find_foods(self):
		pass

if __name__ == '__main__':
	user = specifications()
	sorting = Sort_Nutr()
	sorting.calc_cals_per_meal()
