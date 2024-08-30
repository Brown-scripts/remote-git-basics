from flask import Flask,render_template
from markupsafe import escape
import os
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

app= Flask(__name__)


# Configuring the current path of the project
current_path=os.path.abspath(os.path.dirname(__file__))
print('current path' ,current_path)


app.config['SQLALCHEMY_DATABASE_URI']=  'sqlite:///'+os.path.join(current_path,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

# Creating our Models
class Student(db.Model):
    __tablename__='Student'
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.Text)
    age= db.Column(db.Integer)
    gender= db.Column(db.Text)
    allowance=db.Column(db.Integer)
    




    def __init__(self,name:str,age:int,gender:str,allowance:int):
        self.name=name
        self.age=age
        self.gender=gender
        self.allowance=allowance

    def __repr__(self) -> str:
        return f"{self.name},{self.age},{self.gender},{self.allowance}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    # make a query to the database and get a list of the students
    students_from_database=Student.query.all()
    return render_template('students.html',students=students_from_database)

@app.route('/students/<name>')
def delete_students(name):
    # get a list of all the students from the db
    Student.query.filter(Student.name == name).delete(synchronize_session=False)
    remaining_students = Student.query.all()
    db.session.add_all(remaining_students)
    db.session.commit()
    return render_template('students.html',students=remaining_students)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# Add a student(name,age,gender)
# create an instance of student with the details
# add a new student to the database
# commit to the database
# render the student to the html page
# add button to page for this functionality




