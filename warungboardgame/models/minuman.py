from odoo import api, fields, models


class Makanan(models.Model):
    _name = 'warung.minuman'
    _description = 'Menu minuman'

    name = fields.Char(string='Nama Minuman')
    deskripsi = fields.Char(string='Deskripsi Minuman')
    harga = fields.Integer(string='Harga Minuman')