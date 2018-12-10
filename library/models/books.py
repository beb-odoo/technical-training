from odoo import models, fields

class books(models.Model):
    _name = 'library.books'
    _description = 'books'

    name=fields.Char(string='Title', required = True,)
    description=fields.Text()

    author=fields.Many2many(comodel_name='library.partners', string='Author(s)')
    publisher=fields.Many2one(comodel_name='library.publisher', string='Publisher')
    
    editiondate=fields.Date(string='Edition date')
    isbn=fields.Char(string='ISBN')

    rentals=fields.One2many(comodel_name='library.rentals', relation='book_id', string='Rentals')
