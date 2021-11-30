# -*-coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "library",
    'version': '1.1',
    'category': '',
    'sequence': 45,
    'summary': 'Record Books Details',
    'auto_install': False,
    'application': True,
    'description': 'Putting the Books Details',
    'installable': True,

# any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
