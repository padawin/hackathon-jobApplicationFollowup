from datetime import datetime


class Application:
    def __init__(self, application_id, job_position_id, candidate_name, candidate_status, date_applied=None):
        self.application_id = application_id
        self.job_position_id = job_position_id
        self.candidate_name = candidate_name
        self.candidate_status = candidate_status
        self.date_applied = date_applied or datetime.now()
