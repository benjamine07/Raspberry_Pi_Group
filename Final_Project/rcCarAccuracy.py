#!/usr/bin/env python3
'''
This file is provided by ECE3432 Course Instructor
it has been modified by the students for submission as
the final project. 
It's purpose is to run a prediction on a list of image files
as fast as possible using a model trained by students on
a nueral net
'''
# import modules
import json # used for settings parsing
import pandas as pd # used to parse csv
import time # used to caclulate prediction speed

# local files for neural net
from av_nn_tools import NNTools
from av_parse_data import ParseData

# where we store the csv relative to script
TEST_LIST = 'data/list/final_test.csv'
# where we store settings json relative to script
SETTINGS = 'data/set_accuracy_test.json'

# read the csv and parse it for prediction
data = pd.read_csv(TEST_LIST)
parsedata = ParseData()
# load settings from json file
with open(SETTINGS) as fp:
    content = json.load(fp)

    shape = content['shape']
    servo_pred = NNTools(content["servo_setting"])
    servo_pred.load_model(content['servo_model'])

servo_count = 0

# make predictions from csv and print value
for index in range(len(data)):
    _, servo, motor = parsedata.parse_data(data["image"][index])

    pred_servo = servo_pred.predict(data["image"][index])

    if abs(servo - pred_servo) <= content['error_margin']:
        # print(servo)
        servo_count += 1
    # if (servo-15)*(pred_servo-15) >= 0:
    #     # print(servo)
    #     servo_count += 1


    if (index + 1) % 100 == 0:
        print("[%5d] servo: %2.2f " % \
              (index + 1, 100 * servo_count / (index + 1), ))

print("servo: %2.2f" % (100 * servo_count / (index + 1)))

#------------------------------Timing-Data------------------------------
# arbitrary image to test timing
IMAGE_FILE = 'data/images/03_09_2020_1/output_0033/i0000007_s15_m18.jpg'
servo_pred.test(TEST_LIST) # already created above
start_time = time.time()
servov = servo_pred.predict(IMAGE_FILE)
end_time = time.time()
tot_time = end_time-start_time
print(servov)
print("Total time:", tot_time)