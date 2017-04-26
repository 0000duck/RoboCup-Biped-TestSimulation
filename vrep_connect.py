# quick file to test importing things

try:
    import vrep
except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time
import math

print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
    vrep.simxSynchronous(clientID,True)

    joint_names = []
    for j in range(0,2):
        joint_names.append("Joint" + str(j))
    print("Joint names", joint_names)

    joint_handles = []
    for name in joint_names:
        print(vrep.simxGetObjectHandle(clientID, name, vrep.simx_opmode_oneshot_wait))
        joint_handles.append(vrep.simxGetObjectHandle(clientID, name, vrep.simx_opmode_oneshot_wait)[1])
    print("Joint handles",joint_handles)

    dt = .01
    vrep.simxSetFloatingParameter(clientID, vrep.sim_floatparam_simulation_time_step, dt, vrep.simx_opmode_oneshot)
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)

    # vrep.simxPauseCommunication(clientID,1)
    # print(vrep.simxSetJointTargetPosition(clientID,17, time.clock(),vrep.simx_opmode_oneshot))
    # print(vrep.simxSetJointTargetPosition(clientID,26, -90*math.pi/180,vrep.simx_opmode_oneshot))
    # vrep.simxPauseCommunication(clientID,0)
    # vrep.simxSynchronousTrigger(clientID)

    print(-math.pi/2)

    for i in range(300):
        vrep.simxPauseCommunication(clientID,1)
        vrep.simxSetJointTargetPosition(clientID,joint_handles[0], time.clock() ,vrep.simx_opmode_oneshot))
        vrep.simxSetJointTargetPosition(clientID,joint_handles[1], time.clock(),vrep.simx_opmode_oneshot))
        vrep.simxPauseCommunication(clientID,0)
        vrep.simxSynchronousTrigger(clientID)
        # input("press enter to continue")

    # Before closing the connection to V-REP, make sure that the last command sent out had time to arrive.
    # You can guarantee this with (for example):
    vrep.simxGetPingTime(clientID)

    # Now close the connection to V-REP:
    vrep.simxStopSimulation(clientID,vrep.simx_opmode_blocking)
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')
