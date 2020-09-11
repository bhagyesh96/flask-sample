from app import db
from sqlalchemy.dialects.postgresql import JSON

class Result(db.Model):
    __tablename__ = 'result'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    count_data = db.Column(JSON)
    
    def __init__(self, url, count_data):
        self.url = url
        self.count_data = count_data
        

    
