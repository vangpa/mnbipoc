from app import db

class MNBIPOC(db.Model):
    """"""
    __tablename__ = "mnbipoc"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    gender = db.Column(db.String)
    clinic = db.Column(db.String)
    website = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.Integer)
    race = db.Column(db.String)
    language = db.Column(db.String)
    services = db.Column(db.String)


