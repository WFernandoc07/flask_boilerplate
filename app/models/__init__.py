from app import db
from sqlalchemy_mixins import AllFeaturesMixin


#Crear una clase abstracta
class BaseModel(db.Model, AllFeaturesMixin):
    __abstract__ = True