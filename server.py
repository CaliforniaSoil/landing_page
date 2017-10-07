from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')
@app.route('/ninjas')
def success():
  return render_template('ninjas.html')
@app.route('/dojos/news')
def about():
  return render_template('news.html')
app.run(debug=True)                          
