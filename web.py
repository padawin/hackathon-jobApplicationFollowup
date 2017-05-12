from flask import Flask, send_from_directory
from flask_restful import Api

from json_encoder import JSONEncoder

from mock_job_positions import MockJobPositionsList, MockJobPositions
from mock_applications import ApplicationsList, Applications

job_application_followup = Flask(__name__, static_folder='public', static_url_path='')
job_application_followup.config['RESTFUL_JSON'] = {'cls': JSONEncoder}

api = Api(job_application_followup, '/api')
api.add_resource(MockJobPositionsList, '/positions')
api.add_resource(MockJobPositions, '/positions/<int:job_position_id>')
api.add_resource(ApplicationsList, '/positions/<int:job_position_id>/applications')
api.add_resource(Applications, '/positions/<int:job_position_id>/applications/<int:application_id>')


@job_application_followup.route('/')
def root():
    return "Hello, world"


@job_application_followup.errorhandler(404)
def page_not_found(e):
    return send_from_directory(job_application_followup.static_folder, 'not-found.html'), 404


if __name__ == "__main__":
    job_application_followup.run()
