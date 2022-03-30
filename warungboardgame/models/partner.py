from odoo import api, fields, models


class Partner(models.Model):
    _name = 'warung.partner'
    _description = 'Standard class partners'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='Telepon/HP')