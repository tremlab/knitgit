# github: tremlab
# Hackbright Intro 2016

from 	knitgit_classes import Sweater
import 	knitgit_functions


def main(SWEATER_ATTRIBUTES):	#pass dictionary

	THIS_SWEATER = Sweater(int(SWEATER_ATTRIBUTES["raw_gauge_st"]), 	#accepts users maesurements, returns sweater object
						int(SWEATER_ATTRIBUTES["raw_gauge_r"]), 
						float(SWEATER_ATTRIBUTES["raw_trs_length"]), 
						float(SWEATER_ATTRIBUTES["raw_trs_width"]), 
						float(SWEATER_ATTRIBUTES["raw_slv_length"]))							

	return THIS_SWEATER

def raglan(SWEATER_ATTRIBUTES):			#refactor!!!!  Creating same object again to get to the raglan loop....

	THIS_SWEATER = Sweater(int(SWEATER_ATTRIBUTES["raw_gauge_st"]), 	
						int(SWEATER_ATTRIBUTES["raw_gauge_r"]), 
						float(SWEATER_ATTRIBUTES["raw_trs_length"]), 
						float(SWEATER_ATTRIBUTES["raw_trs_width"]), 
						float(SWEATER_ATTRIBUTES["raw_slv_length"]))	

	RAGLAN_DECREASE = knitgit_functions.raglan_decrease(THIS_SWEATER)

	return RAGLAN_DECREASE    #this is a LIST... jinja will loop through

	

# if __name__ == '__main__':
# 	main()


#####below was for text file output:

# import 	knitgit_output



	# TORSO_START = knitgit_functions.torso_start(THIS_SWEATER)		

	# SLEEVE_START = knitgit_functions.sleeve_start(THIS_SWEATER)		

	# ASSEMBLE_PIECES = knitgit_functions.assemble_pieces() #no parameters here, same instructions for all sweaters.

	# NECK_START = knitgit_functions.neck_start(THIS_SWEATER)

	# RAGLAN_DECREASE = knitgit_functions.raglan_decrease(THIS_SWEATER) #list?

	# FINISH_SWEATER = knitgit_functions.finish_sweater() #no parameters here, same instructions for all sweaters.


	# instructions_output_list = [
	# 		TORSO_START,
	# 		SLEEVE_START,
	# 		ASSEMBLE_PIECES,
	# 		NECK_START,
	# 		RAGLAN_DECREASE, #was a list, now string - easier to loop through same types
	# 		FINISH_SWEATER

	# knitgit_output.create_sweater_pattern(instructions_output_list)	#creates text file