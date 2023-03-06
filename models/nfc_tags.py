# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NfcTags(models.Model):
    _name = 'nfc_tags'
    _description = 'NFC Tags'

    tag_id = fields.Char(string="Tag Id")
    is_linked = fields.Boolean(string="Is Linked")