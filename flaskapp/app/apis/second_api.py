from flask import Blueprint
from flask_restplus import Namespace, Resource, fields, Api, apidoc

second_blueprint = Blueprint('api2', __name__, url_prefix='/api2')
api = Api(second_blueprint, title='WeaponizedTemplate',
    version='1.0',
    description='For some data science project',
    doc='/doc/')

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'felix', 'name': 'Felix'},
]

@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS

