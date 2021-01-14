# src/models/RolModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from . import ma
#from .UserModel import UserSchema


class RolModel(db.Model):
  """
  Rol Model
  """

  # table name
  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)  
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)  
  #user = db.relationship("UserModel", uselist=False, back_populates="roles")
  

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.name = data.get('name')           
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

class RolSchema(ma.Schema):
  """
  Rol Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)  
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
  #rol = fields.Nested(UserSchema, many=False)  