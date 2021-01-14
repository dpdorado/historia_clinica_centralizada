#/src/views/RegistrosView

from flask import request, json, Response, Blueprint,g 
from ..models.UserModel import UserModel, UserSchema
from ..models.RevisionModel import RevisionModel, RevisionSchema
from ..shared.Authentication import Auth

regis_api = Blueprint('regis', __name__)
re_schema = RevisionSchema()
user_schema = UserSchema()

@regis_api.route('/<int:user_id>', methods=['GET'])
@Auth.auth_required
def create(user_id):
  """
  Create Registro Function
  """
  registro = None
  rol=''
  rol_id = UserModel.get_rol_by_id(user_id)
  regs = None

  # Paciente 1, Hospital 2, Médico 3
  if rol_id == 1:
      rol='Registros paciente'
      registro = get_register_paciente(user_id)
      regs = re_schema.dump(registro, many=True)
  elif rol_id ==2:
      rol='Registros hospital'
      registro = get_register_hospital(user_id)
      regs = re_schema.dump(registro, many=True)
  elif rol_id ==3:
      rol='Registros medico'
      registro = get_register_medico(user_id)
      regs = re_schema.dump(registro, many=True)

  
  return custom_response({rol : regs}, 200)  
  
def get_register_paciente(user_id):
    #Todo: hospital, medico y revisiones
    return RevisionModel.get_register_by_user(user_id)

def get_register_hospital(user_id):
    return RevisionModel.get_register_by_medico(user_id)

def get_register_medico(user_id):
    return RevisionModel.get_register_by_medico(user_id)

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )