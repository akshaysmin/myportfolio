from flask import Flask, url_for, render_template, request, redirect
import csv
app=Flask(__name__)
print(__name__)
print(app)


'''
#how to run server
1.Create virtual environment:
	on command prompt: python -m venv <name of venv folder>
2.Activate python interpretor in virtual environment:
	on command prompt: "<venv folder>\Scripts\ activate.bat"
3.Install flask using: pip install Flask
4.Write a python file say server.py like this file, inside venv folder
5.Add FLASK_APP to environment variable:
	on command prompt: set FLASK_APP=<python file name say, "server.py">
6.Set server as live server or setting debug=true:
	on command prompt: set FLASK_ENV=development
7.Start server:
	on command prompt: flask run
#comments for server.py
@app.route('<path>') - on requests to localhost/path return value of the function is returned
render_template('<html file>') - goes to templates folder then returns the html file
{{<python expression>}} - anything inside {{}} in html file is evaluated as a python expression
						-uses jinja templating language
						-if possible, replaces placeholder inside with value passed
						 as keyword argument in render_template method

'''

@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/<string:page_name>')
def get_page(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data=request.form.to_dict()
		print(data)
		write_to_csv(data)
	return render_template('thankyou.html',form_name=data.get('email'))
	#return redirect('thankyou.html')

def write_to_csv(data):
	with open('database.csv','a',newline='') as db:
		email=data.get('email')
		subject=data.get('subject')
		message=data.get('message')
		csv_writer=csv.writer(db, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow((email,subject,message))

if __name__=='__main__':
	app.run()