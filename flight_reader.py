import rospy
import math
from clover import srv
from std_srvs.srv import Trigger
import json

def extract(startPath):
    #extract pose data
    with open(startPath, 'r') as startFile:
        allData = json.load(startFile)
        usefulData = allData["poses"]
        startFile.close()
    return usefulData

def poseLister(startPath):
    poses = extract(startPath)
    return poses

rospy.init_node('flight') #<Думаю в этом дело, но не уверен.

#abrv
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

jsonPath = "trajectories_coords.json"


#initial
navigate(x=0, y=0, z=0, frame_id='body', auto_arm=True)

poses = poseLister(jsonPath)
for pose in poses:
    coords = poses[pose]['drone_1']
    x,y,z = coords[0], coords[1], coords[2]
    navigate(x, y, z, frame_id='body')

rospy.sleep(3)
land()