# -*- coding: utf-8 -*-
# from odoo import http


# class Alvinresto(http.Controller):
#     @http.route('/alvinresto/alvinresto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alvinresto/alvinresto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alvinresto.listing', {
#             'root': '/alvinresto/alvinresto',
#             'objects': http.request.env['alvinresto.alvinresto'].search([]),
#         })

#     @http.route('/alvinresto/alvinresto/objects/<model("alvinresto.alvinresto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alvinresto.object', {
#             'object': obj
#         })
