# -*- coding: utf-8 -*-
# from odoo import http


# class CustomApp1(http.Controller):
#     @http.route('/custom_app1/custom_app1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_app1/custom_app1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_app1.listing', {
#             'root': '/custom_app1/custom_app1',
#             'objects': http.request.env['custom_app1.custom_app1'].search([]),
#         })

#     @http.route('/custom_app1/custom_app1/objects/<model("custom_app1.custom_app1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_app1.object', {
#             'object': obj
#         })
