import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import socket
import json
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 10000))
    
gyro_x_vals=[]
gyro_y_vals=[]
gyro_z_vals=[]
t_vals=[]
t=0
def animate(t):
    data, _ = sock.recvfrom(4096)
    data=data.decode('utf-8')
    data=json.loads(data)
    print(data['AccelData'])
    gyroData=data['AccelData']
    gyroData=data['GyroData']
    print(gyroData)
    t=t+1
    gyro_x_vals.append(gyroData['x'])
    gyro_y_vals.append(gyroData['y'])
    gyro_z_vals.append(gyroData['z'])
    t_vals.append(t)
    plt.cla()
    plt.plot(t_vals, gyro_x_vals, "r", t_vals, gyro_y_vals, 'g', t_vals, gyro_z_vals, "b" )

ani=FuncAnimation(plt.gcf(), animate, interval=1000 )

plt.show()
