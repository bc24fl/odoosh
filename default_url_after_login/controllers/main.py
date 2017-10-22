# -*- coding: utf-8 -*-

import functools
import logging

import json

import werkzeug.utils
from werkzeug.exceptions import BadRequest


import odoo
# import odoo.modules.registry
# from odoo.api import call_kw, Environment
# from odoo.modules import get_resource_path
# from odoo.tools import topological_sort
# from odoo.tools.translate import _
# from odoo.tools.misc import str2bool, xlwt
# from odoo import http
# from odoo.http import content_disposition, dispatch_rpc, request, \
#                       serialize_exception as _serialize_exception
# from odoo.exceptions import AccessError
# from odoo.models import check_method_name

from odoo import api, http, SUPERUSER_ID, _
from odoo.exceptions import AccessDenied
from odoo.http import request
from odoo import registry as registry_get

from odoo.addons.auth_signup.controllers.main import AuthSignupHome as Home
from odoo.addons.web.controllers.main import db_monodb, ensure_db, set_cookie_and_redirect, login_and_redirect


class PropertyHome(Home):
    
    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        ensure_db()
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            return http.redirect_with_hash(redirect)

        if not request.uid:
            request.uid = odoo.SUPERUSER_ID

        values = request.params.copy()
        try:
            values['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
            values['databases'] = None

        if request.httprequest.method == 'POST':
            old_uid = request.uid
            uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
            if uid is not False:
                
                current_user = request.env['res.users'].sudo().browse(uid)
                if current_user.default_url:
                    redirect = current_user.default_url
                
                request.params['login_success'] = True
                if not redirect:
                    redirect = '/web'
                return http.redirect_with_hash(redirect)
            request.uid = old_uid
            values['error'] = _("Wrong login/password")
        return request.render('web.login', values)







