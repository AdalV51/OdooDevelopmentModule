from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    genre_field = fields.Selection(
        string="Genre",
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')], default="other"
    )

    # def change_genre(self):
    #     if self.genre_field == 'male':
    #         self.env.cr.execute("UPDATE res_partner SET genre_field='female'") # Insert female in the DB
    #     else:
    #         self.env.cr.execute("UPDATE res_partner SET genre_field='female'") # Insert male in the DB