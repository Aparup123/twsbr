import json
import mpu6050
import time
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#ARITRA LAPTOP 192.168.81.27
server_address = ('192.168.0.125', 10000)

mpu6050=mpu6050.mpu6050(0x68)
while True:
    accelData=mpu6050.get_accel_data()
    gyroData=mpu6050.get_gyro_data()
    temperature=mpu6050.get_temp()

    message={"AccelData":accelData, "GyroData":gyroData,}
    message=json.dumps(message)
    print("______DATA______")
    print("temp:", temperature)
    print("Gyro:",gyroData)
    print("Accel",accelData)
    sock.sendto(str(message).encode(), server_address)
    time.sleep(.1)
