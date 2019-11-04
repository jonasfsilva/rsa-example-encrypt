from flask_restplus import Namespace, fields


class CardModel:
    """ CardModel is only to validate request data """

    schema = Namespace('', description='Encrypt/Decrypt EndPoints', validate=True)
    model = schema.model('Card', {
        "number": fields.String(required=True, description=(u'Card Number')),
        "cvv": fields.String(required=True, description=(u'CVV')),
        "holder": fields.String(required=True, description=(u'Holder Name')),
    })