# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
      _inherit = 'x_project'

      TotalCost = fields.Decimal('Total cost')
