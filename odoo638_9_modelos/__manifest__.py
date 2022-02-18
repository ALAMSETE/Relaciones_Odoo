# -*- coding: utf-8 -*-
{
    'name': "odoo638_9_modelos",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views_conductores.xml',
        'views/views_jefes.xml',
        'views/views.xml',
        'views/templates.xml',
        'security/odoo638_9_modelos_security.xml',
        'security/ir.model.access.csv',
        'report/odoo638_9_modelos_camiones638_report.xml',
        'report/odoo638_9_modelos_jefes638_report.xml',
        'report/odoo638_9_modelos_conductores638_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
