from flask import Flask,url_for,request,Response,jsonify
from flask import request,abort, redirect, url_for
import traceback
import json


app = Flask(__name__)


@app.route('/example',  methods=['GET'])
def example():
	data = { 'description': 'salary', 'amount': 5000 }
	try:

		return jsonify(data)

	except:
		print(traceback.format_exc().splitlines())




@app.route('/example1',  methods=['POST'])
def example1():
	# data = { 'description': 'salary', 'amount': 5000 }
	try:
		data=request.json
		print(data)
		return jsonify(data)

	except:
		print(traceback.format_exc().splitlines())
