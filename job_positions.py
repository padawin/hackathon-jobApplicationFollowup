class JobPosition:
    def __init__(self, job_position_id, title, description, date_posted, is_new=False):
        self.job_position_id = job_position_id
        self.title = title
        self.description = description
        self.date_posted = date_posted
        self.is_new = is_new
