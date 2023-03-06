# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ScaffoldActive(models.Model):
    _name = 'scaffold_active'
    _description ='scaffold_active'

    name = fields.Char(string='active')
class ScaffoldStatus(models.Model):
    _name = 'scaffold_status'
    _description ='scaffold_status'

    name = fields.Char(string='status')
class ScaffoldDetails(models.Model):
    _name = 'scaffold_details'
    _description = 'Scaffold Details'

    tag_id = fields.Many2one(comodel_name='nfc_tags', string='Tag Id')
    permit_id = fields.Integer(string='Permit Id')
    next_inspection_date = fields.Date(string='Next Inspection Date')
    length = fields.Float(string='Length')
    breadth = fields.Float(string='Breadth')
    height = fields.Float(string='Height')
    safe_working_load = fields.Float(string='Safe Working Load')
    erected_by = fields.Char(string='Erected By')
    erected_by_company = fields.Char(string='Erected By Company')
    status = fields.Many2one(comodel_name='scaffold_status', string='Status')
    active = fields.Many2one(comodel_name='scaffold_active',string='Active')
    latitude = fields.Float(string='Latitude Position')
    longitude = fields.Float(string='Longitude Position')
    details = fields.Text(string='Details')