# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from . import ma
from ..app import bcrypt #Encriptado de contraseña
from .InfoAdicionalModel import InfoAdicionalSchema #Relaciones bd
from .RolModel import RolSchema

class UserModel(db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  #name = db.Column(db.String(128), nullable=False)
  telephone = db.Column(db.String(20), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=True) 
  active = db.Column(db.Boolean, default=False, nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)  
  info_adicional = db.relationship('InfoAdicionalModel', backref='users', lazy=True)
  #blogposts = db.relationship('BlogpostModel', backref='users', lazy=True)
  user_creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
  #creator = db.relationship("UserModel",  backref="users") 
  rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  rol = db.relationship("RolModel",  backref="users")
  

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    #self.name = data.get('name')
    self.telephone = data.get('telephone')
    self.email = data.get('email')
    #self.password = data.get('password')
    self.password = self.__generate_hash(data.get('password'))
    self.rol_id = data.get('rol_id')
    self.user_creator_id = data.get('user_creator_id')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      if key == 'password':
        self.password = self.__generate_hash(value)
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def __generate_hash(self, password):
    return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

  def check_hash(self, password):
    return bcrypt.check_password_hash(self.password, password)

  @staticmethod
  def get_all_users():
    return UserModel.query.all()

  @staticmethod
  def get_one_user(id):
    return UserModel.query.get(id)

  @staticmethod
  def get_user_by_email(em):
    return UserModel.query.filter_by(email=em).first()

  @staticmethod
  def get_rol_by_id(id):
    user = UserModel.query.get(id)        
    rol = user.rol_id        
    return rol

  @staticmethod
  def get_ids_medicos_hospital(id_h):
    ids = []
    registros = UserModel.query.filter_by(user_creator_id=id_h).all()
    for user in registros:
      ids.append(user.id)        
    return ids
  
  def __repr(self):
    return '<id {}>'.format(self.id)

class UserSchema(ma.Schema):
  """
  User Schema
  """
  id = fields.Int(dump_only=True)
  #name = fields.Str(required=True)
  telephone = fields.Str(required=True)
  email = fields.Email(required=True)
  password = fields.Str(required=True) 
  rol_id = fields.Int(required=True)  
  active = fields.Bool(required=True)  
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
  user_creator_id = fields.Int(required=False)
  info_adicional = fields.Nested(InfoAdicionalSchema, many=True)
  #blogposts = fields.Nested(BlogpostSchema, many=True)
  rol = fields.Nested(RolSchema, many=False)
  #creator = fields.Nested('UserSchema', many=False)
