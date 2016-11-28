import knitgit_functions
from knitgit_classes import Sweater


def main():
	print """

vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
 v v v v v v v v v v v v v v v v v v v v v v v v v v v v
    vv     vv     o    vv     vv     o    vv     vv
    vvv   vvv          vvv   vvv          vvv   vvv
vvv vvvv vvvv vvv  vvv vvvv vvvv vvv  vvv vvvv vvvv vvv
 vvv vvv vvv vvv    vvv vvv vvv vvv    vvv vvv vvv vvv
  vvv vv vv vvv      vvv vv vv vvv      vvv vv vv vvv
        o                  o                  o
  vvv vv vv vvv      vvv vv vv vvv      vvv vv vv vvv  
 vvv vvv vvv vvv    vvv vvv vvv vvv    vvv vvv vvv vvv
vvv vvvv vvvv vvv  vvv vvvv vvvv vvv  vvv vvvv vvvv vvv
    vvv   vvv          vvv   vvv          vvv   vvv
    vv     vv    o     vv     vv     o    vv     vv 
 v v v v v v v v v v v v v v v v v v v v v v v v v v v v
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
   
                    GIT YOUR KNIT ON

	"""

	sweater_parameters = [		#setting this up for looping, so I can use this code for future sweaters with different parameters.
					["raw_gauge_st", "stitches to achieve 4 inches across (whole number!):\n"], 
					["raw_gauge_r", "rows to achieve 4 inches up (whole number!):\n"], 
					["raw_trs_length", "length in inches from under-arm seam to hem of the sweater:\n"],
					["raw_trs_width", "length in inches all the way around chest:\n"],
					["raw_slv_length", "length in inches from under-arm seam to cuff of sleeve:\n"]
					]

	sweater_attributes = {}					#to receive the user inputs for 5 variables -- MOST IMPORTANT PART OF THIS CODE!!!!

	for param in sweater_parameters:		#asking user for their measurements
		user_input = raw_input("Please enter the " + param[1])
		sweater_attributes[param[0]] = user_input		#tested, working

###validate input!!!!!!!!!!!!!!!!!!

	this_sweater = Sweater(int(sweater_attributes["raw_gauge_st"]), 	#easier to typacast BEFORE handing over to object.  huzzah!
						int(sweater_attributes["raw_gauge_r"]), 
						float(sweater_attributes["raw_trs_length"]), 
						float(sweater_attributes["raw_trs_width"]), 
						float(sweater_attributes["raw_slv_length"]))	#it works!!!!!!!!  :D

	knitgit_functions.torso_start(this_sweater)		#do I need any value returned???

	knitgit_functions.sleeve_start(this_sweater)		#do I need any value returned???

	knitgit_functions.neck_start()



if __name__ == '__main__':
	main()