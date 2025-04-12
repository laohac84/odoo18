# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json

class BKHNController(http.Controller):

    @http.route('/bkh/test_model', type='http', auth='none', methods=['POST'], csrf=False)
    def create_test_model(self):
        """
        API to create a new test.model record
        Args:
            - kwargs: Contains the data for the new record (name, description, category, value)
        Returns:
            - JSON response with the status of the operation
        """
        # Extract data from the request
        data = request.get_json_data()
        name = data.get('name')
        age = data.get('age')

        if not name:
            return {'status': 'error', 'message': 'Name is required'}

        # Create the new record in the `test.model` model
        test_model = request.env['test.model'].sudo().create({
            'name': name,
            'age': age,
        })

        # Return a success message with the ID of the newly created record
        return json.dumps({
            'status': 'success',
            'message': 'Test model record created successfully',
            'record_id': test_model.id
        })
