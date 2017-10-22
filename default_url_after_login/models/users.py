# -*- coding: utf-8 -*-

from openerp import api, fields, models, _
from odoo.exceptions import ValidationError


class Users(models.Model):
    _inherit = 'res.users'


    def __init__(self, pool, cr):
        init_res = super(Users, self).__init__(pool, cr)
        # duplicate list to avoid modifying the original reference
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(['default_url'])
        # duplicate list to avoid modifying the original reference
        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(['default_url'])
        return init_res

    default_url = fields.Char(string='Default URL')
 
