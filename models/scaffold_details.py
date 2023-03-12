# -*- coding: utf-8 -*-

from odoo import models, fields, api
class ScaffoldStatus(models.Model):
    _name = 'scaffold_status'
    _description ='scaffold_status'

    name = fields.Char(string='status')
    #code = fields.Char(string='code')

    #_sql_constraints = [
    #    ('code', 'unique(code)', "A status with this code already exists. Stuff's name must be unique!"),
    #]

class ScaffoldDetails(models.Model):
    _name = 'scaffold_details'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'format.address.mixin']
    _description = 'Scaffold Details'

    tag_id = fields.Many2one(comodel_name='nfc_tags', string='Tag Id' ,tracking=True , domain=[('is_linked','=',False)])
    permit_id = fields.Char(string='Permit Id',tracking=True)
    next_inspection_date = fields.Date(string='Next Inspection Date',tracking=True)
    length = fields.Float(string='Length',tracking=True)
    breadth = fields.Float(string='Breadth',tracking=True)
    height = fields.Float(string='Height',tracking=True)
    safe_working_load = fields.Float(string='Safe Working Load',tracking=True)
    erected_by = fields.Char(string='Erected By',tracking=True)
    erected_by_company = fields.Char(string='Erected By Company',tracking=True)
    #status = fields.Many2one(comodel_name='scaffold_status', string='Status')
    active = fields.Boolean(string='Active',tracking=True)
    latitude = fields.Float(string='Latitude Position',tracking=True)
    longitude = fields.Float(string='Longitude Position',tracking=True)
    details = fields.Text(string='Details',tracking=True)

    @api.model_create_multi
    def create(self, vals):
        #nfc_tag_id = self.env['nfc_tags'].browse(vals[0]['tag_id'])
        #nfc_tag_id.is_linked=True
        return super(ScaffoldDetails, self).create(vals)