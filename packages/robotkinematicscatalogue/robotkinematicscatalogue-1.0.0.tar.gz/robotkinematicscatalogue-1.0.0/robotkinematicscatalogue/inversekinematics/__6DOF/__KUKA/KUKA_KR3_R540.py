from robotkinematicscatalogue.synthesize import *
from robotkinematicscatalogue.inversekinematics.__6DOF.industrialRobot import *

class KUKA_KR3_R540(industrialRobot):
    
    def __init__(self, gripper=np.diag([-1, -1, 1, 1])):

        # Modified Denavit-Hartenberg parameters (DHM)
        DHM = np.array([[   0,          0,          345,        0           ],
                        [   -np.pi/2,   20,         0,          0           ],
                        [   0,          260,        0,          -np.pi/2    ],
                        [   -np.pi/2,   20,         260,        0           ],
                        [   np.pi/2,    0,          0,          0           ],
                        [   -np.pi/2,   0,          75,         np.pi       ]])

        self.alpha = DHM[:,0]
        self.a = DHM[:,1]
        self.d = DHM[:,2]
        self.theta = DHM[:,3]
                        
        # Joint limits provided in degrees and/or millimeters (mm)
        self.jointMax = [170, 50, 155, 175, 120, 350]
        self.jointMin = [-170, -170, -110, -175, -120, -350]
        
        # Identify inverted joints - joints that rotate counterclockwise in local z-axis frame
        self.inv_joint = [-1, 1, 1, -1, 1, -1]
                
        # Identify nullified joints - prior joints that cancel out at specified self.null_joint element
        self.null_joint = [0, 0, 0, 0, 0, 0]

        # Predefined transform matrices used for inverse kinematics
        self.TB0 = np.eye(4)
        self.TB0[2, 3] = self.d[0]
        self.T6W = gripper
        self.T6W[2, 3] = self.d[5]