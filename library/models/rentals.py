from odoo import models, fields

class rentals(models.Model):
    _name = 'library.rentals'
    _description = 'rentals'

    name=fields.Char(string='Title', required = True,)
    description=fields.Text()

    book_id=fields.Many2one(comodel_name='library.books', string='book')
    customer_id=fields.Many2one(comodel_name='library.partners', string='customer')

    rental_date=fields.Date(string='Rental date')
    return_date=fields.Date(string='Return date')
