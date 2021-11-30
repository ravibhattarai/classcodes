# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Books Management',
    'version': '1.1',
    'category': '',
    'sequence': 45,
    'summary': 'Record Books Details',
    'auto_install': False,
    'application': True,
    'description': 'Putting the Books Details',
    'installable': True,
    'depends':[
        "web",
        "base",
    ],
'data': [
    'views/books.xml',
    'views/books_menu.xml',
    'security/ir.model.access.csv'
],
}
