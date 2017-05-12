from datetime import datetime
from itertools import count

from job_positions import JobPosition

mock_ids = count()

mock_job_positions = [
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
