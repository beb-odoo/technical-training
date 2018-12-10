from odoo import models, fields

class rentals(models.Model):
    _name = 'library.rentals'
    _description = 'rentals'

    name=fields.Char(string='Title', required = True,)
    description=fields.Text()

    book_id=fields.Many2one(comodelname='library.books', relation='book')
    customer_id=fields.Many2one(comodelname='library.partners', relation='customer')

    rental_date=fields.Date(string='Rental date')
    return_date=fields.Date(string='Return date')
