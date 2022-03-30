# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class alvinresto(models.Model):
#     _name = 'alvinresto.alvinresto'
#     _description = 'alvinresto.alvinresto'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
