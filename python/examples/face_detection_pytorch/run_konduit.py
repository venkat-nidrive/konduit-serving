from konduit import *
from konduit.server import Server
from konduit.client import client_from_server
from konduit.utils import default_python_path

import os
import cv2

# Set the working directory to this folder and register
# the "detect_image.py" script as code to be executed by konduit.
work_dir = os.path.abspath('.')
python_config = PythonConfig(
    python_path=default_python_path(work_dir), python_code_path=os.path.join(work_dir, 'detect_image.py'),
    python_inputs={'image': 'NDARRAY'}, python_outputs={'num_boxes': 'NDARRAY'},
)

# Configure a Python pipeline step for your Python code. Internally, konduit will take numpy arrays as input and
# return data in JSON format. Note that the Python variable 'image' and the Konduit step name 'image_data' are separate
# things here.
step_input_name = 'image_data'
python_pipeline_step = PythonStep().step(python_config, input_name=step_input_name)
serving_config = ServingConfig(http_port=1337, input_data_format='NUMPY', output_data_format='NUMPY')

# Start a konduit server and wait for it to start
server = Server(serving_config=serving_config, steps=[python_pipeline_step])
server.start(sleep=10)

# Initialize a konduit client that takes in and outputs JSON
client = client_from_server(server)

encoded_image = cv2.cvtColor(cv2.imread('./Ultra-Light-Fast-Generic-Face-Detector-1MB/imgs/1.jpg'), cv2.COLOR_BGR2RGB)

try:
    # TODO: it's highly confusing that for JSON input you use 'image' and for 'NDARRAY' you need the step input name.
    #  this makes sense only when you know the internals of Konduit serving.
    predicted = client.predict({step_input_name: encoded_image.astype('int16')})
    print(predicted)
finally:
    server.stop()
