from robotkinematicscatalogue.synthesize import *
from robotkinematicscatalogue.inversekinematics.__6DOF.collaborativeRobot import *

class AUCTECH_X3_618(collaborativeRobot):
    
    def __init__(self, gripper=np.diag([-1, -1, 1, 1])):
                                                
        # Modified Denavit-Hartenberg parameters (DHM)
        DHM = np.array([[   0,          0,          111.5,      0           ],
                        [   np.pi/2,    0,          0,          np.pi/2     ],
                        [   0,          270,        0,          0           ],
                        [   0,          248,        149,        -np.pi/2    ],
                        [   -np.pi/2,   0,          100,        0           ],
                        [   np.pi/2,    0,          105,        0           ]])
         
        self.alpha = DHM[:,0]
        self.a = DHM[:,1]
        self.d = DHM[:,2]
        self.theta = DHM[:,3]
                        
        # Joint limits provided in degrees
        self.jointMax = [360, 360, 160, 360, 360, 360] # degrees & mm
        self.jointMin = [-360, -360, -160, -360, -360, -360] # degrees & mm

        # Identify inverted joints - joints that rotate counterclockwise in local z-axis frame
        self.inv_joint = [1] * 6
                
        # Identify nullified joints - prior joints that cancel out at specified self.null_joint element
        self.null_joint = [0, 0, 0, 0, 0, 0]

        # Predefined transform matrices used for inverse kinematics
        self.TB0 = np.eye(4)
        self.TB0[2, 3] = self.d[0]
        self.T6W = gripper