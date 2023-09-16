from odoo import models, fields, api
from odoo.exceptions import ValidationError

MATERIAL_TYPE = [
    ('fabric', 'Fabric'),
    ('jeans', 'Jeans'),
    ('cotton', 'Cotton')
]

class Material(models.Model):
    """ New model material """
    _name = 'material.material'

    name = fields.Char('Material Name', required=True)
    material_code = fields.Char('Material Code', required=True)
    material_type = fields.Selection(MATERIAL_TYPE, string='Material Type', default='fabric', required=True)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.IDR'))
    material_buy_price = fields.Monetary(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier', required=True)

    @api.constrains('material_buy_price')
    def _validate_material_buy_price(self):
        """ Validate material buy price should be above 100 """
        for mat in self:
            if mat.material_buy_price < 100:
                raise ValidationError("Material Buy Price can't be below 100.")
