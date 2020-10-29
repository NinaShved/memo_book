from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    today = StringField('День дд.мм.гг', validators=[DataRequired()], render_kw={"class": "form-control"})
    news = StringField('Дела на день', validators=[DataRequired()], render_kw={"class": "form-control"})
    deb = StringField('Сумма прихода', validators=[DataRequired()], render_kw={"class": "form-control"})
    deb_text = StringField('Детализация прихода', validators=[DataRequired()], render_kw={"class": "form-control"})
    cred = StringField('Сумма расхода', validators=[DataRequired()], render_kw={"class": "form-control"})
    cred_text = StringField('Детализация расхода', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-primary"})

#class InputForm(FlaskForm):
#    today = StringField('День', validators=[DataRequired()], render_kw={"class": "form-control"})
#    news = StringField('Дела на день', validators=[DataRequired()], render_kw={"class": "form-control"})
#    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-primary"})    