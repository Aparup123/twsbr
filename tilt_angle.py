import mpu6050
import time
import motorModule

m=motorModule.Motor(18, 14, 15)
mpu6050=mpu6050.mpu6050(0x68)

current_angle=0
prev_angle=0
dt=0.1

gyroData=mpu6050.get_gyro_data()
offset_angular_vel=gyroData['x']

while True:
    gyroData=mpu6050.get_gyro_data()
    current_angular_vel_x=gyroData['x']-offset_angular_vel
    
    current_angle=prev_angle+(current_angular_vel_x*dt)
    prev_angle=current_angle
    print("Current Angle:",current_angle)
    if(current_angle>2):
        motorSpeed=(current_angle*10)
        motorSpeed=motorSpeed if motorSpeed<=100 else 100
        m.backward(motorSpeed)
    elif(current_angle<(-2)):
        motorSpeed=(-current_angle*10)
        motorSpeed=motorSpeed if motorSpeed<=100 else 100
        m.forward(motorSpeed)
    else:
        m.stop()

    # print(gyroData)
    # print(current_angular_vel_x)
    

    time.sleep(0.1)

