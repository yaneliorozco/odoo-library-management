from odoo import models, fields
from odoo.exceptions import UserError


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    isbn = fields.Char(string='ISBN', required=True, unique=True)
    publication_date = fields.Date(string='Publication Date')
    description = fields.Text(string="Description")
    state = fields.Selection(
        [
            ('available', 'Disponible'),
            ('borrowed', 'Prestado'),
            ('lost', 'Perdido'),
        ],
        string='Estado',
        default='available',
        required=True,
    )


    def action_open_form(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Book',
            'res_model': 'library.book',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }
    
    def action_borrow(self):
        for record in self:
            if record.state != 'available':
                raise UserError(
                    'Solo se pueden prestar libros disponibles.'
                )
            record.state = 'borrowed'

    def action_return(self):
        for record in self:
            if record.state != 'borrowed':
                raise UserError(
                    'Solo se pueden devolver libros prestados.'
                )

            record.state = 'available'

    def action_mark_lost(self):
        for record in self:
            if record.state not in ('available', 'borrowed'):
                raise UserError(
                    'Este libro ya está marcado como perdido.'
                )

            record.state = 'lost'