from services.config import db


class CityState(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)


    def __repr__(self):
        return 'f<CityState - ID: {self.id} - City: {self.city} - State: {self.state}'