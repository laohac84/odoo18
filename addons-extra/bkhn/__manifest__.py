# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'BKHN',
    'version': '1.3',
    'summary': 'Invoices, Payments, Follow-ups & Bank Synchronization',
    'description': "BKHN",
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',

        'views/test_model.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
    },
    'license': 'LGPL-3',
}
