#/src/views/InfoAdicionalView

from flask import request, json, Response, Blueprint,g 
from ..models.UserModel import UserModel, UserSchema
from ..models.InfoAdicionalModel import InfoAdicionalModel, InfoAdicionalSchema
from ..shared.Authentication import Auth

info_api = Blueprint('info', __name__)
info_schema = InfoAdicionalSchema()

@info_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Info Function
  """

  req_data = request.get_json()    

  data = info_schema.load(req_data)
  rol = UserModel.get_rol_by_id(data.get('user_id'))
  
  info = InfoAdicionalModel(data,rol)  
  info.save()      
  return custom_response({'SUCCESS': 'La descripción fue actualizada correctamente'}, 201)  
  
@info_api.route('/<int:user_id>', methods=['GET'])
@Auth.auth_required
def get_info_user(user_id):
  """
  Get a single user
  """
  info = InfoAdicionalModel.get_info(user_id)
  if not info:
    return custom_response({'error': 'Information not found'}, 404)
  
  info_user = info_schema.dump(info)
  return custom_response(info_user, 200)

@info_api.route('/me', methods=['PUT'])
@Auth.auth_required
def update():
  """
  Update me
  """
  req_data = request.get_json()
  
  data = info_schema.load(req_data, partial=True)
  
  info = InfoAdicionalModel.get_info(data.get('user_id'))
  info.update(data)
  info_user = info_schema.dump(info)
  return custom_response(info_user, 200)


@info_api.route('/me', methods=['GET'])
@Auth.auth_required
def get_me():
  """
  Get me
  """
  info = InfoAdicionalModel.get_info(data.get('user_id'))
  info_user = info_schema.dump(info)
  return custom_response(info_user, 200)

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )