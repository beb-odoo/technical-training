from odoo import models, fields

class publisher(models.Model):
    _name='libreary.publisher'
    _description='books publishers'

    name=fields.Char(string='Name', required=True)

    
