# -*- coding: utf-8 -*-
{
    'name': "nitro_gas",

    'summary': """
        Gestión de Estación de Gasolinera Nitro Gas
        http://www.nitro-gas.com""",

    'description': """
        Gestión de Estación de Gasolinera Nitro Gas
    """,

    'author': "Grupo Treming",
    'website': "http://www.treming.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
