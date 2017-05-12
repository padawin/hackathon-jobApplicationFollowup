from flask import Flask, send_from_directory

job_application_followup = Flask(__name__, static_folder='public', static_url_path='')


@job_application_followup.route('/')
def root():
    return "Hello, world"


@job_application_followup.errorhandler(404)
def page_not_found(e):
    return send_from_directory(job_application_followup.static_folder, 'not-found.html'), 404


if __name__ == "__main__":
    job_application_followup.run()
