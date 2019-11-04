from flask import Blueprint, render_template, request
from flask_restplus import Api
from flask_restplus import Resource
from flask_restplus import Namespace
from .models import CardModel
from .encrypt import encrypt_card_data
from .decrypt import decrypt_card_data


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint,
    title='Cryptography API Service',
    default ='Cryptography',
    version='1.0',
    description='Cryptography Services',
    default_label='Cryptography Services'
    # All API metadatas
)

card_schema = CardModel.schema
api.add_namespace(card_schema)


@api.route("/encrypt-card")
class EncryptView(Resource):
    
    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    @card_schema.expect(CardModel.model, validate=True)
    def post(self):
        data = request.json
        holder = data.get('holder')
        number = data.get('number')
        cvv = data.get('cvv')
        encrypted_data = encrypt_card_data(holder, number, cvv)
        normalized_response = {k: v.decode('utf-8') for k, v in  encrypted_data.items()}
        return normalized_response, 201


@api.route("/decrypt-card")
class DencryptView(Resource):
    
    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    @card_schema.expect(CardModel.model, validate=True)
    def post(self):
        data = request.json
        holder = data.get('holder')
        number = data.get('number')
        cvv = data.get('cvv')
        decrypted_data = decrypt_card_data(holder, number, cvv)
        return decrypted_data, 201


# @api.route('/generate-pubkey')
# class PubKeyView(Resource):

#     def get(self):
#         return {}
