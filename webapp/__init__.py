#import calendar
from datetime import datetime
import locale
from flask import Flask, render_template, flash, redirect, url_for
from webapp.model import db, Everyday
from webapp.forms import InputForm
from flask_migrate import Migrate
dt_now = datetime.now()


locale.setlocale(locale.LC_ALL, "ru_RU")

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py") 
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        locale.setlocale(locale.LC_ALL, "russian")
        dt_now.strftime('%A %d %B %Y') 
        day = dt_now.strftime('%d.%m.%y')  
        title = f"Сегодня {dt_now.strftime('%A %d %B %Y')} года"
        input_form = InputForm()
        return render_template('input.html', page_title=title, day=day, form=input_form)
        
  
    @app.route('/save-news', methods=['POST'])
    def save_news():
        form = InputForm()
        if form.validate_on_submit():
            date = form.today.data
            date = datetime.strptime(date, '%d.%m.%y').date()
#            news = f'{form.news.data}\n'
            news = {form.news.data}

            new_day = Everyday(day_data=date, day_news=news) 

            db.session.add(new_day)
            db.session.commit()

            return redirect(url_for('day_process'))    

    @app.route('/day_process', methods=['GET'])      
    def  day_process():
        my_day = Everyday.query.all()[-1]
        print(my_day.day_data)
        input_form = InputForm()
        return render_template('output.html', my_day=my_day, form=input_form)

    return app

