from odoo import models, fields, api


class Checklist(models.Model):
    _name = 'checklist'
    _description = 'checklist'

    checklist_id = fields.Char(string="checklist Id")