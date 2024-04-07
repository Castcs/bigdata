from services.config import db

class SalaryData(db.Model):
    __tablename__ = 'salary_data'
    id = db.Column(db.Integer, primary_key=True)
    cityStateID = db.Column(db.Integer, db.ForeignKey('city_state.id'), nullable=False)
    rateType = db.Column(db.String)
    pct10 = db.Column(db.String)
    pct25 = db.Column(db.String)
    median = db.Column(db.String)
    pct75 = db.Column(db.String)
    pct90 = db.Column(db.String)
    stFips = db.Column(db.String)
    area = db.Column(db.String)