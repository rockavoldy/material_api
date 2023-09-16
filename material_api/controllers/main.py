from werkzeug import Response
from odoo import http
from werkzeug.http import HTTP_STATUS_CODES
import json

class Main(http.Controller):

    @http.route('/material/<int:material_id>', auth='public', type='http', methods=['GET'])
    def get(self, material_id, **kw):
        """ Get specific record material """
        material = http.request.env['material.material'].browse(material_id)
        status = 200
        if not material_id:
            status = 404

        headers = {'Content-Type': 'application/json'}
        result = json.dumps({
            'message': HTTP_STATUS_CODES[status],
            'data': material.read(['name', 'material_code', 'material_type', 'material_buy_price', 'supplier_id'])[0]
        })

        res = Response(result, headers=headers)
        res.status_code = status
        return res

    @http.route('/material/', auth='public', type='http', methods=['GET'])
    def list(self, **kw):
        """ List all available materials """
        materials = http.request.env['material.material'].search([])
        headers = {'Content-Type': 'application/json'}
        result = json.dumps({
            'message': HTTP_STATUS_CODES[200],
            'data': materials.read(['name', 'material_code', 'material_type', 'material_buy_price', 'supplier_id'])
        })
        return Response(result, headers=headers)
    
    @http.route('/material/', auth='public', type='http', methods=['POST'], website=False, csrf=False)
    def create(self, **kw):
        """ Create new material """
        status = 200

        name = kw.get('name', False)
        material_code = kw.get('material_code', False)
        material_type = kw.get('material_type', False)
        material_buy_price = kw.get('material_buy_price', False)
        supplier_id = kw.get('supplier_id', False)

        if name and material_code and material_type and material_buy_price and supplier_id:
            material = http.request.env['material.material'].create({
                'name': name,
                'material_code': material_code,
                'material_type': material_type,
                'material_buy_price': material_buy_price,
                'supplier_id': supplier_id
            })
            if not material:
                status = 400
        else:
            status = 400

        headers = {'Content-Type': 'application/json'}
        result = json.dumps({
            'message': HTTP_STATUS_CODES[status],
        })

        res = Response(result, headers=headers)
        res.status_code = status
        return res

    @http.route('/material/<int:material_id>', auth='public', type='http', methods=['PUT'], website=False, csrf=False)
    def update(self, material_id, **kw):
        """ Update material """
        status = 200
        material = http.request.env['material.material'].browse(material_id)
        if material:
            name = kw.get('name', material.name)
            material_code = kw.get('material_code', material.material_code)
            material_type = kw.get('material_type', material.material_type)
            material_buy_price = kw.get('material_buy_price', material.material_buy_price)
            supplier_id = kw.get('supplier_id', material.supplier_id.id)

            material.update({
                'name': name,
                'material_code': material_code,
                'material_type': material_type,
                'material_buy_price': material_buy_price,
                'supplier_id': supplier_id
            })
        else:
            status = 404


        headers = {'Content-Type': 'application/json'}
        result = json.dumps({
            'message': HTTP_STATUS_CODES[status],
        })

        res = Response(result, headers=headers)
        res.status_code = status
        return res

    @http.route('/material/<int:material_id>', auth='public', type='http', methods=['DELETE'], website=False, csrf=False)
    def delete(self, material_id, **kw):
        """ Delete material """
        status = 200
        material = http.request.env['material.material'].browse(material_id)
        if material:
            material.unlink()
        else:
            status = 400

        headers = {'Content-Type': 'application/json'}
        result = json.dumps({
            'message': HTTP_STATUS_CODES[status],
        })

        res = Response(result, headers=headers)
        res.status_code = status
        return res
