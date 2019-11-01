from flask import Blueprint, render_template
from flask_restplus import Api
from flask_restplus import Resource
from flask_restplus import Namespace



blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint,
    title='Cryptography API Service',
    default ='Cryptography',
    version='1.0',
    description='Cryptography Services',
    default_label='Cryptography Services'
    # All API metadatas
)


@api.route('/encrypt-data')
class EncryptView(Resource):
    
    def post(self):
        return {'hello': 'world'}, 201


@api.route('/generate-pubkeys')
class CertificateView(Resource):

    def get(self):
        return {}