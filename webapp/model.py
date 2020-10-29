from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Everyday(db.Model):
    __tablename__ = "everyday"
    id = db.Column(db.Integer, primary_key=True)
    day_data = db.Column(db.Date, nullable=False)
    day_news = db.Column(db.Text, nullable=False)
    yesterday_balance = db.Column(db.Numeric, nullable=True)
    day_balance = db.Column(db.Numeric, nullable=True)
    day_rate = db.Column(db.Numeric, nullable=True)
    day_wirings = db.relationship("Wiring", lazy=True)

    def __repr__(self):
        return '<Everyday {} {} {}>'.format(self.id, self.yesterday_balance, self.day_balance)

class Wiring(db.Model):
    __tablename__ = "wiring"
    id = db.Column(db.Integer, primary_key=True)
    wir_amount = db.Column(db.Numeric, nullable=False)
    wir_text = db.Column(db.Text, nullable=False)
    wir_dc = db.Column(db.Integer, nullable=False)    
    everyday_id = db.Column(db.Integer, db.ForeignKey('everyday.id'), nullable=False)

        