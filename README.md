# BOLIERPLATE FLASK

---


## Modelos:

- Usuarios


  | Campo       | tipo         | constraint              |
  | ------------| -------------| --------------          |
  | id          | SERIAL       | PRIMARY KEY             |
  | name        | VARCHAR(120) | NOT NULL                |
  | last_name   | VARCHAR(150) | UNIQUE                  |
  | username    | VARCHAR(80)  | NOT NULL                |
  | password    | VARCHAR(255) | NOT NULL                |
  | email       | VARCHAR(160) | UNIQUE                  |
  | rol_id      | INT          | FOREING KEY NOT NULL    |
  | status      | BOOLEAN      |                         |


- Roles

    | Campo       | tipo       | constraint    |
  | ------------| -------------| --------------|
  | id          | SERIAL       | PRIMARY KEY   |
  | name        | CHAR(8)      | NOT NULL      |
  | status      | BOOLEAN      | -             |


## Características

1. Login
  - [X] Creación del token de acceso (JWT | 
  acces_token - refresh - token).
  - [X] Validación de contraseñas encriptadas (bcypt)
2. Registro
  - [X] Encriptación de contraseñas (bcrypt)
3. Recuperar contraseña
  - [X] Generar una nueva contraseña encriptada.
  - [] Enviar un correo con un template (html).
4. CRUD por cada Modelo.
  - [X] Listado por paginación
  - [X] Obtener un registro mediante el id.
  - [X] Creación de un registro
  - [X] Actualización de un registro
  - [X] Eliminar un registro (SoftDelete)
5. Decoradores.
  - [X] Proteger mediante autenticación.
  - [] Proteger las rutas por rol
6. Documentación y validaciones.
  - [X] Swagger OpenAPI
  - [X] Schemas
7. Despliegue
  - [] Render

## Enviroments


## Documentación


## Comandos
- Guardar los cambios en el archivo requirements.txt, el archivo contiene las dependencias instaladas.
```bash
pip freeze > requirements.txt
```
- Intalamos el Flask Migrate, que nos ayudará hacer las migraciones hacia la base de datos.
```bash
pip install Flask-Migrate
```

### Migraciones
- Iniciar el paquete alembic (Una sola vez siempre y cuando no exista la carpeta **migrations**)
```bash
flask db init
```

- Migrar la base de datos
```bash
flask db migrate -m "comentario"
```
- Sincronizar las migraciones
```bash
flask db upgrade
```
- Marshmallow
```bash
pip install marshmallow-sqlalchemy
```
### Encriptar una contraseña
```bash
pip install bcrypt
```
### Instalar Json Web Token (JWT)
```bash
pip install flask-jwt-extended
```
### Instalar Flask-Mail
```bash
pip install Flask-Mail
```
## Notas
* Desacoplar cada instancia por clase.
* Controlador: intermediario entre modelo y
* Estado de creación exitosa se devuelve 201.
* PUT vs PATCH: Con PUT se modifica todo el cuerpo completo, con el PATCH se modifica solo los elementos asignados del cuerpo.
* Flask-RestX: extensión que nos va a dar soporte para documentar nuestras apis. Seguir buenas prácticas de las Apis. Utilizar decoradores para validaciones.
* Validadores (Schemas):

*  #metodo expect: que formato de datos espera recibir nuesta en API en las
  #solicitudes que ingresa.

* [Enlace de página](http://127.0.0.1:5000/swagger-ui)
* UTF-8 Codificación estándar unicode, está adaptada a diferentes idiomas en el mundo.
* Encriptar en 10 rondas, un salto una secuencia de caractarese que se combinan.
* No se debe retornar la contraseña en el método GET.
---
* **PAGINACIÓN**
    - Técnicas que se utilizamos para optimizar para devolver la información desde nuestro backend. Cantidad de peso que debe tener una respuesta no debe superar los megas (8*).
    - Si se supera la cantidad de megas se tendrá un problema de comunicación.
    - Limitar las consultas que queremos traer.
    ---
* **AUTENTICACIÓN**
  * [Documentación Flask blueprint](https://flask.palletsprojects.com/en/3.0.x/blueprints/)
  * [HTTP Code Status Documentación](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
  * ¿Qué permite el JSON web token?
  * ¿Cómo esta compuesto un JWT? [JWT.io](https://jwt.io/)
    - Encabezado: tipo de token y tipo de algoritmo que se está utilizando.
    - Payload: datos clein, fecha y hora, agrupación del token, asunto del token. /***Refresh token***/: un token generado para no cerrar seión si está activa.
    - Firma: Identificar los token que acceden al sistema
  * ¿Qué debe tener un proyecto para ser RestApi? --Debe haber un cliente y un servidor.
  * [Flask-JWT-Extended’s Documentation](https://flask-jwt-extended.readthedocs.io/en/stable/)
  * [AWS COGNITO](https://aws.amazon.com/es/cognito/)
  * [Auth 0](https://auth0.com/resources/whitepapers/Guia-del-Comprador-de-CIAM?utm_content=latamesperubrandauth0-pure%20brand-esciambuyersguide&utm_source=google&utm_campaign=latam_mult_per_all_ciam-all_dg-ao_auth0_search_google_text_kw_utm2&utm_medium=cpc&utm_id=aNK4z0000004IgbGAE&utm_term=auth0-c&gad_source=1&gclid=Cj0KCQjwy4KqBhD0ARIsAEbCt6hrIeMxrdTbTwYc5xr0yTdz1Tui4W-4igw7zCaysNwnwRDPFZX143EaAr1yEALw_wcB)
  * Balanceador web server, servidor web.
  * PASS
  * Full ia
  * [Terraform](https://www.terraform.io/)
  * from secrets import token_hex, va a generar un string random unico en base hexadecimal

  * **Envío de correos**
    - Porcentaje de reputación del dominio
    - [Flask-Mail Documentation](https://pythonhosted.org/Flask-Mail/)
    - MAIL_DEBUG = True, para ver la trazabilidad que se realiza desde nuestro GMAIL hasta que llegue el correo al usuario.

    - [MJML](https://mjml.io/)
