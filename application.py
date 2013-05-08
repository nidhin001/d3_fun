from flask import Flask,request,Response,redirect,url_for,session,abort,render_template,flash

DEBUG = True
SECRET_KEY = ('replace with your secret key')

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def home():
  return render_template('home.html', navbar = 'home')

@app.route('/_data')
def data():
  
  return  1

if __name__ == '__main__':
  app.run()


