class JobPosition:
    def __init__(self, title, description, image, date_posted, is_new=False):
        self.title = title
        self.description = description
        self.image = image
        self.date_posted = date_posted
        self.is_new = is_new
