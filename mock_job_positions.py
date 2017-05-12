from datetime import datetime

from job_positions import JobPosition

mock_job_positions = [
    JobPosition("Software Developer", """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nisi erat, lobortis sed purus id,
        vulputate iaculis turpis. Curabitur vehicula ornare felis dapibus ultricies. Sed pretium augue et
        libero consectetur, vel sagittis turpis bibendum. Duis semper porta lectus quis convallis. Nulla
        feugiat rhoncus convallis. Nam elementum sem in sem tincidunt, nec tristique eros fringilla. Ut nec
        nibh auctor, porttitor ex ac, accumsan leo. Quisque accumsan ultricies sem in posuere. Cras
        ultricies, felis ac accumsan fermentum, nulla tellus egestas nisi, et venenatis arcu elit a velit.
        Fusce dictum faucibus nisl quis iaculis. Aliquam maximus pulvinar est.
    """, 1, datetime(2017, 5, 12), is_new=True),
    JobPosition("Software Developer", """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nisi erat, lobortis sed purus id,
        vulputate iaculis turpis. Curabitur vehicula ornare felis dapibus ultricies. Sed pretium augue et
        libero consectetur, vel sagittis turpis bibendum. Duis semper porta lectus quis convallis. Nulla
        feugiat rhoncus convallis. Nam elementum sem in sem tincidunt, nec tristique eros fringilla. Ut nec
        nibh auctor, porttitor ex ac, accumsan leo. Quisque accumsan ultricies sem in posuere. Cras
        ultricies, felis ac accumsan fermentum, nulla tellus egestas nisi, et venenatis arcu elit a velit.
        Fusce dictum faucibus nisl quis iaculis. Aliquam maximus pulvinar est.
    """, 4, datetime(2017, 5, 10)),
    JobPosition("Software Developer", """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nisi erat, lobortis sed purus id,
        vulputate iaculis turpis. Curabitur vehicula ornare felis dapibus ultricies. Sed pretium augue et
        libero consectetur, vel sagittis turpis bibendum. Duis semper porta lectus quis convallis. Nulla
        feugiat rhoncus convallis. Nam elementum sem in sem tincidunt, nec tristique eros fringilla. Ut nec
        nibh auctor, porttitor ex ac, accumsan leo. Quisque accumsan ultricies sem in posuere. Cras
        ultricies, felis ac accumsan fermentum, nulla tellus egestas nisi, et venenatis arcu elit a velit.
        Fusce dictum faucibus nisl quis iaculis. Aliquam maximus pulvinar est.
    """, 6, datetime(2017, 5, 8)),
    JobPosition("Software Developer", """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nisi erat, lobortis sed purus id,
        vulputate iaculis turpis. Curabitur vehicula ornare felis dapibus ultricies. Sed pretium augue et
        libero consectetur, vel sagittis turpis bibendum. Duis semper porta lectus quis convallis. Nulla
        feugiat rhoncus convallis. Nam elementum sem in sem tincidunt, nec tristique eros fringilla. Ut nec
        nibh auctor, porttitor ex ac, accumsan leo. Quisque accumsan ultricies sem in posuere. Cras
        ultricies, felis ac accumsan fermentum, nulla tellus egestas nisi, et venenatis arcu elit a velit.
        Fusce dictum faucibus nisl quis iaculis. Aliquam maximus pulvinar est.
    """, 8, datetime(2017, 5, 4))
]
