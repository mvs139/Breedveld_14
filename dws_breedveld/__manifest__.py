# -*- coding: utf-8 -*-
#
# COPYRIGHT
#    Copyright (C) 2020 Dutchworld Solutions

# noinspection PyStatementEffect
{
    'name': 'DWS Gascontrol',
    'summary': '''
        This module modifies Odoo to the needs of Gascontrol.''',
    'version': '1.0.0',
    'author': 'Dutchworld Solutions',
    'license': '',
    'depends': [
        # 'base',
        # 'sale',
        # 'product',        
        'base',
        'sale',
        'sale_crm',
        'account',
        'product',
        'purchase'
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
}
