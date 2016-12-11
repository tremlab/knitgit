from flask import Flask
from flask import request
from flask import jsonify

import knitgit4flask


app = Flask(__name__)

SWEATER_ATTRIBUTES = {
	"raw_gauge_st": None,
	"raw_gauge_r": None,
	"raw_trs_length": None,
	"raw_trs_width": None,
	"raw_slv_length": None
	}

SWEATER_OUTPUT = None

@app.route('/', methods=['POST'])
def receive_input():

	SWEATER_ATTRIBUTES["raw_gauge_st"] = int(request.form['raw_gauge_st'])
	SWEATER_ATTRIBUTES["raw_gauge_r"] = int(request.form['raw_gauge_r'])
	SWEATER_ATTRIBUTES["raw_trs_length"] = float(request.form['raw_trs_length'])
	SWEATER_ATTRIBUTES["raw_trs_width"] = float(request.form['raw_trs_width'])
	SWEATER_ATTRIBUTES["raw_slv_length"] = float(request.form['raw_slv_length'])

	SWEATER_OUTPUT = knitgit4flask.main(SWEATER_ATTRIBUTES)


	return jsonify(SWEATER_OUTPUT) #OMG it works!!!! need to format for HTML

	




if __name__ == "__main__":
	app.run(debug=True, port=5000)