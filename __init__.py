from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import *
from werkzeug.security import *
import os

BASEDIR=os.path.abspath(os.path.dirname(__file__))

####################### INITIALIZING FLASK APP ###################
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASEDIR,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='12345'
app.config['UPLOAD_FOLDER'] = '/static/img/'

db=SQLAlchemy(app)
Migrate(app,db)
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
############################################################






