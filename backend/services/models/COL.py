from services.config import db

class CostItem(db.Model):
    __tablename__ = 'cost_items'
    id = db.Column(db.Integer, primary_key=True)
    cityState_id = db.Column(db.Integer, nullable=False)
    item = db.Column(db.String(128), nullable=False)
    cost = db.Column(db.String(128), nullable=False)  # Using string to accommodate '?' entries, but consider converting to numeric values where possible
    low_range = db.Column(db.String(128), nullable=True)  # Could be NULL for items without a range
    high_range = db.Column(db.String(128), nullable=True)  # Could be NULL for items without a range