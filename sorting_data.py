# import nutritional_data.csv as data 
import pandas as pd 
import numpy as np 
import sys


def specifications():
	'''This function asks the user what their daily intake specifications are.

	Returns:
		user: a Sort_Nutr object with parameters of specifications that the user inputted 
	'''
	specs_dict = {'calories': 2000, 'proteins': 150, 'carbs': 150, 'fats': 50, 'meals': 3}
	if input('Would you like to specify calories or macronutrient daily count? Enter cal or macros: ') == 'cal'.lower():
		specs_dict = calories_to_macros(specs_dict)
	else: 
		specs_dict = macros_to_calories(specs_dict)
	
	specs_dict['meals'] = int(input('Input the number of meals you eat per day: '))
	keys = [i + 1 for i in range(specs_dict['meals'])]

	num_of_meals = {key: None for key in keys}
	if input('Would you like to specify the percentage of calories being divided amoungst each meal? y/n ') == 'y'.lower():
		for i in range(len(keys)):
			num_of_meals[i + 1] = input('What percentage (in decimal form) of calories would you like meal {} to be? '.format(i + 1))
	#If they choose not to specify the percentages, it will automatically set equally.
	else:
		num_of_meals = {key: 1/specs_dict['meals'] for key in keys}

	user = Sort_Nutr(specs_dict['calories'], specs_dict['proteins'],\
		specs_dict['carbs'], specs_dict['fats'], num_of_meals)

	return user



def calories_to_macros(specs_dict):
	'''This method will clarify how many calories the user would like, as well as calculating the macros based off of what percentages of each they would like

	Parameters: 
		specs_dict: A dictionary of the specifcations of meals and how they are each divided into proteins, carbs, and proteins'''
	specs_dict['calories'] = int(input('Input the number of calories you would like to eat per day: '))
	for key in specs_dict:
		if key != 'calories' and key != 'meals':
			perc = float(input('Input the percentage(in decimal form) of calories you would like to be {}: '.format(key)))
			specs_dict[key] = specs_dict['calories'] * perc
	return specs_dict



def macros_to_calories(specs_dict):
	'''This method will take in the specifications of macros and return the updated dictionary with the proper number
	of calories'''
	calories = 0
	specs_dict['proteins'] = float(input('Input the number of proteins(in grams) you would like to eat per day: ')) * 4
	specs_dict['carbs'] = float(input('Input the number of carbs you(in grams) you would like to eat per day: ')) * 4
	specs_dict['fats'] = float(input('Input the number of fats you(in grams) you would like to eat per day: ')) * 9
	return specs_dict



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
				'''need to fix this line above'''

	def find_foods(self):
		pass

if __name__ == '__main__':
	user = specifications()
	sorting = Sort_Nutr()
	sorting.calc_cals_per_meal()
