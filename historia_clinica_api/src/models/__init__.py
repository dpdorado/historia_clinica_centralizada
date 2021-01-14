#src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

# initialize our db
db = SQLAlchemy()

ma = Marshmallow()
#Encriptado de contraseña de usuario
bcrypt = Bcrypt()

__all__ = ['RolModel','UserModel', 'InfoAdicionalModel', 'RevisionModel']