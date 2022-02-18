# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo638(http.Controller):
#     @http.route('/odoo638/odoo638/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo638/odoo638/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo638.listing', {
#             'root': '/odoo638/odoo638',
#             'objects': http.request.env['odoo638.odoo638'].search([]),
#         })

#     @http.route('/odoo638/odoo638/objects/<model("odoo638.odoo638"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo638.object', {
#             'object': obj
#         })
