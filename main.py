#-----------------------------------------------------------------------------
# Name:        P2 Resubmission (main.py)
# Purpose:     Correct mistakes in P2
#
# Author:      Michael Chang
# Created:     20-April-2021 
# Updated:     20-April-2021
#-----------------------------------------------------------------------------
'''
8) Documentation
-Changed the diction to correctly correlate to parameter (Line 26) 
-Created better descriptions for parameters and returns (Lines 31, 33, 39, 98, 104) 
 
10) Logging
- Edited logging messages to clearly convey statement (Lines 50, 114, 127, 151, 157, 169) 
'''
import math
import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug("Program Begins")
def possibleMeals(ingrediants, chosen):
	'''
	Finds the maximum amount of meal combinations with no repeats

	Accepts 2 parameters, ingrediants (as an integer) and chosen (as an integer).  If both values are valid, proceeds with calculations and returns value.

	Parameters
	----------
	ingrediants : int
		Number of total ingrediants
	chosen : int
		Number of ingrediants picked 
	

	Returns
	-------
	int
		Number of possible ingrediant arrangements 

	
	Raises
	------
	TypeError
		Raised if ingrediants is not an integer, or if chosen is not an integer.
	ValuError
		Raised if ingrediants is negative or zero, or if chosen is greater than ingrediants.
	'''

	logging.info("Function possibleMeals() beginning with an ingrediants value of " + str(ingrediants) + " and a chosen value of " + str(chosen))
	#Checks if parameter is the correct type
	if not isinstance(ingrediants, int):
		logging.error("Parameter is not the correct type.")
		raise TypeError("Ingrediants is not an acceptable type")
	#Checks if parameter is the correct type
	elif not isinstance(chosen, int):
		logging.error("Parameter is not the correct type.")
		raise TypeError("Chosen is not an acceptable type")
	#Checks if parameter is the correct value
	elif ingrediants <= 0:
		logging.error("Parameter is not in the correct range.")
		raise ValueError("Ingrediants is not an acceptable value")
	#Checks if parameter is the correct value
	elif chosen <= 0 or chosen > ingrediants:
		logging.error("Parameter is not in the correct range.")
		raise ValueError("Chosen is not an acceptable value")
	#Otherwise, proceeds with calculations and returns
	else:
		logging.debug("Proceeds with conversion if parameters are correct.")
		combine = ingrediants
		placement = ingrediants
		while(ingrediants != 1):
			ingrediants -= 1
			combine *= ingrediants
		leftover = placement - chosen
		insurance = leftover		
		store = leftover
		if leftover == 0:
			logging.info("Maximum outcomes with no repeats using ingrediants and chosen when both parameters are equal is calculated to be " + str(combine) + ". Value is being returned.")
			return combine
		else:
			while(leftover != 1):
				leftover -= 1
				store *= leftover
			final = combine/store
			logging.info("Maximum outcomes with no repeats using ingrediants and chosen is calculated to be " + str(final) + ". Value is being returned.")
			return final

def tableSize(radius):
	'''
	Converts given radius to area.

  Accepts 1 parameter, radius (int) and if the input is valid, proceeds with conversion and returns value.
 
  Parameter
  ----------
  radius : int
    Table radius in meters

  
  Returns
  -------
  float
    Area of table in meters
  

  Raises 
  ------
  TypeError
    Raised if radius is not an integer.
	Value Error
		Raised if radius is less than or equal to 0.
	'''
	logging.info("Function tableSize() beginning with a value of " + str(radius) + " meters")
	#Checks if parameter is the correct type
	if not isinstance(radius, int):
		logging.error("Parameter is not the correct type.")
		raise TypeError("Radius is not an acceptable type")
	#Checks if parameter is the correct value
	elif radius <= 0:
		logging.error("Parameter is not in the correct range.")
		raise ValueError("Radius is not an acceptable value")
	#Otherwise, proceeds with calculations and returns value
	else:
		logging.debug("Proceeds with conversion if parameter is correct.")
		calculations = round(math.pi * pow(radius,2),1)
		logging.info("Radius of table is calculated to be " + str(calculations) + " meters. Value is being returned.")
		return calculations

assert possibleMeals(5,2) == 20, "Choosing 2 ingrediants from 5 should equal 20 possible arrangments with no repeats"
assert possibleMeals(10,3) == 720, "Choosing 3 ingrediants from 10 should equal 720 possible arrangments with no repeats"
assert possibleMeals(2,2) == 2, "Choosing 2 ingrediants from 2 should equal 2 possible arrangments with no repeats"
assert possibleMeals(15,5) == 360360, "Choosing 5 ingrediants from 15 should equal 360360 possible arrangments with no repeats"
assert possibleMeals(15,1) == 15, "Choosing 1 ingrediants from 15 should equal 15 possible arrangments with no repeats"

assert tableSize(22) == 1520.5, "Radius of 22 in a circle should have an area of 1520.5"
assert tableSize(2) == 12.6, "Radius of 2 in a circle should have an area of 12.6"
assert tableSize(5) == 78.5, "Radius of 5 in a circle should have an area of 78.5"
assert tableSize(10) == 314.2, "Radius of 10 in a circle should have an area of 314.2"
assert tableSize(150) == 70685.8, "Radius of 150 in a circle should have an area of 70685.8"

#Returns custom error messages if input is incorrect and only continues when inputs are valid
#Calculates the inputs and finds maximum possible outcomes with no repeats
#Prints out which of the stored conversions is greater 
print("************************BreakFast************************")
secondBreakfast = 0
while (secondBreakfast == 0):
	try:
		firstBreakfastStorage = int(input("Please input the number of ingrediants in the first storage room for breakfast: \n"))
		firstBreakfastPicked = int(input("Please input the number of chosen ingrediants for the first storage room for breakfast: \n"))
		logging.info("User entered: " + str(firstBreakfastStorage) + " ingrediants number and " + str(firstBreakfastPicked) + " chosen value for the first stored calculations. Calling function possibleMeals() with those values.")
		firstBreakfast = possibleMeals(firstBreakfastStorage,firstBreakfastPicked)
		logging.debug("Function successful, moving onto next breakfast")

		secondBreakfastStorage = int(input("Please input the number of ingrediants in the second storage room for breakfast: \n"))
		secondBreakfastPicked = int(input("Please input the number of chosen ingrediants for the second storage room for breakfast: \n"))
		logging.info("User entered: " + str(secondBreakfastStorage) + " ingrediants number and " + str(secondBreakfastPicked) + " chosen value for the second stored calculations. Calling function tableSize() with those values.")
		secondBreakfast = possibleMeals(secondBreakfastStorage,secondBreakfastPicked)
		logging.debug("Function successful")
#Prints custom message when exceptions occurs
	except TypeError as e:
		print("Type Error occured: " + str(e))
	except ValueError as e:
		print("Value Error occured: " + str(e))
	except Exception as e:
		print("Unknown Error occured: " + str(e))
#If everything goes well, proceed with maximum outcomes comparison of both storage places
else:
	logging.debug("Everything in the try block is successful, proceed to compare the two values.")
	print("------------------------------------------------------------------------------")
	print("The maximum number of meal combinations in your first stoarge room for breakfast: "
	+ str(firstBreakfast))
	print("The maximum number of meal combinations in your second stoarge room for breakfast: " 
	+ str(secondBreakfast))
	if firstBreakfast > secondBreakfast:
		print("The first stoarge room contains " + str(firstBreakfast - secondBreakfast) + " more combinations of meals")
		logging.debug("First storage room contains more combinations")
	elif firstBreakfast < secondBreakfast:
		print("The second stoarge room contains " + str(secondBreakfast - firstBreakfast) + " more combinations of meals")
		logging.debug("Second storage room contains more combinations")
	else:
		logging.debug("Both storage room contains same number combinations")
		print("Both stoarge room contains " + str(firstBreakfast) + " combinations of meals")
	print("------------------------------------------------------------------------------")

#Returns custom error messages if input is incorrect and only continues when inputs are valid
#Calculates the inputs and finds maximum possible outcomes with no repeats
#Prints out the sum of both stored calculations 	
print("************************Lunch************************")
secondLunch = 0
while (secondLunch == 0):
	try:
		firstLunchStorage = int(input("Please input the number of ingrediants in the first storage room for lunch: \n"))
		logging.info("User inputed value for the number of ingrediants in the first storage room: " + str(firstLunchStorage))
		firstLunchPicked = int(input("Please input the number of chosen ingrediants for the first storage room for lunch: \n"))
		logging.info("User inputed value for the number of ingrediants chosen in the first storage room: " + str(firstLunchPicked))
		firstLunch = possibleMeals(firstLunchStorage,firstLunchPicked)
		secondLunchStorage = int(input("Please input the number of ingrediants in the second storage room for lunch: \n"))
		secondLunchPicked = int(input("Please input the number of chosen ingrediants for the second storage room for lunch: \n"))
		secondLunch = possibleMeals(secondLunchStorage,secondLunchPicked)
	#Prints custom message when exceptions occurs
	except TypeError as e:
		print("Type Error occured: " + str(e))
	except ValueError as e:
		print("Value Error occured: " + str(e))
	except Exception as e:
		print("Unknown Error occured: " + str(e))
#If everything goes well, proceed with maximum outcomes addition of both storage places
else:
	logging.debug("Everything in the try block is successful, proceed to add both values.")
	print("------------------------------------------------------------------------------")
	print("The maximum number of meal combinations in the first stoarge room: "
	+ str(firstLunch))
	logging.info("Maximum number of meals calcualted in the first storage room: " + str(firstLunch))
	print("The maximum number of meal combinations in the second stoarge room: " 
	+ str(secondLunch))
	logging.info("Maximum number of meals calculated in the second storage room: " + str(secondLunch))
	total = firstLunch + secondLunch
	print("The total amount of possible meal combinations for the first storage room and the second storage room: " + str(total))
	logging.info("Combined Maximum number of meals calculated in both storage room: " + str(total))
	print("------------------------------------------------------------------------------")

#Returns custom error messages if input is incorrect and only continues when inputs are valid
#Allows user to input as much as they want and calculates the area of all circles using the given radius
print("*************Circle Table Area Calculator*************")
tables = []
confirmed = []
try:
	addInput = int(input("Input the radius of tables and type '0' to exit: \n"))
	while (addInput != 0):
		tables.append(addInput)
		addInput = int(input("Input the radius of tables and type '0' to exit: \n"))
	print("Table Areas: ")
	for items in tables:
		confirmed.append(tableSize(items))
#Prints custom message when exceptions occurs
except TypeError as e:
	print("Type Error occured: " + str(e))
except ValueError as e:
	print("Value Error occured: " + str(e))
except Exception as e:
	print("Unknown Error occured: " + str(e))
#If everything goes well, prints circle area of provided radius
else:
	logging.debug("Everything in the try block is successful, proceed to print circle area of provided radius.")
	for items in confirmed:
		print(str(items) + "!")

#Returns custom error messages if input is incorrect and only continues when inputs are valid
#Allows user to input as much as they want and calculates the area of a circle using the given radius
#Prints out the average circle area of all given inputs
print("*************Average Circle Table Area Calculator*************")
tables = []
combinedValue = 0
try:
	addInput = int(input("Input the radius of tables and type '0' to exit and find average area of tables: \n"))
	while (addInput != 0):
		tables.append(tableSize(addInput))
		addInput = int(input("Input the radius of tables and type '0' to exit and find average area of tables: \n"))
#Prints custom message when exceptions occurs
except TypeError as e:
	print("Type Error occured: " + str(e))
except ValueError as e:
	print("Value Error occured: " + str(e))
except Exception as e:
	print("Unknown Error occured: " + str(e))
#If everything goes well, prints average circle area of all inputs from provided radius
else:
	logging.debug("Everything in the try block is successful, proceed to calculate average circle area.")
	print("Average Area of Provided Tables: ")
	for i in range (0,len(tables),1):
		if tables[i] == len(tables)+1:
			break
		else:
			combinedValue += tables[i]
	print(str(round(combinedValue/len(tables))))
	

		


