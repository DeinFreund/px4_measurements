#import rosbag
import matplotlib.pyplot as plt
import numpy as np
import sys

dyn_time = []
angle_measured = np.empty((0,6))
angle_cmd = np.empty((0,6))
for line in sys.stdin:
	try:
		if len(line.split()) == 14 and line.split()[0] == 'LOG':
			dyn_time.append(int(line.split()[1])/1e6)
			cmd = []
			measured = []
			for i in range(6):
				cmd.append(float(line.split()[2*i+3]))
				measured.append(float(line.split()[2*i+2]))
			angle_measured = np.concatenate((angle_measured, np.array([measured])))
			angle_cmd = np.concatenate((angle_cmd, np.array([cmd])))
	except:
		pass


dyn_time = np.array(dyn_time) - dyn_time[0]

fig_new, ax_new = plt.subplots(6,1, sharey = True, sharex=True)
fig_new.suptitle('Position tracking')
for i in range(6):
	ax_new[i].plot(dyn_time, angle_measured[:,i], '.', label='measured_angles')
	ax_new[i].plot(dyn_time, angle_cmd[:,i], '.', label='cmd angles' )
	ax_new[i].legend(loc=0)




fig, ax = plt.subplots(6,1, sharey = True, sharex=True)
fig.suptitle('Position tracking')
for i in range(6):
	ax[i].plot(dyn_time, angle_cmd[:,i] - angle_measured[:,i], '.', label='cmd - measured_angles')
	ax[i].legend(loc=0)


plt.show()
