from flask import Flask, send_from_directory, jsonify

from json_encoder import JSONEncoder

from mock_job_positions import mock_job_positions

job_application_followup = Flask(__name__, static_folder='public', static_url_path='')
job_application_followup.json_encoder = JSONEncoder


@job_application_followup.route('/')
def root():
    return "Hello, world"


@job_application_followup.route('/api/positions')
def positions():
    return jsonify(mock_job_positions)


@job_application_followup.route('/api/positions/<int:position_id>')
def position(position_id):
    return jsonify(mock_job_positions[position_id])


@job_application_followup.errorhandler(404)
def page_not_found(e):
    return send_from_directory(job_application_followup.static_folder, 'not-found.html'), 404


if __name__ == "__main__":
    job_application_followup.run()
