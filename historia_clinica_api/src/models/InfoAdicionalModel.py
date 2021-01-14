# src/models/InfoAdicionalModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from . import ma

class InfoAdicionalModel(db.Model):
    """
    InfoAdicional Model
    """

    # table name
    __tablename__ = 'InfoAdicionales'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    direction = db.Column(db.String(20), nullable=False)
    fecha_nacimiento = db.Column(db.String(20), unique=True, nullable=True)
    services = db.Column(db.String(128), unique=True, nullable=True)#Debe ser una lista, y en el mejor de los casos debe ser otro modelo.  
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)    


    # class constructor
    def __init__(self, data, rol):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.direction = data.get('direction')
        self.user_id = data.get('user_id')          
        if (rol == 1 or rol==3):
            self.fecha_nacimiento = data.get('fecha_nacimiento')
            self.services = 'None ---'
        elif (rol == 2):
            self.services = data.get('services')              
            self.fecha_nacimiento = 'None ---'
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_info(u_id):
        return InfoAdicionalModel.query.filter_by(user_id=u_id).first()

class InfoAdicionalSchema(ma.Schema):
    """
    InfoAdicional Schema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    direction = fields.Str(required=True)
    fecha_nacimiento = fields.Str(required=False)
    services = fields.Str(required=False)    
    user_id = fields.Int(required=True)     
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)        
