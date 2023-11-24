from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from http import HTTPStatus
from app.controllers.roles_controller import RoleController
from app.schemas.roles_schema import RoleRequestSchema

role_ns = api.namespace(
   name='Roles',
   description='Rutas del módulo roles',
   path='/roles'
)

schema_request = RoleRequestSchema(role_ns)


#CRUD
@role_ns.route('')
@role_ns.doc(security='Bearer')
class Roles(Resource):
  #dispatch: pasar nuestros verbos a funciones
  
  def get(self):
    ''' Listar todos los roles '''
    controller = RoleController()
    return controller.fetch_all()
  
  @role_ns.expect(schema_request.create(), validate=True)
  def post(self):
    ''' Creación de un ROL '''
    controller = RoleController()
    return controller.save(request.json)

@role_ns.route('/<int:id>')
class RoleById(Resource):
  #dispatch: pasar nuestros verbos a funciones
  @jwt_required()
  def get(self, id):
    ''' Obtener un Rol por su ID'''
    controller = RoleController()
    return controller.find_by_id(id)

  @role_ns.expect(schema_request.update(), validate=True)
  def patch(self, id):
    ''' Actualizar un rol por su Id, enviando el objeto parcial'''
    controller = RoleController()
    return controller.update(id, request.json)

  def delete(self, id):
    ''' Inhabilitar un rol por su Id '''
    controller = RoleController()
    return controller.remove(id)

# #Listar (GET)


# @app.route('/roles', methods=['GET'])
# def list_roles():
#     return 'Listado de roles'


# #Creación
# @app.route('/roles', methods=['POST'])
# def create_roles():
#     return 'Creación de rol', HTTPStatus.CREATED

# # Actualización
# # <id> : identificador del role dinámicamente, pathparent.
# @app.route('/role/<int:id>', methods=['PUT', 'PATCH'])
# def update_roles(id):
#   return f'Actualizar {str(id)}'

# # Eliminar
# @app.route('/role/<int:id>', methods=['DELETE'])
# def delete_roles(id):
#   return f'Eliminar {str(id)}'


# La publicación con el id X que se encuentra en la categoría Y
# /post/int:category_id>/<int:post_id>

