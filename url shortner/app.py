from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pyshorteners
import os


shorter=""
url=""

app=Flask(__name__)


############# SQLAlchemy Configuration ###############

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqllite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)  
Migrate(app,db)
######################################################

################## Create a Model ####################

class Data(db.Model):
    __tablename__='urlshortener'
    id=db.Column(db.Integer,primary_key=True)
    url=db.Column(db.String(100))
    shorter = db.Column(db.String(100))
    
    def __init__(self,url,shorter):
        self.url=url
        self.shorter=shorter

        
    
        
@app.before_first_request
def create_tables():
    db.create_all()
    
######################################################

@app.route('/',methods=["GET","POST"])
def home():
    global shorter,url
    if request.method=='POST':
        url=request.form.get('name')
        s_config=pyshorteners.Shortener()
        shorter=s_config.tinyurl.short(url)
        val=Data(url,shorter)
        db.session.add(val)
        db.session.commit()
        
    return render_template('home.html',s_url=shorter)

@app.route('/history')
def history():
    alllinks=Data.query.all()
    return render_template('history.html',alllinks=alllinks)


######################################################
if __name__=="__main__":
    app.run(debug=True)