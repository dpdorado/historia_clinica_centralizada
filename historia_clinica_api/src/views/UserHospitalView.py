#/src/views/UserView

from flask import request, json, Response, Blueprint,g 
from ..models.UserModel import UserModel, UserSchema
from ..shared.Authentication import Auth
from ..utils.SMTP import SMTP

userh_api = Blueprint('usersh', __name__)
user_schema = UserSchema()

'''
* Ruta que permite a un usuario Hospital registrar un médico
'''
@userh_api.route('/<int:user_id>', methods=['POST'])
@Auth.auth_required
def create(user_id):
  """
  Create User Function
  """
  req_data = request.get_json()    
  data = user_schema.load(req_data,partial=("active",))

  if (not is_creator_rol(user_id) and data.get('rol_id')==1 or data.get('rol_id')==2):
    message = {'error': 'NOT FOUND'}
    return custom_response(message, 400)    

  # check if user already exist in the db
  user_in_db = UserModel.get_user_by_email(data.get('email'))
  
  if user_in_db:
    message = {'error': 'User already exist, please supply another email address'}
    return custom_response(message, 400)
  
  user = UserModel(data)
  user.save()
  user.update({'user_creator_id' : user_id}) #Agregar el id del hospital
  
  ser_data = user_schema.dump(user)  
  
  return custom_response({'SUCCESS': 'Registro de médico exitoso.', 'user_id': ser_data.get('id')}, 201)  
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

def is_creator_rol(user_id):
    rol_creador = UserModel.get_rol_by_id(user_id)
    if ( rol_creador == 1 or rol_creador == 3):
        return False
    return True