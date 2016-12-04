from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_input():
	# SWEATER_ATTRIBUTES = {}
	# SWEATER_ATTRIBUTES 
	print request.form['raw_gauge_st']
	return jsonify('hello') #error

	




if __name__ == "__main__":
	app.run(debug=True, port=5000)