from odoo import api, fields, models


class Boardgame(models.Model):
    _name = 'warung.boardgame'
    _description = 'Boardgame-boardgame yang dijual/disewakan. Bisa dimainkan di tempat.'

    name = fields.Char(string='Nama Permainan')
    type = fields.Selection(string='Jenis Permainan', selection=[('board game', 'Board Game'), ('card game', 'Card Game')])  
    price = fields.Integer(string='Harga Permainan')
    rent = fields.Integer(string='Harga Sewa Permainan')