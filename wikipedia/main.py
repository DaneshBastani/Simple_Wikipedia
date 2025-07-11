from flask import Flask,render_template
import wikipedia
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)
app.config['SECRET_KEY']= 'Secret_key'


#Creating the form
class Searches(FlaskForm):
    text=StringField('Enter the Text')
    submit = SubmitField('Enter')

    

@app.route('/')
def home():
    form = Searches()
    return render_template('index.html',form=form)


@app.route('/searching',methods=['GET','POST'])
def searches():
    form = Searches()
    text1 = form.text.data
    result=wikipedia.summary(text1)
    return render_template('searching.html',result=result)
if __name__=='__main__':
    app.run(debug=True)