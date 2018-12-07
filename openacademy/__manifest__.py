# -*- coding: utf-8 -*-
{
    'name': "OpenAcademy",

    'summary': """
        Manage trainings""",

    'description': """
        Manage course, classes(sessions), attendee registration, teachers, students, ...
    """,

    'author': "beb-odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
	"security/ir.model.access.csv",
        "data/openacademy_data.xml",
        "views/openacademy.xml",
	"views/partner.xml",
    ],
    # only loaded in demonstration mode
    'demo': [],
}
