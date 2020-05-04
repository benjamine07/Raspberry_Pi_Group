#!/usr/bin/env python3

from av_nn_tools import NNTools
import time

TRAIN_DATA = 'data/list/train_1.csv'
TEST_DATA = 'data/list/final_test.csv'

SERVO_TRAIN_SETTING = "data/set_servo_train.json"
SERVO_TEST_SETTING = "data/set_servo_test.json"
SERVO_MODEL = 'models/servo_model.pth'

#MOTOR_TRAIN_SETTING = "data/set_motor_train.json"
#MOTOR_TEST_SETTING = "data/set_motor_test.json"
#MOTOR_MODEL = 'models/motor_model.pth'

# servo_train = NNTools(SERVO_TRAIN_SETTING)
# servo_train.load_model(SERVO_MODEL)
# servo_train.train(TRAIN_DATA)
# servo_train.save_model(SERVO_MODEL)

servo_test = NNTools(SERVO_TEST_SETTING)
servo_test.load_model(SERVO_MODEL)
servo_test.test(TEST_DATA)

IMAGE_FILE = "data/images/03_12_2020_0/output_0002/i0001053_s17_m17.jpg"

servo_test = NNTools(SERVO_TEST_SETTING)
servo_test.load_model(SERVO_MODEL)
servo_test.test(TEST_DATA)
start_time = time.time()
servov=servo_test.predict(IMAGE_FILE)
end_time = time.time()
print(servov)
print(end_time-start_time)
