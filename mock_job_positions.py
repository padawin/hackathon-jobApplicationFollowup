from datetime import datetime
from itertools import count

from flask import request
from flask_restful import Resource

from job_positions import JobPosition

mock_ids = count()

_mock_job_positions = [
    JobPosition(next(mock_ids), "Software Developer", """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nisi erat, lobortis sed purus id,
        vulputate iaculis turpis. Curabitur vehicula ornare felis dapibus ultricies. Sed pretium augue et
        libero consectetur, vel sagittis turpis bibendum. Duis semper porta lectus quis convallis. Nulla
        feugiat rhoncus convallis. Nam elementum sem in sem tincidunt, nec tristique eros fringilla. Ut nec
        nibh auctor, porttitor ex ac, accumsan leo. Quisque accumsan ultricies sem in posuere. Cras
        ultricies, felis ac accumsan fermentum, nulla tellus egestas nisi, et venenatis arcu elit a velit.
        Fusce dictum faucibus nisl quis iaculis. Aliquam maximus pulvinar est.
    """, datetime(2017, 5, 12), is_new=True),
    JobPosition(next(mock_ids), "Software Developer", """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nisi erat, lobortis sed purus id,
        vulputate iaculis turpis. Curabitur vehicula ornare felis dapibus ultricies. Sed pretium augue et
        libero consectetur, vel sagittis turpis bibendum. Duis semper porta lectus quis convallis. Nulla
        feugiat rhoncus convallis. Nam elementum sem in sem tincidunt, nec tristique eros fringilla. Ut nec
        nibh auctor, porttitor ex ac, accumsan leo. Quisque accumsan ultricies sem in posuere. Cras
        ultricies, felis ac accumsan fermentum, nulla tellus egestas nisi, et venenatis arcu elit a velit.
        Fusce dictum faucibus nisl quis iaculis. Aliquam maximus pulvinar est.
    """, datetime(2017, 5, 10)),
    JobPosition(next(mock_ids), "Software Developer", """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nisi erat, lobortis sed purus id,
        vulputate iaculis turpis. Curabitur vehicula ornare felis dapibus ultricies. Sed pretium augue et
        libero consectetur, vel sagittis turpis bibendum. Duis semper porta lectus quis convallis. Nulla
        feugiat rhoncus convallis. Nam elementum sem in sem tincidunt, nec tristique eros fringilla. Ut nec
        nibh auctor, porttitor ex ac, accumsan leo. Quisque accumsan ultricies sem in posuere. Cras
        ultricies, felis ac accumsan fermentum, nulla tellus egestas nisi, et venenatis arcu elit a velit.
        Fusce dictum faucibus nisl quis iaculis. Aliquam maximus pulvinar est.
    """, datetime(2017, 5, 8)),
    JobPosition(next(mock_ids), "Software Developer", """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nisi erat, lobortis sed purus id,
        vulputate iaculis turpis. Curabitur vehicula ornare felis dapibus ultricies. Sed pretium augue et
        libero consectetur, vel sagittis turpis bibendum. Duis semper porta lectus quis convallis. Nulla
        feugiat rhoncus convallis. Nam elementum sem in sem tincidunt, nec tristique eros fringilla. Ut nec
        nibh auctor, porttitor ex ac, accumsan leo. Quisque accumsan ultricies sem in posuere. Cras
        ultricies, felis ac accumsan fermentum, nulla tellus egestas nisi, et venenatis arcu elit a velit.
        Fusce dictum faucibus nisl quis iaculis. Aliquam maximus pulvinar est.
    """, datetime(2017, 5, 4))
]

mock_job_positions = {
    job_position.job_position_id: job_position for job_position in _mock_job_positions
}


class MockJobPositionsList(Resource):
    @staticmethod
    def get():
        return list(mock_job_positions.values())

    @staticmethod
    def post():
        job_position_json = request.json

        if 'job_position_id' in job_position_json:
            del job_position_json['job_position_id']

        job_position_id = next(mock_ids)
        mock_job_positions[job_position_id] = JobPosition(job_position_id, **job_position_json)

        return mock_job_positions[job_position_id]


class MockJobPositions(Resource):
    @staticmethod
    def get(job_position_id):
        if job_position_id not in mock_job_positions:
            return None, 404

        return mock_job_positions[job_position_id]

    @staticmethod
    def put(job_position_id):
        job_position_json = request.json

        if 'job_position_id' in job_position_json:
            del job_position_json['job_position_id']

        mock_job_positions[job_position_id] = JobPosition(job_position_id, **job_position_json)

        return mock_job_positions[job_position_id]

    @staticmethod
    def delete(job_position_id):
        if job_position_id in mock_job_positions:
            del mock_job_positions[job_position_id]