# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import OrderedDict

from odoo import fields, http, _, models
from odoo.osv import expression
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.addons.account.controllers.download_docs import _get_headers, _build_zip_from_data
from odoo.exceptions import AccessError, MissingError
from odoo.http import request


class TestModel(models.Model):

    _name = 'test.model'
    _description = 'Test Model'

    name = fields.Char('Name', required=True)
    age = fields.Integer('Age')

class SensorData(models.Model):

    _name = 'sensor.data'
    _description = 'Sensor Data'

    start_date = fields.Datetime('Start Date')
    end_date = fields.Datetime('End Date')
    count = fields.Integer('Count')
    type = fields.Char('Type')