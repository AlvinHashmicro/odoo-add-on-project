from odoo import api, fields, models


class Makanan(models.Model):
    _name = 'warung.makanan'
    _description = 'Menu makanan'

    name = fields.Char(string='Nama Makanan')
    deskripsi = fields.Char(string='Deskripsi Makanan')
    harga = fields.Integer(string='Harga Makanan')