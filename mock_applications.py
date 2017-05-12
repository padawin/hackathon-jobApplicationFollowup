from itertools import count

from flask import request
from flask_restful import Resource

from applications import Application

mock_application_ids = count()
mock_applications = {}


class ApplicationsList(Resource):
    @staticmethod
    def get(job_position_id):
        return [
            application for application in mock_applications.values()
            if application.job_position_id == job_position_id
        ]

    @staticmethod
    def post(job_position_id):
        application_json = request.json

        if 'application_id' in application_json:
            del application_json['application_id']

        if 'job_position_id' in application_json:
            del application_json['job_position_id']

        application_id = next(mock_application_ids)
        mock_applications[application_id] = Application(application_id, job_position_id, **application_json)

        return mock_applications[application_id]


class Applications(Resource):
    @staticmethod
    def get(job_position_id, application_id):
        if application_id not in mock_applications or mock_applications[application_id].job_position_id != job_position_id:
            return None, 404

        return mock_applications[application_id]

    @staticmethod
    def put(job_position_id, application_id):
        application_json = request.json

        if 'job_position_id' in application_json:
            del application_json['job_position_id']

        if 'application_id' in application_json:
            del application_json['application_id']

        mock_applications[application_id] = Application(application_id, job_position_id, **application_json)

        return mock_applications[application_id]

    @staticmethod
    def delete(job_position_id, application_id):
        if application_id in mock_applications and mock_applications[application_id].job_position_id == job_position_id:
            del mock_applications[application_id]
