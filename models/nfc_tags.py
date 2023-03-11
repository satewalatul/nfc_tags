# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NfcTags(models.Model):
    _name = 'nfc_tags'
    _description = 'NFC Tags'

    tag_id = fields.Char(string="Tag Id")
    is_linked = fields.Boolean(string="Is Linked")

    scaffold_details = fields.One2many('scaffold_details', 'tag_id', string='Scaffold Details', domain=[('active', '=', True)])

    permit_id = fields.Char(compute='_compute_permit_id', inverse='_inverse_permit_id')
    next_inspection_date = fields.Date(compute='_compute_next_inspection_date', inverse='_inverse_next_inspection_date')
    length = fields.Float(compute='_compute_length',inverse='_inverse_length')
    breadth = fields.Float(compute='_compute_breadth', inverse='_inverse_breadth')
    height = fields.Float(compute='_compute_height', inverse='_inverse_height')
    safe_working_load = fields.Float(compute='_compute_safe_working_load', inverse='_inverse_safe_working_load')
    erected_by = fields.Char(compute='_compute_erected_by', inverse='_inverse_erected_by')
    erected_by_company = fields.Char(compute='_compute_erected_by_company', inverse='_inverse_erected_by_company')
    # status = fields.Many2one(compute='_compute_status',if len(self.scaffold_details) else False, inverse=lambda self: None)
    latitude = fields.Float(compute='_compute_latitude', inverse='_inverse_latitude')
    longitude = fields.Float(compute='_compute_longitude', inverse='_inverse_longitude')
    details = fields.Text(compute='_compute_details', inverse='_inverse_details')

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

    def _compute_length(self):
        if len(self.scaffold_details):
            self.length=self.scaffold_details[0].length
        else:
            self.length=False

    def _inverse_length(self):
        pass

    def _compute_breadth(self):
        if len(self.scaffold_details):
            self.breadth = self.scaffold_details[0].breadth
        else:
            self.breadth = False

    def _inverse_breadth(self):
        pass

    def _compute_height(self):
        if len(self.scaffold_details):
            self.height = self.scaffold_details[0].height
        else:
            self.height = False

    def _inverse_height(self):
        pass
    def _compute_safe_working_load(self):
        if len(self.scaffold_details):
            self.safe_working_load = self.scaffold_details[0].safe_working_load
        else:
            self.safe_working_load = False

    def _inverse_safe_working_load(self):
        pass

    def _compute_erected_by(self):
        if len(self.scaffold_details):
            self.erected_by = self.scaffold_details[0].erected_by
        else:
            self.erected_by = False

    def _inverse_erected_by(self):
        pass

    def _compute_erected_by_company(self):
        if len(self.scaffold_details):
            self.erected_by_company = self.scaffold_details[0].erected_by_company
        else:
            self.erected_by_company = False

    def _inverse_erected_by_company(self):
        pass

    def _compute_latitude(self):
        if len(self.scaffold_details):
            self.latitude = self.scaffold_details[0].latitude
        else:
            self.latitude = False

    def _inverse_latitude(self):
        pass

    def _compute_longitude(self):
        if len(self.scaffold_details):
            self.longitude = self.scaffold_details[0].longitude
        else:
            self.longitude = False

    def _inverse_longitude(self):
        pass


    def _compute_details(self):
        if len(self.scaffold_details):
            self.details = self.scaffold_details[0].details
        else:
            self.details = False

    def _inverse_details(self):
        pass


    def write(self, vals):
        if (self.is_linked):
            #update scaffold details
            data = {}
            # add values to data if key exists in vals
            scaffold_detail_fields = ['permit_id', 'next_inspection_date', 'length','height','safe_working_load','erected_by','erected_by_company','latitude','longitude','details']

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
                'active': True,
                'latitude': vals['latitude'],
                'longitude': vals['longitude'],
                'details': vals['details'],
            })
            vals['is_linked'] = True
            vals['scaffold_details'] = scaffold_details


        res = super(NfcTags, self).write(vals)
        return res