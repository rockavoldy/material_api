# -*- coding: utf-8 -*-
{
    'name': "Material API",
    'summary': """
        Add a way to list materials, and fill them via REST API""",
    'description': """
        v1.0.0:
            * Create new menu Materials, with tree and  form view
            * Create REST API endpoint to interact with materials
    """,
    'author': "Akhmad Maulana Akbar",
    'website': "https://akhmad.id",
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
    ],
    'application': True,
    'installable': True,
}
