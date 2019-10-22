from jnius_config import set_classpath
try:
    set_classpath('konduit.jar')
except:
    print("VM already running from previous test")

from konduit import *
from konduit.server import Server
from konduit.client import Client
from konduit.utils import is_port_in_use

import numpy as np
import time
import random

import sys
python_path = ':'.join(sys.path)
workdir = '/home/ubuntu/work/Ultra-Light-Fast-Generic-Face-Detector-1MB'
python_path += ':' + workdir
print(python_path)

input_names = ['default']
output_names = ['default']
port = random.randint(1000, 65535)
port = 9233
parallel_inference_config = ParallelInferenceConfig(workers=1)
serving_config = ServingConfig(http_port=port,
                               input_data_type='JSON',
                               output_data_type='JSON',
                               log_timings=True,
                               parallel_inference_config=parallel_inference_config)


python_config = PythonConfig(
    python_path=python_path,
    #python_code_path='sample_pytorch.py',
    python_code_path=workdir+'/detect_one.py',
    python_inputs={'image': 'STR'},
    python_outputs={'nboxes': 'STR'},
)

python_pipeline_step = PythonPipelineStep(input_names=input_names,
                                          output_names=output_names,
                                          input_schemas=({'default': ['String']}),
                                          output_schemas=({'default': ['String']}),
                                          input_column_names={'default': ['image']},
                                          output_column_names={'default': ['nboxes']},
                                          python_configs={'default': python_config})

inference = InferenceConfiguration(serving_config=serving_config,
                                   pipeline_steps=[python_pipeline_step])

server = Server(config=inference,
                extra_start_args='-Xmx8g',
                jar_path='konduit.jar')
server.start()
print('Process started.')
time.sleep(3)
#print('Process started. Sleeping 10 seconds.')

#client = Client(input_names=input_names,
#                output_names=output_names,
#                input_type='NUMPY',
#                endpoint_output_type='NUMPY',
#                url='http://localhost:' + str(port))
#
#import cv2
#orig_image = cv2.imread(workdir + '/imgs/1.jpg')
#image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
#image = image.astype(np.float32)
#print(image.shape)
##image /= 255.
#data_input = {
#    #'default': np.load('./data/input-0.npy'),
#    'default': image
#}
#print(type(orig_image))

#time.sleep(10)

#assert is_port_in_use(port)

#try:
#    predicted = client.predict(data_input)
#    print(predicted)
#    server.stop()
#except Exception as e:
#    print(e)
#    server.stop()
