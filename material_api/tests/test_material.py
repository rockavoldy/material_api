from odoo.tests import common, tagged
from odoo.exceptions import ValidationError

@tagged('material_api')
class TestMaterial(common.TransactionCase):
    def test_01_create_material_with_correct_price(self):
        material = self.env['material.material'].create({
            'name': 'Test 01',
            'material_code': 'abcde',
            'material_type': 'jeans',
            'material_buy_price': 2000,
            'supplier_id': 1
        })

        self.assertEqual(material.name, "Test 01")
        self.assertGreater(material.material_buy_price, 100)

    def test_02_create_material_with_incorrect_price(self):
        with self.assertRaises(ValidationError):
            self.env['material.material'].create({
                'name': 'Test 02',
                'material_code': 'abcdef',
                'material_type': 'cotton',
                'material_buy_price': 50,
                'supplier_id': 1
            })

        # self.assertEqual(material.name, "Test 02")
        # self.assertGreater(material.material_buy_price, 100)

    def test_03_create_material_with_wrong_material_type(self):
        # material = False
        with self.assertRaises(ValueError):
            self.env['material.material'].create({
                'name': 'Test 03',
                'material_code': 'ab',
                'material_type': 'rubber',
                'material_buy_price': 5000,
                'supplier_id': 1
            })

        # self.assertEqual(material.name, "Test 03")
        # self.assertGreater(material.material_buy_price, 100)