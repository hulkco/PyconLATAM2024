import time
from lsm6dsox import LSM6DSOX
from machine import Pin, I2C

# Initialize the LSM6DSOX sensor with I2C interface
lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))

while True:
    # Read accelerometer values
    accel_values = lsm.accel()
    print('Accelerometer: x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*accel_values))
    
    # Read gyroscope values
    gyro_values = lsm.gyro()
    print('Gyroscope:     x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*gyro_values))
    
    print("")
    time.sleep_ms(100)

