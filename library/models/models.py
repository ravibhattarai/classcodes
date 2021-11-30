# -*-coding: utf-8 -*-

from odoo import models, fields, api


class library(models.Model):
     _name = 'library.library'
     _description = 'library.library'

     bookname = fields.Char()
     isbn = fields.Integer()
     price = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     @api.depends('isbn')
     def _value_pc(self):
         for record in self:
             record.price = float(record.isbn) / 100