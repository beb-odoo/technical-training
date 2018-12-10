from odoo import models, fields

class Partner(models.Model):
    _name='library.partners'
    _description='library partners'

    name=fields.Char(string="Name")
    address=fields.Char(string="Address")
    email=fields.Char(String="Email")

    type=fields.Selection([('customer','customer'), ('author','author')], default="customer")
    rentals_id=fields.One2many(comodel_name='library.rentals', inverse_name='customer_id', string='Rentals')
