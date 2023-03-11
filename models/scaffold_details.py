# -*- coding: utf-8 -*-

from odoo import models, fields, api
class ScaffoldStatus(models.Model):
    _name = 'scaffold_status'
    _description ='scaffold_status'

    name = fields.Char(string='status')
    code = fields.Char(string='code')

    _sql_constraints = [
        ('code', 'unique(code)', "A status with this code already exists. Stuff's name must be unique!"),
    ]

class ScaffoldDetails(models.Model):
    _name = 'scaffold_details'
    _description = 'Scaffold Details'

    tag_id = fields.Many2one(comodel_name='nfc_tags', string='Tag Id',domain=[('is_linked','=',False)])
    permit_id = fields.Char(string='Permit Id')
    next_inspection_date = fields.Date(string='Next Inspection Date')
    length = fields.Float(string='Length')
    breadth = fields.Float(string='Breadth')
    height = fields.Float(string='Height')
    safe_working_load = fields.Float(string='Safe Working Load')
    erected_by = fields.Char(string='Erected By')
    erected_by_company = fields.Char(string='Erected By Company')
    status = fields.Many2one(comodel_name='scaffold_status', string='Status')
    is_active = fields.Boolean(string='Active')
    latitude = fields.Float(string='Latitude Position')
    longitude = fields.Float(string='Longitude Position')
    details = fields.Text(string='Details')

    @api.model_create_multi
    def create(self, vals):
        #nfc_tag_id = self.env['nfc_tags'].browse(vals[0]['tag_id'])
        #nfc_tag_id.is_linked=True
        return super(ScaffoldDetails, self).create(vals)