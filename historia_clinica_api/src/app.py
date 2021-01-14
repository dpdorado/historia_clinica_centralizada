#src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt
# import user_api blueprint
from .views.UserView import user_api as user_blueprint
from .views.InfoAdicionalView import info_api as info_blueprint
from .views.UserHospitalView import userh_api as usersh_blueprint
from .views.RevisionView import re_api as re_blueprint
from .views.RegistrosView import regis_api as regis_blueprint

def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  bcrypt.init_app(app)

  db.init_app(app)

  app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
  app.register_blueprint(info_blueprint, url_prefix='/api/v1/users/info')
  app.register_blueprint(usersh_blueprint, url_prefix='/api/v1/users/usersh')
  app.register_blueprint(re_blueprint, url_prefix='/api/v1/users/re')  
  app.register_blueprint(regis_blueprint, url_prefix='/api/v1/users/regis')  

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your first endpoint is workin'

  return app