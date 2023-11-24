from app import db
from app.models.users_model import UserModel
from app.schemas.users_schema import UserResponseSchema
from http import HTTPStatus


class UserController:
    def __init__(self):
        self.db = db
        self.model = UserModel
        self.schema = UserResponseSchema

    def fetch_all(self, query_params):
        # Paginación
        # Página (a obtener)
        # N° registros x página
        ### Total 100 usuarios
        ## Página 1
        # SELECT * FROM users LIMIT 10 OFFSET(n° página - 1) * n° registros
        ## Página 2
        # SELECT * FROM users LIMIT 10 OFSET 10
        try:
            page = query_params['page']
            per_page = query_params['per_page']

            records = self.model.where(status=True).order_by('id').paginate(
                page=page,
                per_page=per_page
            )

            response = self.schema(many=True)

            return {
                'results': response.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }
        except Exception as e:
            return {
                'message': 'Ocurrió un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def save(self, body):
        try:
            new_record = self.model.create(**body)
            new_record.hash_password()
            self.db.session.add(new_record)
            self.db.session.commit()

            return {
                'message': f'El usuario {body["username"]} se creó con éxito'
            }, HTTPStatus.CREATED
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrió un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()

    def find_by_id(self, id):
        try:
            record = self.model.where(id=id, status=True).first()

            if record:
                response = self.schema(many=False)
                return response.dump(record), HTTPStatus.OK
            return {
                'message': f'No se encontró im isuario con el ID: {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                'message': 'Ocurrió un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR


    def update(self, id, body):
        try:
            record = self.model.where(id=id, status=True).first()

            if record:
                record.update(**body)
                self.db.session.add(record)
                self.db.session.commit()
                return {
                    'message': f'El usuario con el ID: {id} ha sido actualziado'
                }
            return {
                'message': f'No se encontró im isuario con el ID: {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrió un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()

    def remove(self, id):
        try:
            record = self.model.where(id=id).first()

            if record:
                record.update(status=False)
                self.db.session.add(record)
                self.db.session.commit()
                return {
                    'message': f'El usuario con el ID: {id} ha sido deshabilitado'
                }, HTTPStatus.OK
            return {
                'message': f'No se encontró un usuario con el ID: {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message':'Ocurrió un error',
                'error':str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()
    
    def profile_me(self, identity):
        try:
            record = self.model.where(id=identity).first()
            response = self.schema(many=False)
            return response.dump(record), HTTPStatus.OK
        except Exception as e:
            return {
                'message':'Ocurrió un error',
                'error':str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR


