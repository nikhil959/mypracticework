from flask import Flask,url_for,request
from flask import render_template
from flask import request,abort, redirect, url_for
from mongoprac import mongohandler

app = Flask(__name__)


#url_for('static', filename='some.css')


@app.route('/')
def home():
    return render_template('home.html',name="nikhil")


@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)



@app.route('/results', methods=['POST'])
def search():
  import traceback
  try:

    hi = {'phy':50,'che':60,'maths':70}
    data = request.form['search']
    search=str(hi[data])
    print(search)
    return render_template('wathe.html', search=search)
  except:
    print(traceback.format_exc().splitlines())


@app.route('/user/<username>')
def mystuff(username):
	return '{}\'s profile'.format(username)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()



@app.errorhandler(404)
def page_not_found(error):
    return render_template('errorpage.html'), 404

@app.route('/insert_data',methods=['POST'])



def insert_data():
  try:
    data = request.json
    result = mongohandler().insert_data('testdb','test',data)
    return 'success'
  except Exception as error:
    print(str(error))
    return 'fail'



if __name__ == '__main__':
   app.run(debug = True)
