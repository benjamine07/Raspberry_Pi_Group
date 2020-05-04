# README for Group 1 Final Project

## Servo Training and Testing
- Servo training and testing parameters were defined using the set_servo_train.json and set_servo_test.json respectively
- For training the model a batch size of 15 was used for accuracy
    - The smaller the batch size of data being passed through the neural network the more accurate the model
- For testing the model a batch size of 20 was used for small loss
    - A larger batch size significantly increases the speed for testing the model
- For both training and testing a epoch size of 10 was used
    - This means that an entire dataset is passed forward and backward through the neural network ten times for one                iteration

### GitHub Link - https://github.com/benjamine07/Raspberry_Pi_Group/tree/master/Final_Project

#### Task 1 - A Servo Model with MSE less than 0.7

- Test Batch = 20
- MSE of 0.4856
- Accuracy of 63.90% with Error Margin = 2

#### Tast 2 - Port Code to Raspberry Pi

- download pre-compiled pytorch wheel files
    ```bash
    wget https://github.com/lbaitemple/ubuntu_server_rpi/blob/master/torch/torch-1.6.0a0%2B521910e-cp36-cp36m-linux_armv7l.whl
    wget https://github.com/lbaitemple/ubuntu_server_rpi/blob/master/torch/torchvision-0.7.0a0%2Bfed843d-cp36-cp36m-linux_armv7l.whl
    ```

- install wheel files on the system with pip3
    ```bash
    pip3 install torch-1.6.0a0%2B521910e-cp36-cp36m-linux_armv7l.whl
    pip3 install torchvision-0.7.0a0%2Bfed843d-cp36-cp36m-linux_armv7l.whl
    ```
- alternatively you can you use the version of pip with your specific python package 
    ```bash
    python3.6 -m pip install {package_name}
    ```

- install the following pre-requisite modules
    - matplotlib
    - pillow
    - future
    - opencv-python
    - opencv-python-headless
    - numpy
    - cython
    - pandas
    ```bash
    pip3 install -r requirements.txt
    ```
