from flask import Flask,request,Response,redirect,url_for,session,abort,render_template,flash
from flask.ext.sqlalchemy import SQLAlchemy
from database import db_session
from models import Plot

DEBUG = True
SECRET_KEY = ('replace with your secret key')

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
  plots = db_session.query(Plot).filter_by(page='home' ).all()
  #return str(len(plots))
  return render_template('home.html', navbar = 'home', plot_data = plots)

@app.route('/topline')
def topline():
  return render_template('topline.html', navbar = 'topline')


@app.route('/sales')
def sales():
  return render_template('sales.html', navbar = 'sales')




@app.route('/_data')
def data():
  
  return  1

if __name__ == '__main__':
  app.run()


