from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template


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
RAGLAN_LIST = None

@app.route('/', methods=['POST'])
def receive_input():

	SWEATER_ATTRIBUTES["raw_gauge_st"] = int(request.form['raw_gauge_st'])
	# request.args.get(:raw_gauge_st") ???
	SWEATER_ATTRIBUTES["raw_gauge_r"] = int(request.form['raw_gauge_r'])
	SWEATER_ATTRIBUTES["raw_trs_length"] = float(request.form['raw_trs_length'])
	SWEATER_ATTRIBUTES["raw_trs_width"] = float(request.form['raw_trs_width'])
	SWEATER_ATTRIBUTES["raw_slv_length"] = float(request.form['raw_slv_length'])

	SWEATER_OBJECT = knitgit4flask.main(SWEATER_ATTRIBUTES)
	RAGLAN_LIST = knitgit4flask.raglan(SWEATER_ATTRIBUTES)

	# return jsonify(SWEATER_OUTPUT) #replace with below....
	return render_template("knitgit_pattern_output.html", sweater = SWEATER_OBJECT, raglan = RAGLAN_LIST)

# lst = ["apple", 1]

# {{ lst[0] }}
# {{ lst3[3] }}


if __name__ == "__main__":
	app.run(debug=True, port=5000)