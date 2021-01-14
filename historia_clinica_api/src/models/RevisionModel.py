# src/models/RevisionModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from . import ma
from .UserModel import UserModel, UserSchema

class RevisionModel(db.Model):
    """
    Revision Model
    """

    # table name
    __tablename__ = 'Revisiones'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    observaciones = db.Column(db.String(128), nullable=False)
    estado_salud = observaciones = db.Column(db.String(128), nullable=False)
    especialidad_m = observaciones = db.Column(db.String(30), nullable=False)
    fecha = db.Column(db.String(20), unique=True, nullable=True)    
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)     
    medico_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    medico = db.relationship("UserModel", foreign_keys=[medico_id] ,backref="revisiones")
    
    
    def save(self):
      db.session.add(self)
      db.session.commit()

    @staticmethod
    def get_all_registers():
      return RevisionModel.query.all()

    @staticmethod
    def get_register_by_user(u_id):
      return RevisionModel.query.filter_by(user_id=u_id).all()
    
    @staticmethod
    def get_register_by_medico(u_id):      
      print(RevisionModel.query.filter_by(medico_id=u_id).all())
      return RevisionModel.query.filter_by(medico_id=u_id).all()

    @staticmethod
    def get_one_register(id):
      return RevisionModel.query.get(id)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.observaciones = data.get('observaciones')
        self.estado_salud = data.get('estado_salud')
        self.especialidad_m = data.get('especialidad_m')
        self.fecha = data.get('fecha')
        self.user_id = data.get('user_id')
        self.medico_id = data.get('medico_id')                  
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

class RevisionSchema(ma.Schema):
  """
  Revision Schema
  """
  id = fields.Int(dump_only=True)
  #name = fields.Str(required=True)
  observaciones = fields.Str(required=True)
  estado_salud = fields.Str(required=True)
  especialidad_m = fields.Str(required=True) 
  fecha = fields.Str(required=True) 
  user_id = fields.Int(required=True)  
  medico_id = fields.Int(required=True)    
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
  medico = fields.Nested(UserSchema, many=False)
  
