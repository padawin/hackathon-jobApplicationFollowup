from datetime import datetime


class JobPosition:
    def __init__(self, job_position_id, title, description, date_posted=None, is_new=False):
        self.job_position_id = job_position_id
        self.title = title
        self.description = description
        self.date_posted = date_posted or datetime.now()
        self.is_new = is_new
