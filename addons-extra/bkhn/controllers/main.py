# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json
from datetime import datetime
import pytz



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

    @http.route('/bkh/sensor_data', type='http', auth='none', methods=['POST'], csrf=False)
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
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        count = data.get('count')
        type = data.get('type')

        # Convert start_date and end_date to UTC
        local_tz = pytz.timezone('Asia/Ho_Chi_Minh')  # Replace with the relevant timezone
        local_start_date = datetime.strptime(start_date, '%d/%m/%Y %H:%M:%S')
        local_end_date = datetime.strptime(end_date, '%d/%m/%Y %H:%M:%S')

        # Localize the datetime to the correct timezone
        localized_start_date = local_tz.localize(local_start_date)
        localized_end_date = local_tz.localize(local_end_date)

        # Convert the localized datetime to UTC
        utc_start_date = localized_start_date.astimezone(pytz.utc)
        utc_end_date = localized_end_date.astimezone(pytz.utc)

        # Remove the timezone info to make it naive
        naive_start_date = utc_start_date.replace(tzinfo=None)
        naive_end_date = utc_end_date.replace(tzinfo=None)

        # Create the new record in the `sensor.data` model
        test_model = request.env['sensor.data'].sudo().create({
            'count': count,
            'type': type,
            'start_date': naive_start_date,
            'end_date': naive_end_date,
        })

        # production = request.env['mrp.production'].sudo().create({
        #     'name': 'Production-' + str(test_model.id),  # Or any other name generation logic
        #     'product_id': 1,  # Replace with appropriate product ID
        #     'product_qty': count,  # You can set the quantity produced
        #     'date_start': naive_start_date,
        #     'date_finished': naive_end_date,
        #     # Add other necessary fields based on your requirements
        # })

        # Return a success message with the ID of the newly created record
        return json.dumps({
            'status': 'success',
            'message': 'Sensor record created successfully',
            'record_id': test_model.id
        })
