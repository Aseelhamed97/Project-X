# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
      _inherit = 'sale.order'

      birthday = fields.Datetime('Date of birth')
