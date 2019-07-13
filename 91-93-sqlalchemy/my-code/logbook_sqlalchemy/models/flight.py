import datetime
import sqlalchemy

# noinspection PyUnresolvedReferences
from models.model_base import ModelBase

class Flight(ModelBase):
    __tablename__ = 'flights'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created = sqlalchemy.Column(sqlalchemy.Datetime, default=datetime.datetime.now)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    aircraft_id = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    type_id = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    hours_id = sqlalchemy.Column(sqlalchemy.Float, nullable=False)