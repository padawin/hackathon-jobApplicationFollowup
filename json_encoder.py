from datetime import datetime

from flask.json import JSONEncoder as DefaultJSONEncoder

from job_positions import JobPosition
from applications import Application


class JSONEncoder(DefaultJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat() + 'Z'

        if isinstance(obj, (JobPosition, Application)):
            return obj.__dict__

        return DefaultJSONEncoder.default(self, obj)
