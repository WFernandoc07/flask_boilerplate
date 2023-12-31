from app import db
from app.models.roles_model import RoleModel
from app.schemas.roles_schema import RoleResponseSchema
from http import HTTPStatus

class RoleController:
    def __init__(self):
        self.db = db
        self.model = RoleModel
        self.schema = RoleResponseSchema
    
    def fetch_all(self):
        #SELECT * FROM roles;
        records = self.model.where(status=True).all()
        response = self.schema(many=True)
        return response.dump(records)
    def save(self, body):
        try:
            new_record = self.model.create(**body)
            self.db.session.add(new_record)
            self.db.session.commit()
            self.db.session.close()
            #self.model(name=body['name])
            return {
                'message':f'El rol {body["name"]} se creó con éxito'
            }, HTTPStatus.CREATED
        except Exception as e:
            self.db.session.rollback()
            return {
                'message':'Ocurrió un error',
                'error':str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()
    
    def find_by_id(self, id):
        try:
            #SELECT * FROM roles WHERE id=id
            record = self.model.where(id=id, status=True).first()
            if record:
                response = self.schema(many=False)
                return response.dump(record), HTTPStatus.OK
            return {
                'message':f'No se encontró el rol con el ID: {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                'message':'Ocurrió un error',
                'error':str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
    
    def update(self, id, body):
        try:
            #UPDATE roles SET name=' ' WHERE id=?
            record = self.model.where(id=id, status=True).first()

            if record:
                record.update(**body)
                self.db.session.add(record)
                self.db.session.commit()
                return {
                    'message': f'El rol con el ID: {id} ha sido actualizado'
                }, HTTPStatus.OK
            return {
                'message': f'No se encontró un rol con el ID: {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message':'Ocurrió un error',
                'error':str(e)
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
                    'message': f'El rol con el ID: {id} ha sido deshabilitado'
                }, HTTPStatus.OK
            return {
                'message': f'No se encontró un rol con el ID: {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message':'Ocurrió un error',
                'error':str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()
        


