from odoo import models, fields

class books(models.Model):
    _name = 'library.book'
    _description = 'book'

    name=fields.Char(string='Title', required = True,)
    description=fields.Text()

    author=fields.Many2many(comodelname='library.partners', string='Author(s)')
    publisher=fields.Many2one(comodelname='library.publisher', string='Publisher')
    
    editiondate=fields.Date(string='Edition date')
    isbn=fields.Char(string='ISBN')

    rentals=fields.One2many(comodelname='library.rentals', relation='book_id', string='Rentals')
