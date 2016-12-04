import 	knitgit_functions
from 	knitgit_classes import Sweater
import 	knitgit_output



def ask_user_input(param_list):				#loops through parameter list and asks user to assign value for each.

	sweater_attributes = {}					

	for param in param_list:		#asking user for their measurements
		user_input = raw_input("Please enter the " + param[1])
		#basic validation for positive number (int/float) only?
		sweater_attributes[param[0]] = user_input		#tested, working	

	return sweater_attributes #tested - works.


def ask_user_correction(input_dict, key):
	input_dict[key] = raw_input("Please enter the corrected value (numbers only!):\n") #set new value
	corrected_dict = validate_user_input(input_dict) #and test again until there are no errors.
	return corrected_dict  

	

def validate_user_input(input_dict):		#logic works, but research actual values for real-world usage.
	if int(input_dict["raw_gauge_st"]) < 10: 
		print "Your gauge/stitches is too low. :("
		input_dict = ask_user_correction(input_dict, "raw_gauge_st") #it works!!! :D
	elif int(input_dict["raw_gauge_st"]) > 100: 
		print "Your gauge/stitches is too high. :("
		input_dict = ask_user_correction(input_dict, "raw_gauge_st") 
	elif int(input_dict["raw_gauge_r"]) < 10: 
		print "Your gauge/rows is too low. :("
		input_dict = ask_user_correction(input_dict, "raw_gauge_r")
	elif int(input_dict["raw_gauge_r"]) > 100: 
		print "Your gauge/rows is too high. :("
		input_dict = ask_user_correction(input_dict, "raw_gauge_r") 
	elif float(input_dict["raw_trs_width"]) < 25:	
		print "Your torso circumference is too small for this pattern. :( Make sure you measure all the way around!"
		input_dict = ask_user_correction(input_dict, "raw_trs_width")
	elif float(input_dict["raw_trs_width"]) > 100: 
		print "Your torso circumference is too big for this pattern. :("
		input_dict = ask_user_correction(input_dict, "raw_trs_width") 
	# sleevee & torso length -- less urgent, but should set max.
	
	return input_dict   #hooo boy -- not an else statement! wasn't getting any return. :) 


def main():

	print knitgit_functions.print_intro()

	# break this out to a module?
	sweater_parameters = [		#setting this up for looping, so I can use this code for future sweaters with different parameters.
					["raw_gauge_st", "stitches to achieve 4 inches across (whole number!):\n"], 
					["raw_gauge_r", "rows to achieve 4 inches up (whole number!):\n"], 
					["raw_trs_length", "length in inches from under-arm seam to hem of the sweater (decimal ok):\n"],
					["raw_trs_width", "length in inches all the way around the desired chest measurement (decimal ok):\n"],
					["raw_slv_length", "length in inches from under-arm seam to cuff of sleeve (decimal ok):\n"]
					]

	raw_user_input_dict = ask_user_input(sweater_parameters) 			#create dictionary of parameter keys and user's raw input


	sweater_attributes = validate_user_input(raw_user_input_dict) 		#validate all data before executing further code.


	THIS_SWEATER = Sweater(int(sweater_attributes["raw_gauge_st"]), 	#easier to typacast BEFORE handing over to object.  huzzah!
						int(sweater_attributes["raw_gauge_r"]), 
						float(sweater_attributes["raw_trs_length"]), 
						float(sweater_attributes["raw_trs_width"]), 
						float(sweater_attributes["raw_slv_length"]))	#it works!!!!!!!!  :D

	TORSO_START = knitgit_functions.torso_start(THIS_SWEATER)		

	SLEEVE_START = knitgit_functions.sleeve_start(THIS_SWEATER)		

	ASSEMBLE_PIECES = knitgit_functions.assemble_pieces() #no parameters here, same instructions for all sweaters.

	NECK_START = knitgit_functions.neck_start(THIS_SWEATER)

	RAGLAN_DECREASE = knitgit_functions.raglan_decrease(THIS_SWEATER)

	FINISH_SWEATER = knitgit_functions.finish_sweater() #no parameters here, same instructions for all sweaters.

#	this output needs to WRITE to txt or pdf!!!!!!!
	# print TORSO_START
	# print SLEEVE_START
	# print ASSEMBLE_PIECES
	# print NECK_START

	# for line in RAGLAN_DECREASE:
	# 	print line

	# print FINISH_SWEATER

	instructions_output_list = [
			TORSO_START,
			SLEEVE_START,
			ASSEMBLE_PIECES,
			NECK_START,
			RAGLAN_DECREASE, #this is itself a list, not a string - argh! tricky to write from :(
			FINISH_SWEATER
								]

	knitgit_output.create_sweater_pattern(instructions_output_list)

if __name__ == '__main__':
	main()

	#wish I could.... export results to text file. let user save parameters - for future projects. user profile?