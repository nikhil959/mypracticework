from flask import Flask,url_for,request,Response,jsonify
from flask import request,abort, redirect, url_for
import traceback
import json

import pymongo
from pymongo import MongoClient

app = Flask(__name__)

class mongohandler():
	def __init__(self):
		self.client=MongoClient('localhost:27017')
		pass


	def connectdb(self,dbname):		
		db=self.client[dbname]
		print('database connected Successfully')
		return db


	def insert_data(self, dbname, collection, insert_data):
		
		# data={'fname':'nikhil','lname':'j','skills':['python','mongodb','Opencv','pymongo']}
		db = self.connectdb(dbname)
		inserted_data = db[collection].insert_one(insert_data)
		print ('data inserted Successfully')
		return inserted_data

	def find_data(self):
		b=self.collec
		c=b.find_one()
		print('The data is......')
		print(c)
		return c





	def update_data(self):
		b=self.collec
		d=b.update_one({'fname':'nikhil'},{ '$set': {'fname':'nikhitha'}})
		print(d)
		print('The updated data is...')
		e=b.find_one()
		print(e)
		return e

   
	@app.route('/',methods=['POST'])
	def insert_api():
		try:
		  data=request.json
		  print(data)
		  b=self.collec
		  c=b.insert_one(jsonify(data))
		  return c

		except:
		  print(traceback.format_exc().splitlines())
