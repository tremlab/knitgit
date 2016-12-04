from flask import Flask
from flask import request
from flask import jsonify

from knitgit_classes import Sweater 

import knitgit_functions
import knitgit_output

app = Flask(__name__)

SWEATER_ATTRIBUTES = {
	"raw_gauge_st": None,
	"raw_gauge_r": None,
	"raw_trs_length": None,
	"raw_trs_width": None,
	"raw_slv_length": None
	}

@app.route('/', methods=['POST'])
def receive_input():

	SWEATER_ATTRIBUTES["raw_gauge_st"] = int(request.form['raw_gauge_st'])
	SWEATER_ATTRIBUTES["raw_gauge_r"] = int(request.form['raw_gauge_r'])
	SWEATER_ATTRIBUTES["raw_trs_length"] = float(request.form['raw_trs_length'])
	SWEATER_ATTRIBUTES["raw_trs_width"] = float(request.form['raw_trs_width'])
	SWEATER_ATTRIBUTES["raw_slv_length"] = float(request.form['raw_slv_length'])

	THIS_SWEATER - Sweater(SWEATER_ATTRIBUTES)
	

	TORSO_START = knitgit_functions.torso_start(THIS_SWEATER)		

	SLEEVE_START = knitgit_functions.sleeve_start(THIS_SWEATER)		

	ASSEMBLE_PIECES = knitgit_functions.assemble_pieces() #no parameters here, same instructions for all sweaters.

	NECK_START = knitgit_functions.neck_start(THIS_SWEATER)

	RAGLAN_DECREASE = knitgit_functions.raglan_decrease(THIS_SWEATER)

	FINISH_SWEATER = knitgit_functions.finish_sweater() #no parameters here, same instructions for all sweaters.

	instructions_output_list = [
			TORSO_START,
			SLEEVE_START,
			ASSEMBLE_PIECES,
			NECK_START,
			RAGLAN_DECREASE, #was a list, now string - easier to loop through same types
			FINISH_SWEATER
								]

	knitgit_output.create_sweater_pattern(instructions_output_list)



	return jsonify('hello') #give something back to the html....

	




if __name__ == "__main__":
	app.run(debug=True, port=5000)