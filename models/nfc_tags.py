# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NfcTags(models.Model):
    _name = 'nfc_tags'
    _description = 'NFC Tags'

    tag_id = fields.Char(string="Tag Id")
    is_linked = fields.Boolean(string="Is Linked")

    scaffold_details = fields.One2many('scaffold_details', 'tag_id', string='Scaffold Details', domain=[('is_active', '=', True)])

    permit_id = fields.Char(compute='_compute_permit_id', inverse='_inverse_permit_id')
    next_inspection_date = fields.Date(compute='_compute_next_inspection_date', inverse='_inverse_next_inspection_date')
    length = fields.Float(compute=lambda self: self.scaffold_details[0].length if len(self.scaffold_details) else False, inverse=lambda self: None)
    breadth = fields.Float(compute=lambda self: self.scaffold_details[0].breadth if len(self.scaffold_details) else False, inverse=lambda self: None)
    height = fields.Float(compute=lambda self: self.scaffold_details[0].height if len(self.scaffold_details) else False, inverse=lambda self: None)
    safe_working_load = fields.Float(compute=lambda self: self.scaffold_details[0].safe_working_load if len(self.scaffold_details) else False, inverse=lambda self: None)
    erected_by = fields.Char(compute=lambda self: self.scaffold_details[0].erected_by if len(self.scaffold_details) else False, inverse=lambda self: None)
    erected_by_company = fields.Char(compute=lambda self: self.scaffold_details[0].erected_by_company if len(self.scaffold_details) else False, inverse=lambda self: None)
    #status = fields.Many2one(compute=lambda self: self.scaffold_details[0].status if len(self.scaffold_details) else False, inverse=lambda self: None)
    latitude = fields.Float(compute=lambda self: self.scaffold_details[0].latitude if len(self.scaffold_details) else False, inverse=lambda self: None)
    longitude = fields.Float(compute=lambda self: self.scaffold_details[0].longitude if len(self.scaffold_details) else False, inverse=lambda self: None)
    details = fields.Text(compute=lambda self: self.scaffold_details[0].details if len(self.scaffold_details) else False, inverse=lambda self: None)

    def _compute_permit_id(self):
        if len(self.scaffold_details):
            self.permit_id = self.scaffold_details[0].permit_id
        else:
            self.permit_id = False

    def _inverse_permit_id(self):
        pass

    def _compute_next_inspection_date(self):
        if len(self.scaffold_details):
            self.next_inspection_date = self.scaffold_details[0].next_inspection_date
        else:
            self.next_inspection_date = False

    def _inverse_next_inspection_date(self):
        pass

    def write(self, vals):
        if (self.is_linked):
            #update scaffold details
            data = {}
            # add values to data if key exists in vals
            scaffold_detail_fields = ['permit_id', 'next_inspection_date', 'length']

            for field in scaffold_detail_fields:
                if field in vals:
                    data[field] = vals[field]

            self.scaffold_details[0].write(data)
        else:
            #create new scaffold details
            scaffold_details = self.env['scaffold_details'].create({
                'tag_id': self.id,
                'permit_id': vals['permit_id'],
                'next_inspection_date': vals['next_inspection_date'],
                'length': vals['length'],
                'breadth': vals['breadth'],
                'height': vals['height'],
                'erected_by': vals['erected_by'],
                'erected_by_company': vals['erected_by_company'],
                #'status': vals['status'],
                'is_active': True,
                'latitude': vals['latitude'],
                'longitude': vals['longitude'],
                'details': vals['details'],
            })
            vals['is_linked'] = True
            vals['scaffold_details'] = scaffold_details


        res = super(NfcTags, self).write(vals)
        return res