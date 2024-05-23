import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import socket
import json
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 10000))
    
accel_x_vals=[]
accel_y_vals=[]
accel_z_vals=[]
t_vals=[]
t=0
def animate(t):
    data, _ = sock.recvfrom(4096)
    data=data.decode('utf-8')
    data=json.loads(data)
    print(data['AccelData'])
    accelData=data['AccelData']
    gyroData=data['GyroData']
    print(accelData)
    t=t+1
    accel_x_vals.append(accelData['x'])
    accel_y_vals.append(accelData['y'])
    accel_z_vals.append(accelData['z'])
    t_vals.append(t)
    plt.cla()
    plt.plot(t_vals, accel_x_vals, "r", t_vals, accel_y_vals, 'g', t_vals, accel_z_vals, "b" )

ani=FuncAnimation(plt.gcf(), animate, interval=1000 )

plt.show()
