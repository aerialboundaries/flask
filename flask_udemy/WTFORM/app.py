from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, IntegerField
from wtforms.form import Form


app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xa6\x94\xa0-cI\xd7\xc0\xa3\x93%\xec}\x07\x98.'

class UserForm(Form):
    name = StringField('名前')
    age = IntegerField('年齢')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = age = ''
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            name = form.name.data
            age = form.age.data
            form.name.data = ''
            form.age.data = ''
        else:
            print('入力内容に問題があります')

    return render_template('index.html', form=form, name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True)