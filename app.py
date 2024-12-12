from flask import Flask
from flask_restx import Api, Resource, fields

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar Swagger usando Flask-RESTX
api = Api(app, version="1.0", title="Simple API with Swagger",
          description="A simple API example documented with Swagger")

# Definir un espacio de nombres (namespace)
ns = api.namespace('operations', description="Basic Math Operations")

# Modelo de entrada para Swagger
number_model = api.model('Numbers', {
    'num1': fields.Float(required=True, description="First number"),
    'num2': fields.Float(required=True, description="Second number")
})

# Endpoint para sumar dos números
@ns.route('/add')
class AddNumbers(Resource):
    @ns.expect(number_model)
    @ns.response(200, "Success", fields.Raw)
    def post(self):
        """
        Add two numbers.
        Returns the sum of num1 and num2.
        """
        data = api.payload
        num1 = data['num1']
        num2 = data['num2']
        return {"result": num1 + num2}, 200

# Registrar el namespace en la API
api.add_namespace(ns)

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
